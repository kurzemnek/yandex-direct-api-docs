---
title: For agencies | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/agency
crawled_at: 2025-09-17T15:46:17.634239
---

Managing clients' advertising campaigns
# For agencies
  * [Managing clients' advertising campaigns](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#client-login)
  * [Managing clients](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#agencyclients)
  * [Getting agency parameters and representative settings](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#own)
  * [Agency points](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#points)


In Yandex Direct, advertisers are hierarchically subordinate to the agency that they are clients of. Agency representatives can manage agency clients and their advertising campaigns. An agency can be used as a manager account for accessing multiple client accounts (like an MCC).
####  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#learn-more)Learn more
  * [Client](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/client)
  * [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/roles)


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#client-login)Managing clients' advertising campaigns
An agency can manage the data of its advertiser clients (such as campaigns or ads) by sending requests to Yandex Direct API services on behalf of the agency representative. To do this:
  * In the `Authorization` header, specify the access token you received for the agency representative.
  * In the `Client-Login` header, specify the username of the representative of the client advertiser.


For example:
```
Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f
Client-Login: agrom

```

An agency can only work with the data of a single advertiser in each request. If you need to obtain or change data for multiple advertisers, you must make a separate request for each advertiser.
Exceptions:
  * In requests to the `Client-Login` HTTP header.
  * When calling the `Client-Login` header, specify the username of an agency representative, or specify the username of an advertiser representative.
  * When calling `Client-Login` header is optional.


####  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#learn-more1)Learn more
  * [HTTP headers](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/headers)
  * [Access tokens](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/auth-token)


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#agencyclients)Managing clients
Requests to the 
An agency representative can:
  * Get a list of advertisers that are an agency's clients, their parameters, and settings for each advertiser's chief representative using the 
  * Register new advertisers (agency clients) using the 
  * Change the parameters of advertisers (agency clients) and the settings of their chief representatives using the 


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#own)Getting agency parameters and representative settings
Using the 
  * Any agency representative can also get the agency parameters and their own personal settings.
  * The agency's chief representative can also get and edit the settings of another representative (in addition to their own settings). To do this, pass the representative's username in the `Client-Login` request header.


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#points)Agency points
"Points" belong to both the advertiser and the agency. By default, making API requests in the name of an agency representative spends the points of the agency's client advertiser (if the `Client-Login` header is specified). To use the agency's points, you need to set up the HTTP header
```
Use-Operator-Units: true

```

The agency makes its own decision on when to spend its own points, and when to spend a client's points. For example, an agency can use its points to:
  * Create advertising campaigns and ads for a new client who hasn't accumulated enough points yet.
  * Manage campaigns for an active client who has run out of points.


####  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/agency#learn-more2)Learn more
  * [Restrictions, points](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/units)


Copied
### Was the article helpful?
YesNo
Previous
[Recommendations for registering representatives](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/representatives-recommendations)
Next
[Sandbox](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/sandbox)
