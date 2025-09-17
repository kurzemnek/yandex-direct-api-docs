---
title: null (nil) value | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/nillable
crawled_at: 2025-09-17T15:44:48.098722
---

Resetting (clearing) a parameter
# null (nil) value
  * [Resetting (clearing) a parameter](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable#resetting-clearing-a-parameter)
  * [Getting a parameter](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable#getting-a-parameter)


Some parameters support the `null` value. The descriptions of these parameters indicate “nillable”.
**JSON**
```
"_field_name_": null

```

**SOAP**
```
<_field_name_ xsi:nil="true">

```

##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable#resetting-clearing-a-parameter)Resetting (clearing) a parameter
In the `update` and `set` methods, you can pass `null` to delete the value for such a parameter.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable#getting-a-parameter)Getting a parameter
If a parameter is requested but its value is not set, the `get` method returns `null`.
Copied
### Was the article helpful?
YesNo
Previous
[Editing separate parameters](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/part-update)
Next
[Running an advertising campaign](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign)
