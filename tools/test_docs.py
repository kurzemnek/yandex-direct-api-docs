"""Negative acceptance cases for offline navigation and integrity checks."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import docs


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.scope = patch.object(docs, 'ROOT', self.root)
        self.scope.start()
        self.addCleanup(self.scope.stop)
        self.addCleanup(self.tmp.cleanup)
        originals = {
            'README.md': '# Original\n',
            'SITEMAP.md': '# Snapshot\n',
            'campaigns/get.md': '---\ntitle: Campaign get\nurl: https://yandex.com/dev/direct/doc/en/campaigns/get\n---\nFields\n',
            'campaigns/add.md': '---\ntitle: Are you not a robot?\nurl: https://yandex.com/dev/direct/doc/en/campaigns/add\n---\n# Please confirm that you and not a robot\n',
            'campaigns/broken.md': '---\ntitle: Campaign broken\n---\nMissing source\n',
        }
        for name, text in originals.items():
            self.write(name, text)
        self.write('guide/upstream/README.md', originals['README.md'])
        self.write('README.md', '# Adaptation\n[Start](guide/START.md)\n')
        self.write('AGENTS.md', '# Agent\n')
        self.write('guide/START.md', '# Start\n')
        self.json('guide/upstream.json', {
            'base_commit': 'fixture', 'snapshot_date': '2000-01-01',
            'files': [{'path': n, 'sha256': docs.digest(t.encode())} for n, t in originals.items()]})
        self.json('guide/routes.json', {'routes': [{
            'id': 'campaign', 'title': 'Campaign preparation',
            'path': 'guide/START.md', 'keywords': ['campaign']}]})
        self.json('guide/sources.json', {'facts': [{
            'id': 'fixture', 'url': 'https://yandex.ru/dev/direct/doc/ru/',
            'checked_at': '2000-01-01'}]})
        with contextlib.redirect_stdout(io.StringIO()):
            docs.index()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def json(self, name, value):
        self.write(name, json.dumps(value))

    def checked(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = docs.check()
        return code, json.loads(out.getvalue())

    def test_clean_fixture_passes(self):
        code, result = self.checked()
        self.assertEqual(code, 0)
        self.assertFalse(result['real_api_tested'])

    def test_default_search_hides_challenge_and_invalid_source(self):
        paths = [r['path'] for r in docs.find('campaign')]
        self.assertIn('campaigns/get.md', paths)
        self.assertNotIn('campaigns/add.md', paths)
        self.assertNotIn('campaigns/broken.md', paths)

    def test_unusable_pages_need_explicit_opt_in(self):
        paths = [r['path'] for r in docs.find('campaign', include_unusable=True)]
        self.assertIn('campaigns/add.md', paths)
        self.assertIn('campaigns/broken.md', paths)

    def test_route_precedes_archived_page(self):
        self.assertEqual(docs.find('campaign')[0]['status'], 'guide')
        self.assertEqual(len(docs.find('campaign', route_only=True)), 1)

    def test_path_escape_is_rejected(self):
        with self.assertRaises(ValueError):
            docs.local_path('../outside.md')

    def test_changed_snapshot_fails(self):
        self.write('campaigns/get.md', 'silently changed')
        code, result = self.checked()
        self.assertEqual(code, 1)
        self.assertTrue(any('snapshot' in e for e in result['errors']))

    def test_broken_guide_link_fails(self):
        self.write('guide/START.md', '[Missing](not-provided.md)')
        code, result = self.checked()
        self.assertEqual(code, 1)
        self.assertTrue(any('Broken local link' in e for e in result['errors']))

    def test_stale_catalog_fails(self):
        self.json('guide/catalog.json', {'pages': []})
        code, result = self.checked()
        self.assertEqual(code, 1)
        self.assertIn('Stale catalog; run python3 tools/docs.py index', result['errors'])

    def test_nonprimary_undated_source_fails(self):
        self.json('guide/sources.json', {'facts': [{'id': 'bad', 'url': 'https://example.com'}]})
        code, result = self.checked()
        self.assertEqual(code, 1)
        self.assertTrue(any('Non-primary' in e for e in result['errors']))
        self.assertTrue(any('Undated' in e for e in result['errors']))


if __name__ == '__main__':
    unittest.main()
