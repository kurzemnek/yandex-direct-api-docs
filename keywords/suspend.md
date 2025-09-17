---
title: suspend | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywords/suspend
crawled_at: 2025-09-17T15:59:22.313292
---

Learn more
# suspend
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#output)


Stops displays for keywords and autotargetings.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#learn-more)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#restrictions)Restrictions
A maximum of `ids-select` of objects per method call.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#input)Request
Request structure in JSON format:
```
{
  "method": "suspend",
  "params": { /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / SuspendRequest structure (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting the keywords and autotargetings to stop. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of the keywords and autotargetings that you want to stop (a maximum of `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "SuspendResults": [{  /* ActionResult */
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
**result structure (for JSON) / SuspendResponse structure (for SOAP)** |  |   
`SuspendResults` |  array of ActionResult |  Results of suspending keywords and autotargetings.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the keyword or autotargeting. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[resume](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume)
Next
[update](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update)
