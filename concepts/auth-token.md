---
title: Access tokens | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/auth-token
crawled_at: 2025-09-17T15:39:31.164476
---

App registration
# Access tokens
  * [App registration](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#register)
  * [Getting a token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#get-token)
    * [Getting a token manually](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#getting-a-token-manually)
    * [Getting a token automatically](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#getting-a-token-automatically)
    * [Which method should I choose for getting a token?](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#which-method-should-i-choose-for-getting-a-token)
  * [Using the token when calling methods](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#use-token)
  * [Discontinuation of a token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#new-token-required)


The access token, or OAuth token, is a special code that grants access to a specific user's data. You need to get a separate token for each Yandex Direct user you make API requests for.
The token must be specified in every API request. The Yandex Direct server uses the token to determine the user the app is making a request for and to check whether this user actually granted access to their personal data in Yandex Direct to this app. The app can only perform the actions that are allowed for the user the token was issued for.
For more information, see the [Yandex.OAuth guide](https://yandex.com/dev/id/doc/ru/).
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#register)App registration
You only need to register your app with Yandex ID once. To do this, log in on Yandex with the app developer's username. For more information, see [Registering your app with Yandex ID](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register) under [App registration](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register).
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#get-token)Getting a token
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#getting-a-token-manually)Getting a token manually
At the app debugging stage, you can get a so-called debugging token in the name of a test user. See [Debugging token](https://yandex.com/dev/id/doc/ru/tokens/debug-token) in the Yandex ID documentation.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#getting-a-token-automatically)Getting a token automatically
When you are ready to begin working with real user data, you need to implement a user-friendly way to get tokens in the application. To get a token, the application should redirect the user to a special access request page in Yandex ID. The user logs in to Yandex (with their login for Yandex Direct) and clicks the Allow button to grant the application access to their personal data. Yandex.OAuth generates a token and transmits it to the application automatically.
Yandex ID offers multiple token delivery methods that support different types of applications, including web services, desktop programs, and mobile apps. For more information about token delivery methods, see the [Yandex ID documentation](https://yandex.com/dev/id/doc/ru/).
See also: [PHP example](https://yandex.com/dev/direct/doc/examples-v5/php5-file_get_contents-token.html), [Python example](https://yandex.com/dev/direct/doc/examples-v5/python3-requests-token.html).
Alert
Regardless of whether the token is obtained manually or automatically, it allows you to manage the user's real advertising materials.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#which-method-should-i-choose-for-getting-a-token)Which method should I choose for getting a token?
In some cases, you can use tokens that you obtain manually after you switch to working with real user data. For example:
  * If the application only has a small number of users, who are representatives of a single advertiser.
  * If the application doesn't interact with the user. For example, this is a script for automatically updating bids.


Tokens should be obtained automatically if the application is accessed by multiple advertisers or a large number of users with different access rights.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#use-token)Using the token when calling methods
The token obtained for a user must be specified in the HTTP `Authorization` header for every request to the Yandex Direct API on behalf of this user.
If an invalid token is specified, an error message is returned with the code [1002](https://yandex.com/dev/direct/doc/ref-v5/concepts/errors-list.html#errors-list__e1002).
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token#new-token-required)Discontinuation of a token
The scenarios when a token may become invalid and a new one must be obtained are listed in the [Revoking tokens](https://yandex.com/dev/id/doc/ru/tokens/token-invalidate) section of the Yandex ID documentation.
Tip
If you are using an application, we recommend that you register a special representative in Yandex Direct and obtain a token for the representative. See [Recommendations for registering representatives](https://yandex.com/dev/direct/doc/en/concepts/en/objects/representatives-recommendations).
Copied
### Was the article helpful?
YesNo
Previous
[App registration](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register)
Next
[Roles and access of Yandex.Direct users](https://yandex.com/dev/direct/doc/en/concepts/en/objects/roles)
