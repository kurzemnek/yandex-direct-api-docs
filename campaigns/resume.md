---
title: resume | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/resume
crawled_at: 2025-09-17T16:00:32.868965
---

Learn more
# resume
  * [Learn more](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#input)
  * [Response](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#output)


Resumes displays on the campaign level.
Note
If displays were suspended on the level of an individual ad, resuming displays on the campaign level does not affect it.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#learn-more)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#restrictions)Restrictions
Maximum of 1000 campaigns per method call.
You can't resume displays for archived campaigns (the ARCHIVED state).
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#input)Request
Request structure in JSON format:
```
{
  "method": "resume",
  "params": { /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / ResumeRequest structure (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting campaigns to resume. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of campaigns to resume (maximum of 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "ResumeResults": [{  /* ActionResult */
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
**result structure (for JSON) / ResumeResponse structure (for SOAP)** |  |   
`ResumeResults` |  array of ActionResult |  Results of resuming campaigns.  
**ActionResult structure** |  |   
`Id` |  long |  The campaign ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get: CpmBannerCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-cpm-banner-campaign)
Next
[suspend](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/suspend)
