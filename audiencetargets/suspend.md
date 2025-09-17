---
title: suspend | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/audiencetargets/suspend
crawled_at: 2025-09-17T15:49:55.335869
---

Learn more
# suspend
  * [Learn more](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#input)
  * [Response](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#output)


Pauses displays for audience targets.
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#learn-more)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#restrictions)Restrictions
Maximum of 10,000 audience targets per method call.
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#input)Request
Request structure in JSON format:
```
{
  "method": "suspend",
  "params": {  /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / SuspendRequest structure (for SOAP)**  
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting audience targets to pause. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the audience targets for which you want to pause impressions (maximum of 10,000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/suspend#output)Response
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
`SuspendResults` |  array of ActionResult |  Results of resuming displays for the audience targets.  
**ActionResult structure**  
`Id` |  long |  ID of the audience target. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[setBids](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/setBids)
Next
[Bids: managing bids](https://yandex.com/dev/direct/doc/en/audiencetargets/en/bids/bids)
