---
title: Client | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/client
crawled_at: 2025-09-17T15:42:51.060343
---

Client
# Client
  * [Yandex Direct users and their roles](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#user)
    * [Learn more](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#learn-more)
  * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#service)
    * [For advertisers](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#service-advertisers)
    * [For agencies](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#service-agencies)


The Client object corresponds to an advertiser or advertising agency.
Advertisers are divided into direct advertisers and agency clients.
Advertising campaigns belong to the advertiser.
Advertisers are logically subordinate to the agency that they are clients of.
![client-types](https://yandex.com/dev/direct/doc/en/objects/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_images/client-types.png)
An advertiser's campaigns are managed by Yandex Direct users in accordance with the assigned role.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#user)Yandex Direct users and their roles
A user who has a Yandex username becomes a Yandex Direct user (gets a Yandex Direct account) when this user becomes the **representative** of an advertiser or agency, meaning one of the following roles is assigned:
  * Chief representative of an advertiser.
  * Representative of an advertiser.
  * Chief representative of an agency.
  * Representative of an agency.
  * Agency client representative.


For example:
  * The user creates an account in Yandex Direct by selecting a country and currency. This creates an advertiser that is a direct client, and the user becomes the chief representative of this advertiser.
  * An agency representative registers a username for the new client in Yandex Direct. This creates an advertiser that is an agency's client, and the user with the specified username becomes the chief representative for this advertiser.
  * A different user assigns the user as a representative of an advertiser or agency.


If a Yandex user is not a Yandex Direct user, you can still get an OAuth token for the user, but requests to the Yandex Direct API on behalf of this user will result in an error.
Alert
The user's ID is the Yandex username. When we refer to the username of the advertiser or the agency, we mean the username of the chief representative. The advertiser's ID is `ClientId`.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#learn-more)Learn more
  * [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles)
  * [Recommendations for registering representatives](https://yandex.com/dev/direct/doc/en/objects/en/objects/representatives-recommendations)


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#service)Methods
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#service-advertisers)For advertisers
For managing advertiser parameters and user settings for the advertiser's representative, use the 
Methods: 
Any advertiser representative can get and edit the advertiser's parameters as well as their own settings.
The advertiser's chief representative can also get and edit the settings of another representative (in addition to their own settings). To do this, pass the representative's username in the `Client-Login` request header.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/client#service-agencies)For agencies
For managing advertisers who are agency clients, use the 
Methods: 
The 
For details, see the section [For agencies](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/agency).
Copied
### Was the article helpful?
YesNo
Previous
[Ad target for dynamic ads (DynamicTextAdTarget — Webpage)](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget)
Next
[SharedAccount](https://yandex.com/dev/direct/doc/en/objects/en/objects/shared-account)
