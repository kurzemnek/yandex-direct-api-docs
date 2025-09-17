---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/update
crawled_at: 2025-09-17T15:50:24.176667
---

Restrictions
# update
  * [Restrictions](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/update#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/update#output)


Changes the sets of negative keywords.## Learn more
  * [How the "update" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/update#restrictions)Restrictions
Maximum 30 sets of negative keywords per method call.
##  [](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/update#input)Request
Request structure in JSON format:
```
{
  "method": "update",
  "params": { /* params */
    "NegativeKeywordSharedSets": [{  /* NegativeKeywordSharedSetUpdateItem */
      "Id": (long), /* required */
      "Name": (string),
      "NegativeKeywords": [(string), ... ]
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / UpdateRequest structure (for SOAP)** |  |  |   
`NegativeKeywordSharedSets` |  array of NegativeKeywordSharedSetUpdateItem |  Sets of negative keywords to change. Maximum of 30 items in the array. |  Yes  
**NegativeKeywordSharedSetUpdateItem structure** |  |  |   
`Id` |  long |  ID of the retargeting list. |  Yes  
`Name` |  string |  Name of a set of negative keywords (maximum 255 characters). |  No  
`NegativeKeywords` |  array of string |  Array of negative keywords. A keyword should be specified without the minus sign before the first word. Maximum of 7 words per keyword. The maximum length of each word is 35 characters. The maximum combined length of negative keywords in the array is 4096 characters. Spaces, dashes, and operators are not counted as part of the total length. |  No  
##  [](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/update#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "UpdateResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ]
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / UpdateResponse structure (for SOAP)** |  |   
`UpdateResults` |  array of ActionResult |  The results of changing the sets of negative keywords.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the set of negative keywords. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/negativekeywordsharedsets/get)
Next
[RetargetingLists: managing retargeting lists](https://yandex.com/dev/direct/doc/en/negativekeywordsharedsets/en/retargetinglists/retargetinglists)
