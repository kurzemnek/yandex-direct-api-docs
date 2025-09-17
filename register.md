---
title: Lesson 2. API access: how to register an app in Yandex OAuth | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/register
crawled_at: 2025-09-17T15:56:50.229997
---

What is OAuth authorization and OAuth token?
# Lesson 2. API access: how to register an app in Yandex OAuth
  * [What is OAuth authorization and OAuth token?](https://yandex.com/dev/direct/doc/en/en/register#register_whats_apiauth_token)
  * [How to register an app in Yandex OAuth](https://yandex.com/dev/direct/doc/en/en/register#register_reg_application)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/register#register_whats_now)
  * [Useful links](https://yandex.com/dev/direct/doc/en/en/register#register_usfull_links)


In this lesson, you will learn about the first step of getting access to Yandex Direct API for your app: registering your app in Yandex OAuth. The second step, requesting access, is covered in the next lesson.
In the previous lesson, you created your app developer account in Yandex Direct. Now you need to register your app with Yandex OAuth (you can do this even before creating your app).
##  [](https://yandex.com/dev/direct/doc/en/en/register#register_whats_apiauth_token)What is OAuth authorization and OAuth token?
_OAuth authorization_ is a mechanism that allows an application to work with the user data on their behalf without using the account password.
The authorization process uses OAuth tokens which are strings containing encrypted data:
  * user ID
  * ID of the app allowed to access user data in the service
  * set of permissions, i.e., actions permitted to the app.


To work with Yandex Direct API, your application must be registered with Yandex OAuth. After that, the user can allow the app to access their ads, and the app can get an OAuth token. The token must be specified in every API request: this way Yandex Direct can recognize the account the app is accessing and can check permissions for the actions to be done.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/register_whats_auth.png)
Alert
  * Each token is unique, as it is issued for an "app + user" pair. You can not get two identical tokens or get more than one token for the same app-user pair.
  * If an app fails to pass the token in the API request, the server won't allow the app to get or change any data.


##  [](https://yandex.com/dev/direct/doc/en/en/register#register_reg_application)How to register an app in Yandex OAuth
Log in to Yandex with your developer username. In Yandex OAuth, open the 
  * **Service name** : Name to display to all users of your service. You can also attach your service icon.
  * **Platforms** : Enable **Web services**. In **Redirect URI** , specify the link to redirect the user to once they allow or deny the app access.


![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/oauth-common.png)
**Data access**
Specify the source of data for managing ads:
  * **Working with Yandex ID organizations (passport:business)** , to get access to authorization on behalf a Yandex ID organization.
  * **Using the Yandex Direct API (direct:api)** , to get access to managing advertising materials. You can enter part of the name and then choose the appropriate one from the list.


Note
If you want the app to access data of other Yandex services, for example, Yandex Metrica, you can also select relevant accesses. In this tutorial, we focus on access to Yandex Direct data only.
  * **Email address** : Specify your personal or corporate email address.


![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/oauth-data-access.png)
After filling in the fields, click **Create app**. The page will show the ID assigned to the app and the secret that the access token will be signed with. You will need the app ID to fill out the API access application form and to obtain the token. You can look up the ID and other parameters in the Yandex OAuth web interface anytime.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/oauth-client-id.png)
Alert
Only the developer has to register the app with Yandex OAuth. Users of your app do not need to do this, even if each user is working with their own instance (copy) of the app.
##  [](https://yandex.com/dev/direct/doc/en/en/register#register_whats_now)What's next
So, you took your first step in getting access to Yandex Direct API: registered your app in Yandex OAuth. In the next lesson, you will learn how to request the API access, and then how to get an OAuth token.
##  [](https://yandex.com/dev/direct/doc/en/en/register#register_usfull_links)Useful links
  * Yandex OAuth documentation: 


### Was the article helpful?
YesNo
Previous
[Lesson 1. What is Yandex Direct API](https://yandex.com/dev/direct/doc/en/en/intro)
Next
[Lesson 3. API access: how to submit a request](https://yandex.com/dev/direct/doc/en/en/access-request)
