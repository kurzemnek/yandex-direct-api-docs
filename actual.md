---
title: How to get updated statistics | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/actual
crawled_at: 2025-09-17T15:42:57.001322
---

Use the Changes.check method
# How to get updated statistics
  * [Use the Changes.check method](https://yandex.com/dev/direct/doc/en/en/actual#check)
  * [Use DataRangeType: AUTO](https://yandex.com/dev/direct/doc/en/en/actual#auto)


Yandex Direct statistics are sometimes updated and added to. The data normally stabilizes within three days.
In unusual cases, older statistics might be corrected. Statistics are usually adjusted when the click rate has declined and the campaign balance or a shared account balance has increased.
This means that you might see a discrepancy between the statistics you received earlier and the actual data in Yandex Direct. You can use one of the following approaches to keep your statistics up to date in your database:
  * Use the [Changes.check](https://yandex.com/dev/direct/doc/en/en/actual#check) method
  * Use [DataRangeType: AUTO](https://yandex.com/dev/direct/doc/en/en/actual#auto)


##  [](https://yandex.com/dev/direct/doc/en/en/actual#check)Use the Changes.check method
  1. Run the Changes.check method daily (or on a schedule that you choose) to check whether statistics were adjusted:
```
{
"method": "check",
"params": { 
    "CampaignIds": [...], /* The campaigns for which you are tracking statistics */
    "Timestamp": "...", /* The timestamp returned at the previous method call */
    "FieldNames": ["CampaignsStat"]
} 
}

```

The method returns the `BorderDate` parameter for each campaign with statistics that were adjusted after the specified time.
  2. If statistics weren't adjusted, get statistics for the past three days: in the report request, set the `DateRangeType` parameter to LAST_3_DAYS. Save the new statistics (for yesterday) in your database and update the existing statistics (for the previous two days).
  3. If statistics were adjusted, get statistics starting from the date in `BorderDate` up to yesterday's date. Save the new statistics (for yesterday) in your database, and update the existing statistics (for the previous days starting from `BorderDate`).


##  [](https://yandex.com/dev/direct/doc/en/en/actual#auto)Use DataRangeType: AUTO
  1. Get statistics daily by setting DateRangeType to AUTO. The time period for the report is selected automatically based on whether or not the statistics has been updated the day before.
     * Not adjusted: the report is created for the past three days.
     * Adjusted: the start date is the earliest date with corrected statistics, and the end date is yesterday's date.
Choose a time for running the request that is during the night in Moscow (UTC+3), such as 00:23 or 02:47. Avoid “round” numbers, since the server load peaks at these times.
  2. The first row in the report shows the dates it is for.
Save or update the statistics for these dates in your database.


Copied
### Was the article helpful?
YesNo
Previous
[Online and offline reports](https://yandex.com/dev/direct/doc/en/en/mode)
Next
[Response codes and error codes](https://yandex.com/dev/direct/doc/en/en/codes)
