---
title: add: CpmBannerCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/add-cpm-banner-campaign
crawled_at: 2025-09-17T16:01:20.817099
---

add: CpmBannerCampaign parameters
# add: CpmBannerCampaign parameters
Request structure in JSON format:
```
{
  "method": "add",
  "params": {
    "Campaigns": [{  /* CampaignAddItem */
      ...
      "CpmBannerCampaign": {  /* CpmBannerCampaignAddItem */
        "BiddingStrategy": {  /* CpmBannerCampaignStrategyAdd */
          "Search": {  /* CpmBannerCampaignSearchStrategyAdd */
            "BiddingStrategyType": ( "SERVING_OFF" ) /* required */
          }, /* required */
          "Network": {  /* CpmBannerCampaignNetworkStrategyAdd */
            "BiddingStrategyType": ( "MANUAL_CPM" | ... | "WB_DECREASED_PRICE_FOR_REPEATED_IMPRESSIONS" ), /* required */
            "WbMaximumImpressions": {  /* StrategyWbMaximumImpressionsAdd */
              "AverageCpm": (long), /* required */
              "SpendLimit": (long) /* required */
            },
            "CpMaximumImpressions": {  /* StrategyCpMaximumImpressionsAdd */
              "AverageCpm": (long), /* required */
              "SpendLimit": (long), /* required */
              "StartDate": (string), /* required */
              "EndDate": (string), /* required */
              "AutoContinue": ( "YES" | "NO" ) /* required */
            },
            "WbDecreasedPriceForRepeatedImpressions": {  /* StrategyWbDecreasedPriceForRepeatedImpressionsAdd */
              "AverageCpm": (long), /* required */
              "SpendLimit": (long) /* required */
            },
            "CpDecreasedPriceForRepeatedImpressions": {  /* StrategyCpDecreasedPriceForRepeatedImpressionsAdd */
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
          } /* required */
        }, /* required */
        "Settings": [{  /* CpmBannerCampaignSetting */
          "Option": ( "ADD_METRICA_TAG" | ... | "REQUIRE_SERVICING" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
        "CounterIds": {  /* ArrayOfInteger */
          "Items": [(int), ... ] /* required */
        },
        "FrequencyCap": {  /* FrequencyCapSetting */
          "Impressions": (int), /* required */
          "PeriodDays": (int) /* required */ /* nillable */
        },
        "VideoTarget": ("VIEWS"|"CLICKS")
      }
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**CpmBannerCampaignAddItem structure** |  |  |   
`BiddingStrategy` |  CpmBannerCampaignStrategyAdd |  Display strategy. |  Yes  
`Settings` |  array of CpmBannerCampaignSetting |  Array of settings that only accept the values YES or NO. |  No  
`CounterIds` |  ArrayOfInteger |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |  No  
`FrequencyCap` |  FrequencyCapSetting |  Limits the frequency of impressions per user. If the structure is omitted, the frequency of impressions is not limited. |  No  
`VideoTarget` |  VideoTargetEnum |  Goal for video ads. Available values:
  * VIEWS: Full views.
  * CLICKS: Site traffic.

In the AUTOBUDGET_AVG_CPV and AUTOBUDGET_AVG_CPV_CUSTOM_PERIOD strategies, the value is reset to null. |  No  
**CpmBannerCampaignSetting structure** |  |  |   
`Option` |  CpmBannerCampaignSettingsEnum |  Setting name:
  * ADD_METRICA_TAG
  * ADD_OPENSTAT_TAG
  * ADD_TO_FAVORITES
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * ENABLE_SITE_MONITORING
  * REQUIRE_SERVICING

|  Yes  
`Value` |  YesNoEnum |  Setting value. |  Yes  
**FrequencyCapSetting structure** |  |  |   
`Impressions` |  int |  Maximum number of impressions per user during a period. |  Yes  
`PeriodDays` |  int, nillable |  Number of days from 1 to 30. null (nil) — The limit applies to the entire time the advertising campaign is running. |  Yes  
**CpmBannerCampaignStrategyAdd structure** |  |  |   
`Search` |  CpmBannerCampaignSearchStrategyAdd |  Display strategy in search results. |  Yes  
`Network` |  CpmBannerCampaignNetworkStrategyAdd |  Display strategy in ad networks. |  Yes  
**CpmBannerCampaignSearchStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  CpmBannerCampaignSearchStrategyTypeEnum |  The type of display strategy in search results. Only one value is available: SERVING_OFF. |  Yes  
**CpmBannerCampaignNetworkStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  CpmBannerCampaignNetworkStrategyTypeEnum |  The type of display strategy in ad networks:
  * MANUAL_CPM
  * CP_DECREASED_PRICE_FOR_REPEATED_IMPRESSIONS
  * WB_DECREASED_PRICE_FOR_REPEATED_IMPRESSIONS
  * CP_MAXIMUM_IMPRESSIONS
  * WB_MAXIMUM_IMPRESSIONS
  * CP_AVERAGE_CPV
  * WB_AVERAGE_CPV

|  Yes  
`WbMaximumImpressions` |  StrategyWbMaximumImpressionsAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_IMPRESSIONS  
`CpMaximumImpressions` |  StrategyCpMaximumImpressionsAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to CP_MAXIMUM_IMPRESSIONS  
`WbDecreasedPriceForRepeatedImpressions` |  StrategyWbDecreasedPriceForRepeatedImpressionsAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to WB_DECREASED_PRICE_FOR_REPEATED_IMPRESSIONS  
`CpDecreasedPriceForRepeatedImpressions` |  StrategyCpDecreasedPriceForRepeatedImpressionsAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to CP_DECREASED_PRICE_FOR_REPEATED_IMPRESSIONS  
`WbAverageCpv` |  StrategyWbAverageCpvAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to WB_AVERAGE_CPV  
`CpAverageCpv` |  [StrategyCpAverageCpvAdd](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-cpm-banner-campaign#StrategyCpAverageCpvAdd) |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to CP_AVERAGE_CPV  
**StrategyWbMaximumImpressionsAdd structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`SpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
**StrategyCpMaximumImpressionsAdd structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`SpendLimit` |  long |  The budget for the period in the advertiser's currency, multiplied by 1,000,000. The minimum budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`StartDate` |  string |  Date of the start of the period, in the format YYYY-MM-DD. Can't be earlier than the current date or the campaign start date. |  Yes  
`EndDate` |  string |  Date of the end of the period, in the format YYYY-MM-DD. Can't be later than the campaign end date. |  Yes  
`AutoContinue` |  YesNoEnum |  Extend the campaign period automatically in order to use the remaining budget. |  Yes  
**StrategyWbDecreasedPriceForRepeatedImpressionsAdd structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`SpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
**StrategyCpDecreasedPriceForRepeatedImpressionsAdd structure** |  |  |   
`AverageCpm` |  long |  The average CPM in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`SpendLimit` |  long |  The budget for the period in the advertiser's currency, multiplied by 1,000,000. The minimum budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`StartDate` |  string |  Date of the start of the period, in the format YYYY-MM-DD. Can't be earlier than the current date or the campaign start date. |  Yes  
`EndDate` |  string |  Date of the end of the period, in the format YYYY-MM-DD. Can't be later than the campaign end date. |  Yes  
`AutoContinue` |  YesNoEnum |  Extend the campaign period automatically in order to use the remaining budget. |  Yes  
**StrategyWbAverageCpvAdd structure** |  |  |   
`AverageCpv` |  long |  The average CPV in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`SpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
**StrategyCpAverageCpvAdd structure** |  |  |   
`AverageCpv` |  long |  The average CPV in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`SpendLimit` |  long |  The budget for the period in the advertiser's currency, multiplied by 1,000,000. The minimum budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`StartDate` |  string |  Date of the start of the period, in the format YYYY-MM-DD. Can't be earlier than the current date or the campaign start date. |  Yes  
`EndDate` |  string |  Date of the end of the period, in the format YYYY-MM-DD. Can't be later than the campaign end date. |  Yes  
`AutoContinue` |  YesNoEnum |  Extend the campaign period automatically in order to use the remaining budget. |  Yes  
Copied
### Was the article helpful?
YesNo
Previous
[add: MobileAppCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-mobile-app-campaign)
Next
[archive](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/archive)
