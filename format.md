---
title: Lesson 6. How to make an API request | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/format
crawled_at: 2025-09-17T15:49:36.427845
---

What you need to make an API request
# Lesson 6. How to make an API request
  * [What you need to make an API request](https://yandex.com/dev/direct/doc/en/en/format#format_how_req)
  * [What are the formats for interacting with the Yandex Direct API?](https://yandex.com/dev/direct/doc/en/en/format#format_formats)
  * [Where do I send requests](https://yandex.com/dev/direct/doc/en/en/format#format_destination_req)
  * [Which HTTP headers are used](https://yandex.com/dev/direct/doc/en/en/format#format_http_headers)
  * [What do I use to make requests](https://yandex.com/dev/direct/doc/en/en/format#format_req_app)
  * [Make the first request](https://yandex.com/dev/direct/doc/en/en/format#format_first_req)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/format#format_whats_now)


In this lesson, you will see formats of interaction with the Yandex Direct API and learn how to make your first request.
##  [](https://yandex.com/dev/direct/doc/en/en/format#format_how_req)What you need to make an API request
Having completed the previous lessons, you have already met all the conditions to be able to make API requests:
  1. You have a Yandex Direct account and have accepted the user agreement in the **API** section of the Yandex Direct web interface.
  2. You have registered your app with Yandex OAuth.
  3. You have requested API access and got your request approved.
  4. You have received an OAuth token.
  5. You have enabled Sandbox.
Alert
Since you have requested trial access, you can only work with Sandbox and test data.


##  [](https://yandex.com/dev/direct/doc/en/en/format#format_formats)What are the formats for interacting with the Yandex Direct API?
The app accesses the Yandex Direct API server via the HTTPS network protocol, making POST requests. Each POST request must meet a specific format. The API server will return a response in the same format.
The Yandex Direct API supports two formats:
  * _JSON (JavaScript Object Notation)_ : Text-based data interchange format.
  * _SOAP (Simple Object Access Protocol)_ : XML-based protocol for exchanging structured messages.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/format_formats.png)


##  [](https://yandex.com/dev/direct/doc/en/en/format#format_destination_req)Where do I send requests
The URL for sending requests to Sandbox depends on the format selected:
  * For JSON requests — `https://api-sandbox.direct.yandex.com/json/v5/{service}`
  * For SOAP requests — `https://api-sandbox.direct.yandex.com/v5/{service}`
  * A WSDL description is available at URL: `https://api-sandbox.direct.yandex.com/v5/{service}?wsdl`


Here `{service}` is the name of the service you want to access. Each service is intended for use with a particular class of objects. For example, to manage ad campaigns you can use the `Campaigns` service, sending requests to this service by the following URLs:
  * `https://api-sandbox.direct.yandex.com/json/v5/campaigns` — JSON requests
  * `https://api-sandbox.direct.yandex.com/v5/campaigns` — SOAP requests.


The URL used in the request is case-sensitive: you must specify all characters in lowercase, including the name of the service, otherwise an error will occur.
Alert
The URLs to access the real ad data differ from the Sandbox URLs: they start with `https://api.direct.yandex.com`.
##  [](https://yandex.com/dev/direct/doc/en/en/format#format_http_headers)Which HTTP headers are used
The API request must contain the `Authorization` HTTP header with the OAuth token of the user who makes the request:
```
Authorization: Bearer ТОКЕН

```

  * `Authorization` is the HTTP header name.
  * `Bearer` is an OAuth constant (mandatory parameter).
  * `TOKEN` is the token itself.


We discussed how to get a token in a previous lesson.
Note
There are several types of accounts in Yandex Direct: accounts of the direct advertisers and their representatives; accounts of the advertising agencies and their representatives; and accounts of the agency clients. Different account types have different permissions. When accessing the Yandex Direct API, your app will only have the features and permissions granted to the user account that the OAuth token was obtained for.
The request may also contain other HTTP headers:
  * `Client-Login` — the username of the advertising agency's client. This header is required when you are making a request from an agency.
  * `Accept-Language` - response message language.


Your app must be able to process the following **response headers** :
  * `RequestId`— a unique identifier of your request.
  * `Units` — information about restrictions. You will learn about restrictions in a following lesson.


##  [](https://yandex.com/dev/direct/doc/en/en/format#format_req_app)What do I use to make requests
You can develop your app in any programming language to make the API requests. For learning purposes, you can use any program to send POST requests: for example, you can use a browser plugin or the cURL command line utility.
##  [](https://yandex.com/dev/direct/doc/en/en/format#format_first_req)Make the first request
The examples shown here and below are suitable for the cURL utility. You can adjust the proposed code to your app written in any programming language.
The format of the Windows-based examples is different: the JSON code is enclosed in double quotes, with all the double quotes escaped in the code itself. For example:
```
-d "{\"method\":\"get\",\"params\"...

```

Alert
Don't forget to replace the token and object IDs used in the sample code with your own data.
Let's see what test campaigns were created in the Sandbox. Please note the key request parameters:
  * Request is sent to the `Campaigns` service to the following Sandbox address:
`https://**api-sandbox**.direct.yandex.com/json/v5/**campaigns**`
  * The OAuth token has been passed in the `Authorization` header.
  * The `get` method has been called to get the campaigns.


**cURL**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{},"FieldNames":["Id","Name"]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**cURL for Windows**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"get\",\"params\":{\"SelectionCriteria\":{},\"FieldNames\":[\"Id\",\"Name\"]}}" https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**Request**
```
    POST /json/v5/campaigns/ HTTP/1.1
    Host: api-sandbox.direct.yandex.com
    Authorization: Bearer ТОКЕН
    Accept-Language: ru 
    Client-Login: ЛОГИН_КЛИЕНТА
    Content-Type: application/json; charset=utf-8
    
    {
      "method": "get",
      "params": {
        "SelectionCriteria": {},
        "FieldNames": ["Id", "Name"]
      }
    }

```

**Response**
```
    HTTP/1.1 200 OK
    Connection:close
    Content-Type:application/json
    Date:Fri, 28 Jun 2016 17:07:02 GMT
    RequestId: 1111111111111111112
    Units: 10/20828/64000
    Server:nginx
    Transfer-Encoding:chunked
    
    {
      "result": {
        "Campaigns": [{
          "Name": "Test API Sandbox campaign 1",
          "Id": 1234567
        }, {
          "Name": "Test API Sandbox campaign 2",
          "Id": 1234578
        }, {
          "Name": "Test API Sandbox campaign 3",
          "Id": 1234589
        }]
      }
    }

```

##  [](https://yandex.com/dev/direct/doc/en/en/format#format_whats_now)What's next
So you have made your first request to the Yandex.Direct API. In the next lesson, you will learn more about the principles of data access via the API and see somewhat more sophisticated code samples.
Copied
### Was the article helpful?
YesNo
Previous
[Lesson 5. How to enable Sandbox](https://yandex.com/dev/direct/doc/en/en/sandbox)
Next
[Lesson 7. How to get data via the API](https://yandex.com/dev/direct/doc/en/en/get)
