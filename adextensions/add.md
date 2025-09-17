---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adextensions/add
crawled_at: 2025-09-17T15:37:26.254006
---

Learn more
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#output)


Creates extensions.
Only one type of extension, the callout, is available at this time.
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#learn-more)Learn more
  * [How the "add" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#restrictions)Restrictions
To check the callout limit for an advertiser, use the [Clients](https://yandex.com/dev/direct/doc/en/adextensions/en/clients/clients).[get](https://yandex.com/dev/direct/doc/en/adextensions/en/clients/get) or [AgencyClients](https://yandex.com/dev/direct/doc/en/adextensions/en/agencyclients/agencyclients).[get](https://yandex.com/dev/direct/doc/en/adextensions/en/agencyclients/get) method (look for the AD_EXTENSIONS_TOTAL element in the Restrictions array).
Maximum of 1000 extensions per method call.
If there are identical extensions, an error is returned for each of them.
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "AdExtensions": [{  /* AdExtensionAddItem */
      "Callout": {  /* Callout */
        "CalloutText": (string) /* required */
      }
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`AdExtensions` |  array of AdExtensionAddItem |  Extensions to add. |  Yes  
**AdExtensionAddItem structure**  
`Callout` |  Callout |  A callout. |  No  
**Callout structure**  
`CalloutText` |  string |  Callout text. Maximum of 25 characters. |  No  
##  [](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/add#output)Response
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
**result structure (for JSON) / AddResponse structure (for SOAP)**  
`AddResults` |  array of ActionResult |  Results of adding extensions.  
**ActionResult structure**  
`Id` |  long |  ID of the created extension. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[AdExtensions: operations with ad extensions](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/adextensions)
Next
[delete](https://yandex.com/dev/direct/doc/en/adextensions/en/adextensions/delete)
