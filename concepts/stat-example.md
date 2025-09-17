---
title: Example: Reports instead of GetBannersStat (Live) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/stat-example
crawled_at: 2025-09-17T16:01:50.902663
---

Example: Reports instead of GetBannersStat (Live)
# Example: Reports instead of GetBannersStat (Live)
This example switches to using the `Reports` service to get statistics.
It shows a `GetBannersStat (Live)` call with the following parameters:
```
curl \
  -d '{
    "method": "GetBannersStat",
    "locale": "en",
    "token": "0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f",
    "param": {
      "CampaignID": 10007,
      "StartDate": "2018-05-01",
      "EndDate": "2018-05-07",
      "GroupByColumns": [ "clDate", "clPhrase", "clROI" ],
      "Limit": 200,
      "Offset": 0,
      "OrderBy": [ "clDate" ],
      "Currency": "RUB",
      "IncludeVAT": "YES",
      "IncludeDiscount": "YES"
   }
  }' \
  https://api.direct.yandex.com/live/v4/json/

```

Example of returned data:
```
{
  "data": {
    "Stat": [{
      "StatDate": "2018-05-01",
      "PhraseID": 414808784,
      "Phrase": "trip !to outerspace",
      "BannerID": 7654321,
      "Revenue": 8271.77,
      "ROI": 2.51,
      "Clicks": 329,
      "ClicksSearch": 307,
      "ClicksContext": 22,
      "Shows": 2224,
      "ShowsSearch": 1246,
      "ShowsContext": 978,
      "Sum": 2356.29,
      "SumSearch": 2303.68,
      "SumContext": 52.61,
    }, ... ],
    "StartDate": "2018-05-01",
    "EndDate": "2018-05-07",
    "CampaignID": 10007
  }
}

```

The following request to the `Reports` service allows you to get the same data:
```
curl \
  -H 'Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f' \
  -H 'Accept-Language: en' \
  -H 'Client-Login: agrom' \
  -H 'returnMoneyInMicros: false' \
  -d '{
    "params": {
      "SelectionCriteria": {
        "DateFrom": "2018-05-01",
        "DateTo": "2018-05-07",
        "Filter": [{
          "Field": "CampaignId",
          "Operator": "IN",
          "Values": [ "10007" ]
        }]
      },
      "FieldNames": [ "Date", "AdId", "CriterionId", "CriterionType",
                      "Criterion", "Cost", "Clicks", "Impressions", 
                      "AdNetworkType", "Revenue", "GoalsRoi" ], 
      "Page": {
        "Limit": 200
      },
      "OrderBy": [{
        "Field": "Date"
      }],
      "ReportName": "Revenue and ROI",
      "ReportType": "CUSTOM_REPORT",
      "DateRangeType": "CUSTOM_DATE",
      "Format": "TSV",
      "IncludeVAT": "YES",
      "IncludeDiscount": "YES"
    }
  }' \
  https://api.direct.yandex.com/json/v5/reports

```

Explanation:
  * To get a report on an Agency client, specify the client's login in the `Client-Login` HTTP header.
  * To get monetary values in the advertiser's currency in the report, set the `returnMoneyInMicros: false` HTTP header.
  * To get a report on a specific campaign, filter by `CampaignId`.
  * To get a report for certain dates, specify these dates in the `DateFrom` and `DateTo` parameters, and set the `DateRangeType` parameter to CUSTOM_DATE.
  * To get statistics in the context of ads, include the `AdId` field in the `FieldNames` parameter.
  * To get statistics in the context of keywords, include the `CriterionId`, `CriterionType` and `Criterion` fields in the `FieldNames` parameter.
  * To get statistics separately for search and ad networks, specify the `AdNetworkType` field in the `FieldNames` parameter. The report rows that have the SEARCH value in this field contain the statistics on search, while rows with the AD_NETWORK value show statistics in ad networks.


Sample report:
```
"Revenue and ROI (2018-05-01 - 2018-05-07)"
Date	AdId	CriterionId	CriterionType	Criterion	Cost	Clicks	Impressions	AdNetworkType	Revenue	GoalsRoi
2018-05-01	7654321	414808784	KEYWORD	"trip !to outerspace"	2303.68	307	1246	SEARCH	8104.22	2.52
2018-05-01	7654321	414808784	KEYWORD	"trip !to outerspace"	52.61	22	978	AD_NETWORK	167.55	2.18
...

```

Copied
### Was the article helpful?
YesNo
Previous
[Parameters of clients](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/clients)
Next
[Error calling a Yandex Direct API method](https://yandex.com/dev/direct/doc/en/concepts/en/troubleshooting/issue)
