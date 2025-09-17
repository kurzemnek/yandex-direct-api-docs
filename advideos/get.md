---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/advideos/get
crawled_at: 2025-09-17T15:45:33.208991
---

Request
# get
  * [Request](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/get#request)
  * [Response](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/get#response)


Returns the status of processing uploaded videos.
##  [](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/get#request)Request
Request structure in JSON format.
```
{
   "method": "GetRequest",
   "params" : { /* required */
        "Page" : {
            "Limit" : (long),
            "Offset" : (long)
        },
        "SelectionCriteria" : { /* required */
            "Ids" : [ (string) ] /* required */
        },
        "FieldNames" : [ ("Id"|"Status") ] /* required */
    }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)**  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  Yes  
`SelectionCriteria` |  AdVideosSelectionCriteria |  Criteria for selecting videos. |  Yes  
`FieldNames` |  array of AdVideosFieldEnum |  Names of video parameters to get. |  Yes  
**AdVideosSelectionCriteria structure**  
`Ids` |  array of string |  Select videos with the specified IDs. From 1 to 10 items in the array. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/get#response)Response
Response structure in JSON format.
```
{
   "method": "GetResponse",
   "result" : { /* required */
        "LimitedBy" : (long),
        "AdVideos" : [{
            "Id" : (string),
            "Status" : ("READY"|"ERROR"|"CONVERTING"|"NEW")
        }, ... ]
    }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
`AdVideos` |  array of AdVideoGetItem |  Video.  
**AdVideoGetItem structure**  
`Id` |  string |  ID of the video.  
`Status` |  StatusEnum |  Video conversion status.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/add)
Next
[AgencyClients: managing agency clients](https://yandex.com/dev/direct/doc/en/advideos/en/agencyclients/agencyclients)
