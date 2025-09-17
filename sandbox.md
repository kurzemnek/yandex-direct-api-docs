---
title: Lesson 5. How to enable Sandbox | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/sandbox
crawled_at: 2025-09-17T15:52:45.246903
---

What is Sandbox?
# Lesson 5. How to enable Sandbox
  * [What is Sandbox?](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_whats_sandbox)
  * [How to enable](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_connect)
  * [Working with Sandbox](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_feachures)
  * [Task](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_task)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_whats_now)
  * [Useful links](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_usfull_links)


In this lesson you will learn to access Yandex Direct via the API without the risk to launch a real advertising campaign with a real budget.
##  [](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_whats_sandbox)What is Sandbox?
_Sandbox_ is a test environment used to debug apps accessing Yandex Direct API. In Sandbox, you can make requests, get responses, and monitor status of campaigns and ads. However, in Sandbox you are working with the **test data only** , and your actions will not affect your real advertising campaigns. Test ads are never served, the test budget does not affect your real account in Yandex Direct, while the statistical report contains some pseudorandom data.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/sandbox_whats_sandbox1.png)
Your app's requests to the Sandbox must be in the same format as your real data requests. Sandbox uses real OAuth tokens. The only difference between the Sandbox requests and real data requests are the URLs they use.
Sandbox **has no web interface** , hence you can not see test clients and test ad campaigns in the interface. You can only work with the Sandbox by calling API methods.
##  [](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_connect)How to enable
To enable Sandbox for your account, do the following:
  1. In the Yandex Direct web interface, open the **API** section and go to the 
  2. Click the **Launch sandbox** link.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/sandbox_connect1.png)
  3. Choose a role: "Client" (direct advertiser) or "Agency" (advertising agency with its clients). Specify the currency for the test account. Select the **Create test campaigns** checkbox.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/sandbox_connect2.png)
  4. Click the **Continue** button.
Depending on the role you have selected, three test campaigns or three test clients are created immediately in Sandbox. Virtual money will be credited to one of the campaigns.


##  [](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_feachures)Working with Sandbox
  * The Sandbox is active while you are using it. If no requests have been sent to the Sandbox over a month, your test accounts and all their settings are deleted. You will have to set up the test data again.
  * If you want to disable the Sandbox, click the **Stop using Sandbox** link.
  * If you switch the role, the test data is deleted and the Sandbox is created from scratch.


##  [](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_task)Task
Enable Sandbox with the "Client" role, creating the client account in rubles with preset test campaigns.
##  [](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_whats_now)What's next
So you have completed all the preparation steps and are ready to start working with Yandex Direct API. In the next lesson, you will make your first request to the API.
##  [](https://yandex.com/dev/direct/doc/en/en/sandbox#sandbox_usfull_links)Useful links
### Was the article helpful?
YesNo
Previous
[Lesson 4. How to get an OAuth token](https://yandex.com/dev/direct/doc/en/en/token)
Next
[Lesson 6. How to make an API request](https://yandex.com/dev/direct/doc/en/en/format)
