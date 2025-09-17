---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adimages/add
crawled_at: 2025-09-17T15:50:38.351353
---

Learn more
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#output)
  * [Example](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#samples)


Synchronously uploads images as binary data.
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#learn-more)Learn more
  * [How the "add" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#restrictions)Restrictions
The maximum number of images per advertiser is 1000 + 2 × the number of ads.
Maximum of 100 images per method call. We recommend uploading no more than 3 images per call.
If images are identical, only one image is created.
Restrictions on the size of the image are listed in [Requirements for images uploaded via the API](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#requirements).
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "AdImages": [{  /* AdImageAddItem */
      "ImageData": (base64Binary), /* required */
      "Type" : ("REGULAR" | "WIDE" | "FIXED_IMAGE" | "AUTO" ),
      "Name": (string) /* required */
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`AdImages` |  array of AdImageAddItem |  Images to add (maximum of 100). |  Yes  
**AdImageAddItem structure**  
`ImageData` |  base64Binary |  Image to upload: base64-encoded binary data. Note When using the SOAP library, place the binary data directly in this field, and the library automatically encodes it as base64 during transmission. When using JSON format, first encode the binary data in base64, then pass it as a string. |  Yes  
`Type` |  AdImageAddTypeEnum |  Type of image. See [here](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#type). The type is determined automatically if the `Type` value isn't specified or is set to `AUTO`. If an image fits two types, such as `FIXED_IMAGE` and `REGULAR/WIDE`, the `REGULAR/WIDE` type is selected. |  No  
`Name` |  string |  Caption for the image. Maximum of 255 characters. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AddResults": [{  /* AdImageActionResult */
      "AdImageHash": (string),
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
**result structure (for JSON) / AddResponse structure (for SOAP)**  
`AddResults` |  array of AdImageActionResult |  Results of adding images.  
**AdImageActionResult structure**  
`AdImageHash` |  string |  Hash of the image. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/add#samples)Example
```
{
  "method": "add",
  "params": {
    "AdImages": [{
      "ImageData": "iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAA...",
      "Name": "elephants.jpg"
    }]
  }
}

```

Copied
### Was the article helpful?
YesNo
Previous
[AdImages: operations with images](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/adimages)
Next
[delete](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete)
