---
title: archive | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/archive
crawled_at: 2025-09-17T16:00:38.938018
---

Learn more
# archive
  * [Learn more](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#input)
  * [Response](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#output)


Archives campaigns.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#learn-more)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#restrictions)Restrictions
Maximum of 1000 campaigns per method call.
You can't archive a campaign that has funds.
The campaign must be suspended before archiving.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#input)Request
Request structure in JSON format:
```
{
  "method": "archive",
  "params": { /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / ArchiveRequest structure (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting campaigns to archive. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of campaigns to archive (maximum of 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "ArchiveResults": [{  /* ActionResult */
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
**result structure (for JSON) / ArchiveResponse structure (for SOAP)** |  |   
`ArchiveResults` |  array of ActionResult |  Results of archiving campaigns.  
**ActionResult structure** |  |   
`Id` |  long |  The campaign ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[add: CpmBannerCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-cpm-banner-campaign)
Next
[delete](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete)
