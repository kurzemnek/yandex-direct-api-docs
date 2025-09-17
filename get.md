---
title: Lesson 7. How to get data via the API | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/get
crawled_at: 2025-09-17T15:47:29.527492
---

Lesson 7. How to get data via the API
# Lesson 7. How to get data via the API
  * [How to get objects](https://yandex.com/dev/direct/doc/en/en/get#get_get_obj)
  * [Sandbox practice](https://yandex.com/dev/direct/doc/en/en/get#get_training)
  * [Task](https://yandex.com/dev/direct/doc/en/en/get#get_task)
  * [What's next](https://yandex.com/dev/direct/doc/en/en/get#get_whats_now)


In this lesson, you will learn about the API structure and look at some examples of getting data.
Let's remember how objects are linked in the Yandex Direct API (see Lesson 1):
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_objects_scheme.png)
The API provides a service for each object class: `Campaigns` for managing campaigns, `AdGroups` for managing ad groups, `Ads` for managing ads, and others. You can find the full list of services in the documentation.
The logic of working with the API objects is unified, with all the service methods assigned standard names. A service typically includes the following methods:
  * `add` — Adding objects.
  * `update` — Changing object parameters.
  * `delete` — Deleting objects.
  * `get` - Getting objects.


A service can also have other methods. For example, the `Campaigns` service provides the following methods:
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/get_methods.png)
##  [](https://yandex.com/dev/direct/doc/en/en/get#get_get_obj)How to get objects
Let's look how you can get ad campaign parameters using the `get` method.
The `get` method is designed so that you can request only the data you need. For example, for campaigns you can get their IDs and names only, rather than all their parameters. List the names of the parameters you need in the `FieldNames` input parameter.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/get_params.png)
Use the `SelectionCriteria` input structure to set criteria for selecting objects. If there are several selection criteria, the server searches for objects fitting all the criteria at once. Some services allow you to specify an empty `SelectionCriteria` structure: in this case, all objects are returned.
##  [](https://yandex.com/dev/direct/doc/en/en/get#get_training)Sandbox practice
Let's remember a query example from the previous lesson. In that example, we got an entire list of campaigns by specifying an empty `SelectionCriteria` structure, getting only an ID and name for each campaign by specifying relevant parameters in `FieldNames`.
Alert
Don't forget to change the token and IDs used in the examples to your own data.
**cURL**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{},"FieldNames":["Id","Name"]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**cURL for Windows**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"get\",\"params\":{\"SelectionCriteria\":{},\"FieldNames\":[\"Id\",\"Name\"]}}" https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**Request**
```
    {
      "method": "get",
      "params": {
        "SelectionCriteria": {},
        "FieldNames": ["Id", "Name"]
      }
    }

```

**Response**
```
    {
      "result": {
        "Campaigns": [{
          "Name": "Test API Sandbox campaign 1",
          "Id": 1234567
        }, {
          "Name": "Test API Sandbox campaign 2",
          "Id": 1234578
        }, {
          "Name": "Test API Sandbox campaign 3",
          "Id": 1234589
        }]
      }
    }

```

Some campaign parameters (such as name and ID) are shared across all campaign types, while some of them (such as display strategies) depend on the campaign type. In the following example, we only get campaigns with the "Text & Image Ads" type. To get display strategies for those campaigns, specify the relevant parameter name in the `TextCampaignFieldNames` input parameter .
**cURL**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{ "Types": ["TEXT_CAMPAIGN"]},"FieldNames":["Id","Name"],"TextCampaignFieldNames":["BiddingStrategy"]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**cURL for Windows**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"get\",\"params\":{\"SelectionCriteria\":{ \"Types\": [\"TEXT_CAMPAIGN\"]},\"FieldNames\":[\"Id\",\"Name\"],\"TextCampaignFieldNames\":[\"BiddingStrategy\"]}}" https://api-sandbox.direct.yandex.com/json/v5/campaigns

```

**Request**
```
    {
      "method": "get",
      "params": {
        "SelectionCriteria": {
          "Types": ["TEXT_CAMPAIGN"]
        },
        "FieldNames": ["Id", "Name"],
        "TextCampaignFieldNames": ["BiddingStrategy"]
      }
    }

```

**Response**
```
    {
      "result": {
        "Campaigns": [{
          "Id": 1234567,
          "Name": "Test API Sandbox campaign 1",
          "TextCampaign": {
            "BiddingStrategy": {
              "Search": {
                "BiddingStrategyType": "HIGHEST_POSITION"
              }, 
              "Network": {
                "BiddingStrategyType":"NETWORK_DEFAULT",
                "NetworkDefault": {
                  "LimitPercent": 100
                }
              } 
            }
          }
        }]
      }
    }

```

**Paginated selection**
If you are working with large data arrays, all the objects might not fit in a single request response, since the `get` method returns a maximum of 10,000 objects. In this case, the `get` method returns the `LimitedBy` parameter with a sequential number of the last object returned. If you get this parameter, this indicates that not all objects were received.
To set up paginated selection parameters, use the `Page` input structure. Specify the number of objects to select (for example, 10) and the number of objects to be skipped before the selection (for example, 20); as a result, you will get a range of data, i.e., 10 objects from 21st to 30th.
##  [](https://yandex.com/dev/direct/doc/en/en/get#get_task)Task
We have prepared several examples for other services as well. Try to reproduce the relevant requests in the Sandbox.
**AdGroups Service**
Get a list of ad groups from a campaign.
```
{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{"CampaignIds":[ИДЕНТИФИКАТОР_КАМПАНИИ]},"FieldNames":["Id","Name","Status","Type"]}}' https://api-sandbox.direct.yandex.com/json/v5/adgroups

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"get\",\"params\":{\"SelectionCriteria\":{\"CampaignIds\":[ИДЕНТИФИКАТОР_КАМПАНИИ]},\"FieldNames\":[\"Id\",\"Name\",\"Status\",\"Type\"]}}" https://api-sandbox.direct.yandex.com/json/v5/adgroups

```

```
{% endcut %}

{% cut "Request" %}

```

```
    {
      "method": "get",
      "params": {
        "SelectionCriteria": {
          "CampaignIds": [ИДЕНТИФИКАТОР_КАМПАНИИ]
        },
        "FieldNames": ["Id", "Name", "Status", "Type"]
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
        "AdGroups": [{
          "Status": "ACCEPTED",
          "Name": "Группа №1296502",
          "Id": 1296502,
          "Type": "TEXT_AD_GROUP"
        }, {
          "Name": "Группа №1296517",
          "Status": "DRAFT",
          "Id": 1296517,
          "Type": "TEXT_AD_GROUP"
        }]
      }
    }

```

```
{% endcut %}

```

**Service Ads**
Get the list of ads in an ad group.
```
{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{"AdGroupIds":[ИДЕНТИФИКАТОР_ГРУППЫ]},"FieldNames":["Id","State","Status","Type"]}}'  https://api-sandbox.direct.yandex.com/json/v5/ads

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"get\",\"params\":{\"SelectionCriteria\":{\"AdGroupIds\":[ИДЕНТИФИКАТОР_ГРУППЫ]},\"FieldNames\":[\"Id\",\"State\",\"Status\",\"Type\"]}}" https://api-sandbox.direct.yandex.com/json/v5/ads

```

```
{% endcut %}

{% cut "Request" %}

```

```
    {
      "method": "get",
      "params": {
        "SelectionCriteria": {
          "AdGroupIds": [ИДЕНТИФИКАТОР_ГРУППЫ]
        },
        "FieldNames": ["Id", "State", "Status", "Type"]
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
        "Ads": [{
          "State": "ON",
          "Id": 1381459,
          "Status": "ACCEPTED",
          "Type": "TEXT_AD"
        }, {
          "Type": "TEXT_AD",
          "Status": "DRAFT",
          "Id": 1381470,
          "State": "OFF"
        }]
      }
    }

```

```
{% endcut %}



Get parameters of a single ad.



{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{"Ids":[ИДЕНТИФИКАТОР_ОБЪЯВЛЕНИЯ]},"FieldNames":["Id"],"TextAdFieldNames":["Text","Title","Href","VCardId"]}}' https://api-sandbox.direct.yandex.com/json/v5/ads

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"get\",\"params\":{\"SelectionCriteria\":{\"Ids\":[ИДЕНТИФИКАТОР_ОБЪЯВЛЕНИЯ]},\"FieldNames\":[\"Id\"],\"TextAdFieldNames\":[\"Text\",\"Title\",\"Href\",\"VCardId\"]}}" https://api-sandbox.direct.yandex.com/json/v5/ads

```

```
{% endcut %}

{% cut "Request" %}

```

```
    {
      "method": "get",
      "params": {
        "SelectionCriteria": {
          "Ids": [1381459]
        },
        "FieldNames": ["Id"],
        "TextAdFieldNames": ["Text", "Title", "Href", "VCardId"]
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
        "Ads": [{
          "Id": 1381459,
          "TextAd": {
            "Title": "Test sandbox banner 5",
            "Href": "http://www.yandex.ru",
            "VCardId": 171518,
            "Text": "Test sandbox banner 5 text"
          }
        }]
      }
    }

```

```
{% endcut %}

```

**Keywords service**
Get keywords for an ad group.
```
{% cut "cURL" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"get","params":{"SelectionCriteria":{"AdGroupIds":[ИДЕНТИФИКАТОР_ГРУППЫ]},"FieldNames":["Id","Keyword","Bid","State","Status"]}}' https://api-sandbox.direct.yandex.com/json/v5/keywords

```

```
{% endcut %}

{% cut "cURL for Windows" %}

```

```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"get\",\"params\":{\"SelectionCriteria\":{\"AdGroupIds\":[ИДЕНТИФИКАТОР_ГРУППЫ]},\"FieldNames\":[\"Id\",\"Keyword\",\"Bid\",\"State\",\"Status\"]}}" https://api-sandbox.direct.yandex.com/json/v5/keywords

```

```
{% endcut %}

{% cut "Request" %}

```

```
    {
      "method": "get",
      "params": {
        "SelectionCriteria": {
          "AdGroupIds": [1296506]
        },
        "FieldNames": ["Id", "Keyword", "Bid", "State", "Status"]
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
        "Keywords": [{
          "State": "ON",
          "Keyword": "test keyword 5.1",
          "Status": "ACCEPTED",
          "Bid": 7700000,
          "Id": 3458327
        }, {
          "Keyword": "Новая фраза",
          "Id": 3458351,
          "Bid": 400000,
          "Status": "ACCEPTED",
          "State": "ON"
        }]
      }
    }

```

```
{% endcut %}

```

##  [](https://yandex.com/dev/direct/doc/en/en/get#get_whats_now)What's next
So, you have learned how to use the `get` method. In the next lesson, you will learn about the methods that change the data.
Copied
### Was the article helpful?
YesNo
Previous
[Lesson 6. How to make an API request](https://yandex.com/dev/direct/doc/en/en/format)
Next
[Lesson 8. How to make changes via the API](https://yandex.com/dev/direct/doc/en/en/modify)
