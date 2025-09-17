---
title: Lesson 9. How to get to real work | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/real-world
crawled_at: 2025-09-17T15:42:07.718232
---

How to get full access to the Yandex Direct API
# Lesson 9. How to get to real work
  * [How to get full access to the Yandex Direct API](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_get_access)
  * [What do I do if my request is approved but I didn't get the access.](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_no_access)
  * [Request URLs](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_addresses)
  * [OAuth tokens for the app users](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_user_tokens)
  * [Task](https://yandex.com/dev/direct/doc/en/en/real-world#modify_task)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_whats_now)
  * [Useful links](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_usfull_links)


You have learned how to work with Yandex Direct API, have practiced with campaign management in Sandbox, and, finally, having spent many hours coding, developed your first application. So what do you need to ensure that your app can run not only in Sandbox, but also handle Yandex Direct real user data?
##  [](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_get_access)How to get full access to the Yandex Direct API
Since you have already registered your application with Yandex OAuth, all you have to do is to apply for the full API access.
  1. Log in to Yandex with your developer username.
  2. Open the Yandex Direct web interface, go to **API** section, **My requests** tab.
  3. Convert the request for trial access into a full access request.


![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/real-world_get_access.gif)
When filling out the request, please do not skip the **Technical app info** section. Make sure to specify accurate data there. In the **Describe diagram of interaction between your app and Direct** section, indicate your API interaction scenario. You do not need to attach your app code or complete SOW with algorithms (this is your company's trade secret). It is sufficient to describe the services and Yandex Direct API methods used by your app, the sequence of method invocation, and frequency of call for each method (every minute, every hour, etc.), and the purpose behind chosing this frequency. Tell us how the application accounts for Yandex Direct API limitations and handles errors. Based on this data we can see whether your app interacts correctly with the API and also notify you of the API changes affecting your app.
##  [](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_no_access)What do I do if my request is approved but I didn't get the access.
If you get an error in response to your API request, check your request destination URL: probably, you are trying to access a wrong API version or wrong service. Make sure that you have obtained the token for the same Yandex Direct user whose data the app is accessing.
##  [](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_addresses)Request URLs
URLs for real advertising materials are different from the Sandbox URLs. Make sure to change URLs in the app:
  * For JSON requests — `https://api.direct.yandex.com/json/v5/{service}`
  * For SOAP requests — `https://api.direct.yandex.com/v5 /{service}`
  * A WSDL description is available at URL: `https://api.direct.yandex.com/v5/{service}?wsdl`


Here `{service}` is the name of the service you want to access.
Some methods from the previous Yandex Direct API versions are available now also. URLs from previous versions differ from version 5 addresses.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/real-world_adr_questions.png)
##  [](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_user_tokens)OAuth tokens for the app users
In previous lessons, you used a debug token received manually in your API requests. Now you need to implement a mechanism allowing real users easily get the tokens. From the user's viewpoint, obtaining a token should look as follows:
  1. The app opens an access request page of the Yandex OAuth service.
  2. The user must log into Yandex under their Yandex Direct username (if logged off).
  3. On the access request page, the user clicks **Allow**.
  4. Depending on the app settings, Yandex OAuth redirects the user to the URL specified in the **Callback URL** parameter or returns the user to the app.


Yandex OAuth generates a token and transmits it to the application automatically. Yandex OAuth has multiple methods of passing the token for different types of applications, including web services, desktop programs, and mobile apps. All of these methods are detailed in the Yandex OAuth documentation.
##  [](https://yandex.com/dev/direct/doc/en/en/real-world#modify_task)Task
  1. Submit a request for full access to the Yandex Direct API.
  2. Register a test Yandex Direct user. For this new user, create an advertising campaign in the web interface and accept the user agreement in the **API** section.
  3. Get an OAuth token for the test user.
  4. Get real campaigns of the test user: make an API request on behalf of this user.


##  [](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_whats_now)What's next
Now you know how to manage real ads using the Yandex Direct API. In the next lesson, you will learn about the restriction system used in the API and see a recommended app use case.
##  [](https://yandex.com/dev/direct/doc/en/en/real-world#real-world_usfull_links)Useful links
Copied
### Was the article helpful?
YesNo
Previous
[Lesson 8. How to make changes via the API](https://yandex.com/dev/direct/doc/en/en/modify)
Next
[Lesson 10. How to efficiently use the API: restrictions and recommendations](https://yandex.com/dev/direct/doc/en/en/optimize)
