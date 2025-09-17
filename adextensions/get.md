---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adextensions/get
crawled_at: 2025-09-17T15:37:31.692631
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#output)


Returns extensions that meet the specified criteria.
Only one type of extension, the callout, is available at this time.
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#learn-more)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
    "params": { /* params */
    "SelectionCriteria": {  /* AdExtensionsSelectionCriteria */
      "Ids": [(long), ... ],
      "Types": [( "CALLOUT" ), ... ],
      "States": [( "ON" | "DELETED" ), ... ],
      "Statuses": [( "ACCEPTED" | "DRAFT" | "MODERATION" | "REJECTED" ), ... ],
      "ModifiedSince": (string)
    }, /* required */
    "FieldNames": [( "Id" | "Type" | "Status" | "StatusClarification" | "Associated" ), ... ], /* required */
    "CalloutFieldNames": [( "CalloutText" )],
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
`SelectionCriteria` |  AdExtensionsSelectionCriteria |  Criteria for selecting extensions. To get all of an advertiser's extensions, leave `SelectionCriteria` empty. |  Yes  
`FieldNames` |  array of AdExtensionFieldEnum |  Names of parameters to get that are common to all types of extensions. |  Yes  
`CalloutFieldNames` |  array of CalloutFieldEnum |  Parameter names for "Callout" extensions you want to get. |  No  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page) of data. |  No  
**AdExtensionsSelectionCriteria structure**  
`Ids` |  array of long |  Selects extensions with the specified IDs. Maximum of 10,000 items in the array. |  No  
`Types` |  array of AdExtensionTypeEnum |  Selects extensions based on the specified types. Currently, only one extension type is supported, the Callout (CALLOUT). |  No  
`States` |  array of AdExtensionStateSelectionEnum |  Selects extensions based on the specified states. See [Extension state](https://yandex.com/dev/direct/doc/dg/objects/adextension.html#state). Note The "get" method returns an extension in the DELETED state only if the `States` parameter is set to DELETED or the ID of this extension is specified in the `Ids` parameter. If both the `Ids` and `States` parameters are omitted, the method doesn't return extensions in the DELETED state. |  No  
`Statuses` |  array of ExtensionStatusSelectionEnum |  Selects extensions based on the specified statuses. See [Status of the extension](https://yandex.com/dev/direct/doc/dg/objects/adextension.html#status). |  No  
`ModifiedSince` |  string |  Selects extensions that were changed after the specified date. Specified in the format `YYYY-MM-DDThh:mm:ssZ` (following ISO 8601), such as `2015-05-24T23:59:59Z`. |  No  
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AdExtensions": [{  /* AdExtensionGetItem */
      "Id": (long),
      "Associated": ( "YES" | "NO" ),
      "Type": ( "CALLOUT" | "UNKNOWN" ),
      "Callout": {  /* Callout */
        "CalloutText": (string) /* required */
      },
      "State": [( "ON" | "DELETED" | "UNKNOWN" ), ... ],
      "Status": ( "ACCEPTED" | "DRAFT" | "MODERATION" | "REJECTED" | "UNKNOWN" ),
      "StatusClarification": (string)
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`AdExtensions` |  array of AdExtensionGetItem |  Ad extensions.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page).  
**AdExtensionGetItem structure**  
`Id` |  long |  Extension ID.  
`Associated` |  YesNoEnum |  Whether the extension is assigned to at least one of the client's ads.  
`Type` |  AdExtensionTypeEnum |  Extension type.  
`Callout` |  Callout |  Parameters of a "Callout" extension.  
`State` |  StateEnum |  State of the extension. See [Extension state](https://yandex.com/dev/direct/doc/dg/objects/adextension.html#state).  
`Status` |  StatusEnum |  Status of the extension. See [Status of the extension](https://yandex.com/dev/direct/doc/dg/objects/adextension.html#status).  
`StatusClarification` |  string |  Text explanation of the status and/or reasons for rejection after review.  
**Callout structure** |  |   
`CalloutText` |  string |  Callout text.  
Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete)
Next
[AdGroups: operations with ad groups](https://yandex.com/dev/direct/doc/en/adextensions/en/adgroups/adgroups)
