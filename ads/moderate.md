---
title: moderate | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/ads/moderate
crawled_at: 2025-09-17T15:58:42.225750
---

Restrictions
# moderate
  * [Restrictions](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate#input)
  * [Response](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate#output)


Submits ads for review.
###  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate#see-also)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate#restrictions)Restrictions
A maximum of 10,000 ads per method call.
Only ads with the DRAFT status can be submitted for review.
Ads can't be submitted for review if the ad group doesn't have any targeting criteria (keywords, audience targets, or dynamic text ad targets). Ads can't be submitted for review if they belong to an archived campaign.
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate#input)Request
Request structure in JSON format:
```
{
  "method": "moderate",
  "params": {  /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / ModerateRequest structure (for SOAP)**  
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting ads to submit for review. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the ads that you want to submit for review (no more than `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/moderate#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "ModerateResults": [{  /* ActionResult */
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
**result structure (for JSON) / ModerateResponse structure (for SOAP)**  
`ModerateResults` |  array of ActionResult |  Results of submitting for review.  
**ActionResult structure**  
`Id` |  long |  The ad ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/ads/en/ads/get)
Next
[resume](https://yandex.com/dev/direct/doc/en/ads/en/ads/resume)
