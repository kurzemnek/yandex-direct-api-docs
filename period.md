---
title: Report period | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/period
crawled_at: 2025-09-17T15:37:50.371085
---

Report period
# Report period
In the _DateRangeType_ parameter, specify the period to get statistics for:
  * TODAY — The current day.
  * YESTERDAY — The previous day.
  * LAST_3_DAYS, LAST_5_DAYS, LAST_7_DAYS, LAST_14_DAYS, LAST_30_DAYS, LAST_90_DAYS, LAST_365_DAYS — The specified number of previous days, not including the current day.
  * THIS_WEEK_MON_TODAY — The current week starting from Monday, including the current day.
  * THIS_WEEK_SUN_TODAY — The current week starting from Sunday, including the current day.
  * LAST_WEEK — The past week from Monday to Sunday.
  * LAST_BUSINESS_WEEK — The past work week from Monday to Friday.
  * LAST_WEEK_SUN_SAT — The past week from Sunday to Saturday.
  * THIS_MONTH — The current calendar month.
  * LAST_MONTH — The entire last calendar month.
  * ALL_TIME — All available statistics, including the current day.
  * CUSTOM_DATE — A custom period. If you select this value, specify the start date and end date of the period in the _DateFrom_ and _DateTo_ parameters.
  * AUTO — The time period when statistics for impressions and clicks might have changed. The period is selected automatically, depending on whether statistics were adjusted on the previous day. For more information, see in [How to get updated statistics](https://yandex.com/dev/direct/doc/en/en/actual).


You can aggregate the report data by different periods. In the _FieldNames_ parameter, set one of the values `Date`, `Week`, `Month`, `Quarter` or `Year`.
##  [](https://yandex.com/dev/direct/doc/en/en/period#learn-more)Learn more
  * [Data availability](https://yandex.com/dev/direct/doc/en/en/restrictions#data)


The period that the report is generated for. **Required** Yes
The start date of the report, YYYY-MM-DD. **Required** When the DateRangeType parameter has the value CUSTOM_DATE
The end date of the report, YYYY-MM-DD. The `DateFrom` and `DateTo` parameters are required when the `DateRangeType` parameter is set to CUSTOM_DATE. They are not allowed when other values are set.
Copied
Names of fields (columns) that will be in the report. To see which fields you can specify, see the sections [Available fields](https://yandex.com/dev/direct/doc/en/en/fields-list) and [Incompatible fields and dependencies](https://yandex.com/dev/direct/doc/en/en/compatibility). For the REACH_AND_FREQUENCY_PERFORMANCE_REPORT report type, the CampaignId field is required. **Required** Yes
Copied
### Was the article helpful?
YesNo
Previous
[How to generate a report](https://yandex.com/dev/direct/doc/en/en/how-to)
Next
[Report type](https://yandex.com/dev/direct/doc/en/en/type)
