---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/turbopages/get
crawled_at: 2025-09-17T15:56:33.617088
---

Restrictions
# get
  * [Restrictions](https://yandex.com/dev/direct/doc/en/turbopages/en/turbopages/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/turbopages/en/turbopages/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/turbopages/en/turbopages/get#output)


Returns the parameters of Turbo pages.## Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/turbopages/en/turbopages/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
The method returns only published Turbo pages.
##  [](https://yandex.com/dev/direct/doc/en/turbopages/en/turbopages/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": { /* IdsCriteria */
      "Ids": [(long), ... ],
      "BoundWithHrefs": [(string), ...]
    },
    "FieldNames": [( "Id" | "Name" | "Href" | "PreviewHref" | "TurboSiteHref" | "BoundWithHref" ), ... ], /* required */
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
`SelectionCriteria` |  IdsCriteria |  Criteria for selecting Turbo pages. To get all of an advertiser's published Turbo pages, omit `SelectionCriteria`. |  No  
`FieldNames` |  array of TurboPageFieldEnum |  Names of top-level parameters to get. |  Yes  
`Page` |  [LimitOffset](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#LimitOffset) |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  No  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  Selects Turbo pages with the specified IDs. From 1 to 10,000 items in the array. |  No  
`BoundWithHrefs` |  array of string |  Select Turbo pages with the specified links. |  No  
##  [](https://yandex.com/dev/direct/doc/en/turbopages/en/turbopages/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "TurboPages": [{ /* TurboPageGetItem */
      "Id": (long),
      "Name": (string),
      "Href": (string),
      "PreviewHref": (string),
      "TurboSiteHref": (string),
      "BoundWithHref": (string)
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`TurboPages` |  array of TurboPageGetItem |  Turbo page parameters.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
**TurboPageGetItem structure** |  |   
`Id` |  long |  ID of the Turbo page.  
`Name` |  string |  Name of the Turbo page.  
`Href` |  string |  Link to the published Turbo page.  
`PreviewHref` |  string |  Link for previewing the Turbo page.  
`TurboSiteHref` |  string |  Link in the format `name.turbo.site`. If the link is not associated with a Turbo page, the value is empty.  
`BoundWithHref` |  string |  The link where the Turbo page was found (it matches the link from the query parameters, without case-folding and normalization).  
Copied
### Was the article helpful?
YesNo
Previous
[TurboPages: getting parameters of Turbo pages](https://yandex.com/dev/direct/doc/en/turbopages/en/turbopages/turbopages)
Next
[VCards: operations with vCards](https://yandex.com/dev/direct/doc/en/turbopages/en/vcards/vcards)
