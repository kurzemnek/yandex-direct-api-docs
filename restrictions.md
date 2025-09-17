---
title: Restrictions | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/restrictions
crawled_at: 2025-09-17T15:43:06.309331
---

Technical limitations
# Restrictions
  * [Technical limitations](https://yandex.com/dev/direct/doc/en/en/restrictions#technical-limitations)
  * [Data availability](https://yandex.com/dev/direct/doc/en/en/restrictions#data-availability)
    * [Availability of Yandex Metrica data](https://yandex.com/dev/direct/doc/en/en/restrictions#availability-of-yandex-metrica-data)
  * [Filter availability](https://yandex.com/dev/direct/doc/en/en/restrictions#filter-availability)


##  [](https://yandex.com/dev/direct/doc/en/en/restrictions#technical-limitations)Technical limitations
Each advertiser can send a maximum of 20 requests in 10 seconds to the Reports service.
The report queue can contain a maximum of 5 offline reports at once per user.
Generated offline reports are stored for 5 hours, then deleted automatically.
##  [](https://yandex.com/dev/direct/doc/en/en/restrictions#data-availability)Data availability
Statistics are available for the three years prior to the current month. For example: on August 15, 2019, you can get data starting from August 1, 2016.
The table shows the availability of data in specific fields.
**Field** |  **Data available**  
---|---  
Query |  For the past 180 days  
AvgTrafficVolume |  Starting on 08.06.2018 On the preceding dates, the AvgTrafficVolume value is 100, WeightedCtr is the same as Ctr, and WeightedImpressions is the same as Impressions.  
WeightedCtr  
WeightedImpressions  
###  [](https://yandex.com/dev/direct/doc/en/en/restrictions#availability-of-yandex-metrica-data)Availability of Yandex Metrica data
  * Data for the “Last click from Yandex Direct” attribution model is available starting from July 30, 2019.
  * AvgPageviews, Bounces, and BounceRate are available if the advertiser's site has a Yandex.Metrica tag installed and the tag number is specified in the CounterIds campaign parameter.
  * Conversions, ConversionRate, and CostPerConversion are available if goals are also set up for the tag (see Goals in the Yandex Metrica Help).
  * Revenue, Profit and GoalsRoi are available if the goals are also specified as priority goals in the campaign settings (see “Setting up priority goals” in the Yandex Direct Help) or if the tag snippet transmits the order value (see Ecommerce in the Yandex Metrica Help).


It can take up to several hours for Yandex Metrica data to appear in reports because the data transmitted from the tags must be correlated with the ad campaigns.
##  [](https://yandex.com/dev/direct/doc/en/en/restrictions#filter-availability)Filter availability
Filtering by AudienceTargetId is available for data starting from December 8, 2017.
### Was the article helpful?
YesNo
Previous
[Response codes and error codes](https://yandex.com/dev/direct/doc/en/en/codes)
Next
[Clicks and cost](https://yandex.com/dev/direct/doc/en/en/example)
