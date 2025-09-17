---
title: add: MobileAppCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/add-mobile-app-campaign
crawled_at: 2025-09-17T16:02:00.542124
---

add: MobileAppCampaign parameters
# add: MobileAppCampaign parameters
Request structure in JSON format:
```
{
  "method": "add",
  "params": {
    "Campaigns": [{  /* CampaignAddItem */
      ...
      "MobileAppCampaign": {  /* MobileAppCampaignAddItem */
        "BiddingStrategy": {  /* MobileAppCampaignStrategyAdd */
          "Search": {  /* MobileAppCampaignSearchStrategyAdd */
            "BiddingStrategyType": ( "AVERAGE_CPC" | ... | "WEEKLY_CLICK_PACKAGE" ), /* required */
            "WbMaximumClicks": {  /* StrategyMaximumClicksAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long)
            },
            "WbMaximumAppInstalls": {  /* StrategyMaximumAppInstallsAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long)
            },
            "AverageCpc": {  /* StrategyAverageCpcAdd */
              "AverageCpc": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "AverageCpi": {  /* StrategyAverageCpiAdd */
              "AverageCpi": (long), /* required */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "WeeklyClickPackage": {  /* StrategyWeeklyClickPackageAdd */
              "ClicksPerWeek": (long), /* required */
              "AverageCpc": (long),
              "BidCeiling": (long)
            },
            "PayForInstall" : {  /* StrategyPayForInstallAdd */
              "AverageCpi" : (long) /* required */,
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            }
          }, /* required */
          "Network": {  /* MobileAppCampaignNetworkStrategyAdd */
            "BiddingStrategyType": ( "AVERAGE_CPC" | ... | "WEEKLY_CLICK_PACKAGE" ), /* required */
            "NetworkDefault": {  /* StrategyNetworkDefaultAdd */
              "LimitPercent": (int)
            },
            "WbMaximumClicks": {  /* StrategyMaximumClicksAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long)
            },
            "WbMaximumAppInstalls": {  /* StrategyMaximumAppInstallsAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long)
            },
            "AverageCpc": {  /* StrategyAverageCpcAdd */
              "AverageCpc": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "AverageCpi": {  /* StrategyAverageCpiAdd */
              "AverageCpi": (long), /* required */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "WeeklyClickPackage": {  /* StrategyWeeklyClickPackageAdd */
              "ClicksPerWeek": (long), /* required */
              "AverageCpc": (long),
              "BidCeiling": (long)
            },
            "PayForInstall" : {  /* StrategyPayForInstallAdd */
              "AverageCpi" : (long) /* required */,
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            }
          } /* required */
        }, /* required */
        "Settings": [{  /* MobileAppCampaignSetting */
          "Option": ( "ADD_TO_FAVORITES" | ... | "REQUIRE_SERVICING" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
        "NegativeKeywordSharedSetIds" : { /* nillable */
          "Items" : [ (long) ] /* required */
        }
      }
    }, ...] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**MobileAppCampaignAddItem structure** |  |  |   
`Settings` |  array of MobileAppCampaignSetting |  Array of settings that only accept the values YES or NO. |  No  
`BiddingStrategy` |  MobileAppCampaignStrategyAdd |  Display strategy. |  Yes  
`NegativeKeywordSharedSetIds` |  ArrayOfLong, nillable |  IDs of sets of negative keywords. Maximum of 3 items in the array. To get the IDs of sets, use the [NegativeKeywordSharedSets](https://yandex.com/dev/direct/doc/en/campaigns/en/negativekeywordsharedsets/negativekeywordsharedsets).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/negativekeywordsharedsets/get) method. |  No  
**MobileAppCampaignSetting structure** |  |  |   
`Option` |  MobileAppCampaignSettingsEnum |  Setting name:
  * ADD_TO_FAVORITES
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * MAINTAIN_NETWORK_CPC
  * REQUIRE_SERVICING

|  Yes  
  * CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED

|  No |  |   
`Value` |  YesNoEnum |  Setting value. |  Yes  
**MobileAppCampaignStrategyAdd structure** |  |  |   
`Search` |  MobileAppCampaignSearchStrategyAdd |  Display strategy in search results. |  Yes  
`Network` |  MobileAppCampaignNetworkStrategyAdd |  Display strategy in ad networks. |  Yes  
**MobileAppCampaignSearchStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  MobileAppCampaignSearchStrategyTypeEnum |  The type of display strategy in search results:
  * HIGHEST_POSITION
  * WB_MAXIMUM_CLICKS
  * WB_MAXIMUM_APP_INSTALLS
  * AVERAGE_CPC
  * AVERAGE_CPI
  * WEEKLY_CLICK_PACKAGE
  * PAY_FOR_INSTALL
  * SERVING_OFF

For information about the compatibility of strategies in search results and ad networks, see the section [Display strategies](https://yandex.com/dev/direct/doc/dg/objects/campaign-strategies.html). |  Yes  
`WbMaximumClicks` |  StrategyMaximumClicksAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CLICKS  
`WbMaximumAppInstalls` |  StrategyMaximumAppInstallsAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_APP_INSTALLS  
`AverageCpc` |  StrategyAverageCpcAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC  
`AverageCpi` |  StrategyAverageCpiAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPI  
`PayForInstall` |  StrategyPayForInstallAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_INSTALL  
`WeeklyClickPackage` |  StrategyWeeklyClickPackageAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WEEKLY_CLICK_PACKAGE  
**MobileAppCampaignNetworkStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  MobileAppCampaignNetworkStrategyTypeEnum |  The type of display strategy in ad networks:
  * NETWORK_DEFAULT
  * MAXIMUM_COVERAGE
  * WB_MAXIMUM_CLICKS
  * WB_MAXIMUM_APP_INSTALLS
  * AVERAGE_CPC
  * AVERAGE_CPI
  * WEEKLY_CLICK_PACKAGE
  * PAY_FOR_INSTALL
  * SERVING_OFF

For information about the compatibility of strategies in search results and ad networks, see the section [Display strategies](https://yandex.com/dev/direct/doc/dg/objects/campaign-strategies.html) |  Yes  
`NetworkDefault` |  StrategyNetworkDefaultAdd |  Settings for impressions in ad networks based on the settings for search. If a search strategy other than HIGHEST_POSITION is selected, pass an empty structure. |  When the `BiddingStrategyType` parameter is set to NETWORK_DEFAULT  
`WbMaximumClicks` |  StrategyMaximumClicksAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CLICKS  
`WbMaximumAppInstalls` |  StrategyMaximumAppInstallsAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_APP_INSTALLS  
`AverageCpc` |  StrategyAverageCpcAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC  
`AverageCpi` |  StrategyAverageCpiAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPI  
`PayForInstall` |  StrategyPayForInstallAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_INSTALL  
`WeeklyClickPackage` |  StrategyWeeklyClickPackageAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WEEKLY_CLICK_PACKAGE  
**StrategyMaximumClicksAdd structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyMaximumAppInstallsAdd structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyAverageCpcAdd structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyAverageCpiAdd structure** |  |  |   
`AverageCpi` |  long |  The average cost per app install in the advertiser's currency, multiplied by 1,000,000. The minimum acceptable value is shown in the section [Currency parameters and limits](https://yandex.com/dev/direct/doc/dg/objects/campaign.html). |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyPayForInstallAdd structure** |  |  |   
`AverageCpi` |  long |  Cost per app install in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum acceptable values are shown in [Currency parameters and restrictions](https://yandex.com/dev/direct/doc/dg/objects/campaign.html). |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyWeeklyClickPackageAdd structure** |  |  |   
`ClicksPerWeek` |  long |  Desired number of clicks per week. |  Yes  
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note The `AverageCpc` and `BidCeiling` parameters are mutually exclusive. You can't specify both of them. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyNetworkDefaultAdd structure** |  |  |   
`LimitPercent` |  int |  The maximum percentage of the budget to spend on displays in ad networks. The value is a multiple of ten: 10, 20, ..., 100. The default value is 100. If a search strategy other than HIGHEST_POSITION is selected, the parameter is not used and the passed value is ignored. |  No  
**CustomPeriodBudget structure** |  |  |   
`SpendLimit` |  long |  Budget size for a custom period. |  Yes  
`StartDate` |  string |  Start of the budget period. |  Yes  
`EndDate` |  string |  End of the budget period. |  Yes  
`AutoContinue` |  YesNoEnum |  Flag to autocontinue the budget period. |  Yes  
Copied
### Was the article helpful?
YesNo
Previous
[add: DynamicTextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-dynamic-text-campaign)
Next
[add: CpmBannerCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-cpm-banner-campaign)
