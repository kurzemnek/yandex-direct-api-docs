#!/usr/bin/env python3
"""Offline navigation and integrity checks; never calls the advertising API."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def local_path(value):
    path = (ROOT / value).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f'Path escapes repository: {value}')
    return path


def make_catalog():
    manifest = read_json('guide/upstream.json')
    records = []
    for record in manifest['files']:
        name = record['path']
        if not name.endswith('.md') or name in ('README.md', 'SITEMAP.md'):
            continue
        raw = local_path(name).read_text(encoding='utf-8')
        title_match = re.search(r'^title:\s*(.+)$', raw, re.M)
        url_match = re.search(r'^url:\s*(\S+)', raw, re.M)
        title = title_match.group(1).strip() if title_match else name
        source = url_match.group(1) if url_match else None
        challenge = ('Please confirm that you and not a robot' in raw
                     or bool(re.search(r'^title:.*(?:Are you not a robot|[Cc]aptcha)', raw, re.M)))
        invalid = source is None or '%28https' in source or '(https' in source
        health = 'challenge' if challenge else 'invalid_source' if invalid else 'historical_unverified'
        candidate = source.replace('https://yandex.com/dev/direct/doc/en',
                                   'https://yandex.ru/dev/direct/doc/ru') if source else None
        records.append({'path': name, 'title': title, 'status': health, 'source_url': source,
                        'official_candidate_url': candidate, 'snapshot_sha256': record['sha256']})
    return {'upstream_commit': manifest['base_commit'], 'snapshot_date': manifest['snapshot_date'],
            'candidate_urls_are_verified': False, 'pages': records}


def index():
    catalog = make_catalog()
    (ROOT / 'guide/catalog.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
    counts = {status: sum(p['status'] == status for p in catalog['pages'])
              for status in ('historical_unverified', 'challenge', 'invalid_source')}
    print(json.dumps({'indexed': len(catalog['pages']), **counts}, ensure_ascii=False))


def normalized(value):
    return value.casefold().replace('ё', 'е')


def rank(query, text):
    query, text = normalized(query), normalized(text)
    terms = re.findall(r'[\w-]+', query)
    return (10 if query in text else 0) + sum(2 for term in terms if term in text)


def find(query, limit=8, route_only=False, include_unusable=False):
    results = []
    for route in read_json('guide/routes.json')['routes']:
        score = rank(query, route['title'] + ' ' + ' '.join(route['keywords']))
        if score:
            results.append((score + 20, route['path'], 'guide', route['title']))
    if not route_only:
        for page in read_json('guide/catalog.json')['pages']:
            if page['status'] != 'historical_unverified' and not include_unusable:
                continue
            score = rank(query, page['title'] + ' ' + page['path'])
            if score:
                results.append((score, page['path'], page['status'], page['title']))
    results.sort(key=lambda item: (-item[0], item[1]))
    return [{'path': p, 'status': s, 'title': t} for _, p, s, t in results[:limit]]


def check():
    errors = []
    manifest = read_json('guide/upstream.json')
    for item in manifest['files']:
        # Root README has our introduction; its exact original is kept separately.
        path = 'guide/upstream/README.md' if item['path'] == 'README.md' else item['path']
        if not local_path(path).is_file() or digest(local_path(path).read_bytes()) != item['sha256']:
            errors.append(f'Changed or missing upstream snapshot: {path}')
    catalog = read_json('guide/catalog.json')
    if catalog != make_catalog():
        errors.append('Stale catalog; run python3 tools/docs.py index')
    ours = [ROOT / 'README.md', ROOT / 'AGENTS.md'] + sorted((ROOT / 'guide').rglob('*.md'))
    links = 0
    for path in ours:
        if path == ROOT / 'guide/upstream/README.md':
            continue
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target = target.strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            links += 1
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f'Broken local link in {path.relative_to(ROOT)}: {target}')
        if re.search(r'/(?:home|mnt)/|gh[pousr]_[A-Za-z0-9]{20,}', text):
            errors.append(f'Private path or token-shaped value in {path.relative_to(ROOT)}')
    sources = read_json('guide/sources.json')
    for fact in sources['facts']:
        if urlsplit(fact['url']).hostname not in ('yandex.ru', 'yandex.com'):
            errors.append(f'Non-primary source: {fact["id"]}')
        if not fact.get('checked_at'):
            errors.append(f'Undated source: {fact["id"]}')
    for route in read_json('guide/routes.json')['routes']:
        if not local_path(route['path']).is_file():
            errors.append(f'Missing route: {route["id"]}')
    result = {'passed': not errors, 'upstream_files_preserved': len(manifest['files']),
              'indexed_snapshot_pages': len(catalog['pages']), 'local_links_checked': links,
              'dated_primary_facts': len(sources['facts']), 'errors': errors,
              'real_api_tested': False}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('index', help='Rebuild the snapshot index without network')
    commands.add_parser('check', help='Check adaptation links and preserved snapshot hashes')
    search = commands.add_parser('find', help='Find a route or archived page without loading all docs')
    search.add_argument('query')
    search.add_argument('--limit', type=int, choices=range(1, 31), default=8, metavar='1..30')
    search.add_argument('--route', action='store_true', help='Only search our task routes')
    search.add_argument('--include-unusable', action='store_true', help='Also show flagged archive pages')
    args = parser.parse_args()
    try:
        if args.command == 'index':
            index()
        elif args.command == 'check':
            return check()
        else:
            print(json.dumps(find(args.query, args.limit, args.route, args.include_unusable),
                             ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print(f'Documentation check failed: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
