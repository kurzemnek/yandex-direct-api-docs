---
title: get: DynamicTextCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/get-dynamic-text-campaign
crawled_at: 2025-09-17T16:02:05.848373
---

get: DynamicTextCampaign parameters
# get: DynamicTextCampaign parameters
Response structure in JSON format:
```
{
  "result": {
    "Campaigns": [{  /* CampaignGetItem */
      ...
      "DynamicTextCampaign": {  /* DynamicTextCampaignGetItem */
        "BiddingStrategy": {  /* DynamicTextCampaignStrategy */
          "Search": {  /* DynamicTextCampaignSearchStrategy */
            "BiddingStrategyType": ( "AVERAGE_CPA" | ... | "WEEKLY_CLICK_PACKAGE" ), /* required */
            "PlacementTypes" : {
              "SearchResults" : ( "YES" | "NO" ),
              "ProductGallery" : ( "YES" | "NO" ),
              "DynamicPlaces" : ( "YES" | "NO" )
            },
            "WbMaximumClicks": {  /* StrategyMaximumClicks */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "WbMaximumConversionRate": {  /* StrategyMaximumConversionRate */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long), /* nillable */
              "GoalId": (long),
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
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
            "AverageCpa": {  /* StrategyAverageCpa */
              "AverageCpa": (long),
              "GoalId": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
              "BidCeiling": (long), /* nillable */
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES"| "NO") /* required */
              }
            },
            "WeeklyClickPackage": {  /* StrategyWeeklyClickPackage */
              "ClicksPerWeek": (long),
              "AverageCpc": (long), /* nillable */
              "BidCeiling": (long) /* nillable */
            },
            "AverageRoi": {  /* StrategyAverageRoi */
              "ReserveReturn": (int),
              "RoiCoef": (long),
              "GoalId": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
              "BidCeiling": (long), /* nillable */
              "Profitability": (long), /* nillable */
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES"| "NO") /* required */
              }
            },
            "AverageCrr": {  /* StrategyAverageCrr */
              "Crr": (int),
              "GoalId": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES"| "NO") /* required */
              }
            },
            "PayForConversionCrr": {  /* StrategyPayForConversionCrr */
              "Crr": (int),
              "GoalId": (long),
              "WeeklySpendLimit": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
            },
            "PayForConversion" : { /* StrategyPayForConversion */
              "Cpa" : (long),
              "GoalId" : (long),
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
          "Network": {  /* DynamicTextCampaignNetworkStrategy */
            "BiddingStrategyType": ( "SERVING_OFF" | "UNKNOWN" ) /* required */
          }
        },
        "Settings": [{  /* DynamicTextCampaignSettingGet */
          "Option": ( "ADD_METRICA_TAG" | ... | "SHARED_ACCOUNT_ENABLED" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
        "PlacementTypes" : { /* PlacementTypesItem */
          "Items" : [{ /* required */
             "Type" : ("SEARCH_RESULTS"|"PRODUCT_GALLERY") /* required */,
             "Value" : ("YES"|"NO") /* required */}, ... ]
        },
        "CounterIds": {  /* ArrayOfInteger */
          "Items": [(int), ... ] /* required */
        }, /* nillable */
        "PriorityGoals": { /* PriorityGoalsArray */
          "Items": [{ /* PriorityGoalsItem */
            "GoalId": (long), /* required */
            "Value": (long), /* required */
            "IsMetrikaSourceOfValue": ( "YES" | "NO" )
          }, ... ] /* required */
        }, /* nillable */
        "TrackingParams" : (string),
        "AttributionModel": ( "FC" | "LC" | "LSC" | "LYDC" | "FCCD" | "LSCCD" | "LYDCCD" | "AUTO" ),
        "PackageBiddingStrategy" : { /* nillable */
          "StrategyId" : (long) /* required */
        },
        "CanBeUsedAsPackageBiddingStrategySource" : ( "YES" | "NO" ),
        "NegativeKeywordSharedSetIds" : { /* nillable */
          "Items" : [ (long) ] /* required */
        },
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description** |   
---|---|---|---  
**DynamicTextCampaignGetItem structure** |  |  |   
`Settings` |  array of DynamicTextCampaignSettingGet |  Array of settings that only accept the values YES or NO. |   
`PlacementTypes` |  PlacementTypesItem |  Ad placements in search results. |   
`CounterIds` |  ArrayOfInteger, nillable |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |   
`BiddingStrategy` |  DynamicTextCampaignStrategy |  Display strategy. |   
`PriorityGoals` |  PriorityGoalsArray, nillable |  Priority goals for automatic bid adjustments. If the array is omitted, automatic bid adjustments are used for obtaining the maximum number of engaged sessions (see  You can't add more than 30 priority goals. |   
`TrackingParams` |  string |  URL parameters for templates. |   
`AttributionModel` |  AttributionModelEnum |  The attribution model used for optimizing conversions (see  Possible values:
  * FC — First click.
  * LC — Last click.
  * LSC — Last significant (non-direct) click.
  * LYDC — Last click from Yandex Direct.
  * FCCD – First cross-device click.
  * LSCCD – Last significant (non-direct) cross-device click.
  * LYDCCD – Last cross-device click from Yandex Direct.
  * AUTO – Automatic attribution.

|   
`PackageBiddingStrategy` |  DynamicTextCampaignPackageBiddingStrategyGet, nillable |  Information about the portfolio strategy. Null (nil): The campaign is not part of the portfolio strategy. |   
`CanBeUsedAsPackageBiddingStrategySource` |  string |  Shows if the strategy for this campaign can be portfolio. |   
`NegativeKeywordSharedSetIds` |  ArrayOfLong, nillable |  IDs of sets of negative keywords. Maximum of 3 items in the array. |   
**DynamicTextCampaignSettingGet structure** |  |  |   
`Option` |  DynamicTextCampaignSettingsGetEnum |  Setting name:
  * ADD_METRICA_TAG
  * ADD_OPENSTAT_TAG
  * ADD_TO_FAVORITES
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * ENABLE_COMPANY_INFO
  * ENABLE_EXTENDED_AD_TITLE
  * ENABLE_SITE_MONITORING
  * REQUIRE_SERVICING
  * SHARED_ACCOUNT_ENABLED
  * DAILY_BUDGET_ALLOWED
  * CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED

|   
`Value` |  YesNoEnum |  Setting value. |   
**PlacementTypesItem structure** |  |  |   
`Type` |  DynamicTextCampaignPlacementTypesEnum |  Type of ad placement in search results:
  * SEARCH_RESULTS — In search results.
  * PRODUCT_GALLERY — In the product gallery.

|   
`Value` |  YesNoEnum |  Setting value. |   
**PriorityGoalsArray structure** |  |  |   
`Items` |  array of PriorityGoalsItem |  A set of priority goals and corresponding conversion values. |   
**DynamicTextCampaignPackageBiddingStrategyGet structure** |  |  |   
`StrategyId` |  long |  Portfolio strategy ID. |   
**PriorityGoalsItem structure** |  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal to prioritize when automatically adjusting bids. For more information about goals, see  To get the list of goals, use the  A value of 12 corresponds to the "Engaged sessions" goal. |   
`Value` |  long |  The conversion value is a monetary estimation of the advertiser's profit when the goal is completed, in the advertiser's currency, multiplied by 1,000,000. The higher the conversion value, the higher the priority to achieve conversions for this goal. |   
`IsMetrikaSourceOfValue` |  YesNoEnum |  Priority goal value source: Yandex Metrica goal. The `YES` value is only used for strategies with cost revenue ratio. |   
**DynamicTextCampaignStrategy structure** |  |  |   
`Search` |  DynamicTextCampaignSearchStrategy |  Display strategy in search results. |   
`Network` |  DynamicTextCampaignNetworkStrategy |  Display strategy in ad networks. |   
**DynamicTextCampaignSearchStrategy structure** |  |  |   
`BiddingStrategyType` |  DynamicTextCampaignSearchStrategyTypeEnum |  The type of display strategy in search results:
  * HIGHEST_POSITION
  * WB_MAXIMUM_CLICKS
  * WB_MAXIMUM_CONVERSION_RATE
  * AVERAGE_CPC
  * AVERAGE_CPA
  * AVERAGE_ROI
  * AVERAGE_CRR
  * PAY_FOR_CONVERSION
  * PAY_FOR_CONVERSION_CRR
  * WEEKLY_CLICK_PACKAGE
  * UNKNOWN

|   
`PlacementTypes` |  DynamicTextCampaignSearchStrategyPlacementTypes |  Placements in search results. |   
`WbMaximumClicks` |  StrategyMaximumClicks |  Parameters of the  |   
`WbMaximumConversionRate` |  StrategyMaximumConversionRate |  Parameters of the  |   
`AverageCpc` |  StrategyAverageCpc |  Parameters of the  |   
`AverageCpa` |  StrategyAverageCpa |  Parameters of the  |   
`AverageRoi` |  StrategyAverageRoi |  Parameters of the  |   
`AverageCrr` |  StrategyAverageCrr |  Parameters of the strategy  |   
`PayForConversionCrr` |  StrategyPayForConversionCrr |  Parameters of the strategy  |   
`PayForConversion` |  StrategyPayForConversion |  Parameters of the  |   
`WeeklyClickPackage` |  StrategyWeeklyClickPackage |  Parameters of the  |   
**DynamicTextCampaignNetworkStrategy structure** |  |  |   
`BiddingStrategyType` |  DynamicTextCampaignNetworkStrategyTypeEnum |  The type of display strategy in ad networks. Only one value is available: SERVING_OFF. Displays are disabled |   
**DynamicTextCampaignSearchStrategyPlacementTypes structure** |  |  |   
`SearchResults` |  YesNoEnum |  Search results. |   
`ProductGallery` |  YesNoEnum |  Product gallery. |   
`DynamicPlaces` |  YesNoEnum |  Dynamic placements in search results. |   
**StrategyMaximumClicks structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
**StrategyMaximumConversionRate structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  The value 13 indicates priority goals. Allowed if the array specifies at least one goal that is different from engaged sessions. To get the list of goals, use the  |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
**StrategyAverageCpc structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`WeeklySpendLimit` |  long, nillable |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyAverageCpa structure** |  |  |   
`AverageCpa` |  long |  The average goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long, nillable |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  |   
**StrategyAverageRoi structure** |  |  |   
`ReserveReturn` |  int |  The maximum percentage of saved funds that can be returned to advertising (spent) if the forecasted return on investment exceeds the value of the `RoiCoef` parameter. A value from 0 to 100 as a multiple of ten: 0, 10, 20... 100. |   
`RoiCoef` |  long |  The desired average return on investment per week. The value represents the ratio between sales profits and ad costs, multiplied by 1,000,000. The value must be an integer. If the value is not a multiple of 10,000, the last 4 digits are reset to zero (which is the same as discarding extra decimal digits). |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  The value 13 indicates priority goals. Allowed if the array specifies at least one goal that is different from engaged sessions. To get the list of goals, use the  |   
`WeeklySpendLimit` |  long, nillable |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`Profitability` |  long, nillable |  The percentage of revenue that is the cost value of products or services. The value is a percentage multiplied by 1,000,000. The value must be an integer between 0 and 100,000,000 (which corresponds to 100%). If the value is not a multiple of 10,000, the last 4 digits are reset to zero (which is the same as discarding extra decimal digits). |   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  |   
**StrategyAverageCrr structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  |   
**StrategyPayForConversionCrr structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyPayForConversion structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long, nillable |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyWeeklyClickPackage structure** |  |  |   
`ClicksPerWeek` |  long |  Desired number of clicks per week. |   
`AverageCpc` |  long, nillable |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note The `AverageCpc` and `BidCeiling` parameters are mutually exclusive. You can't specify both of them. |   
`BidCeiling` |  long, nillable |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note The `AverageCpc` and `BidCeiling` parameters are mutually exclusive. You can't specify both of them. |   
**ExplorationBudget structure** |  |  |   
`MinimumExplorationBudget` |  long |  Minimum budget value. Acceptable value: between 0 and the weekly budget (if set). |   
`IsMinimumExplorationBudgetCustom` |  YesNoEnum |  A flag indicating a custom minimum budget. |   
**CustomPeriodBudget structure** |  |  |   
`SpendLimit` |  long |  Budget size for a custom period. |   
`StartDate` |  string |  Start of the budget period. |   
`EndDate` |  string |  End of the budget period. |   
`AutoContinue` |  YesNoEnum |  Flag to autocontinue the budget period. |   
Copied
### Was the article helpful?
YesNo
Previous
[get: SmartCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-smart-campaign)
Next
[get: MobileAppCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-mobile-app-campaign)
