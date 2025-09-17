---
title: resume | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/ads/resume
crawled_at: 2025-09-17T15:56:55.622843
---

Restrictions
# resume
  * [Restrictions](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume#input)
  * [Response](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume#output)


Resumes ad displays that were previously stopped by the owner.
###  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume#see-also)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume#restrictions)Restrictions
A maximum of 10,000 ads per method call.
You can't resume archived ads, drafts of ads (see [Ad status and state](https://yandex.com/dev/direct/doc/dg/objects/ad.html)), or ads that belong to an archived campaign.
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume#input)Request
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
**params structure (for JSON) / ResumeRequest structure (for SOAP)**  
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting ads to resume displaying. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the ads that you want to resume (no more than `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume#output)Response
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
**result structure (for JSON) / ResumeResponse structure (for SOAP)**  
`ResumeResults` |  array of ActionResult |  Results of resuming ad displays.  
**ActionResult structure**  
`Id` |  long |  The ad ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[moderate](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate)
Next
[suspend](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend)
