---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/creatives/add
crawled_at: 2025-09-17T15:49:41.079180
---

Learn more
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#output)


Builds creatives for video extensions based on the video ID received from [AdVideos](https://yandex.com/dev/direct/doc/en/creatives/en/advideos/advideos).
##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#learn-more)Learn more
  * [Creative](https://yandex.com/dev/direct/doc/dg/objects/creative.html)
  * [How the "add" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#restrictions)Restrictions
Maximum of 10 videos per method call.
##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params" : { /* required */
    "Creatives" : [{ /* required */
      "VideoExtensionCreative" : { /* required */
        "VideoId" : (string) /* required */
        }
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`Creatives` |  array of CreativeAddItem |  Creatives to add (a maximum of 10). |  Yes  
**CreativeAddItem structure**  
`VideoExtensionCreative` |  array of VideoExtensionCreativeAddItem |  Settings of a [creative for video extensions](https://yandex.com/dev/direct/doc/dg/objects/creative.html#types). |  Yes  
**VideoExtensionCreativeAddItem structure**  
`VideoId` |  string |  ID of the video. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/add#output)Response
Response structure in JSON format:
```
{
  "result" : { /* required */
    "AddResults" : [{
      "Warnings" : [{
        "Code" : (integer) /* required */,
        "Message" : (string) /* required */,
        "Details" : (string)
      }, ... ],
      "Errors" : [{
        "Code" : (integer) /* required */,
        "Message" : (string) /* required */,
        "Details" : (string)
      }, ... ],
      "Id" : (long)
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / AddResponse structure (for SOAP)**  
`AddResults` |  array |  Results of adding creatives.  
**AddResults structure**  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Array of errors that occured when adding videos to the upload queue.  
`Id` |  long |  The ID of the newly built creative. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
**Warnings, Errors structure**  
`Code` |  int |  Error code.  
`Message` |  string |  Textual message about the error.  
`Details` |  string |  Detailed description of the reason for the error.  
Copied
### Was the article helpful?
YesNo
Previous
[Creatives: getting creatives](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/creatives)
Next
[get](https://yandex.com/dev/direct/doc/en/creatives/en/creatives/get)
