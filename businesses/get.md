---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/businesses/get
crawled_at: 2025-09-17T15:54:45.604468
---

Request
# get
  * [Request](https://yandex.com/dev/direct/doc/en/businesses/en/businesses/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/businesses/en/businesses/get#output)


Returns data from the advertiser's   
The advertiser can get data for businesses that meet at least one of the following criteria:
  * The advertiser's [chief representative](https://yandex.com/dev/direct/doc/dg/objects/roles.html) has 
  * The business profile is linked to one of the advertiser's ads.


If the business profile doesn't pass moderation in Yandex Business Directory, the NO value is returned in the `IsPublished` parameter. You won't be able to link this business profile to an ad.
###  [](https://yandex.com/dev/direct/doc/en/businesses/en/businesses/get#see-also)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/businesses/en/businesses/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    },
    "FieldNames": [( "Id" | "Name" | "Address" | "Phone"
                     | "ProfileUrl" | "InternalUrl" | "IsPublished"
                     | "MergedIds" | "Rubric" | "Urls"
                     | "HasOffice" ), ... ], /* required */
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting business profiles. |  No  
`FieldNames` |  array of BusinessFieldEnum |  The names of parameters to get. |  Yes  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  No  
**IdsCriteria structure**  
`Ids` |  array of long |  IDs of the requested business profiles (a maximum of `ids-select`). |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/businesses/en/businesses/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Businesses": [{ /* BusinessGetItem */
      "Id": (long),
      "Name": (string),
      "Address": (string), /* nillable */
      "Phone": (string),
      "ProfileUrl": (string),
      "InternalUrl": (string),
      "IsPublished": ( "YES" | "NO" ),
      "MergedIds": {  /* ArrayOfLong */
        "Items": [(long), ... ]
      },
      "Rubric": (string),
      "Urls": {  /* ArrayOfString */
        "Items": [(string), ... ]
      },
      "HasOffice": ( "YES" | "NO" )
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`Businesses` |  array of BusinessGetItem |  Business profiles.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
**BusinessGetItem structure**  
`Id` |  long |  ID of the business profile.  
`Name` |  string |  Name of the organization.  
`Address` |  string, nillable |  Address of the business.  
`Phone` |  string |  Phone number of the business.  
`ProfileUrl` |  string |  Link to the business profile on Yandex.  
`InternalUrl` |  string |  Link to the business editing page in Yandex Business Directory.  
`IsPublished` |  YesNoEnum |  Indicates that the business profile passed moderation in Yandex Business Directory and is published. You can link a business profile to an ad only if the YES value is returned in the `IsPublished` parameter.  
`MergedIds` |  ArrayOfLong |  IDs of business profiles that are combined with the main profile (the ID of the main profile is specified in the `Id` field). Only IDs of profiles linked to the advertiser's ads are returned, and only if the request omitted `SelectionCriteria`.  
`Rubric` |  string |  Type of business.  
`Urls` |  ArrayOfString |  Links to the site and social networks.  
`HasOffice` |  YesNoEnum |  Indicates that the organization has a physical location.  
Copied
### Was the article helpful?
YesNo
Previous
[Businesses: getting business profiles](https://yandex.com/dev/direct/doc/en/businesses/en/businesses/businesses)
Next
[BidModifiers: managing bid adjustments](https://yandex.com/dev/direct/doc/en/businesses/en/bidmodifiers/bidmodifiers)
