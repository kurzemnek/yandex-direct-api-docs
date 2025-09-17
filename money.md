---
title: Output for monetary values | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/money
crawled_at: 2025-09-17T15:38:04.328559
---

Report currency
# Output for monetary values
  * [Report currency](https://yandex.com/dev/direct/doc/en/en/money#report-currency)
  * [Units](https://yandex.com/dev/direct/doc/en/en/money#units)
  * [VAT](https://yandex.com/dev/direct/doc/en/en/money#vat)


##  [](https://yandex.com/dev/direct/doc/en/en/money#report-currency)Report currency
Monetary values are shown in the advertiser's currency.
##  [](https://yandex.com/dev/direct/doc/en/en/money#units)Units
Monetary values in the fields _AvgCpc_ , _AvgCpm_ , _AvgEffectiveBid_ , _Cost_ , _CostPerConversion_ , _Profit_ , and _Revenue_ are:
  * Amounts in a currency if the request specifies the HTTP header `returnMoneyInMicros: false`. Rounded to two decimal places.
  * Integers resulting from multiplying the amount in the currency by 1,000,000 if this header is omitted. Rounded to 10,000.


Note
Due to rounding errors, the sum of the values in the Cost and Profit fields for the report rows may differ slightly from the actual totals. The final values can be obtained by generating an aggregated report (without data groupings).
##  [](https://yandex.com/dev/direct/doc/en/en/money#vat)VAT
Monetary values in the _AvgCpc_ , _AvgCpm_ , _AvgEffectiveBid_ , _Cost_ , and _CostPerConversion_ fields, as well as _Profit_ и _Revenue_ for priority campaign goals, can be obtained either with or without VAT by using the _IncludeVAT_ input parameter.
The _Revenue_ value that is calculated from Yandex.Metrica data does not depend on the _IncludeVAT_ parameter.
Average cost per click.
Average price per thousand impressions. Data is only available for display campaigns.
Average bid per click with all adjustments. Data is only available for pay-per-click campaigns.
The cost of clicks.
The average cost of converted sessions (according to Yandex Metrica data): the ratio of the cost per click to the number of conversions. If the request included Yandex Metrica goals (the `Goals` parameter), the `CostPerConversion` field is replaced with `CostPerConversion_<goal_ID>_<attribution_model>` fields.
Copied
Profit. Calculated as the total revenue for goals minus the cost of clicks.
Revenue by goals. For priority goals, revenue is calculated based on the conversion values specified in the campaign settings. For other goals, it is calculated using Yandex Metrica data. If the request included Yandex Metrica goals (the `Goals` parameter), the `Revenue` field is replaced with `Revenue_<goal_ID>_<attribution_model>`.
Copied
Whether to include VAT in the monetary amounts in the report.  
**Required** Yes
Copied
### Was the article helpful?
YesNo
Previous
[Report fields](https://yandex.com/dev/direct/doc/en/en/fields)
Next
[Filtering data](https://yandex.com/dev/direct/doc/en/en/filters)
