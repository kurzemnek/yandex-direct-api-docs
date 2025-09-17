---
title: Lesson 8. How to make changes via the API | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/modify
crawled_at: 2025-09-17T15:44:53.442834
---

Lesson 8. How to make changes via the API
# Lesson 8. How to make changes via the API
  * [How to edit object parameters](https://yandex.com/dev/direct/doc/en/en/modify#modify_red_obj_params)
  * [Sandbox practice](https://yandex.com/dev/direct/doc/en/en/modify#modify_training)
  * [Task](https://yandex.com/dev/direct/doc/en/en/modify#modify_task)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/modify#modify_whats_now)


All the data-changing methods, such as `add`, `update`, `delete`, accept an array of objects as an input. Each object contained in the request is processed separately. For example, if your app has sent a request to create 100 ads and an error has occurred to 10 of them, the other 90 ads are created successfully. The API server returns IDs for the 90 ads created, and errors for the other 10 ads.
Alert
The object ID is returned only if the operation has been completed successfully (warnings may also be issued).
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/modify_method_scheme.png)
If errors preclude request execution (for example, their format is invalid or a required parameter is missing), the request is rejected completely.
Your application must account for this while interacting with the API, to properly handle the errors returned by the server.f
##  [](https://yandex.com/dev/direct/doc/en/en/modify#modify_red_obj_params)How to edit object parameters
When using the `update` method to change an object, you do not have to pass all the object parameters. You only have to specify the object ID and the parameters to be changed. The other parameters won't change. The Yandex Direct server will check anyway the entire object and return an error if the new parameter values have invalidated the object.
##  [](https://yandex.com/dev/direct/doc/en/en/modify#modify_training)Sandbox practice
In the previous lesson, we received a list of all campaigns. Now let's continue working with one of the campaigns: enable separate bid management on search and in ad networks.
**cURL**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"update","params":{"Campaigns":[{"Id":ИДЕНТИФИКАТОР_КАМПАНИИ,"TextCampaign":{"BiddingStrategy":{"Network":{"BiddingStrategyType":"MAXIMUM_COVERAGE"}}}}]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**cURL for Windows**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"update\",\"params\":{\"Campaigns\":[{\"Id\":ИДЕНТИФИКАТОР_КАМПАНИИ,\"TextCampaign\":{\"BiddingStrategy\":{\"Network\":{\"BiddingStrategyType\":\"MAXIMUM_COVERAGE\"}}}}]}}" https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**Request**
```
    {
      "method": "update",
      "params": {
        "Campaigns": [{
          "Id": ИДЕНТИФИКАТОР_КАМПАНИИ,
          "TextCampaign": {
            "BiddingStrategy": {
              "Network": {
                "BiddingStrategyType": "MAXIMUM_COVERAGE"
              }
            }
          }
        }]
      }
    }

```

**Response**
```
    {
      "result": {
        "UpdateResults": [{
          "Id": ИДЕНТИФИКАТОР_КАМПАНИИ
        }]
      }
    }

```

##  [](https://yandex.com/dev/direct/doc/en/en/modify#modify_task)Task
We have prepared several examples for other services as well. Try to reproduce the relevant requests in the Sandbox.  
**AdGroups Service**
Add an ad group.
```
{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"add","params":{"AdGroups":[{"Name":"Новая группа","CampaignId":ИДЕНТИФИКАТОР_КАМПАНИИ,"RegionIds":[213]}]}}' https://api-sandbox.direct.yandex.com/json/v5/adgroups

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"add\",\"params\":{\"AdGroups\":[{\"Name\":\"Новая группа\",\"CampaignId\":ИДЕНТИФИКАТОР_КАМПАНИИ,\"RegionIds\":[213]}]}}" https://api-sandbox.direct.yandex.com/json/v5/adgroups

```

```
{% endcut %}

{% cut "Request" %}

```

```
    {
      "method": "add",
      "params": {
        "AdGroups": [{
          "Name": "Новая группа",
          "CampaignId": ИДЕНТИФИКАТОР_КАМПАНИИ,
          "RegionIds": [213]
        }]
      }
    }

```

```
{% endcut %}

{% cut "Response" %}

```

```
    {
      "result": {
        "AddResults": [{
          "Id": ИДЕНТИФИКАТОР_ГРУППЫ
        }]
      }
    }

```

```
{% endcut %}

```

**Service Ads**
Create ads in an ad group.
```
{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"add","params":{"Ads":[{"AdGroupId":ИДЕНТИФИКАТОР_ГРУППЫ,"TextAd":{"Title":"Заголовок объявления","Text":"Текст объявления","Mobile":"NO","Href":"http://example.com"}}]}}' https://api-sandbox.direct.yandex.com/json/v5/ads

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"add\",\"params\":{\"Ads\":[{\"AdGroupId\":ИДЕНТИФИКАТОР_ГРУППЫ,\"TextAd\":{\"Title\":\"Заголовок объявления\",\"Text\":\"Текст объявления\",\"Mobile\":\"NO\",\"Href\":\"http://example.com\"}}]}}" https://api-sandbox.direct.yandex.com/json/v5/ads

```

```
{% endcut %}

{% cut "Request" %}

```

```
    {
      "method": "add",
      "params": {
        "Ads": [{
          "AdGroupId": "ИДЕНТИФИКАТОР_ГРУППЫ",
          "TextAd": {
            "Title": "Заголовок объявления",
            "Text": "Текст объявления",
            "Mobile": "NO",
            "Href": "http://example.com"
          }
        }]
      }
    }

```

```
{% endcut %}

{% cut "Response" %}

```

```
    {
      "result": {
        "AddResults": [{
          "Id": ИДЕНТИФИКАТОР_ОБЪЯВЛЕНИЯ
        }]
      }
    }

```

```
{% endcut %}

```

**Keywords service**
Add a keyword.
```
{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"add","params":{"Keywords":[{"Keyword":"Новая фраза","AdGroupId":ИДЕНТИФИКАТОР_ГРУППЫ,"Bid":300000}]}}' https://api-sandbox.direct.yandex.com/json/v5/keywords

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"add\",\"params\":{\"Keywords\":[{\"Keyword\":\"Новая фраза\",\"AdGroupId\":ИДЕНТИФИКАТОР_ГРУППЫ,\"Bid\":300000}]}}" https://api-sandbox.direct.yandex.com/json/v5/keywords

```

```
{% endcut %}

{% cut "Request" %}

```

```
    {
      "method": "add",
      "params": {
        "Keywords": [{
          "Keyword": "Новая фраза",
          "AdGroupId": ИДЕНТИФИКАТОР_ГРУППЫ,
          "Bid": 300000
        }]
      }
    }

```

```
{% endcut %}

{% cut "Response" %}

```

```
    {
      "result": {
        "AddResults": [{
          "Id": ИДЕНТИФИКАТОР_ФРАЗЫ
        }]
      }
    }

```

```
{% endcut %}

```

**Service KeywordBids**
Change bid for a single keyword.
```
{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"set","params":{"KeywordBids":[{"KeywordId":ИДЕНТИФИКАТОР_ФРАЗЫ,"SearchBid":400000}]}}' https://api-sandbox.direct.yandex.com/json/v5/keywordbids

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"set\",\"params\":{\"KeywordBids\":[{\"KeywordId\":ИДЕНТИФИКАТОР_ФРАЗЫ,\"SearchBid\":400000}]}}" https://api-sandbox.direct.yandex.com/json/v5/keywordbids

```

```
{% endcut %}

{% cut "Request" %}

<pre >{ "method": "set", "params": { "KeywordBids": [{ "KeywordId": KEYWORD&lowbar;ID, "SearchBid": 400000 }] } }</pre>

{% endcut %}

{% cut "Response" %}

```

```
    {
      "result": {
        "SetResults": [{
          "KeywordId": ИДЕНТИФИКАТОР_ФРАЗЫ
        }]
      }
    }

```

```
{% endcut %}

```

##  [](https://yandex.com/dev/direct/doc/en/en/modify#modify_whats_now)What's next
So you have learned how to make requests in the Sandbox, both to get and change data. Now it's time to graduate from Sandbox practice to real life experience.
Copied
### Was the article helpful?
YesNo
Previous
[Lesson 7. How to get data via the API](https://yandex.com/dev/direct/doc/en/en/get)
Next
[Lesson 9. How to get to real work](https://yandex.com/dev/direct/doc/en/en/real-world)
