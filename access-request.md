---
title: Lesson 3. API access: how to submit a request | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/access-request
crawled_at: 2025-09-17T15:55:52.194734
---

Lesson 3. API access: how to submit a request
# Lesson 3. API access: how to submit a request
  * [How to submit a request for access](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_submit_app)
  * [How to find out the result of your request review](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_get_result)
  * [Request review timeframes](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_processing)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_whats_now)


In this lesson, we are going to discuss the second step of enabling your app with access to Yandex Direct API: submitting a request.
Having registered your app with Yandex OAuth, you should submit a request for access to Yandex Direct API. An approved request is mandatory to perform API requests. Having received your request, we will add your app to the Yandex Direct compatible app registry to contact you as its developer: e.g., to notify you of important news or adjustments in your app operation.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/access-request_scheme.png)
There are two types of Yandex Direct API access:
  * _Trial access_ is a limited to Yandex Direct API; it allows you to run your app in the test environment (Sandbox) isolated from the real user data
  * _Full_ - full access to the Yandex Direct API; it allows your app to run both within the test environment and manage real ad campaigns.


![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/access-request_direct_types.png)
Since you are learning to work with Yandex Direct API, request trial access for your app for now. You can make a request even if you haven't created your app yet. You can convert this request to a full access request at anytime later.
Alert
  * Only the developer can submit a request for app access (as well as register the app with Yandex OAuth).
  * Your app users don't need to do this.
  * Please create a single request per each of your apps registered on Yandex OAuth: one app ID — one request for access. Once the request is approved, any number of users can run the app.


##  [](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_submit_app)How to submit a request for access
  1. Go to 
  2. Click **Get API access**.
  3. Accept the user agreement.
  4. Go to the 
  5. Click the **New request** button. In the menu that opens, select the "Trial access" request type.
  6. On the request creation form:
     * Select the app ID you have obtained while registering with Yandex OAuth in the previous lesson, from the list.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/access-request_submit_app2.png)
     * Enter an email address you currently use. We will use it to contact you when necessary.
     * Enter your app details in the other fields.
     * Confirm your compliance with the developer's user agreement.
     * Click the **Send** button.


##  [](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_get_result)How to find out the result of your request review
You can view your requests in the Yandex Direct web interface: go to the **API** section, **My requests** tab. On the tab you can:
  * track the status of your request review; if it is declined, you can see the reasons here
  * add, edit, and delete requests.


![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/access-request_get_result1.png)
##  [](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_processing)Request review timeframes
Access requests are reviewed from 10 a.m. to 7 p.m. on business days (excluding holidays in Russia). Request review can take from one hour up to three business days (during peak periods, it can take up to seven days).
##  [](https://yandex.com/dev/direct/doc/en/en/access-request#access_request_whats_now)What's next
So, you have created a request for access to Yandex Direct API. In the next lesson, you will learn how to get an OAuth token and then create and configure Sandbox. You can continue with this tutorial without having to wait until your request review is complete: you will need your approved request only later, when you proceed to making API requests.
### Was the article helpful?
YesNo
Previous
[Lesson 2. API access: how to register an app in Yandex OAuth](https://yandex.com/dev/direct/doc/en/en/register)
Next
[Lesson 4. How to get an OAuth token](https://yandex.com/dev/direct/doc/en/en/token)
