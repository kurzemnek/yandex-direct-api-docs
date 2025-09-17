---
title: Lesson 10. How to efficiently use the API: restrictions and recommendations | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/optimize
crawled_at: 2025-09-17T15:37:21.246807
---

Lesson 10. How to efficiently use the API: restrictions and recommendations
# Lesson 10. How to efficiently use the API: restrictions and recommendations
  * [How to find points spent and point balance](https://yandex.com/dev/direct/doc/en/en/optimize#optimize_point_ballance)
  * [How to optimize your points spending](https://yandex.com/dev/direct/doc/en/en/optimize#optimize_points_opt)
  * [How to track changes using the Changes service](https://yandex.com/dev/direct/doc/en/en/optimize#opimize_changes)
  * [Task](https://yandex.com/dev/direct/doc/en/en/optimize#optimize_task)


In this lesson, you will learn what restrictions can be applied in the Yandex Direct API and how you can run your app efficiently in view of those restrictions.
Various types of restrictions are applied to balance the load on the API server. A maximum of 5 concurrent requests can be run on behalf of a single advertiser. Each method imposes limitations on the number of objects per request. Also, the API applies a point-based system.
Each advertiser (or an agency) is granted an individual daily limit of points. Points are granted in regular intervals throughout the day. Points are deducted per calling a method, per changing or getting an object, or per error in a request. If you don't have enough points, you can't make API requests.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/optimize_time_dgrm.png)
##  [](https://yandex.com/dev/direct/doc/en/en/optimize#optimize_point_ballance)How to find points spent and point balance
In response to each request, the API server sends the HTTP `Units` header that indicates the number of points:
`Units: spent on request/available points/daily limit`
**Response example**
```
    HTTP/1.1 200 OK
    Connection:close
    Content-Type:application/json
    Date:Fri, 28 Jun 2018 17:07:02 GMT
    RequestId: 1111111111111111112
    Units: 10/20828/64000
    Server:nginx
    Transfer-Encoding:chunked
    
    {
      "result": {
        ...
      }
    }

```

  * `RequestId`— request identifier.
  * `Units` — number of points.


Note
If a request to the API is made on behalf of the agency, the advertiser's points are spent by default. However, the agency can choose to spend their points instead of the advertiser's points.
##  [](https://yandex.com/dev/direct/doc/en/en/optimize#optimize_points_opt)How to optimize your points spending
We recommend that you store all the data used by the app in the cache, for example, in the local database. Having got the parameters of campaigns, groups, ads, keywords, as well as reference lists of regions and time zones, from the server, you can use the methods of the `Changes` service to track whether they are up-to-date. Before updating the cached data, please check for changes. You need not get objects from the server again, unless they have actually changed. This way you can reduce the amount of data transmitted, speed up your app, and reduce the point spending.
##  [](https://yandex.com/dev/direct/doc/en/en/optimize#opimize_changes)How to track changes using the Changes service
1. At the first launch of your app, call the `checkDictionaries` method of the `Changes` service, without any parameters. In the response, you will get the `Timestamp` parameter with the current UTC time set on the server.
**cURL**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"checkDictionaries","params":{}}' https://api.direct.yandex.com/json/v5/changes

```

**cURL for Windows**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"checkDictionaries\",\"params\":{}}" https://api.direct.yandex.com/json/v5/changes

```

**Request**
```
    {
      "method": "checkDictionaries",
      "params": { }
    }

```

**Response**
```
    {
      "result": {
        "Timestamp": "2018-06-03T12:48:27Z"
      } 
    }

```

2. To get a list of campaigns changed, call method `checkCampaigns`. In each next call, specify `Timestamp` retrieved by the previous call: this ensures absense of gaps between the change check intervals.
**cURL**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"checkCampaigns","params":{"Timestamp":"2018-06-03T12:48:27Z"}}' https://api.direct.yandex.com/json/v5/changes

```

**cURL for Windows**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"checkCampaigns\",\"params\":{\"Timestamp\":\"2018-06-03T12:48:27Z\"}}" https://api.direct.yandex.com/json/v5/changes

```

**Request**
```
    {
      "method": "checkCampaigns",
      "params": {
        "Timestamp": "2018-06-03T12:48:27Z"
      }
    }

```

**Response**
```
    {
      "result": {
        "Timestamp": "2018-07-01T13:11:27Z",
        "Campaigns": [{
          "CampaignId": 136200,
          "ChangesIn": [ "SELF", "CHILDREN" ]
        }, {
          "CampaignId": 136201,
          "ChangesIn": [ "STAT" ]
        }]
      }
    }

```

The method returns the IDs of the campaigns that were changed. The `ChangesIn` parameter specifies where the changes were made:
  * `SELF` — In campaign parameters.
  * `CHILDREN` — In child objects (groups, ads, or keywords).
  * `STAT` — Corrected campaign statistics (usually related to filtering out false clicks).


3. If the `checkCampaigns` method showed that the child objects have changed, get more details of the changes using the `check` method.
**cURL**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d '{"method":"check","params": {"Timestamp":"2018-06-03T12:48:27Z","CampaignIds": [136200],"FieldNames": ["AdGroupIds","AdIds"]}}'  https://api.direct.yandex.com/json/v5/changes

```

**cURL for Windows**
```
    curl -k -H "Authorization: Bearer ТОКЕН" -d "{\"method\":\"check\",\"params\": {\"Timestamp\":\"2018-06-03T12:48:27Z\",\"CampaignIds\": [136200],\"FieldNames\": [\"AdGroupIds\",\"AdIds\"]}}" https://api.direct.yandex.com/json/v5/changes

```

**Request**
```
    {
      "method": "check",
      "params": {
        "CampaignIds": [136200],
        "FieldNames": ["AdGroupIds","AdIds"],
        "Timestamp": "2018-06-03T12:48:27Z"
      }
    }

```

**Response**
```
    {
      "result": {
        "Timestamp": "2018-07-01T13:12:22Z",
        "Modified": {
          "AdGroupIds": [22222222],
          "AdIds": [33333333,33333334]      
        }
      }
    }

```

Alert
If the `check` method shows that an ad group has changed (the ad group ID is specified in the `AdGroupIds` array), this could mean a change either in the ad group parameters or in the keywords.
Use the `get` methods of the applicable services — `Campaigns`, `AdGroups`, `Ads` или `Keywords` to get the changed objects from the server.
##  [](https://yandex.com/dev/direct/doc/en/en/optimize#optimize_task)Task
  1. Create a new campaign, ad group, and ad in Sandbox.
  2. Use the `moderate` method of the `Ads` service to submit the ad for moderation.
  3. Get data of all the campaigns.
  4. Get data on changes in all the campaigns.
  5. Use the `check` method to find out which ads have changed (the status of the ad sent for moderation should have changed).
  6. Get the titles and texts of the ads accepted at ad moderation.
  7. See how many points you have spent on those requests.


For detailed instructions on how to work with Yandex Direct API, see .
Best of luck!
Copied
### Was the article helpful?
YesNo
Previous
[Lesson 9. How to get to real work](https://yandex.com/dev/direct/doc/en/en/real-world)
Next
[Overview of the Yandex.Direct API version 5](https://yandex.com/dev/direct/doc/en/en/concepts/overview)
