---
title: JSON format | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/json
crawled_at: 2025-09-17T15:39:42.824892
---

JSON requests
# JSON format
  * [JSON requests](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#json-request)
  * [Request example](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#request-example)
  * [Response example](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#response-example)
  * [Error example](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#error-example)
  * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#learn-more)


Many programming languages have modules and libraries for working with JSON. The recommended modules and libraries for popular languages are listed below.
  * **Perl** : the 
  * **PHP** : built-in JSON support starting from version 5.2.0.
  * **Python** : the 


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#json-request)JSON requests
The address for requests is given in the documentation for each service.
The request always contains the `method` key with the name of the invoked method, and in most cases, it also includes the `params` key (see the example below). Some methods do not have any input parameters, so the `params` key is not required for them.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#request-example)Request example
Calling the `Ads.add` method to create ads for the advertiser `agrom`. Performed in the name of an advertising agency.
```
POST /json/v5/ads/ HTTP/1.1
Host: api.direct.yandex.com
Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f
Accept-Language: ru
Client-Login: agrom
Content-Type: application/json; charset=utf-8

{
"method": "add",
"params": {
    "Ads": [{
    "AdGroupId": 1234567,
    "TextAd": {
        "Text": "All breeds of elephants. Certified breeder",
        "Title": "Buy an elephant!",
        "Href": "http://exotic-farm.com/elefants",
        "Mobile": "NO"
    }
    },
    {
    "AdGroupId": 1234567,
    "TextAd": {
        "Text": "Rhino delivery. Spring sale.",
        "Title": "Buy a rhinoceros!",
        "Mobile": "NO"
    }
    }]
}
}

```

##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#response-example)Response example
```
HTTP/1.1 200 OK
Connection:close
Content-Type:application/json; charset=utf-8
Date:Fri, 28 Nov 2014 17:07:02 GMT
RequestId:1010101010101010101
Units:10/20828/64000
Units-Used-Login:agrom
Server:nginx
Transfer-Encoding:chunked

{
"result": {
    "AddResults": [{
    "Id": 7654321
    }, /* Ad created and its ID returned */
    {
    "Errors": [{
        "Code": 6000,
        "Message": "Inconsistent object state",
        "Details": "The ad must specify the vCard or the main link"
    }] /* Error creating ad */
    }]
}
}

```

##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#error-example)Error example
If the request could not be processed, an error message is returned.
```
HTTP/1.1 200 OK
Connection:close
Content-Type:application/json; charset=utf-8
Date:Fri, 28 Nov 2014 17:07:02 GMT
RequestId:1010101010101010101
Units:10/20828/64000
Units-Used-Login:agrom
Server:nginx
Transfer-Encoding:chunked

{
"error" : {
    "request_id": "1010101010101010101",
    "error_code": 8000,
    "error_string": "Invalid request",
    "error_detail": "TextAd is missing the required Text field"
}
}

```

For more information about errors, see the Errors section.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json#learn-more)Learn more
Copied
### Was the article helpful?
YesNo
Previous
[HTTP headers](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers)
Next
[SOAP protocol](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap)
