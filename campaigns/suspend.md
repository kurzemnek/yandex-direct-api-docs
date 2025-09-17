---
title: suspend | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/suspend
crawled_at: 2025-09-17T16:00:26.504499
---

Restrictions
# suspend
  * [Restrictions](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend#input)
  * [Response](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend#output)


Stops impressions at the campaign level.
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend#restrictions)Restrictions
Maximum of 1000 campaigns per method call.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend#input)Request
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting campaigns to suspend. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of campaigns to suspend (maximum of 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend#output)Response
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
`SuspendResults` |  array of ActionResult |  Results of suspending campaigns.  
**ActionResult structure** |  |   
`Id` |  long |  The campaign ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[resume](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume)
Next
[unarchive](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/unarchive)
