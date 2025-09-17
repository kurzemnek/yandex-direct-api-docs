---
title: delete | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adimages/delete
crawled_at: 2025-09-17T15:50:48.223627
---

Learn more
# delete
  * [Learn more](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#output)


Deletes images.
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#learn-more)Learn more
  * [How the "delete" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#restrictions)Restrictions
Maximum of 10,000 images per method call.
If an image is assigned to an ad, it can't be deleted.
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#input)Request
Request structure in JSON format:
```
{
  "method": "delete",
  "params": {
    "SelectionCriteria": {  /* AdImageIdsCriteria */
      "AdImageHashes": [(string), ... ] /* required */
    } /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / DeleteRequest structure (for SOAP)**  
`SelectionCriteria` |  AdImageIdsCriteria |  Criteria for selecting images to delete. |  Yes  
**AdImageIdsCriteria structure**  
`AdImageHashes` |  array of string |  Hashes of images to be deleted (maximum of 10,000). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "DeleteResults": [{  /* AdImageActionResult */
      "AdImageHash": (string),
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
`DeleteResults` |  array of AdImageActionResult |  Results of deleting images.  
**AdImageActionResult structure**  
`AdImageHash` |  string |  Hash of the deleted image. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add)
Next
[get](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get)
