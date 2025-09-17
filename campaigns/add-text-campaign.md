---
title: add: TextCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/add-text-campaign
crawled_at: 2025-09-17T16:03:04.731155
---

add: TextCampaign parameters
# add: TextCampaign parameters
Request structure in JSON format:
```
{
  "method": "add",
  "params": {
    "Campaigns": [{  /* CampaignAddItem */
      ...
      "TextCampaign": {  /* TextCampaignAddItem */
        "BiddingStrategy": {  /* TextCampaignStrategyAdd */
          "Search": {  /* TextCampaignSearchStrategyAdd */
            "BiddingStrategyType": ( "AVERAGE_CPA" | ... | "WEEKLY_CLICK_PACKAGE" ), /* required */
            "PlacementTypes" : {
              "SearchResults" : ( "YES" | "NO" ),
              "ProductGallery" : ( "YES" | "NO" ),
              "DynamicPlaces" : ( "YES" | "NO" )
            },
            "WbMaximumClicks": {  /* StrategyMaximumClicksAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "WbMaximumConversionRate": {  /* StrategyMaximumConversionRateAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long),
              "GoalId": (long), /* required */
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
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
            "AverageCpa": {  /* StrategyAverageCpaAdd */
              "AverageCpa": (long), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long),
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "AverageCpaMultipleGoals": {  /* StrategyAverageCpaMultipleGoalsAdd */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long),
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "WeeklyClickPackage": {  /* StrategyWeeklyClickPackageAdd */
              "ClicksPerWeek": (long), /* required */
              "AverageCpc": (long),
              "BidCeiling": (long)
            },
            "AverageRoi": {  /* StrategyAverageRoiAdd */
              "ReserveReturn": (int), /* required */
              "RoiCoef": (long), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long),
              "Profitability": (long),
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "AverageCrr": {  /* StrategyAverageCrrAdd */
              "Crr": (int), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "PayForConversionCrr" : {  /* StrategyPayForConversionCrrAdd */
              "Crr": (int), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "PayForConversion" : { /* StrategyPayForConversionAdd */
              "Cpa" : (long) /* required */,
              "GoalId" : (long) /* required */,
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "PayForConversionMultipleGoals" : { /* StrategyPayForConversionMultipleGoalsAdd */
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            }
          }, /* required */
          "Network": {  /* TextCampaignNetworkStrategyAdd */
            "BiddingStrategyType": ( "AVERAGE_CPA" | ... | "WEEKLY_CLICK_PACKAGE" ), /* required */
            "NetworkDefault": {  /* StrategyNetworkDefaultAdd */
              "LimitPercent": (int)
            },
            "WbMaximumClicks": {  /* StrategyMaximumClicksAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
            },
            "WbMaximumConversionRate": {  /* StrategyMaximumConversionRateAdd */
              "WeeklySpendLimit": (long), /* required */
              "BidCeiling": (long),
              "GoalId": (long), /* required */
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
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
            "AverageCpa": {  /* StrategyAverageCpaAdd */
              "AverageCpa": (long), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long),
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "AverageCpaMultipleGoals": {  /* StrategyAverageCpaMultipleGoalsAdd */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long),
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "WeeklyClickPackage": {  /* StrategyWeeklyClickPackageAdd */
              "ClicksPerWeek": (long), /* required */
              "AverageCpc": (long),
              "BidCeiling": (long)
            },
            "AverageRoi": {  /* StrategyAverageRoiAdd */
              "ReserveReturn": (int), /* required */
              "RoiCoef": (long), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long),
              "Profitability": (long),
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "AverageCrr": {  /* StrategyAverageCrrAdd */
              "Crr": (int), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "ExplorationBudget" : {
                "MinimumExplorationBudget" : (long) /* required */,
                "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
              }
            },
            "PayForConversionCrr" : {  /* StrategyPayForConversionCrrAdd */
              "Crr": (int), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "PayForConversion" : { /* StrategyPayForConversionAdd */
              "Cpa" : (long) /* required */,
              "GoalId" : (long) /* required */,
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "PayForConversionMultipleGoals" : { /* StrategyPayForConversionMultipleGoalsAdd */
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
        "Settings": [{  /* TextCampaignSetting */
          "Option": ( "ADD_METRICA_TAG" | ... | "REQUIRE_SERVICING" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
        "CounterIds": {  /* ArrayOfInteger */
          "Items": [(int), ... ] /* required */
        },
        "RelevantKeywords": {  /* RelevantKeywordsSettingAdd */
          "BudgetPercent": (int), /* required */
          "OptimizeGoalId": (long) /* nillable */
        },
        "PriorityGoals": { /* PriorityGoalsArray */
          "Items": [{ /* PriorityGoalsItem */
            "GoalId": (long), /* required */
            "Value": (long), /* required */
            "IsMetrikaSourceOfValue": ( "YES" | "NO" )
          }, ... ] /* required */
        },
        "TrackingParams": (string),
        "AttributionModel": ( "FC" | "LC" | "LSC" | "LYDC" | "FCCD" | "LSCCD" | "LYDCCD" | "AUTO" ),
        "PackageBiddingStrategy": { /* TextCampaignPackageBiddingStrategyAdd */
          "StrategyId": (long),
          "StrategyFromCampaignId": (long),
          "Platforms" : { /* required */
            "SearchResult" : ( "YES" | "NO" ) /* required */,
            "ProductGallery" : ( "YES" | "NO" ) /* required */,
            "Network" : ( "YES" | "NO" ) /* required */,
            "DynamicPlaces" : ( "YES" | "NO" )
          }
        },
        "NegativeKeywordSharedSetIds" : { /* nillable */
          "Items" : [ (long) ] /* required */
        }
      }, ... ] /* required */
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**TextCampaignAddItem structure** |  |  |   
`BiddingStrategy` |  TextCampaignStrategyAdd |  Display strategy. |  No if PackageBiddingStrategy is specified  
`Settings` |  array of TextCampaignSetting |  Array of settings that only accept the values YES or NO. |  No  
`CounterIds` |  ArrayOfInteger |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |  No  
`RelevantKeywords` |  RelevantKeywordsSettingAdd |  Settings for impressions for related keywords (see  |  No  
`PriorityGoals` |  PriorityGoalsArray |  Priority goals for automatic bid adjustments. If the array is omitted, automatic bid adjustments are used for obtaining the maximum number of engaged sessions (see  You can't add more than 30 priority goals. |  When passing the `AverageCpaMultipleGoals` or `PayForConversionMultipleGoals` parameter.  
`TrackingParams` |  string |  URL parameters for templates. |  No  
`AttributionModel` |  AttributionModelEnum |  The attribution model used for optimizing conversions (see  Possible values:
  * FC — First click.
  * LC — Last click.
  * LSC — Last significant (non-direct) click.
  * LYDC — Last click from Yandex Direct.
  * FCCD – First cross-device click.
  * LSCCD – Last significant (non-direct) cross-device click.
  * LYDCCD – Last cross-device click from Yandex Direct.
  * AUTO – Automatic attribution.

The default value is AUTO. |  No  
`PackageBiddingStrategy` |  TextCampaignPackageBiddingStrategyAdd |  Links a campaign to the specified strategy. You can't pass the following parameters in this field:
  * `BiddingStrategy`.
  * `PriorityGoals`.
  * `CounterIds`.
  * `AttributionModel`.

To pass these parameters, unlink the campaign from the portfolio strategy: specify a new value for `BiddingStrategy` and reset the `PackageBiddingStrategy: null` parameter value. |  No if BiddingStrategy is specified  
`NegativeKeywordSharedSetIds` |  ArrayOfLong |  IDs of sets of negative keywords. Maximum of 3 items in the array. To get the IDs of sets, use the [NegativeKeywordSharedSets](https://yandex.com/dev/direct/doc/en/campaigns/en/negativekeywordsharedsets/negativekeywordsharedsets).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/negativekeywordsharedsets/get) method. |  No  
**TextCampaignSetting structure** |  |  |   
`Option` |  TextCampaignSettingsEnum |  Setting name:
  * ADD_METRICA_TAG
  * ADD_OPENSTAT_TAG
  * ADD_TO_FAVORITES
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * ENABLE_COMPANY_INFO
  * ENABLE_EXTENDED_AD_TITLE
  * ENABLE_SITE_MONITORING
  * EXCLUDE_PAUSED_COMPETING_ADS
  * MAINTAIN_NETWORK_CPC
  * REQUIRE_SERVICING

|  Yes  
  * CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED

|  No |  |   
`Value` |  YesNoEnum |  Setting value. |  Yes  
**RelevantKeywordsSettingAdd structure** |  |  |   
`BudgetPercent` |  int |  Maximum percent of the budget to be spent on clicks on related keywords (from 1 to 100). |  Yes  
`OptimizeGoalId` |  long, nillable |  The ID of the Yandex Metrica goal for optimizing related keywords. You can't set a specific goal during campaign creation. The following values are allowed:
  * 0 — Related keywords are optimized for all the goals available for the campaign.
  * null (nil) — No optimization.

If the parameter is omitted, the default value is 0. |  No  
**TextCampaignPackageBiddingStrategyAdd structure** |  |  |   
`StrategyId` |  long |  Portfolio strategy ID. |  No  
`StrategyFromCampaignId` |  long |  ID of the campaign the portfolio strategy was created from. |  No  
`Platforms` |  TextCampaignPlatforms |  Ad placement platform. |  Yes  
**PriorityGoalsArray structure** |  |  |   
`Items` |  array of PriorityGoalsItem |  A set of priority goals and corresponding conversion values. |  Yes  
**PriorityGoalsItem structure** |  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal to prioritize when automatically adjusting bids. For more information about goals, see  To get the list of goals, use the  A value of 12 corresponds to the "Engaged sessions" goal. |  Yes  
`Value` |  long |  The conversion value is a monetary estimation of the advertiser's profit when the goal is completed, in the advertiser's currency, multiplied by 1,000,000. The higher the conversion value, the higher the priority to achieve conversions for this goal. |  Yes  
`IsMetrikaSourceOfValue` |  YesNoEnum |  Priority goal value source: Yandex Metrica goal. The `YES` value is only used for strategies with cost revenue ratio. |  If the BiddingStrategyType parameter is set to AVERAGE_CRR or PAY_FOR_CONVERSION_CRR  
**TextCampaignPlatforms structure** |  |  |   
`SearchResult` |  YesNoEnum |  Search results. |  Yes  
`ProductGallery` |  YesNoEnum |  Product gallery. |  Yes  
`Network` |  YesNoEnum |  Yandex Advertising Network. |  Yes  
`DynamicPlaces` |  YesNoEnum |  Dynamic placements in search results. |  No  
**TextCampaignStrategyAdd structure** |  |  |   
`Search` |  TextCampaignSearchStrategyAdd |  Display strategy in search results. |  Yes  
`Network` |  TextCampaignNetworkStrategyAdd |  Display strategy in ad networks. |  Yes  
**TextCampaignSearchStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  TextCampaignSearchStrategyTypeEnum |  The type of display strategy in search results:
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
  * SERVING_OFF

For information about the compatibility of strategies in search results and ad networks, see the section  |  Yes  
`PlacementTypes` |  TextCampaignSearchStrategyPlacementTypes |  Placements in search results. Note When creating a campaign, the "Dynamic placements in search results" placement type takes the same value as the "Search results" type (`SearchResults` field). In the future, we'll add the ability to manage the "Dynamic placements in search results" type through the API. |  No  
`WbMaximumClicks` |  StrategyMaximumClicksAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CLICKS  
`WbMaximumConversionRate` |  StrategyMaximumConversionRateAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CONVERSION_RATE  
`AverageCpc` |  StrategyAverageCpcAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC  
`AverageCpa` |  StrategyAverageCpaAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA  
`AverageCpaMultipleGoals` |  StrategyAverageCpaMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_MULTIPLE_GOALS  
`AverageRoi` |  StrategyAverageRoiAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_ROI  
`AverageCrr` |  StrategyAverageCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CRR  
`PayForConversionCrr` |  StrategyPayForConversionCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_CRR  
`WeeklyClickPackage` |  StrategyWeeklyClickPackageAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WEEKLY_CLICK_PACKAGE  
`PayForConversion` |  StrategyPayForConversionAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
`PayForConversionMultipleGoals` |  StrategyPayForConversionMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
**TextCampaignNetworkStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  TextCampaignNetworkStrategyTypeEnum |  The type of display strategy in ad networks:
  * NETWORK_DEFAULT
  * MAXIMUM_COVERAGE
  * WB_MAXIMUM_CLICKS
  * WB_MAXIMUM_CONVERSION_RATE
  * AVERAGE_CPC
  * AVERAGE_CPA
  * AVERAGE_ROI
  * AVERAGE_CRR
  * PAY_FOR_CONVERSION
  * PAY_FOR_CONVERSION_CRR
  * WEEKLY_CLICK_PACKAGE
  * SERVING_OFF

For information about the compatibility of strategies in search results and ad networks, see the section  |  Yes  
`NetworkDefault` |  StrategyNetworkDefaultAdd |  Settings for impressions in ad networks based on the settings for search. If a search strategy other than HIGHEST_POSITION is selected, pass an empty structure. |  When the `BiddingStrategyType` parameter is set to NETWORK_DEFAULT  
`WbMaximumClicks` |  StrategyMaximumClicksAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CLICKS  
`WbMaximumConversionRate` |  StrategyMaximumConversionRateAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CONVERSION_RATE  
`AverageCpc` |  StrategyAverageCpcAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC  
`AverageCpa` |  StrategyAverageCpaAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA  
`AverageCpaMultipleGoals` |  StrategyAverageCpaMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_MULTIPLE_GOALS  
`AverageRoi` |  StrategyAverageRoiAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_ROI  
`AverageCrr` |  StrategyAverageCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CRR  
`PayForConversion` |  StrategyPayForConversionAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
`PayForConversionMultipleGoals` |  StrategyPayForConversionMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
`PayForConversionCrr` |  StrategyPayForConversionCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_CRR  
`WeeklyClickPackage` |  StrategyWeeklyClickPackageAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WEEKLY_CLICK_PACKAGE  
**StrategyMaximumClicksAdd structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**TextCampaignSearchStrategyPlacementTypes structure** |  |  |   
`SearchResults` |  YesNoEnum |  Search results. |  No  
`ProductGallery` |  YesNoEnum |  Product gallery. |  No  
`DynamicPlaces` |  YesNoEnum |  Dynamic placements in search results. |  No  
**StrategyMaximumConversionRateAdd structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  The value 13 indicates priority goals. Allowed if the PriorityGoals array specifies at least one goal that is different from engaged sessions. To get the list of goals, use the  |  Yes  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyAverageCpcAdd structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyAverageCpaAdd structure** |  |  |   
`AverageCpa` |  long |  The average goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCpaMultipleGoalsAdd structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageRoiAdd structure** |  |  |   
`ReserveReturn` |  int |  The maximum percentage of saved funds that can be returned to advertising (spent) if the forecasted return on investment exceeds the value of the `RoiCoef` parameter. A value from 0 to 100 as a multiple of ten: 0, 10, 20... 100. |  Yes  
`RoiCoef` |  long |  The desired average return on investment per week. The value represents the ratio between sales profits and ad costs, multiplied by 1,000,000. The value must be an integer. If the value is not a multiple of 10,000, the last 4 digits are reset to zero (which is the same as discarding extra decimal digits). |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  The value 13 indicates priority goals. Allowed if the PriorityGoals array specifies at least one goal that is different from engaged sessions. To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`Profitability` |  long |  The percentage of revenue that is the cost value of products or services. The value is a percentage multiplied by 1,000,000. The value must be an integer between 0 and 100,000,000 (which corresponds to 100%). If the value is not a multiple of 10,000, the last 4 digits are reset to zero (which is the same as discarding extra decimal digits). |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCrrAdd structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyPayForConversionAdd structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**PayForConversionMultipleGoals structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyPayForConversionCrrAdd structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyWeeklyClickPackageAdd structure** |  |  |   
`ClicksPerWeek` |  long |  Desired number of clicks per week. |  Yes  
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note The `AverageCpc` and `BidCeiling` parameters are mutually exclusive. You can't specify both of them. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note The `AverageCpc` and `BidCeiling` parameters are mutually exclusive. You can't specify both of them. |  No  
**StrategyNetworkDefaultAdd structure** |  |  |   
`LimitPercent` |  int |  The maximum percentage of the budget to spend on displays in ad networks. The value is a multiple of ten: 10, 20, ..., 100. The default value is 100. If a search strategy other than HIGHEST_POSITION is selected, the parameter is not used and the passed value is ignored. |  No  
**ExplorationBudget structure** |  |  |   
`MinimumExplorationBudget` |  long |  Minimum budget value. Acceptable value: between 0 and the weekly budget (if set). |  Yes, if the request includes the `ExplorationBudget` structure.  
`IsMinimumExplorationBudgetCustom` |  YesNoEnum |  A flag indicating a custom minimum budget. |  Yes, if the request includes the `ExplorationBudget` structure.  
**CustomPeriodBudget structure** |  |  |   
`SpendLimit` |  long |  Budget size for a custom period. |  Yes  
`StartDate` |  string |  Start of the budget period. |  Yes  
`EndDate` |  string |  End of the budget period. |  Yes  
`AutoContinue` |  YesNoEnum |  Flag to autocontinue the budget period. |  Yes  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add)
Next
[add: UnifiedCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-unified-campaign)
