---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/leads/get
crawled_at: 2025-09-17T15:50:33.511990
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#output)


Returns data entered by users in forms on Turbo pages.
##  [](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#learn-more)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
##  [](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": { /* LeadsSelectionCriteria */
      "TurboPageIds": [(long), ... ], /* required */
      "DateTimeFrom": (string),
      "DateTimeTo": (string)
    }, /* required */
    "FieldNames": [( "SubmittedAt" | "TurboPageId" | "TurboPageName" | "Id" | "Data" ), ... ], /* required */
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
`SelectionCriteria` |  LeadsSelectionCriteria |  Criteria for selecting data that was entered by users in forms on Turbo pages. |  Yes  
`FieldNames` |  array of LeadFieldEnum |  Names of top-level parameters to get. |  Yes  
`Page` |  [LimitOffset](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#LimitOffset) |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  No  
**LeadsSelectionCriteria structure** |  |  |   
`TurboPageIds` |  array of long |  Select data that was entered by users in forms on Turbo pages with the specified IDs. From 1 to 1000 items in the array. |  Yes  
`DateTimeFrom` |  string |  The start of the time period to get data for. Specified in YYYY-MM-DDThh:mm:ssZ format (conforming to ISO 8601). |  No  
`DateTimeTo` |  string |  The end of the time period to get data for. Specified in YYYY-MM-DDThh:mm:ssZ format (conforming to ISO 8601). |  No  
##  [](https://yandex.com/dev/direct/doc/en/leads/en/leads/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Leads": [{ /* LeadGetItem */
      "Id": (string), /* required */
      "SubmittedAt": (string), /* required */
      "TurboPageId": (string), /* required */
      "TurboPageName": (string), /* required */
      "Data": [{ /* LeadDataItem */
        "Name": (string), /* required */
        "Value": (string) /* required */
      }, ... ] /* required */
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`Leads` |  array of LeadGetItem |  Data entered by users in forms on Turbo pages.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
**LeadGetItem structure** |  |   
`Id` |  string |  ID of the data entered by a user in a form.  
`SubmittedAt` |  string |  The date and time when the form was submitted. Output in YYYY-MM-DDThh:mm:ssZ format (conforming to ISO 8601).  
`TurboPageId` |  string |  ID of the Turbo page where the form was submitted.  
`TurboPageName` |  string |  Name of the Turbo page where the form was submitted.  
`Data` |  array of LeadDataItem |  Data entered by the user.  
**LeadDataItem structure** |  |   
`Name` |  string |  Name of the form field.  
`Value` |  string |  The value entered by the user.  
Copied
### Was the article helpful?
YesNo
Previous
[Leads: receiving form data from Turbo pages](https://yandex.com/dev/direct/doc/en/leads/en/leads/leads)
Next
[NegativeKeywordSharedSets: managing sets of negative keywords](https://yandex.com/dev/direct/doc/en/leads/en/negativekeywordsharedsets/negativekeywordsharedsets)
