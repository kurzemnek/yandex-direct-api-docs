---
title: delete | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/sitelinks/delete
crawled_at: 2025-09-17T15:57:46.331970
---

Learn more
# delete
  * [Learn more](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#input)
  * [Response](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#output)


Deletes sets of sitelinks.
##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#learn-more)Learn more
  * [How the "delete" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#restrictions)Restrictions
Maximum of 1000 sets per method call.
If a set of sitelinks is assigned to an ad, it can't be deleted.
##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#input)Request
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting sets to delete. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of sitelink sets to delete (no more than 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete#output)Response
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
`DeleteResults` |  array of ActionResult |  Results of deleting sitelink sets.  
**ActionResult object** |  |   
`Id` |  long |  ID of the deleted set of sitelinks. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/add)
Next
[get](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/get)
