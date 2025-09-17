---
title: unarchive | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/strategies/unarchive
crawled_at: 2025-09-17T16:00:57.098942
---

Request
# unarchive
  * [Request](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/unarchive#input)
  * [Response](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/unarchive#output)


Unarchives the portfolio strategy.
##  [](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/unarchive#input)Request
Input data structure in JSON format:
```

  "params": {  /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }


```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / UnarchiveRequest structure (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting portfolio strategies to unarchive. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of the portfolio strategies that you want to unarchive (no more than `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/unarchive#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "UnarchiveResults": [{  /* ActionResult */
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
**result structure (for JSON) / UnarchiveResponse structure (for SOAP)** |  |   
`UnarchiveResults` |  array of ActionResult |  What happens when portfolio strategies are unarchived.  
**ActionResult structure** |  |   
`Id` |  long |  Portfolio strategy ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/get)
Next
[update](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update)
