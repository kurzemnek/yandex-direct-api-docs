---
title: Error handling | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/errors
crawled_at: 2025-09-17T15:44:42.452417
---

Request execution errors
# Error handling
When calling a method, errors and warnings may occur:
  * Errors that prevent the request from being executed: invalid request format (including omission of a required parameter), invalid token, API server unavailable, and so on.
  * Errors and warnings when performing an action with one of the objects in the request that do not affect the success of the operation with other objects. For more information about operation errors, see the section [Operations with object arrays](https://yandex.com/dev/direct/doc/en/concepts/en/best-practice/modify).


Codes and descriptions for errors and warnings are listed in the section [Errors and warnings](https://yandex.com/dev/direct/doc/ref-v5/concepts/errors-list.html).
Note
The language for error messages is defined in the [Accept-Language](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#accept-language) request header.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/errors#request-execution-errors)Request execution errors
If the request cannot be executed, the following structure is returned:
SOAP
JSON
```
<SOAP-ENV:Fault>
  <faultcode>SOAP-ENV:Client</faultcode>
  <faultstring>(string)</faultstring>
  <detail>
    <ns3:FaultResponse xmlns:ns3="http://direct.yandex.com/api/v5/general">
      <requestId>(string)</requestId>
      <errorCode>(int)</errorCode>
      <errorDetail>(string)</errorDetail>
    </ns3:FaultResponse>
  </detail>
</SOAP-ENV:Fault>

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**Fault object**  
faultstring |  string |  Textual message about the error.  
detail |  ApiExceptionMessage |  Information about the error.  
**ApiExceptionMessage object**  
requestId |  string |  Unique request ID assigned by the Yandex Direct API server. It is also passed in the `RequestId` HTTP header.  
errorCode |  int |  Numeric error code.  
errorDetail |  string |  Detailed description of the error.  
```
{
  "error" : {
    "request_id": (string),
    "error_code": (int),
    "error_string": (string),
    "error_detail": (string)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
`request_id` |  string |  Unique request ID assigned by the Yandex Direct API server. It is also passed in the `RequestId` HTTP header.  
`error_code` |  int |  Numeric error code.  
`error_string` |  string |  Textual message about the error.  
`error_detail` |  string |  Detailed description of the error.  
Copied
### Was the article helpful?
YesNo
Previous
[SOAP protocol](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap)
Next
[Restrictions, points](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units)
