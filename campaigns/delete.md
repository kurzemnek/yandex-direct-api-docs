---
title: delete | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/delete
crawled_at: 2025-09-17T16:00:22.124330
---

Restrictions
# delete
  * [Restrictions](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete#input)
  * [Response](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete#output)


Deletes campaigns.## Learn more
  * [How the "delete" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete#restrictions)Restrictions
Maximum of 1000 campaigns per method call.
Campaigns can't be deleted in the following cases:
  * The campaign received funds or has invoices for payment.
  * The campaign had impressions and has accumulated statistics.
  * The campaign is currently being activated or paused.
  * The campaign has the CONVERTED status.


For these types of campaigns, archiving is available using the [archive](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive) method.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete#input)Request
Request structure in JSON format:
```
{
  "method": "delete",
  "params": { /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / DeleteRequest structure (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting campaigns to delete. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of campaigns to delete (maximum of 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "DeleteResults": [{  /* ActionResult */
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
**result structure (for JSON) / DeleteResponse structure (for SOAP)** |  |   
`DeleteResults` |  array of ActionResult |  Results of deleting campaigns.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the deleted campaign. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[archive](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive)
Next
[get](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get)
