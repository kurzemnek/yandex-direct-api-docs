---
title: Request for access | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/troubleshooting/register
crawled_at: 2025-09-17T16:02:35.839670
---

Who should submit the request?
# Request for access
  * [Who should submit the request?](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#request)
  * [What username should I use to submit the request?](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#what-username-should-i-use-to-submit-the-request)
  * [How long does it take to process the access request?](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#how-long-does-it-take-to-process-the-access-request)
  * [I submitted three access requests and two of them were rejected](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#i-submitted-three-access-requests-and-two-of-them-were-rejected)
  * [I don't see my application in the “My applications” list](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#i-dont-see-my-application-in-the-my-applications-list)
  * [My access request was approved, but I get the error code 58 when I send a request](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#my-access-request-was-approved,-but-i-get-the-error-code-58-when-i-send-a-request)


For information on registering an application and submitting a request for access to the Yandex Direct API, see the section [App registration](https://yandex.com/dev/direct/doc/dg/concepts/register.html) in the Developer's guide.
Here are answers to some common questions about submitting the access request:
##  [](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#request)Who should submit the request?
The application developer registers the application on the Yandex.OAuth service and submits a request for access to the Yandex Direct API. Application users don't need to do this.
If you purchased or use a ready-made program, you do not need to register the application or submit the access request.
##  [](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#what-username-should-i-use-to-submit-the-request)What username should I use to submit the request?
To register an application and create an access request, log in on Yandex using the application developer's username.
If the application is developed and used by an advertising agency, you can use the agency's chief representative username.
##  [](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#how-long-does-it-take-to-process-the-access-request)How long does it take to process the access request?
Access requests are reviewed from 10 a.m. to 7 p.m. on business days (excluding holidays in Russia). Request review can take from one hour up to three business days (during peak periods, it can take up to seven days).
##  [](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#i-submitted-three-access-requests-and-two-of-them-were-rejected)I submitted three access requests and two of them were rejected
You only need to register your application and submit an access request one time, regardless of how many instances of the application you have. Submit only one access request per application registered in Yandex OAuth. Once the request is approved, any number of users can work with your application.
##  [](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#i-dont-see-my-application-in-the-my-applications-list)I don't see my application in the “My applications” list
On the **API settings** page, in the [Authorization token](https://yandex.com/dev/direct/doc/dg/concepts/auth-token.html)).
To see the list of applications that you have registered as a developer, go to these pages:
  * Applications for which you have requested access to the Yandex Direct API are in the **API settings** page.
  * All the applications that you have registered in Yandex OAuth can be found at 


##  [](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/register#my-access-request-was-approved,-but-i-get-the-error-code-58-when-i-send-a-request)My access request was approved, but I get the error code 58 when I send a request
Go to the **API settings** page and check which type of access you requested. If you requested test access, you can only send requests to the sandbox at `https://**api-sandbox**.direct.yandex.com/...`
![](https://yandex.com/dev/direct/doc/en/troubleshooting/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/test-request.png)
To make requests using real user data at `https://**api**.direct.yandex.com/...`, change your request for test access to a request for full access.
If you have more questions, contact us using the form below. Please explain your question and the situation in as much detail as possible so that we can give you a comprehensive answer.
Feedback
Copied
### Was the article helpful?
YesNo
Previous
[Error calling a Yandex Direct API method](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/issue)
Next
[Yandex Direct API restrictions](https://yandex.com/dev/direct/doc/en/troubleshooting/en/troubleshooting/limits)
