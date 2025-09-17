---
title: resume | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywords/resume
crawled_at: 2025-09-17T15:59:28.285232
---

Learn more
# resume
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#output)


Resumes displays for keywords and autotargetings that were suspended earlier.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#learn-more)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#restrictions)Restrictions
A maximum of `ids-select` of objects per method call.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#input)Request
Request structure in JSON format:
```
{
  "method": "resume",
  "params": {  /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / ResumeRequest structure (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting the keywords and autotargetings to resume. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of the keywords and autotargetings that you want to resume (a maximum of `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume#output)Response
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
`ResumeResults` |  array of ActionResult |  Results of starting keywords and autotargetings.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the keyword or autotargeting. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get)
Next
[suspend](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend)
