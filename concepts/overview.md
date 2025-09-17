---
title: Overview of the Yandex Direct API version 5 | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/overview
crawled_at: 2025-09-17T15:35:36.353564
---

Structure of the API
# Overview of the Yandex Direct API version 5
  * [Structure of the API](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/overview#objects)
  * [Access to the API](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/overview#access)
  * [Interaction format](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/overview#format)


The Yandex Direct application programming interface (API) automates management of advertising campaigns. External applications use the API to add and edit campaigns, ads and keywords, set bids, and get statistics on impressions and clicks.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/overview#objects)Structure of the API
The Yandex Direct API consists of web services. Each service has its URL.
Each service is intended for a particular class of object: for example, `AdGroups` manages ad groups, `Ads` manages ads, and so on.
[Learn more about objects](https://yandex.com/dev/direct/doc/en/concepts/en/objects/objects)
A service provides a set of methods for performing various operations with objects. A service typically includes the following methods:
  * `add`: Adding objects.
  * `update`: Changing object parameters.
  * `delete`: Deleting objects.
  * `get`: Retrieving object parameters.


Services can also include other object-specific methods. For example, the `moderate` method in the `Ads` service is for submitting ads for review.
[Learn more about methods](https://yandex.com/dev/direct/doc/en/concepts/en/best-practice/principles)
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/overview#access)Access to the API
You can connect to and use the Yandex Direct API for free.
API requests are made by an app on behalf of Yandex Direct users: advertisers and advertising agencies. The API uses the OAuth 2.0 protocol for authentication. The access token must be included in requests.
The developer of an app that makes API requests must register the app beforehand.
[Learn more about managing access](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/access)
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/overview#format)Interaction format
API requests are made over the HTTPS protocol using the POST method. The access token and other special parameters are passed in the HTTP header. Input and output data structures are passed in the body of the request and response.
The Yandex Direct API supports two formats: JSON and SOAP/XML.
[Learn more about formats](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/format)
Copied
### Was the article helpful?
YesNo
Previous
[Lesson 10. How to efficiently use the API: restrictions and recommendations](https://yandex.com/dev/direct/doc/en/concepts/en/optimize)
Next
[Usage](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/use-cases)
