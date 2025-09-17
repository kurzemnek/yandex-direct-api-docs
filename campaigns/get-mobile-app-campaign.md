---
title: get: MobileAppCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/get-mobile-app-campaign
crawled_at: 2025-09-17T16:01:33.595351
---

get: MobileAppCampaign parameters
# get: MobileAppCampaign parameters
Response structure in JSON format:
```
{
  "result": {
    "Campaigns": [{  /* CampaignGetItem */
      ...
      "MobileAppCampaign": {  /* MobileAppCampaignGetItem */
        "BiddingStrategy": {  /* MobileAppCampaignStrategy */
          "Search": {  /* MobileAppCampaignSearchStrategy */
            "BiddingStrategyType": ( "AVERAGE_CPC" | ... | "WEEKLY_CLICK_PACKAGE" ), /* required */
            "WbMaximumClicks": {  /* StrategyMaximumClicks */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long) /* nillable */
            },
            "WbMaximumAppInstalls": {  /* StrategyMaximumAppInstalls */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long) /* nillable */
            },
            "AverageCpc": {  /* StrategyAverageCpc */
              "AverageCpc": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
            },
            "AverageCpi": {  /* StrategyAverageCpi */
              "AverageCpi": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
              "BidCeiling": (long) /* nillable */
            },
            "WeeklyClickPackage": {  /* StrategyWeeklyClickPackage */
              "ClicksPerWeek": (long),
              "AverageCpc": (long), /* nillable */
              "BidCeiling": (long) /* nillable */
            },
            "PayForInstall" : {  /* StrategyPayForInstall */
              "AverageCpi" : (long),
              "WeeklySpendLimit" : (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
            }
          },
          "Network": {  /* MobileAppCampaignNetworkStrategy */
            "BiddingStrategyType": ( "AVERAGE_CPC" | ... | "WEEKLY_CLICK_PACKAGE" ), /* required */
            "NetworkDefault": {  /* StrategyNetworkDefault */
              "LimitPercent": (int)
            },
            "WbMaximumClicks": {  /* StrategyMaximumClicks */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long) /* nillable */
            },
            "WbMaximumAppInstalls": {  /* StrategyMaximumAppInstalls */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long) /* nillable */
            },
            "AverageCpc": {  /* StrategyAverageCpc */
              "AverageCpc": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
            },
            "AverageCpi": {  /* StrategyAverageCpi */
              "AverageCpi": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "BidCeiling": (long) /* nillable */
            },
            "WeeklyClickPackage": {  /* StrategyWeeklyClickPackage */
              "ClicksPerWeek": (long),
              "AverageCpc": (long), /* nillable */
              "BidCeiling": (long) /* nillable */
            },
            "PayForInstall" : {  /* StrategyPayForInstall */
              "AverageCpi" : (long),
              "WeeklySpendLimit" : (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
          }
        },
        "Settings": [{  /* MobileAppCampaignSettingGet */
          "Option": ( "ADD_TO_FAVORITES" | ... | "SHARED_ACCOUNT_ENABLED" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
        "PackageBiddingStrategy" : { /* nillable */
          "StrategyId" : (long), /* required */
        },
        "CanBeUsedAsPackageBiddingStrategySource" : ( "YES" | "NO" ),
        "NegativeKeywordSharedSetIds" : { /* nillable */
          "Items" : [ (long) ] /* required */
        },
       }
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description** |   
---|---|---|---  
**MobileAppCampaignGetItem structure** |  |  |   
`Settings` |  array of MobileAppCampaignSettingGet |  Array of settings that only accept the values YES or NO. |   
`BiddingStrategy` |  MobileAppCampaignStrategy |  Display strategy. |   
`PackageBiddingStrategy` |  MobileAppCampaignPackageBiddingStrategyGet, nillable, deprecated |  Information about the portfolio strategy. Null (nil): The campaign is not part of the portfolio strategy. |   
`CanBeUsedAsPackageBiddingStrategySource` |  string, deprecated |  Shows if the strategy for this campaign can be portfolio. |   
`NegativeKeywordSharedSetIds` |  ArrayOfLong, nillable |  IDs of sets of negative keywords. Maximum of 3 items in the array. |   
**MobileAppCampaignSettingGet structure** |  |  |   
`Option` |  MobileAppCampaignSettingsEnum |  Setting name:
  * ADD_TO_FAVORITES
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * MAINTAIN_NETWORK_CPC
  * REQUIRE_SERVICING
  * SHARED_ACCOUNT_ENABLED
  * DAILY_BUDGET_ALLOWED
  * CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED

|   
`Value` |  YesNoEnum |  Setting value. |   
**MobileAppCampaignPackageBiddingStrategyGet structure** |  |  |   
`StrategyId` |  long |  Portfolio strategy ID. |   
**MobileAppCampaignStrategy structure** |  |  |   
`Search` |  [MobileAppCampaignSearchStrategy](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-mobile-app-campaign#MobileAppCampaignSearchStrategy) |  Display strategy in search results. |   
`Network` |  [MobileAppCampaignNetworkStrategy](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-mobile-app-campaign#MobileAppCampaignNetworkStrategy) |  Display strategy in ad networks. |   
**MobileAppCampaignSearchStrategy structure** |  |  |   
`BiddingStrategyType` |  MobileAppCampaignSearchStrategyTypeEnum |  The type of display strategy in search results:
  * HIGHEST_POSITION
  * WB_MAXIMUM_CLICKS
  * WB_MAXIMUM_APP_INSTALLS
  * AVERAGE_CPC
  * AVERAGE_CPI
  * WEEKLY_CLICK_PACKAGE
  * PAY_FOR_INSTALL
  * SERVING_OFF
  * UNKNOWN

|   
`WbMaximumClicks` |  StrategyMaximumClicks |  Parameters of the  |   
`WbMaximumAppInstalls` |  StrategyMaximumAppInstalls |  Parameters of the  |   
`AverageCpc` |  StrategyAverageCpc |  Parameters of the  |   
`WeeklyClickPackage` |  StrategyWeeklyClickPackage |  Parameters of the  |   
`AverageCpi` |  StrategyAverageCpi |  Parameters of the  |   
`PayForInstall` |  StrategyPayForInstall |  Parameters of the  |   
**MobileAppCampaignNetworkStrategy structure** |  |  |   
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
  * UNKNOWN

|   
`NetworkDefault` |  StrategyNetworkDefault |  Settings for impressions in ad networks based on the settings for search. If a search strategy other than HIGHEST_POSITION is selected, this structure is not returned. |   
`WbMaximumClicks` |  StrategyMaximumClicks |  Parameters of the  |   
`WbMaximumAppInstalls` |  StrategyMaximumAppInstalls |  Parameters of the  |   
`AverageCpc` |  StrategyAverageCpc |  Parameters of the  |   
`WeeklyClickPackage` |  StrategyWeeklyClickPackage |  Parameters of the  |   
`AverageCpi` |  StrategyAverageCpi |  Parameters of the  |   
`PayForInstall` |  StrategyPayForInstall |  Parameters of the  |   
**StrategyMaximumClicks structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
**StrategyMaximumAppInstalls structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
**StrategyAverageCpc structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`WeeklySpendLimit` |  long, nillable |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyAverageCpi structure** |  |  |   
`AverageCpi` |  long |  The average cost per app install in the advertiser's currency, multiplied by 1,000,000. The minimum acceptable value is shown in the section [Currency parameters and limits](https://yandex.com/dev/direct/doc/dg/objects/campaign.html). |   
`WeeklySpendLimit` |  long, nillable |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
**StrategyWeeklyClickPackage structure** |  |  |   
`ClicksPerWeek` |  long |  Desired number of clicks per week. |   
`AverageCpc` |  long, nillable |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note The `AverageCpc` and `BidCeiling` parameters are mutually exclusive. You can't specify both of them. |   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note The `AverageCpc` and `BidCeiling` parameters are mutually exclusive. You can't specify both of them. |   
**StrategyPayForInstall structure** |  |  |   
`AverageCpi` |  long |  Cost per app install in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum acceptable values are shown in [Currency parameters and restrictions](https://yandex.com/dev/direct/doc/dg/objects/campaign.html). |   
`WeeklySpendLimit` |  long, nillable |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyNetworkDefault structure** |  |  |   
`LimitPercent` |  int |  The maximum percentage of the budget to spend on displays in ad networks. The value is a multiple of ten: 10, 20, ..., 100. |   
**CustomPeriodBudget structure** |  |  |   
`SpendLimit` |  long |  Budget size for a custom period. |   
`StartDate` |  string |  Start of the budget period. |   
`EndDate` |  string |  End of the budget period. |   
`AutoContinue` |  YesNoEnum |  Flag to autocontinue the budget period. |   
Copied
### Was the article helpful?
YesNo
Previous
[get: DynamicTextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-dynamic-text-campaign)
Next
[get: CpmBannerCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-cpm-banner-campaign)
