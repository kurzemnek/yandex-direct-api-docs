---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/feeds/get
crawled_at: 2025-09-17T15:54:50.480619
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#output)


Returns parameters of feeds that meet the specified criteria.
##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#learn-more)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#restrictions)Restrictions
The method returns a maximum of `page-size` objects.
##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* FeedSelectionCriteria */
      "Ids": [(long), ... ],  /* required */
    },
    "FieldNames": [( "Id" | "Name" | "BusinessType" | "SourceType" | "FilterSchema" | "UpdatedAt" | "CampaignIds" | "NumberOfItems" | "Status" | "TitleAndTextSources" ), ... ], /* required */
    "FileFeedFieldNames": [( "Filename" )],
    "UrlFeedFieldNames": [( "Login" | "Url" | "RemoveUtmTags" ), ... ],
    "Page": {  /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)** |  |  |   
`SelectionCriteria` |  FeedsSelectionCriteria |  Criteria for selecting feeds. To get all of an advertiser's feeds, omit `SelectionCriteria`. |  No  
`FieldNames` |  array of FeedFieldEnum |  The names of feed parameters to get. |  Yes  
`UrlFeedFieldNames` |  array of UrlFeedFieldEnum |  Names of feed parameters with the URL source type. Note If a feed with a different source type is selected using `SelectionCriteria`, parameters from `UrlFeedFieldNames` are not returned. |  No  
`FileFeedFieldNames` |  FileFeedFieldEnum |  Names of feed parameters with the FILE source type. Note If a feed with a different source type is selected using `SelectionCriteria`, parameters from `FileFeedFieldNames` are not returned. |  No  
`Page` |  [LimitOffset](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#LimitOffset) |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  No  
**FeedsSelectionCriteria structure** |  |  |   
`Ids` |  array of long |  Selects feeds with the specified IDs. Maximum of 10,000 items in the array. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Feeds": [{ /* FeedGetItem */
      "Id": (long),
      "Name": (string),
      "BusinessType": ( "RETAIL" | "HOTELS" | "REALTY" | "AUTOMOBILES" | "FLIGHTS" | "OTHER"),
      "SourceType": ( "URL" | "FILE" ),
      "FilterSchema": (string),
      "UpdatedAt": (string),  /* nillable */
      "CampaignIds": { /* ArrayOfLong */
        "Items": [(long), ... ] /* required */
      }, /* nillable */
      "FileFeed": { /* FileFeedGet */
        "Filename": (string)
      }, /* nillable */
      "NumberOfItems": (int), /* nillable */
      "Status": ( "NEW" | "UPDATING" | "DONE" | "ERROR"),
      "UrlFeed" : { /* UrlFeedGet */
        "Url": (string),
        "RemoveUtmTags": ( "YES" | "NO" ),
        "Login": (string) /* nillable */
      }, /* nillable */
      "TitleAndTextSources" : { /* nillable */
        "Items" : [ (string) ] /* required */
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`Feeds` |  array of FeedGetItem |  Feeds.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
**FeedGetItem structure** |  |   
`Id` |  long |  The feed ID.  
`Name` |  string |  The name of the feed.  
`BusinessType` |  BusinessTypeEnum |  Type of business.  
`SourceType` |  SourceTypeEnum |  The type of data source: URL or uploaded file.  
`FilterSchema` |  string |  The name of the schema for creating filters. The value is returned only for processed feeds ( `Status = DONE` ).  
`UpdatedAt` |  string, nillable |  The date the data in the feed was last changed.  
`CampaignIds` |  ArrayOfLong, nillable |  Campaigns that use the feed.  
`FileFeed` |  FileFeedGet, nillable |  Parameters of the feed uploaded as a file.  
`NumberOfItems` |  int, nillable |  The number of offers in the feed.  
`Status` |  FeedStatusEnum |  The processing status of the feed.  
`UrlFeed` |  UrlFeedGet, nillable |  Parameters of the feed that is available at the URL.  
`TitleAndTextSources` |  ArrayOfString, nillable |  A list of feed fields that can be used to generate ad titles and ad texts from a feed.  
**FileFeedGet structure** |  |   
`Filename` |  string |  Name of the feed file.  
**UrlFeedGet structure** |  |   
`Url` |  string |  Feed URL.  
`Login` |  string, nillable |  Login for accessing the feed (if required). Maximum of 255 characters.  
`RemoveUtmTags` |  YesNoEnum |  Automatically delete UTM tags from links in the feed.  
Object that contains the `Items` numeric array
Copied
Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/delete)
Next
[update](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update)
