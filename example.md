---
title: Example: clicks and cost | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/example
crawled_at: 2025-09-17T15:38:27.002467
---

Request
# Example: clicks and cost
  * [Request](https://yandex.com/dev/direct/doc/en/en/example#request)
  * [Response](https://yandex.com/dev/direct/doc/en/en/example#response)


This example shows how to get the number of clicks and their cost for campaigns, broken down by day (in the advertiser's currency, including VAT). The report period is determined automatically (see section [How to get updated statistics](https://yandex.com/dev/direct/doc/reports/actual.html)).
##  [](https://yandex.com/dev/direct/doc/en/en/example#request)Request
JSON
XML
```
curl \
-H 'Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f' \
-H 'Accept-Language: en' \
-H 'Client-Login: agrom' \
-H 'returnMoneyInMicros: false' \
-d '{
  "params": {
    "SelectionCriteria": {
      "Filter": [{
        "Field": "CampaignId",
        "Operator": "IN",
        "Values": [ "10002", "10007" ]
      }]
    },
    "FieldNames": [ "Date", "CampaignId", "Clicks", "Cost" ], 
    "OrderBy": [{
      "Field": "Date"
    }],
    "ReportName": "Actual Data",
    "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
    "DateRangeType": "AUTO",
    "Format": "TSV",
    "IncludeVAT": "YES",
    "IncludeDiscount": "YES"
  }
}' \
https://api.direct.yandex.com/json/v5/reports

```

```
curl \
-H 'Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f' \
-H 'Accept-Language: en' \
-H 'Client-Login: agrom' \
-H 'returnMoneyInMicros: false' \
-d '<?xml version="1.0" encoding="UTF-8"?>
  <ReportDefinition xmlns="http://api.direct.yandex.com/v5/reports">
    <SelectionCriteria>
      <Filter>
        <Field>CampaignId</Field>
        <Operator>IN</Operator>
        <Values>10002</Values>
        <Values>10007</Values>
      </Filter>
    </SelectionCriteria>
    <FieldNames>Date</FieldNames>
    <FieldNames>CampaignId</FieldNames>
    <FieldNames>Clicks</FieldNames>
    <FieldNames>Cost</FieldNames>
    <OrderBy>
      <Field>Date</Field>
    </OrderBy>
    <ReportName>Actual Data</ReportName>
    <ReportType>CAMPAIGN_PERFORMANCE_REPORT</ReportType>
    <DateRangeType>AUTO</DateRangeType>
    <Format>TSV</Format>
    <IncludeVAT>YES</IncludeVAT>
    <IncludeDiscount>YES</IncludeDiscount>
  </ReportDefinition>' \
https://api.direct.yandex.com/v5/reports

```

##  [](https://yandex.com/dev/direct/doc/en/en/example#response)Response
```
"Actual Data (2018-04-01 - 2018-04-03)"
Date CampaignId Clicks Cost
2018-04-01 10002 6 90.20
2018-04-01 10007 397 1496.50
2018-04-02 10002 13 158.60
2018-04-02 10007 314 1181.40
2018-04-03 10002 15 165.10
2018-04-03 10007 447 1619.60
Total rows: 6

```

####  [](https://yandex.com/dev/direct/doc/en/en/example#learn-more)Learn more
[PHP examples for JSON](https://yandex.com/dev/direct/doc/examples-v5/php5-json-curl.html)  
[Python examples for JSON](https://yandex.com/dev/direct/doc/examples-v5/python3-json.html)  
[Python examples for XML](https://yandex.com/dev/direct/doc/examples-v5/python3-xml.html)
### Was the article helpful?
YesNo
Previous
[Restrictions](https://yandex.com/dev/direct/doc/en/en/restrictions)
Next
[Yandex Metrica data](https://yandex.com/dev/direct/doc/en/en/example-metrika)
