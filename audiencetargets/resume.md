---
title: resume | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/audiencetargets/resume
crawled_at: 2025-09-17T15:50:00.292583
---

Learn more
# resume
  * [Learn more](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#input)
  * [Response](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#output)


Resumes displays for previously paused audience targets.
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#learn-more)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#restrictions)Restrictions
Maximum of 10,000 audience targets per method call.
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#input)Request
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting audience targets for which you want to resume impressions. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the audience targets for which you want to resume impressions (maximum of 10,000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume#output)Response
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
`ResumeResults` |  array of ActionResult |  Results of resuming impressions for the audience targets.  
**ActionResult structure**  
`Id` |  long |  ID of the audience target. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get)
Next
[setBids](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/setBids)
