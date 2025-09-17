---
title: Response codes and error codes | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/codes
crawled_at: 2025-09-17T15:44:17.521461
---

Response codes and error codes
# Response codes and error codes
The table lists HTTP response codes.
**Value** |  **Description**  
---|---  
200 |  The report was created successfully in online mode  
201 |  The report was successfully added to the offline queue  
202 |  The report is being generated in offline mode  
400 |  Error in the request, or exceeded the limit on requests in the queue  
500 |  Server error when generating the report  
502 |  Request processing timed out on the server  
If an error occurs, the following structure is returned:
JSON
XML
```
{
  "error": {
      "request_id": (string),
      "error_code": (int),
      "error_string": (string),
      "error_detail": (string)
  }
}

```

```
<?xml version="1.0" encoding="UTF-8"?>
  <reports:reportDownloadError xmlns:reports="http://api.direct.yandex.com/v5/reports">
  <reports:ApiError>
      <reports:requestId>(string)</reports:requestId>
      <reports:errorCode>(int)</reports:errorCode>
      <reports:errorMessage>(string)</reports:errorMessage>
      <reports:errorDetail>(string)</reports:errorDetail>
  </reports:ApiError>
  </reports:reportDownloadError>

```

**reports:ApiError object**
**Parameter** |  **Type** |  **Description**  
---|---|---  
`reports:requestId` |  string |  Unique request ID assigned by the Yandex.Direct API server. It is also passed in the `RequestId` HTTP header.  
`reports:errorCode` |  int |  Numeric error code.  
`reports:errorMessage` |  string |  Textual message about the error.  
`reports:errorDetail` |  string |  Detailed description of the error.  
Errors are described in the section [Errors and warnings](https://yandex.com/dev/direct/doc/ref-v5/concepts/errors-list.html).
Copied
### Was the article helpful?
YesNo
Previous
[Data freshness](https://yandex.com/dev/direct/doc/en/en/actual)
Next
[Restrictions](https://yandex.com/dev/direct/doc/en/en/restrictions)
