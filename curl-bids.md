---
title: Setting bids | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/curl-bids
crawled_at: 2025-09-17T15:39:07.002394
---

Setting bids
# Setting bids
Uses the cURL utility
The example shows how to implement custom bid management using the [KeywordBids](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/keywordbids.md).[setAuto](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/setAuto.md) method. All keywords in the campaign are assigned a bid on search that is equal to the bid for the traffic volume of 75 plus 10%, which corresponds to premium impressions.
To use this example, specify the OAuth token and ID of the campaign where you are setting bids. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
curl \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Client-Login: CLIENT_LOGIN' \
  -d '{ "method": "setAuto",
  "params": {
    "KeywordBids": [{
      "CampaignId": CAMPAIGN_ID,
      "BiddingRule": {
        "SearchByTrafficVolume": {
          "TargetTrafficVolume": 75,
          "IncreasePercent": 10
        }
      }
    }] 
  }
}' https://api.direct.yandex.com/json/v5/keywordbids

```

Note
For cURL in Windows, replace all single quotes with double quotes, and escape double quotes in JSON code. For example: `-d "{\"method\"`...
Copied
### Was the article helpful?
YesNo
Previous
[Stop and start ads](https://yandex.com/dev/direct/doc/en/en/curl-ads-launch)
Next
[Examples in PHP 5](https://yandex.com/dev/direct/doc/en/en/php5)
