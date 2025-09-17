---
title: unarchive | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/ads/unarchive
crawled_at: 2025-09-17T15:54:35.598345
---

Restrictions
# unarchive
  * [Restrictions](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive#input)
  * [Response](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive#output)


Unarchives ads.
###  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive#see-also)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive#restrictions)Restrictions
A maximum of 10,000 ads per method call.
Ads can't be unarchived if they are in an archived campaign.
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive#input)Request
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
**params structure (for JSON) / UnarchiveRequest structure (for SOAP)**  
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting ads to unarchive. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the ads that you want to unarchive (no more than `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive#output)Response
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
**result structure (for JSON) / UnarchiveResponse structure (for SOAP)**  
`UnarchiveResults` |  array of ActionResult |  Results of unarchiving ads.  
**ActionResult structure**  
`Id` |  long |  The ad ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[suspend](https://yandex.com/dev/direct/doc/en/ads/en/ads/suspend)
Next
[update](https://yandex.com/dev/direct/doc/en/ads/en/ads/update)
