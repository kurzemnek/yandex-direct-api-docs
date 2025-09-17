---
title: HTTP headers | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/headers
crawled_at: 2025-09-17T15:40:01.188114
---

Request headers
# HTTP headers
  * [Request headers](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#request)
    * [Authorization](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#authorization)
    * [Accept-Language](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#accept-language)
    * [Client-Login](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#client-login)
    * [Use-Operator-Units: true](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#use-operator-units-true)
    * [Accept-Encoding: gzip](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#accept-encoding-gzip)
    * [Payment-Token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#payment-token)
  * [Response headers](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#response)
    * [RequestId](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#requestid)
    * [Units](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#units)
    * [Units-Used-Login](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#units-used-login)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#request)Request headers
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#authorization)Authorization
Contains the [OAuth token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token) of the Yandex Direct user that the API request is being made on behalf of.
Example:
```
Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f

```

###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#accept-language)Accept-Language
Language for response messages. The selected language is used when returning textual explanations for statuses of objects (campaigns, ads, and others), and for the texts of errors and warnings. The following languages are supported:
  * en — English
  * ru — Russian
  * en — English


Example:
```
Accept-Language: ru

```

If this header is omitted or contains a language that isn't supported by the Yandex Direct API, response messages are given in English.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#client-login)Client-Login
The username of an advertiser who is a client of the advertising agency. It is required if the request is made on behalf of an agency.
Example:
```
Client-Login: agrom

```

###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#use-operator-units-true)Use-Operator-Units: true
Spend the agency's points, not the advertiser's, when making a request. See the section [Restrictions and points](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units). This header is only allowed in requests from an agency.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#accept-encoding-gzip)Accept-Encoding: gzip
Get the response body using GZIP compression.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#payment-token)Payment-Token
Finance token. Required when calling finance methods.
Request example:
```
POST /json/v5/ads/ HTTP/1.1
Host: api.direct.yandex.com
Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f
Accept-Language: ru
Client-Login: agrom
Use-Operator-Units: true
Content-Type: application/json; charset=utf-8

{
  "method":"add",
  "params": {
    ...
  }
}

```

##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#response)Response headers
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#requestid)RequestId
Unique request ID (string) assigned by the Yandex Direct API server. Returned for both successful and failed requests.
Please indicate this ID when contacting the [Support service](https://yandex.com/dev/direct/doc/support/troubleshooting/issue.html).
Example:
```
RequestId: 8695244274068608439

```

###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#units)Units
The number of points: 1. spent on executing the request, 2. available remainder of the daily limit, 3. the daily limit. See the section [Restrictions and points](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units).
Example:
```
Units: 10/20828/64000

```

###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers#units-used-login)Units-Used-Login
The username of the advertiser's representative (if the advertiser's points were spent on the request), or the username of the agency's representative (if the agency's points were spent on the request).
Example:
```
Units-Used-Login: ttt-agency

```

Response example:
```
HTTP/1.1 200 OK
Connection:close
Content-Type:application/json; charset=utf-8
Date:Fri, 28 Nov 2014 17:07:02 GMT
RequestId:8695244274068608439
Units:10/20828/64000
Units-Used-Login:ttt-agency
Server:nginx
Transfer-Encoding:chunked

{
  "result": {
    ...
  }
}

```

### Was the article helpful?
YesNo
Previous
[Interaction format](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/format)
Next
[JSON format](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json)
