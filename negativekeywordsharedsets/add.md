---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/add
crawled_at: 2025-09-17T15:50:19.505930
---

Restrictions
# add
  * [Restrictions](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/add#output)


Creates sets of negative keywords.
##  [](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/add#restrictions)Restrictions
Maximum 30 sets of negative keywords per advertiser.
Maximum 30 sets of negative keywords per method call.
##  [](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "NegativeKeywordSharedSets": [{  /* NegativeKeywordSharedSetAddItem */
      "Name": (string), /* required */
      "NegativeKeywords": [(string), ... ] /* required */
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)** |  |  |   
`NegativeKeywordSharedSets` |  array of NegativeKeywordSharedSetAddItem |  Sets of negative keywords to add. Maximum of 30 items in the array. |  Yes  
**NegativeKeywordSharedSetAddItem structure** |  |  |   
`Name` |  string |  Name of a set of negative keywords (maximum 255 characters). |  Yes  
`NegativeKeywords` |  array of string |  Array of negative keywords. A keyword should be specified without the minus sign before the first word. Maximum of 7 words per keyword. The maximum length of each word is 35 characters. The maximum combined length of negative keywords in the array is 4096 characters. Spaces, dashes, and operators are not counted as part of the total length. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/add#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AddResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ]
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / AddResponse structure (for SOAP)** |  |   
`AddResults` |  array of ActionResult |  Results of adding sets of negative keywords.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the created set of negative keywords. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[NegativeKeywordSharedSets: managing sets of negative keywords](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/negativekeywordsharedsets)
Next
[delete](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/delete)
