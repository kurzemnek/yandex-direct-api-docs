---
title: unarchive | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/unarchive
crawled_at: 2025-09-17T16:00:45.566825
---

Restrictions
# unarchive
  * [Restrictions](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/unarchive#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/unarchive#input)
  * [Response](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/unarchive#output)


Unarchives campaigns.## Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/unarchive#restrictions)Restrictions
Maximum of 1000 campaigns per method call.
You can't unarchive campaigns from the special archive (the CONVERTED state).
Maximum of 1000 unarchived campaigns per advertiser.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/unarchive#input)Request
Input data structure in JSON format:
```
{
  "method": "unarchive",
  "params": {  /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / UnarchiveRequest structure (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting campaigns to unarchive. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of campaigns to unarchive (maximum of 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/unarchive#output)Response
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
`UnarchiveResults` |  array of ActionResult |  Results of unarchiving campaigns.  
**ActionResult structure** |  |   
`Id` |  long |  The campaign ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[suspend](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend)
Next
[update](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/update)
