---
title: delete | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/bidmodifiers/delete
crawled_at: 2025-09-17T15:57:05.774543
---

Restrictions
# delete
  * [Restrictions](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete#input)
  * [Response](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete#output)


Deletes bid adjustments.
###  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete#see-also)Learn more
  * [How the "delete" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete#restrictions)Restrictions
Maximum of 1000 adjustments per method call.
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete#input)Request
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
**params structure (for JSON) / DeleteRequest structure (for SOAP)**  
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting adjustments to delete. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of adjustments to delete (maximum of 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete#output)Response
Response structure in JSON format:
```
{
  "result": {
    "DeleteResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ]
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / DeleteResponse structure (for SOAP)**  
`DeleteResults` |  array of ActionResult |  Results of deleting bid adjustments.  
**ActionResult structure**  
`Id` |  long |  ID of the deleted bid adjustment. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add)
Next
[get](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get)
