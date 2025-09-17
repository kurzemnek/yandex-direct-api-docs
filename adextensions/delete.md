---
title: delete | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adextensions/delete
crawled_at: 2025-09-17T15:37:36.448772
---

Learn more
# delete
  * [Learn more](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#output)


Deletes extensions.
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#learn-more)Learn more
  * [How the "delete" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#restrictions)Restrictions
Maximum of 10,000 extensions per method call.
If an extension is assigned to an ad, you can't delete it. First you must [unassign](https://yandex.com/dev/direct/doc/dg/best-practice/launch-campaign.html#harness) the extension from all ads.
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#input)Request
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting extensions to delete. |  Yes  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of extensions to be deleted (maximum of 10,000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete#output)Response
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
`DeleteResults` |  array of ActionResult |  Results of deleting extensions.  
**ActionResult structure**  
`Id` |  long |  ID of the deleted extension. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add)
Next
[get](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get)
