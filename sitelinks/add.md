---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/sitelinks/add
crawled_at: 2025-09-17T15:57:33.449643
---

Restrictions
# add
  * [Restrictions](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/add#output)


Creates sets of sitelinks.## Learn more
  * [How the "add" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/add#restrictions)Restrictions
Maximum of 1000 sets of sitelinks per method call.
If all the fields in the sets are identical, only one set is created.
##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "SitelinksSets": [{  /* SitelinksSetAddItem */
      "Sitelinks": [{  /* Sitelink */
        "Title": (string), /* required */
        "Href": (string),
        "Description": (string),
        "TurboPageId": (long)
       }, ... ] /* required */
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)** |  |  |   
`SitelinksSets` |  array of SitelinksSetAddItem |  The sets of sitelinks to add. |  Yes  
**SitelinksSetAddItem structure** |  |  |   
`Sitelinks` |  array of Sitelink |  Set of sitelinks. From 1 to 8 items in the array. |  Yes  
**Sitelink structure** |  |  |   
`Title` |  string |  Text of a sitelink (maximum 30 characters). The maximum total length of texts for sitelinks 1–4 is 66 characters. The maximum total length of texts for sitelinks 5–8 is 66 characters. |  Yes  
`Href` |  string |  Link to the advertiser's website (maximum of 1024 characters). It must include the protocol and domain name. May contain [substitution variables](https://yandex.com/support/direct/statistics/url-tags.html). Alert The values of the `{campaign_id}`, `{ad_id}`, `{banner_id}`, and `{phrase_id}` variables will be substituted in the sitelinks only if the same variables are present in the main link for the ad. |  One or both of the `Href` and `TurboPageId` parameters  
`TurboPageId` |  long |  ID of the Turbo page. |   
`Description` |  string |  Sitelink description (maximum 60 characters) for displaying the ad in expanded format. |  No  
##  [](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/add#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AddResults": [{  /* ActionResult */
      "Id": (long),
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
**result structure (for JSON) / AddResponse structure (for SOAP)** |  |   
`AddResults` |  array of ActionResult |  Results of adding sets of sitelinks.  
**ActionResult object** |  |   
`Id` |  long |  ID of the created set of sitelinks. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[Sitelinks: operations with sitelinks](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/sitelinks)
Next
[delete](https://yandex.com/dev/direct/doc/en/sitelinks/en/sitelinks/delete)
