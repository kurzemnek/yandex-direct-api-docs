---
title: App registration | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/register
crawled_at: 2025-09-17T15:39:24.853081
---

Registering your app with Yandex ID
# App registration
  * [Registering your app with Yandex ID](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#oauth)
  * [Creating a request for API access](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#request)
  * [Changing a request for API access](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#modify)


The registration procedure is completed by the app developer and includes two stages:
  1. [Registering your app with Yandex ID](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#oauth)
  2. [Creating a request for API access](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#request)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#oauth)Registering your app with Yandex ID
  1. Log in on Yandex with the app developer's username.
  2. Go to <https://oauth.yandex.com/client/new>.
  3. In the registration form, enter the app parameters and click the **Create** button.  
For more information about app parameters, see the [App registration](https://yandex.com/dev/id/doc/ru/register-client) section of the Yandex ID documentation. In the **Permissions** field, select **Access to Yandex Direct API (direct:api)**. You can change the app parameters later.


As a result of registration, Yandex.OAuth generates and displays the app ID and password on the page. The app ID must be specified when creating a [request for API access](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#request). The app ID and password are necessary for getting an [access token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token) that allows the app to access the data of a specific user.
Your list of registered apps is available at <https://oauth.yandex.com/>. You can find out an app's ID and password, change app parameters, or remove an app.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#request)Creating a request for API access
  1. Log in on Yandex with the app developer's username.
  2. Go to the [My requests](https://direct.yandex.com/registered/main.pl?cmd=apiCertificationRequestList) page on the **API settings** page.
Alert
To get access to the API settings page, you must create at least one [advertising campaign](https://direct.yandex.com/registered/main.pl?cmd=editCamp&new_camp=1&mediaType=text&) in the Yandex Direct web interface.
The first time you open the API settings page, you must accept the user agreement.
  3. Click the **New request** button. In the menu that opens, select the type of request:
     * “Full access” — Request for full access to the Yandex Direct API, including the ability to manage clients' real advertising campaigns and access to the [Sandbox](https://direct.yandex.com/registered/main.pl?cmd=apiSandboxSettings).
     * “Test access” — Request for limited access to the Yandex Direct API that **only** includes access to the [Sandbox](https://direct.yandex.com/registered/main.pl?cmd=apiSandboxSettings), which is sufficient for developing and debugging an app. Later, a request for limited access can be changed to a request for full access.
  4. On the request creation form:
     * Select the app ID that was assigned during [registration on the Yandex.OAuth service](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#oauth).
     * Enter a valid email address that you currently use.
     * In the other fields, provide the most accurate and complete information about the app as possible.
     * Confirm your compliance with the user agreement.
Click the **Send** button.


The request is reviewed for up to 7 days. When a request has been reviewed, it gets the status “approved” or “rejected”.
A list of app registration requests you have created is available on the [My requests](https://direct.yandex.com/registered/main.pl?cmd=apiCertificationRequestList) tab on the **API Settings** page. You can track the status of requests being processed, and if a request is declined, you can find out the reasons for rejection, edit and delete requests, and also change a request for limited access to a request for full access.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register#modify)Changing a request for API access
Alert
You must make sure the information entered in the API access request is correct and current. If the data changed (for example, the app developer's email address has changed, or the numer of copies of the app in use has grown significantly), edit the request.
You can edit a request from the [My requests](https://direct.yandex.com/registered/main.pl?cmd=apiCertificationRequestList) tab on the **API Settings** page. After making changes to a request, it will be re-sent for processing. The parameters from the previous request will be effective until the new version of the request is approved.
### Was the article helpful?
YesNo
Previous
[Access and authorization](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/access)
Next
[Access tokens](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token)
