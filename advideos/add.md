---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/advideos/add
crawled_at: 2025-09-17T15:47:54.241547
---

Request
# add
  * [Request](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/add#output)


Synchronously uploads videos by their URL links or as binary data. In one method call, you can use a maximum of 10 links or 1 video in binary format.
##  [](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/add#input)Request
Request structure in JSON format.
```
{
   "method": "add",
   "params" : { /* required */
        "AdVideos" : [{ /* AdVideoAddItem */
            "Url" : (string),
            "VideoData" : (base64Binary),
            "Name" : (string)
        }, .. ]
    }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`AdVideos` |  array of AdVideoAddItem |  Videos to add (a maximum of 10 for URL links and a maximum of 1 for binary data). |  Yes  
**AdVideoAddItem structure**  
`URL` |  string |  Link to video. |  Use either `URL` or `VideoData` and `Name`  
`VideoData` |  base64Binary |  Video to upload: base64-encoded binary data.  
`Name` |  string |  Any name for the video (up to 255 characters).  
##  [](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/add#output)Response
Alert
An error when creating an upload job (adding to the queue) for one of the videos neither cancels the operation nor affects creation of upload jobs for other videos.
Response structure in JSON format.
```
{
   "result" : { /* required */
       "AddResults" : [{
           "Warnings" : [{
               "Code" : (integer) /* required */,
               "Message" : (string) /* required */,
               "Details" : (string)
            }, .. (unbounded)],
           "Errors" : [{
               "Code" : (integer) /* required */,
               "Message" : (string) /* required */,
               "Details" : (string)
            }, .. ],
           "Id" : (string)
        }, ... ]
    }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / AddResponse structure (for SOAP)**  
`AddResults` |  array of `VideoActionResult` |  Array of `VideoActionResult` objects. Each object corresponds to an item in the `AdVideoAddItem` input array and contains:
  * If the video is queued successfully, the identification number of the video being processed.
  * The `Errors` array if an error occurred.

The items in the array follow the same order as objects in the `AdVideoAddItem` input array.  
**AddResults structure**  
`Warnings` |  array of ExceptionNotification |  Array of `Warnings` objects: Warnings that occurred when adding videos to the upload queue.  
`Errors` |  array of ExceptionNotification |  Array of `Error` objects: Errors that occurred when adding videos to the upload queue.  
`Id` |  array of ExceptionNotification |  ID of the video.  
Copied
### Was the article helpful?
YesNo
Previous
[AdVideos: Operations with videos](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/advideos)
Next
[get](https://yandex.com/dev/direct/doc/en/advideos/en/advideos/get)
