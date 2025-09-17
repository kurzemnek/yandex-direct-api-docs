---
title: What's new in version 5 | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/compare
crawled_at: 2025-09-17T15:53:44.569770
---

Addresses
# What's new in version 5
  * [Addresses](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#url)
    * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more)
  * [Request for API access](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#request)
  * [Authorization](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#token)
    * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more1)
  * [Working with agency clients](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#subclients)
    * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more2)
  * [Structure of objects](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#struct)
    * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more3)
  * [Working with data](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#partial-edit)
  * [Currency](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#currency)
  * [Technical limitations](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#limits)
  * [Points](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#units)
    * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more4)
  * [Request ID](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#request-id)
    * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more5)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#url)Addresses
Version 5 doesn't have universal addresses that are the same for all requests. The API version 5 consists of separate services, each with its own unique address.
The services are designed to work with specific classes of objects. For example, the `Campaigns` service is used for managing campaigns. It has the following addresses:
  * For JSON requests:
```
https://api.direct.yandex.com/json/v5/campaigns

```

  * For SOAP requests:
```
https://api.direct.yandex.com/v5/campaigns

```

  * WSDL description:
```
https://api.direct.yandex.com/v5/campaigns?wsdl

```



The addresses and methods for each of the services are listed in the API reference guide.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more)Learn more
  * [Services in version 5 of the API](https://yandex.com/dev/direct/doc/ref-v5/concepts/about.html)
  * [Sandbox addresses](https://yandex.com/dev/direct/doc/dg/concepts/sandbox.html)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#request)Request for API access
To get access to version 5 of the API, you must [submit a request](https://yandex.com/dev/direct/doc/dg/concepts/register.html) and wait for approval. This is mandatory for all applications, including those that integrated with the API before application registration was required and continued to use version 4 and Live 4 without submitting a request.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#token)Authorization
Similar to older versions of the API, version 5 requests must specify an OAuth access token that authorizes access to a specific user's data. The difference is that the access token must be passed in the HTTP `Authorization` header, not in the request body. For example:
```
Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f

```

Alert
`Bearer` is an OAuth constant. It must always be specified.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more1)Learn more
  * [Access and authorization](https://yandex.com/dev/direct/doc/dg/concepts/access.html)
  * [HTTP headers](https://yandex.com/dev/direct/doc/dg/concepts/headers.html)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#subclients)Working with agency clients
In version 5, an agency can only work with the data of a single advertiser – a client of the agency – in each request. Pass the advertiser's username in the HTTP `Client-Login` header.
For example:
```
Client-Login: agrom

```

If you need to obtain or change data for multiple advertisers, you must make a separate request for each advertiser.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more2)Learn more
  * [HTTP headers](https://yandex.com/dev/direct/doc/dg/concepts/headers.html)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#struct)Structure of objects
Sitelinks, vCards, callouts, and keywords are independent objects in version 5 of the API. There are separate services provided for working with them. This simplifies data management. For example, to change the phone number in a vCard, you don't need to edit all the ads that use it. The API version 5 also provides full support for ad groups.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more3)Learn more
  * [Objects in version 5 of the API](https://yandex.com/dev/direct/doc/dg/objects/objects.html)
  * [Method equivalents](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/methods)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#partial-edit)Working with data
Version 5 uses a completely different logic for working with objects (creating, editing, getting, and so on).
In a request to create or change multiple objects, each object is processed separately. For example, if an application sends a request to create 100 ads and some parameter values are invalid for one of them, the other 99 ads are still created successfully.
Unlike previous versions, you don't need to pass all the object parameters when editing an object. You only need to specify values for the parameters that you want to change. The other parameters won't change. The Yandex Direct server will check anyway the entire object and return an error if the new parameter values have invalidated the object.
A similar rule applies to getting data – the server only returns the object parameters requested by the application, instead of returning all the parameters. By requesting only the necessary parameters, you can significantly speed up data exchange.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#currency)Currency
In version 5, all the methods accept and return monetary values in the advertiser's currency. The `Currency` parameter, which was introduced in the Live 4 version for backward compatibility, is not used.
Alert
All monetary values (bids, strategy parameters, and others) are passed via the API as integers: the amount in the currency, multiplied by 1 000 000. For example, for a bid of 2.5 rubles, you would pass the integer 2 500 000.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#limits)Technical limitations
In versions 4 and Live 4 of the API, there was a maximum of five simultaneous requests per **user**. In version 5, up to five simultaneous requests are allowed per **advertiser**. It doesn't matter which of the advertiser's representatives or agencies makes the request.
Version 5 doesn't apply any restrictions to the number of calls of individual methods.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#units)Points
The point system in version 5 is similar to version 4 and Live 4, but there are a few differences:
  * Points are granted in regular intervals throughout the day, rather than once a day.
  * Points are deducted both for errors and for successful calls.
  * An agency can spend its own points on operations with data for a client advertiser.
  * The response to every request returns the available points remaining. You don't need to call a separate method to check the point balance.


###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more4)Learn more
  * [Points in version 5](https://yandex.com/dev/direct/doc/dg/concepts/units.html)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#request-id)Request ID
Version 5 of the API assigns each request a unique ID and returns it in the request response. Please indicate this ID when contacting the [Support service](https://yandex.com/dev/direct/doc/support/troubleshooting/issue.html).
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/compare#learn-more5)Learn more
  * [HTTP headers](https://yandex.com/dev/direct/doc/dg/concepts/headers.html)


Copied
### Was the article helpful?
YesNo
Previous
[Get statistics for a selection of rows](https://yandex.com/dev/direct/doc/en/concepts/en/python3_pyxb_stat2)
Next
[Method equivalents](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/methods)
