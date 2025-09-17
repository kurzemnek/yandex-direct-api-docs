---
title: delete | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adgroups/delete
crawled_at: 2025-09-17T15:45:55.939194
---

Learn more
# delete
  * [Learn more](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#output)


Deletes ad groups.
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#learn-more)Learn more
  * [How the "delete" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#restrictions)Restrictions
Maximum of 10,000 groups per method call.
You can only delete an empty group that doesn't contain ads or targeting criteria (keywords, audience targets, or dynamic text ad targets).
You can't delete groups from archived campaigns.
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#input)Request
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting groups to delete. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the groups that you want to delete (maximum of 10,000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete#output)Response
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
**result structure (for JSON) / DeleteResponse structure (for SOAP)**  
`DeleteResults` |  array of ActionResult |  Results of deleting groups.  
**ActionResult structure**  
`Id` |  long |  ID of the deleted group. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add)
Next
[get](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get)
