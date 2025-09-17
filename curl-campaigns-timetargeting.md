---
title: Configure time targeting | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/curl-campaigns-timetargeting
crawled_at: 2025-09-17T15:38:40.419960
---

Configure time targeting
# Configure time targeting
Uses the cURL utility
This example shows how to configure time targeting and hourly bid adjustments using the [Campaigns](https://yandex.com/dev/direct/docref-v5/campaigns/campaigns.md).[update](https://yandex.com/dev/direct/docref-v5/campaigns/update.md) method.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/timetargeting-example.png)
To use this example, change the input data to include the OAuth token, the campaign ID, and the bid adjustments for each day of the week and each hour. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
curl \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Client-Login: CLIENT_LOGIN' \
  -d '{ "method": "update",
  "params": {
    "Campaigns": [{
      "Id": CAMPAIGN_ID,
      "TimeTargeting": {
        "Schedule": {
          "Items": [
            "1,0,0,0,0,0,0,0,0,0,80,80,100,100,100,100,100,120,150,150,150,120,100,80,0",
            "2,0,0,0,0,0,0,0,0,0,80,80,100,100,100,100,100,120,150,150,150,120,100,80,0",
            "3,0,0,0,0,0,0,0,0,0,80,80,100,100,100,100,100,120,150,150,150,120,100,80,0",
            "4,0,0,0,0,0,0,0,0,0,80,80,100,100,100,100,100,120,150,150,150,120,100,80,0",
            "5,0,0,0,0,0,0,0,0,0,80,80,100,100,100,100,100,170,200,200,200,170,100,80,0",
            "6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100,100,100,100,100,100,100,100,100,100",
            "7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100,100,100,100,100,100,100,100,100,100"
          ]
        },
        "ConsiderWorkingWeekends": "YES",
        "HolidaysSchedule": {
          "StartHour": 14,
          "EndHour": 24,
          "SuspendOnHolidays": "NO",
          "BidPercent": 100
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
[Examples for the cURL utility](https://yandex.com/dev/direct/doc/en/en/curl)
Next
[Change the strategy](https://yandex.com/dev/direct/doc/en/en/curl-campaigns-strategy)
