---
title: Change the strategy | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/curl-campaigns-strategy
crawled_at: 2025-09-17T15:38:46.444186
---

Change the strategy
# Change the strategy
Uses the cURL utility
The example shows how to configure the “Optimize clicks” strategy (with impressions enabled in search results and ad networks) using the [Campaigns](https://yandex.com/dev/direct/docref-v5/campaigns/campaigns.md).[update](https://yandex.com/dev/direct/docref-v5/campaigns/update.md) method.
To use this example, the input data must include the OAuth token, the campaign ID, and the amount of the weekly budget (multiplied by 1 000 000). If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
curl \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Client-Login: CLIENT_LOGIN' \
  -d '{ "method": "update",
  "params": {
    "Campaigns": [{
      "Id": CAMPAIGN_ID,
      "TextCampaign": {
        "BiddingStrategy": {
          "Search": {
            "BiddingStrategyType": "WB_MAXIMUM_CLICKS",
            "WbMaximumClicks": {
              "WeeklySpendLimit": BUDGET_AMOUNT
            }
          },
          "Network": { 
            "BiddingStrategyType": "NETWORK_DEFAULT",
            "NetworkDefault": {  }
          }
        }
      }
    }]
  }
}' https://api.direct.yandex.com/json/v5/campaigns

```

Note
For cURL in Windows, replace all single quotes with double quotes, and escape double quotes in JSON code. For example: `-d "{\"method\"`...
Copied
### Was the article helpful?
YesNo
Previous
[Configure time targeting](https://yandex.com/dev/direct/doc/en/en/curl-campaigns-timetargeting)
Next
[Add tags to an ad URL](https://yandex.com/dev/direct/doc/en/en/curl-ads-keywords-modify)
