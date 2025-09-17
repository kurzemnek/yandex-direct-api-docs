---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/feeds/update
crawled_at: 2025-09-17T15:56:15.845731
---

Learn more
# update
  * [Learn more](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#output)


Changes feed parameters.
##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#learn-more)Learn more
  * [How the "update" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#restrictions)Restrictions
Maximum of 50 feeds per method call.
Changing the business type and source type is not allowed.
##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#input)Request
Request structure in JSON format:
```
{
  "method": "update",
  "params": { /* params */
    "Feeds": [{ /* FeedUpdateItem */
      "Id": (long), /* required */
      "Name": (string),
      "UrlFeed": { /* UrlFeedUpdate */
        "Url": (string),
        "Login": (string), /* nillable */
        "Password": (string), /* nillable */
        "RemoveUtmTags": ( "YES" | "NO" )
      },
      "FileFeed": { /* FileFeedUpdate */
        "Data": (base64Binary), /* required */
        "Filename": (string) /* required */
      }
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / UpdateRequest structure (for SOAP)** |  |  |   
`Feeds` |  array of FeedUpdateItem |  Feeds to change. |  Yes  
**FeedUpdateItem structure** |  |  |   
`Id` |  long |  The feed ID. |  Yes  
`Name` |  string |  The name of the feed. Maximum of 255 characters. |  No  
`UrlFeed` |  UrlFeedUpdate |  Parameters of the feed that is available at the URL. |  No  
`FileFeed` |  FileFeedUpdate |  Parameters of the feed that is passed in the request. |  No  
**UrlFeedUpdate structure** |  |  |   
`Url` |  string |  Feed URL. Maximum of 1024 characters. It must include the protocol and domain name. |  No  
`Login` |  string, nillable |  Login for accessing the feed (if required). Maximum of 255 characters. |  No  
`Password` |  string, nillable |  Password for accessing the feed (if required). Maximum of 255 characters. |  No  
`RemoveUtmTags` |  YesNoEnum |  Automatically delete UTM tags from links in the feed. The default value is NO. |  No  
**FileFeedUpdate structure** |  |  |   
`Data` |  base64Binary |  A base64-encoded feed to upload. The feed size is limited by the total request size — maximum of 50 MB. Note When using the SOAP library, place the feed file directly in this field, and the library automatically encodes it as base64 during transmission. When using JSON format, first encode the binary data in base64, then pass it as a string. |  Yes  
`Filename` |  string |  Name of the feed file. Maximum of 255 characters. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/update#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "UpdateResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ]
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / UpdateResponse structure (for SOAP)** |  |   
`UpdateResults` |  array of ActionResult |  Results of changing the feed parameters.  
**ActionResult structure** |  |   
`Id` |  long |  The feed ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/feeds/en/feeds/get)
Next
[KeywordBids: managing bids](https://yandex.com/dev/direct/doc/en/feeds/en/keywordbids/keywordbids)
