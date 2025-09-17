---
title: delete | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/retargetinglists/delete
crawled_at: 2025-09-17T15:55:06.605121
---

Learn more
# delete
  * [Learn more](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#input)
  * [Response](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#output)


Deletes retargeting lists.
##  [](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#learn-more)Learn more
  * [How the "delete" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#restrictions)Restrictions
Maximum of 1000 retargeting lists per method call.
##  [](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#input)Request
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting retargeting lists to delete. |  Yes  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of retargeting lists to delete (maximum of 1000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/delete#output)Response
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
`DeleteResults` |  array of ActionResult |  Results of deleting retargeting lists.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the deleted retargeting list. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/add)
Next
[get](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/get)
