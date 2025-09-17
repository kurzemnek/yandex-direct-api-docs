---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/sitelinks/get
crawled_at: 2025-09-17T15:57:40.595734
---

Restrictions
# get
  * [Restrictions](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/get#output)


Returns sets of sitelinks that match the specified criteria.## Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/get#restrictions)Restrictions
The method returns a maximum of `page-size` objects.
##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": {  /* params */
    "SelectionCriteria": {  /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    },
    "FieldNames": [( "Id" | "Sitelinks" ), ... ],
    "SitelinkFieldNames": [( "Title" | "Href" | "Description" | "TurboPageId" ), ... ],
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting sets. If omitted, all the advertiser's sets are returned. |  No  
`FieldNames` |  array of SitelinksSetFieldEnum |  Names of top-level parameters to get. If the `Sitelinks` value is specified, then the `Sitelinks` array returns the following sitelink fields: `Title`, `Href`, and `Description`. If you need to get a different set of fields, list their names in the `SitelinkFieldNames` parameter and omit the `Sitelinks` value in the `FieldNames` parameter. |  No  
`SitelinkFieldNames` |  array of SitelinkFieldEnum |  Names of sitelink fields to get. |  No  
`Page` |  [LimitOffset](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#LimitOffset) |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  No  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of sets to get. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "SitelinksSets": [{  /* SitelinksSetGetItem */
      "Id": (long),
      "Sitelinks": [{  /* Sitelink */
        "Title": (string),
        "Href": (string), /* nillable */
        "Description": (string), /* nillable */
        "TurboPageId": (long) /* nillable */
      }, ... ]
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`SitelinksSets` |  array of SitelinksSetGetItem |  Sets of sitelinks.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
**SitelinksSetGetItem structure** |  |   
`Id` |  long |  ID of a set of sitelinks.  
`Sitelinks` |  Sitelink |  Array of 1 to 4 Sitelink objects.  
**Sitelink structure** |  |   
`Title` |  string |  Sitelink text.  
`Href` |  string, nillable |  Sitelink address.  
`Description` |  string, nillable |  Sitelink description for displaying the ad in expanded format.  
`TurboPageId` |  long, nillable |  ID of the Turbo page.  
Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete)
Next
[SmartAdTargets: managing smart banner targeting filters](https://yandex.com/dev/direct/doc/en/sitelinks/en/smartadtargets/smartadtargets)
