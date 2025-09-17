---
title: get: UnifiedCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/get-unified-campaign
crawled_at: 2025-09-17T16:01:39.766365
---

get: UnifiedCampaign parameters
# get: UnifiedCampaign parameters
To manage a unified performance campaign, use the URL: `https://api.direct.yandex.com/v501/`.
Copied
Response structure in JSON format:
```
{
  "result": {
    "Campaigns": [{  /* CampaignGetItem */
      ...
      "UnifiedCampaign": {  /* UnifiedCampaignGetItem */
        "BiddingStrategy": {  /* UnifiedCampaignStrategy */
          "Search": {  /* UnifiedCampaignSearchStrategy */
            "BiddingStrategyType": ("AVERAGE_CPC"|"AVERAGE_CPA"|"PAY_FOR_CONVERSION"|"WB_MAXIMUM_CONVERSION_RATE"|"HIGHEST_POSITION"|"SERVING_OFF"|"UNKNOWN"|"WB_MAXIMUM_CLICKS"|"AVERAGE_CRR"|"PAY_FOR_CONVERSION_CRR"), /* required */
            "PlacementTypes" : {
              "SearchResults" : ( "YES" | "NO" ),
              "ProductGallery" : ( "YES" | "NO" ),
              "DynamicPlaces" : ( "YES" | "NO" ),
              "Maps" : ( "YES" | "NO" ),
              "SearchOrganizationList" : ( "YES" | "NO" )
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
              "CustomPeriodBudget": { /* nillable */
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
            "AverageCpaMultipleGoals": {  /* StrategyAverageCpaMultipleGoals */
              "WeeklySpendLimit": (long), /* nillable */
              "BidCeiling": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
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
            },
            "PayForConversionMultipleGoals" : { /* StrategyPayForConversionMultipleGoals */
              "WeeklySpendLimit" : (long) /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
            }
          },
          "Network": {  /* UnifiedCampaignNetworkStrategy */
            "BiddingStrategyType": ("AVERAGE_CPC"|"AVERAGE_CPA"|"PAY_FOR_CONVERSION"|"WB_MAXIMUM_CONVERSION_RATE"|"NETWORK_DEFAULT"|"SERVING_OFF"|"UNKNOWN"|"WB_MAXIMUM_CLICKS"|"AVERAGE_CRR"|"PAY_FOR_CONVERSION_CRR"), /* required */
            "WbMaximumClicks": {  /* StrategyMaximumClicks */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
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
              },
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
            "AverageCpaMultipleGoals": {  /* StrategyAverageCpaMultipleGoals */
              "WeeklySpendLimit": (long), /* nillable */
              "BidCeiling": (long), /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
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
            },
            "PayForConversionMultipleGoals" : { /* StrategyPayForConversionMultipleGoals */
              "WeeklySpendLimit" : (long) /* nillable */
              "CustomPeriodBudget": { /* nillable */
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
            }
          }
        },
        "Settings": [{  /* UnifiedCampaignSettingGet */
          "Option" : ("ADD_METRICA_TAG"|"ADD_TO_FAVORITES"|"ENABLE_AREA_OF_INTEREST_TARGETING"|"ENABLE_SITE_MONITORING"|"REQUIRE_SERVICING"|"ENABLE_COMPANY_INFO"|"SHARED_ACCOUNT_ENABLED"|"CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED" | "ALTERNATIVE_TEXTS_ENABLED"), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
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
        "TrackingParams": (string), /* nillable */
        "AttributionModel": ( "FC" | "LC" | "LSC" | "LYDC" | "FCCD" | "LSCCD" | "LYDCCD" | "AUTO" ),
        "PackageBiddingStrategy" : { /* nillable */
          "StrategyId" : (long), /* required */
          "Platforms" : { /* required */
            "SearchResult" : ( "YES" | "NO" ) /* required */,
            "ProductGallery" : ( "YES" | "NO" ) /* required */,
            "Maps" : ( "YES" | "NO" ) /* required */,
            "SearchOrganizationList" : ( "YES" | "NO" ) /* required */,
            "Network" : ( "YES" | "NO" ) /* required */,
            "DynamicPlaces" : ( "YES" | "NO" )
          }
        },
        "CanBeUsedAsPackageBiddingStrategySource" : ( "YES" | "NO" ),
        "NegativeKeywordSharedSetIds" : { /* nillable */
          "Items" : [ (long) ] /* required */
        }
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description** |   
---|---|---|---  
**UnifiedCampaignGetItem structure** |  |  |   
`Settings` |  array of UnifiedCampaignSettingGet |  Array of settings that only accept the values YES or NO. |   
`CounterIds` |  ArrayOfInteger, nillable |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |   
`BiddingStrategy` |  UnifiedCampaignStrategy |  Display strategy. |   
`PriorityGoals` |  PriorityGoalsArray, nillable |  Priority goals for automatic bid adjustments. If the array is omitted, automatic bid adjustments are used for obtaining the maximum number of engaged sessions (see  You can't add more than 30 priority goals. |   
`TrackingParams` |  string, nillable |  URL parameters for templates. |   
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
`PackageBiddingStrategy` |  UnifiedCampaignPackageBiddingStrategyGet, nillable |  Information about the portfolio strategy. Null (nil): The campaign is not part of the portfolio strategy. |   
`CanBeUsedAsPackageBiddingStrategySource` |  YesNoEnum |  Shows if the strategy for this campaign can be portfolio. |   
`NegativeKeywordSharedSetIds` |  ArrayOfLong, nillable |  IDs of sets of negative keywords. Maximum of 3 items in the array. |   
**UnifiedCampaignSettingGet structure** |  |  |   
`Option` |  UnifiedCampaignSettingsGetEnum |  Setting name:
  * ADD_METRICA_TAG
  * ADD_TO_FAVORITES
  * CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * ENABLE_COMPANY_INFO
  * ENABLE_SITE_MONITORING
  * REQUIRE_SERVICING
  * SHARED_ACCOUNT_ENABLED
  * ALTERNATIVE_TEXTS_ENABLED

|   
`Value` |  YesNoEnum |  Setting value. |   
**PriorityGoalsArray structure** |  |  |   
`Items` |  array of PriorityGoalsItem |  A set of priority goals and corresponding conversion values. |   
**UnifiedCampaignPackageBiddingStrategyGet structure** |  |  |   
`StrategyId` |  long |  Portfolio strategy ID. |   
`Platforms` |  UnifiedCampaignPlatforms |  Ad placement platform. |   
**PriorityGoalsItem structure** |  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal to prioritize when automatically adjusting bids. For more information about goals, see  To get the list of goals, use the  A value of 12 corresponds to the "Engaged sessions" goal. |   
`Value` |  long |  The conversion value is a monetary estimation of the advertiser's profit when the goal is completed, in the advertiser's currency, multiplied by 1,000,000. The higher the conversion value, the higher the priority to achieve conversions for this goal. |   
`IsMetrikaSourceOfValue` |  YesNoEnum |  Priority goal value source: Yandex Metrica goal. The `YES` value is only used for strategies with cost revenue ratio. |   
**UnifiedCampaignPlatforms structure** |  |  |   
`SearchResult` |  YesNoEnum |  Search results. |   
`ProductGallery` |  YesNoEnum |  Product gallery. |   
`Maps` |  YesNoEnum |  Yandex Maps. |   
`SearchOrganizationList` |  YesNoEnum |  List of organizations in search results. |   
`Network` |  YesNoEnum |  Yandex Advertising Network. |   
`DynamicPlaces` |  YesNoEnum |  Dynamic placements in search results. |   
**UnifiedCampaignStrategy structure** |  |  |   
`Search` |  UnifiedCampaignSearchStrategy |  Display strategy in search results. |   
`Network` |  UnifiedCampaignNetworkStrategy |  Display strategy in ad networks. |   
**UnifiedCampaignSearchStrategy structure** |  |  |   
`BiddingStrategyType` |  UnifiedCampaignSearchStrategyTypeEnum |  The type of display strategy in search results:
  * WB_MAXIMUM_CLICKS
  * WB_MAXIMUM_CONVERSION_RATE
  * AVERAGE_CPC
  * AVERAGE_CPA
  * AVERAGE_CRR
  * HIGHEST_POSITION
  * PAY_FOR_CONVERSION
  * PAY_FOR_CONVERSION_CRR
  * SERVING_OFF

|   
`PlacementTypes` |  UnifiedCampaignSearchStrategyPlacementTypes |  Placements in search results. |   
`WbMaximumClicks` |  StrategyMaximumClicks |  Parameters of the  |   
`WbMaximumConversionRate` |  StrategyMaximumConversionRate |  Parameters of the  |   
`AverageCpc` |  StrategyAverageCpc |  Parameters of the  |   
`AverageCpa` |  StrategyAverageCpa |  Parameters of the  |   
`AverageCpaMultipleGoals` |  StrategyAverageCpaMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |   
`AverageCrr` |  StrategyAverageCrr |  Parameters of the strategy  |   
`PayForConversionCrr` |  StrategyPayForConversionCrr |  Parameters of the strategy  |   
`PayForConversion` |  StrategyPayForConversion |  Parameters of the  |   
`PayForConversionMultipleGoals` |  StrategyPayForConversionMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |   
**UnifiedCampaignNetworkStrategy structure** |  |  |   
`BiddingStrategyType` |  UnifiedCampaignNetworkStrategyTypeEnum |  The type of display strategy in ad networks:
  * NETWORK_DEFAULT
  * WB_MAXIMUM_CLICKS
  * WB_MAXIMUM_CONVERSION_RATE
  * AVERAGE_CPC
  * AVERAGE_CPA
  * AVERAGE_CRR
  * PAY_FOR_CONVERSION
  * PAY_FOR_CONVERSION_CRR
  * SERVING_OFF

|   
`WbMaximumClicks` |  StrategyMaximumClicks |  Parameters of the  |   
`WbMaximumConversionRate` |  StrategyMaximumConversionRate |  Parameters of the  |   
`AverageCpc` |  StrategyAverageCpc |  Parameters of the  |   
`AverageCpa` |  StrategyAverageCpa |  Parameters of the  |   
`AverageCpaMultipleGoals` |  StrategyAverageCpaMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |   
`AverageCrr` |  StrategyAverageCrr |  Parameters of the strategy  |   
`PayForConversionCrr` |  StrategyPayForConversionCrr |  Parameters of the strategy  |   
`PayForConversion` |  StrategyPayForConversion |  Parameters of the  |   
`PayForConversionMultipleGoals` |  StrategyPayForConversionMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |   
**UnifiedCampaignSearchStrategyPlacementTypes structure** |  |  |   
`SearchResults` |  YesNoEnum |  Search results. |   
`ProductGallery` |  YesNoEnum |  Product gallery. |   
`DynamicPlaces` |  YesNoEnum |  Dynamic placements in search results. |   
`Maps` |  YesNoEnum |  Yandex Maps. |   
`SearchOrganizationList` |  YesNoEnum |  List of organizations in search results. |   
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
**StrategyAverageCpaMultipleGoalsAdd structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |   
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
**PayForConversionMultipleGoals structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
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
[get: TextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-text-campaign)
Next
[get: SmartCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-smart-campaign)
