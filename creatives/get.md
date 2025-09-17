---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/creatives/get
crawled_at: 2025-09-17T15:47:43.325172
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#output)


Returns the parameters of creatives that match the specified criteria.
##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#learn-more)Learn more
  * [Creative](https://yandex.com/dev/direct/doc/dg/objects/creative.html)
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": {
    "SelectionCriteria": { /* CreativesSelectionCriteria */
      "Ids": [(long), ... ],
      "Types": [( "IMAGE_CREATIVE" | "HTML5_CREATIVE" | "VIDEO_EXTENSION_CREATIVE" | "CPC_VIDEO_CREATIVE" | "CPM_VIDEO_CREATIVE" | "SMART_CREATIVE" ), ... ]
    }, /* required */
    "FieldNames": [( "Id" | "Type" | "Name" | "PreviewUrl" | "Width" | "Height" | "ThumbnailUrl" | "Associated" | "IsAdaptive" ), ... ], /* required */
    "VideoExtensionCreativeFieldNames": [( "Duration" ), ... ],
    "CpcVideoCreativeFieldNames": [( "Duration" ), ... ],
    "CpmVideoCreativeFieldNames": [( "Duration" ), ... ],
    "SmartCreativeFieldNames" : [( "CreativeGroupId" | "CreativeGroupName" | "BusinessType" ), ... ],
    "Page": {  /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

Parameters are described below.
**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)**  
`SelectionCriteria` |  CreativesSelectionCriteria |  Criteria for selecting creatives. To get all of an advertiser's creatives, leave `SelectionCriteria` empty. |  Yes  
`FieldNames` |  array of AdFieldEnum |  Names of top-level parameters to get. |  Yes  
`VideoExtensionCreativeFieldNames` |  array of VideoExtensionCreativeFieldNames |  The names of the parameters for video extension creatives to get. See [Type of creative](https://yandex.com/dev/direct/doc/dg/objects/creative.html#types). Note If a different type of creative was selected using `SelectionCriteria`, parameters from `VideoExtensionCreativeFieldNames` are not returned. |  No  
`CpcVideoCreativeFieldNames` |  array of CpcVideoCreativeFieldEnum |  Names of the requested creatives for video ads in the “Text & Image Ads” campaigns. Note If a different type of creative was selected using `SelectionCriteria`, parameters from `CpcVideoCreativeFieldNames` are not returned. |  No  
`CpmVideoCreativeFieldNames` |  array of CpmVideoCreativeFieldEnum |  Names of the requested parameters of creatives for video ads in display campaigns. Note If a different type of creative was selected using `SelectionCriteria`, parameters from `CpmVideoCreativeFieldNames` are not returned. |  No  
`SmartCreativeFieldNames` |  array of SmartCreativeFieldEnum |  The names of parameters for smart banner creatives to get. Note If a different type of creative was selected using `SelectionCriteria`, parameters from `SmartCreativeFieldNames` are not returned. |  No  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page) of data. |  No  
**CreativesSelectionCriteria structure**  
`Ids` |  array of long |  Selects creatives with the specified IDs. From 1 to 10,000 items in the array. |  No  
`Types` |  array of CreativeTypeEnum |  Selects creatives of the specified types. See [Type of creative](https://yandex.com/dev/direct/doc/dg/objects/creative.html#types). |  No  
##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Creatives": [{  /* CreativeGetItem */
      "Id": (long),
      "Type": ( "IMAGE_CREATIVE" | "HTML5_CREATIVE" | "VIDEO_EXTENSION_CREATIVE" | "CPC_VIDEO_CREATIVE" | "CPM_VIDEO_CREATIVE" | "SMART_CREATIVE" ),
      "Name": (string),
      "PreviewUrl": (string),
      "Width": (int),
      "Height": (int),
      "ThumbnailUrl": (string),
      "Associated": ( "YES" | "NO" ),
      "IsAdaptive": ( "YES" | "NO" ),
      "VideoExtensionCreative": {  /* VideoExtensionCreativeGet */
        "Duration": (int) /* required */
      },
      "CpcVideoCreative": {  /* CpcVideoCreativeGet */
        "Duration": (int) /* required */
      },
      "CpmVideoCreative": {  /* CpmVideoCreativeGet */
        "Duration": (int) /* required */
      },
      "SmartCreative" : {  /* SmartCreativeGet */
        "CreativeGroupId" : (long),
        "CreativeGroupName" : (string),
        "BusinessType" : ( "RETAIL" | "HOTELS" | "REALTY" | "AUTOMOBILES" | "FLIGHTS" | "CLOTHES" | "OTHER" )
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

Parameters are described below.
**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`Creatives` |  array of CreativeGetItem |  Creatives.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page).  
**CreativeGetItem structure**  
`Id` |  long |  ID of the creative.  
`Type` |  CreativeTypeEnum |  Type of creative. See [Type of creative](https://yandex.com/dev/direct/doc/dg/objects/creative.html#types).  
`Name` |  string |  Name of the video creative or group of image creatives.  
`PreviewUrl` |  string |  Link for previewing.  
`Width` |  int |  Width of the creative.  
`Height` |  int |  Height of the creative.  
`ThumbnailUrl` |  string |  URL for the preview thumbnail.  
`Associated` |  YesNoEnum |  Whether the creative is assigned to at least one of the client's ads.  
`IsAdaptive` |  YesNoEnum |  Whether the creative is adaptive.  
`VideoExtensionCreative` |  VideoExtensionCreativeGet |  Parameters of the video extension creative.  
`CpcVideoCreative` |  CpcVideoCreativeGet |  Parameters of a creative for video ads in the “Text & Image Ads“ campaigns.  
`CpmVideoCreative` |  CpmVideoCreativeGet |  Parameters of a creative for video ads in display campaigns.  
`SmartCreative` |  SmartCreativeGet |  Parameters of a creative for smart banners in the “Smart banners” campaigns.  
**VideoExtensionCreativeGet structure**  
`Duration` |  int |  The length of the video in seconds.  
**CpcVideoCreativeGet structure**  
`Duration` |  int |  The length of the video in seconds.  
**CpmVideoCreativeGet structure**  
`Duration` |  int |  The length of the video in seconds.  
**SmartCreativeGet structure**  
`CreativeGroupId` |  long |  ID of the group of creatives.  
`CreativeGroupName` |  string |  Name of the group of creatives.  
`BusinessType` |  BusinessTypeEnum |  The subject of the creative, which matches the type of business feed.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add)
Next
[Dictionaries: getting reference lists](https://yandex.com/dev/direct/doc/en/creatives/en/dictionaries/dictionaries)
