---
title: Quick start | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/quick-start
crawled_at: 2025-09-17T15:40:18.674559
---

App registration
# Quick start
  * [App registration](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/quick-start#connection)
  * [Debugging with test data](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/quick-start#sandbox)
  * [Switching to using real user data](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/quick-start#real-world)


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/quick-start#connection)App registration
  1. Create an account in Yandex Direct that you will use as an application developer:
    1. If you don't have a Yandex username, [register](https://passport.yandex.com/registration?mode=register).
    2. In the Yandex Direct web interface, [create an account ](https://direct.yandex.com/registered/main.pl?cmd=advertize): enter a valid email address, choose your country and currency, and click **Get started**.
    3. On the [API Settings](https://direct.yandex.com/registered/main.pl?cmd=apiSettings) page, click **Get API access** and accept the user agreement.
  2. [Register](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/register#oauth) your app on the Yandex.OAuth server.
  3. [Submit a request](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/register#request) for test access for your application. Wait for your request to be approved.


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/quick-start#sandbox)Debugging with test data
You can use your developer account as a test user. You can also create a special test user (repeat steps above).
  1. Get a [debugging OAuth token](https://yandex.com/dev/id/doc/ru/access) on behalf of the test user.
  2. Enable the [Sandbox](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/sandbox-init), which is an application debugging environment where you can manage test campaigns without actual impressions and spending.
  3. Send HTTP POST requests to the Sandbox using the debugging token. Request example: 
```
 -H 'Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f' \
 -H 'Accept-Language: en' \
 -d '
   {
     "method":"get",
     "params": {
       "SelectionCriteria": {},
       "FieldNames": [
         "Name",
         "DailyBudget",
         "Funds",
         "Statistics",
         "Type"
       ],
       "TextCampaignFieldNames": [
         "CounterIds",
         "RelevantKeywords",
         "Settings",
         "BiddingStrategy"
       ]
     }
   }' \
 "https://api-sandbox.direct.yandex.com/json/v5/campaigns"

```



##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/quick-start#real-world)Switching to using real user data
  1. In your application, implement a [way to get a token](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/auth-token#get-token) that is convenient for your users.
  2. [Switch](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/register#modify) the request for test access to full access. Wait for your request to be approved.
  3. In your application, replace the sandbox addresses with the real addresses. The address for each service is provided in the service description.


### Was the article helpful?
YesNo
Previous
[Usage](https://yandex.com/dev/direct/doc/en/best-practice/en/concepts/use-cases)
Next
[Main objects](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/objects)
