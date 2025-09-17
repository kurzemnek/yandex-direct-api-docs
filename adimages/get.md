---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adimages/get
crawled_at: 2025-09-17T15:50:43.613280
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#output)


Returns images that meet the specified criteria.
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#learn-more)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* AdImageSelectionCriteria */
      "AdImageHashes": [(string), ... ],
      "Associated": ( "YES" | "NO" )
    },
    "FieldNames": [( "AdImageHash" | "OriginalUrl" | "PreviewUrl" | "Name" | "Type" | "Subtype" | "Associated" ), ... ], /* required */
    "Page": {  /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)**  
`SelectionCriteria` |  AdImageSelectionCriteria |  Criteria for selecting images. If omitted, all the advertiser's images are returned. |  No  
`FieldNames` |  array of AdImageFieldEnum |  Names of parameters of images to get. |  Yes  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page) of data. |  No  
**AdImageSelectionCriteria structure**  
`AdImageHashes` |  array of string |  Selects images with the specified hashes. Maximum of 10,000 items in the array. |  No  
`Associated` |  YesNoEnum |  Selects images based on whether they are assigned to ads: YES — assigned; NO — unassigned. |  No  
##  [](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AdImages": [{  /* AdImageGetItem */
      "AdImageHash": (string),
      "Name": (string),
      "Associated": ( "YES" | "NO" ),
      "Type": ( "SMALL" | "REGULAR" | "WIDE" | "FIXED_IMAGE" | "UNFIT" ),
      "Subtype": ( "IMG_240_400" | "IMG_300_250" | "IMG_300_500" | "IMG_300_600" | "IMG_320_50" | "IMG_320_100" | "IMG_320_480" | "IMG_336_280" | "IMG_480_320" | "IMG_480_800" | "IMG_600_500" | "IMG_600_1000" | "IMG_600_1200" | "IMG_640_100" | "IMG_640_200" | "IMG_640_960" | "IMG_672_560" | "IMG_720_1200" | "IMG_728_90" | "IMG_900_750" | "IMG_900_1500" | "IMG_900_1800" | "IMG_960_150" | "IMG_960_300" | "IMG_960_640" | "IMG_960_1440" | "IMG_960_1600" | "IMG_970_250" | "IMG_1008_840" | "IMG_1200_1000" | "IMG_1200_2000" | "IMG_1200_2400" | "IMG_1280_200" | "IMG_1280_400" | "IMG_1280_1920" | "IMG_1344_1120" | "IMG_1440_960" | "IMG_1456_180" | "IMG_1920_1280" | "IMG_1940_500" | "IMG_2184_270" | "IMG_2910_750" | "IMG_2912_360" | "IMG_3880_1000" | "NONE" ),
      "OriginalUrl": (string), /* nillable */
      "PreviewUrl": (string) /* nillable */
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`AdImages` |  array of AdImageGetItem |  Images.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page).  
**AdImageGetItem structure**  
`AdImageHash` |  string |  Hash of the image.  
`Name` |  string |  Caption for the image. Maximum of 255 characters.  
`Associated` |  YesNoEnum |  Whether the image is assigned to at least one of the client's ads.  
`Type` |  AdImageTypeEnum |  The type of image. See [Type of image](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#type).  
`Subtype` |  AdImageSubtypeEnum |  The image size for the FIXED_IMAGE type. For images with any type other than FIXED_IMAGE, NONE is returned.  
`OriginalUrl` |  string, nillable |  A link to the full-size image.  
`PreviewUrl` |  string, nillable |  A link to the image preview.  
Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/adimages/en/adimages/delete)
Next
[Ads: operations with ads](https://yandex.com/dev/direct/doc/en/adimages/en/ads/ads)
