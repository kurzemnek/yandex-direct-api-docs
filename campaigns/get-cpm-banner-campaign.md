---
title: get: CpmBannerCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/get-cpm-banner-campaign
crawled_at: 2025-09-17T16:01:14.456247
---

get: CpmBannerCampaign parameters
# get: CpmBannerCampaign parameters
Response structure in JSON format:
```
{
  "result": {
    "Campaigns": [{  /* CampaignGetItem */
      ...
      "CpmBannerCampaign": {  /* CpmBannerCampaignGetItem */
        "BiddingStrategy": {  /* CpmBannerCampaignStrategy */
          "Search": {  /* CpmBannerCampaignSearchStrategy */
            "BiddingStrategyType": ( "SERVING_OFF" | "UNKNOWN" ) /* required */
          },
          "Network": {  /* CpmBannerCampaignNetworkStrategy */
            "BiddingStrategyType": ( "MANUAL_CPM" | ... | "WB_MAXIMUM_IMPRESSIONS" ), /* required */
            "WbMaximumImpressions": {  /* StrategyWbMaximumImpressions */
              "AverageCpm": (long), /* required */
              "SpendLimit": (long) /* required */
            },
            "CpMaximumImpressions": {  /* StrategyCpMaximumImpressions */
              "AverageCpm": (long), /* required */
              "SpendLimit": (long), /* required */
              "StartDate": (string), /* required */
              "EndDate": (string), /* required */
              "AutoContinue": ( "YES" | "NO" ) /* required */
            },
            "WbDecreasedPriceForRepeatedImpressions": {  /* StrategyWbDecreasedPriceForRepeatedImpressions */
              "AverageCpm": (long), /* required */
              "SpendLimit": (long) /* required */
            },
            "CpDecreasedPriceForRepeatedImpressions": {  /* StrategyCpDecreasedPriceForRepeatedImpressions */
              "AverageCpm": (long), /* required */
              "SpendLimit": (long), /* required */
              "StartDate": (string), /* required */
              "EndDate": (string), /* required */
              "AutoContinue": ( "YES" | "NO" ) /* required */
            },
            "WbAverageCpv" : {  /* StrategyWbAverageCpvAdd */
              "AverageCpv" : (long) /* required */,
              "SpendLimit" : (long) /* required */
            },
            "CpAverageCpv" : {  /* StrategyCpAverageCpvAdd */
              "AverageCpv" : (long) /* required */,
              "SpendLimit" : (long) /* required */,
              "StartDate" : (string) /* required */,
              "EndDate" : (string) /* required */,
              "AutoContinue" : ( "YES" | "NO" ) /* required */
            }
          }
        },
        "Settings": [{  /* CpmBannerCampaignSettingGet */
          "Option": ( "ADD_METRICA_TAG" | ... | "SHARED_ACCOUNT_ENABLED" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
        "CounterIds": {  /* ArrayOfInteger */
          "Items": [(int), ... ] /* required */
        }, /* nillable */
        "FrequencyCap": {  /* FrequencyCapSetting */
          "Impressions": (int), /* required */
          "PeriodDays": (int) /* required */ /* nillable */
        }, /* nillable */
        "VideoTarget": ("VIEWS"|"CLICKS")
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description** |   
---|---|---|---  
**CpmBannerCampaignGetItem structure** |  |  |   
`BiddingStrategy` |  CpmBannerCampaignStrategy |  Display strategy. |   
`Settings` |  array of CpmBannerCampaignSettingGet |  Array of settings that only accept the values YES or NO. |   
`CounterIds` |  ArrayOfInteger, nillable |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |   
`FrequencyCap` |  FrequencyCapSetting, nillable |  Limits the frequency of impressions per user. If the structure is omitted, the frequency of impressions is not limited. |   
`VideoTarget` |  VideoTargetEnum |  Goal for video ads. Available values:
  * VIEWS: Full views.
  * CLICKS: Site traffic.

In the AUTOBUDGET_AVG_CPV and AUTOBUDGET_AVG_CPV_CUSTOM_PERIOD strategies, the value is reset to null. |   
**CpmBannerCampaignSettingGet structure** |  |  |   
`Option` |  CpmBannerCampaignSettingsGetEnum |  Setting name:
  * ADD_METRICA_TAG
  * ADD_OPENSTAT_TAG
  * ADD_TO_FAVORITES
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * ENABLE_SITE_MONITORING
  * REQUIRE_SERVICING
  * SHARED_ACCOUNT_ENABLED
  * DAILY_BUDGET_ALLOWED

|   
`Value` |  YesNoEnum |  Setting value. |   
**FrequencyCapSetting structure** |  |  |   
`Impressions` |  int |  Maximum number of impressions per user during a period. |   
`PeriodDays` |  int, nillable |  Number of days from 1 to 30. null (nil) — The limit applies to the entire time the advertising campaign is running. |   
**CpmBannerCampaignStrategy structure** |  |  |   
`Search` |  [CpmBannerCampaignSearchStrategy](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-cpm-banner-campaign#CpmBannerCampaignStrategy) |  Display strategy in search results. |   
`Network` |  CpmBannerCampaignNetworkStrategy |  Display strategy in ad networks. |   
**CpmBannerCampaignSearchStrategy structure** |  |  |   
`BiddingStrategyType` |  CpmBannerCampaignSearchStrategyTypeEnum |  The type of display strategy in search results. Only one value is available: SERVING_OFF |   
**CpmBannerCampaignNetworkStrategy structure** |  |  |   
`BiddingStrategyType` |  CpmBannerCampaignNetworkStrategyTypeEnum |  The type of display strategy in ad networks:
  * MANUAL_CPM
  * CP_DECREASED_PRICE_FOR_REPEATED_IMPRESSIONS
  * WB_DECREASED_PRICE_FOR_REPEATED_IMPRESSIONS
  * CP_MAXIMUM_IMPRESSIONS
  * WB_MAXIMUM_IMPRESSIONS
  * CP_AVERAGE_CPV
  * WB_AVERAGE_CPV
  * UNKNOWN

|   
`WbMaximumImpressions` |  StrategyWbMaximumImpressions |  Parameters of the strategy  |   
`CpMaximumImpressions` |  StrategyCpMaximumImpressions |  Parameters of the strategy  |   
`WbDecreasedPriceForRepeatedImpressions` |  StrategyWbDecreasedPriceForRepeatedImpressions |  Parameters of the strategy  |   
`CpDecreasedPriceForRepeatedImpressions` |  StrategyCpDecreasedPriceForRepeatedImpressions |  Parameters of the strategy  |   
`WbAverageCpv` |  StrategyWbAverageCpv |  Parameters of the strategy  |   
`CpAverageCpv` |  StrategyCpAverageCpv |  Parameters of the strategy  |   
**StrategyWbMaximumImpressions structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`SpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
**StrategyCpMaximumImpressions structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`SpendLimit` |  long |  The budget for the period in the advertiser's currency, multiplied by 1,000,000. The minimum budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`StartDate` |  string |  Date of the start of the period, in the format YYYY-MM-DD. Can't be earlier than the current date or the campaign start date. |   
`EndDate` |  string |  Date of the end of the period, in the format YYYY-MM-DD. Can't be later than the campaign end date. |   
`AutoContinue` |  YesNoEnum |  Extend the campaign period automatically in order to use the remaining budget. |   
**StrategyWbDecreasedPriceForRepeatedImpressions structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`SpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
**StrategyCpDecreasedPriceForRepeatedImpressions structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`SpendLimit` |  long |  The budget for the period in the advertiser's currency, multiplied by 1,000,000. The minimum budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`StartDate` |  string |  Date of the start of the period, in the format YYYY-MM-DD. Can't be earlier than the current date or the campaign start date. |   
`EndDate` |  string |  Date of the end of the period, in the format YYYY-MM-DD. Can't be later than the campaign end date. |   
`AutoContinue` |  YesNoEnum |  Extend the campaign period automatically in order to use the remaining budget. |   
**StrategyWbAverageCpv structure** |  |  |   
`AverageCpv` |  long |  The average CPV in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`SpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
**StrategyCpAverageCpv structure** |  |  |   
`AverageCpv` |  long |  The average CPV in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`SpendLimit` |  long |  The budget for the period in the advertiser's currency, multiplied by 1,000,000. The minimum budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`StartDate` |  string |  Date of the start of the period, in the format YYYY-MM-DD. Can't be earlier than the current date or the campaign start date. |   
`EndDate` |  string |  Date of the end of the period, in the format YYYY-MM-DD. Can't be later than the campaign end date. |   
`AutoContinue` |  YesNoEnum |  Extend the campaign period automatically in order to use the remaining budget. |   
Copied
### Was the article helpful?
YesNo
Previous
[get: MobileAppCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-mobile-app-campaign)
Next
[resume](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/resume)
