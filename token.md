---
title: Lesson 4. How to get an OAuth token | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/token
crawled_at: 2025-09-17T15:54:14.396042
---

Lesson 4. How to get an OAuth token
# Lesson 4. How to get an OAuth token
  * [How to get an OAuth token manually](https://yandex.com/dev/direct/doc/en/en/token#token_how_get)
  * [Why can the OAuth token stop working](https://yandex.com/dev/direct/doc/en/en/token#token_why_expire)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/token#token_whats_now)
  * [Useful links](https://yandex.com/dev/direct/doc/en/en/token#token_usfull_links)


In this lesson, you will learn more about OAuth tokens, how to get them and use them.
From the previous lessons, you already know that Yandex Direct API uses OAuth authorization. Remember that you must specify your OAuth token in every API request. The token encrypts information both about the app and user. The token is used in order to determine, on behalf of which Yandex Direct user the app executes the query; if the user has authorized the app to access their data in Yandex Direct; if the user is authorized to access the requested ads.
Hence, when accessing Yandex Direct via the API, you do not need to pass the user account password. It is sufficient to pass the OAuth token: it makes the interaction with the Yandex Direct API more secure. However, it is important to keep in mind that you need to get a separate token for each user of your app.
At the initial stages of app development, you only need to manually obtain a so-called debugging token. Later, when you roll out your app into production, you should implement a user-friendly way to get a token from within the app: the user clicks **Allow** in the Yandex OAuth web interface, and Yandex OAuth returns the token to your app automatically.
Please note that the manually obtained token is in no way different from the automatically obtained one. With the token you can manage the user's real advertising materials, regardless of how the token was obtained.
##  [](https://yandex.com/dev/direct/doc/en/en/token#token_how_get)How to get an OAuth token manually
In the previous lesson, you registered your app on Yandex OAuth, adding the development URL to the **Callback URI #1** field. If you haven't done so (by leaving the field blank or entering a different value), go to Yandex OAuth (**Web services** checkbox, click the **Set URL for development** , and save the changes. Now you can manually get a token for the test user.
As a test user, you can use the same developer account you have used to register your app and apply for access. We'll focus on this very option in this tutorial.
To get a token manually, follow these steps:
  1. Log in to Yandex with your username.
  2. Follow link
`https://oauth.yandex.ru/authorize?response_type=token&client_id=APPLICATION_ID`
(put your app identifier instead of `APP_ID`).
  3. On the page that opens, click **Allow**.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/token_get1.png)
  4. Yandex OAuth redirects you to the page displaying the token. The token is also added to the URL shown in the address bar. Copy the token to use it in your API requests.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/token_get2.png)


Alert
  * Do not share the token with anyone: one can use it to access the user's data in Yandex Direct.
  * You can create a separate test user account (or multiple accounts). For a new user, you must create an account in the Yandex Direct web interface, having selected the country and payment currency, and accepted the user agreement in the **API** section. To get a token for the user, log in to Yandex using their username and repeat the above procedure.


Tip
If you couldn't get a token for some reason, follow the 
##  [](https://yandex.com/dev/direct/doc/en/en/token#token_why_expire)Why can the OAuth token stop working
The token may expire over time, so you may need to get a new one.
All the user's tokens are revoked if:
  * the user has changed their Yandex password
  * the user clicked the **Log out of all computers** link.


A token issued for a specific app is revoked if:
  * the user revoked the app access to their data (this feature is available in the Yandex Passport web interface)
  * the app developer changed the access rights for their app
  * the token has expired.


For the full list of situations when Yandex OAuth revokes tokens, see the Yandex OAuth documentation.
##  [](https://yandex.com/dev/direct/doc/en/en/token#token_whats_now)What's next
So you have received a token you can use to make the API requests. The last preparation stage is ahead: create and configure Sandbox, a test environment for app debugging. Then we will proceed directly to making API requests.
##  [](https://yandex.com/dev/direct/doc/en/en/token#token_usfull_links)Useful links
Yandex OAuth documentation:
Copied
### Was the article helpful?
YesNo
Previous
[Lesson 3. API access: how to submit a request](https://yandex.com/dev/direct/doc/en/en/access-request)
Next
[Lesson 5. How to enable Sandbox](https://yandex.com/dev/direct/doc/en/en/sandbox)
