---
title: suspend | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/ads/suspend
crawled_at: 2025-09-17T15:55:58.599110
---

Restrictions
# suspend
  * [Restrictions](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend#input)
  * [Response](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend#output)


Stops ad displays.
###  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend#see-also)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend#restrictions)Restrictions
A maximum of 10,000 ads per method call.
You can't pause archived ads, drafts of ads (see [Ad status and state](https://yandex.com/dev/direct/doc/dg/objects/ad.html)), or ads that belong to an archived campaign.
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend#input)Request
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
**params structure (for JSON) / SuspendRequest structure (for SOAP)**  
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting ads to suspend. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the ads that you want to stop (no more than `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend#output)Response
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
**result structure (for JSON) / SuspendResponse structure (for SOAP)**  
`SuspendResults` |  array of ActionResult |  Results of suspending ads.  
**ActionResult structure**  
`Id` |  long |  The ad ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[resume](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume)
Next
[unarchive](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive)
