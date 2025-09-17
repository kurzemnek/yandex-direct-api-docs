---
title: Editing separate parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/part-update
crawled_at: 2025-09-17T15:41:56.244900
---

Editing separate parameters
# Editing separate parameters
When using the `update` method to change an object, there is no need to pass the full set of object parameters. It is sufficient to specify the object ID and the parameters being changed. Values of omitted parameters don't change.
Note
Before saving the changes in the Yandex.Direct database, the validity of the entire object as a whole is checked (not just the parameters that were passed). If an object is invalid, the operation won't apply to this object.
If a parameter supports the `null` value, you can reset (clear) the value. See the section [The null (nil) value](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable).
Copied
### Was the article helpful?
YesNo
Previous
[Operations on object arrays](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify)
Next
[null (nil) value](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable)
