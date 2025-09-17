---
title: List of terms | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/glossary
crawled_at: 2025-09-17T15:37:41.126630
---

List of terms
# List of terms
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#oauth)OAuth token
A code that grants the [application](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#app) access to the [user's](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#user) data. The token is a string with encoded data: the username, the application ID, and the set of action permissions granted to the application.
The OAuth token must be specified in every request sent to the Yandex Direct API.
See the section [Access tokens](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token).
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#auth-token)Access token
The same as an [OAuth token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#oauth).
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#client)Client
An advertiser or advertising agency.
Advertisers are divided into direct advertisers and agency clients.
The client identifier is `ClientId`.
See the [Client](https://yandex.com/dev/direct/doc/en/concepts/en/objects/client) section.
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#master-token)Master token
A code that the user obtained in the Yandex Direct web interface. It is used for generating [finance tokens](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#finance-token)
See [Accessing finance methods](https://yandex.com/dev/direct/doc/dg-v4/concepts/finance-token.html) in the documentation for the API version 4 and Live 4.
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#debug-token)Debugging token
An [OAuth token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#oauth) that is obtained manually. It is normally used for debugging an application, but it does allow access to real user data.
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#user)Yandex Direct user
A user who has an account in Yandex Direct.
The [application](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#app) sends requests to the Yandex Direct API on behalf of a Yandex Direct user.
The user's ID is their Yandex username.
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#representative)Representative
A Yandex Direct user who has one of the following roles:
  * Chief representative of an advertiser.
  * Representative of an advertiser.
  * Chief representative of an agency.
  * Representative of an agency.
  * Agency client representative.


See the sections [Yandex Direct users and their roles](https://yandex.com/dev/direct/doc/en/concepts/en/objects/client#user) and [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/en/concepts/en/objects/roles).
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#app)Application
A program, mobile app, script, or web service that interacts with the Yandex Direct API.
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#finance-token)Finance token
A code that is used to increase the security of financial transactions: generating invoices, transferring funds, and making payments using credit or overdraft. The finance token must be specified in addition to the [OAuth token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary#oauth) when calling finance methods.
See [Accessing finance methods](https://yandex.com/dev/direct/doc/dg-v4/concepts/finance-token.html) in the documentation for the API version 4 and Live 4.
Copied
### Was the article helpful?
YesNo
Previous
[Managing the Sandbox](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox-init)
Next
[AdExtensions: operations with ad extensions](https://yandex.com/dev/direct/doc/en/concepts/en/adextensions/adextensions)
