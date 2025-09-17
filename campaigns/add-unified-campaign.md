---
title: add: UnifiedCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/add-unified-campaign
crawled_at: 2025-09-17T16:02:53.948521
---

add: UnifiedCampaign parameters
# add: UnifiedCampaign parameters
To manage a unified performance campaign, use this URL: `https://api.direct.yandex.com/v501/`.
Request structure in JSON format:
```
{
  "method": "add",
  "params": {
    "Campaigns": [{  /* CampaignAddItem */
      ...
      "UnifiedCampaign" : {
        "BiddingStrategy" : {
            "Search" : { /* required */
                "WbMaximumClicks" : {
                    "WeeklySpendLimit" : (long) /* required */,
                    "BidCeiling" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    }
                },
                "WbMaximumConversionRate" : {
                    "WeeklySpendLimit" : (long) /* required */,
                    "BidCeiling" : (long),
                    "GoalId" : (long), /* required */
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                },
                "AverageCpc" : {
                    "AverageCpc" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    }
                },
                "AverageCpa" : {
                    "AverageCpa" : (long) /* required */,
                    "GoalId" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                    "BidCeiling" : (long),
                    "ExplorationBudget" : {
                        "MinimumExplorationBudget" : (long) /* required */,
                        "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
                    }
                },
                "AverageCpaMultipleGoals" : {
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                    "BidCeiling" : (long),
                    "ExplorationBudget" : {
                        "MinimumExplorationBudget" : (long) /* required */,
                        "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
                    }
                },
                "PayForConversion" : {
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
                "PayForConversionMultipleGoals" : {
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    }
                },
                "AverageCrr" : {
                    "Crr" : (integer) /* required */,
                    "GoalId" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                    "ExplorationBudget" : {
                        "MinimumExplorationBudget" : (long) /* required */,
                        "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
                    }
                },
                "PayForConversionCrr" : {
                    "Crr" : (integer) /* required */,
                    "GoalId" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    }
                },
                "BiddingStrategyType" : ("AVERAGE_CPC"|"AVERAGE_CPA"|"PAY_FOR_CONVERSION"|"WB_MAXIMUM_CONVERSION_RATE"|"HIGHEST_POSITION"|"SERVING_OFF"|"WB_MAXIMUM_CLICKS"|"AVERAGE_CRR"|"PAY_FOR_CONVERSION_CRR") /* required */,
                "PlacementTypes" : {
                    "SearchResults" : ("YES"|"NO"),
                    "ProductGallery" : ("YES"|"NO"),
                    "DynamicPlaces" : ( "YES" | "NO" ),
                    "Maps" : ("YES"|"NO"),
                    "SearchOrganizationList" : ("YES"|"NO")
                }
            },
            "Network" : { /* required */
                "WbMaximumClicks" : {
                    "WeeklySpendLimit" : (long) /* required */,
                    "BidCeiling" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                },
                "WbMaximumConversionRate" : {
                    "WeeklySpendLimit" : (long) /* required */,
                    "BidCeiling" : (long),
                    "GoalId" : (long), /* required */
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                },
                "AverageCpc" : {
                    "AverageCpc" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    }
                },
                "AverageCpa" : {
                    "AverageCpa" : (long) /* required */,
                    "GoalId" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                    "BidCeiling" : (long),
                    "ExplorationBudget" : {
                        "MinimumExplorationBudget" : (long) /* required */,
                        "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
                    }
                },
                "AverageCpaMultipleGoals" : {
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                    "BidCeiling" : (long),
                    "ExplorationBudget" : {
                        "MinimumExplorationBudget" : (long) /* required */,
                        "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
                    }
                },
                "PayForConversion" : {
                    "Cpa" : (long) /* required */,
                    "GoalId" : (long) /* required */,
                    "WeeklySpendLimit" : (long)
                },
                "PayForConversionMultipleGoals" : {
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    }
                },
                "AverageCrr" : {
                    "Crr" : (integer) /* required */,
                    "GoalId" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    },
                    "ExplorationBudget" : {
                        "MinimumExplorationBudget" : (long) /* required */,
                        "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
                    }
                },
                "PayForConversionCrr" : {
                    "Crr" : (integer) /* required */,
                    "GoalId" : (long) /* required */,
                    "WeeklySpendLimit" : (long),
                    "CustomPeriodBudget": {
                      "SpendLimit": (long),
                      "StartDate": (string),
                      "EndDate": (string),
                      "AutoContinue": ("YES" | "NO")
                    }
                },
                "BiddingStrategyType" : ("AVERAGE_CPC"|"AVERAGE_CPA"|"PAY_FOR_CONVERSION"|"WB_MAXIMUM_CONVERSION_RATE"|"NETWORK_DEFAULT"|"SERVING_OFF"|"WB_MAXIMUM_CLICKS"|"AVERAGE_CRR"|"PAY_FOR_CONVERSION_CRR") /* required */,
                "PlacementTypes" : {
                    "Network" : ("YES"|"NO"),
                    "Maps" : ("YES"|"NO")
                }
            }
        },
        "Settings" : [{
            "Option" : ("ADD_METRICA_TAG"|"ADD_TO_FAVORITES"|"ENABLE_AREA_OF_INTEREST_TARGETING"|"ENABLE_SITE_MONITORING"|"REQUIRE_SERVICING"|"ENABLE_COMPANY_INFO"|"CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED"| "ALTERNATIVE_TEXTS_ENABLED") /* required */,
            "Value" : ("YES"|"NO") /* required */
        }, ... ],
        "CounterIds" : {
            "Items" : [ (integer) ] /* required */
        },
        "PriorityGoals" : {
            "Items" : [{ /* required */
                "GoalId" : (long) /* required */,
                "Value" : (long) /* required */,
                "IsMetrikaSourceOfValue" : ("YES"|"NO")
            }, ... ]
        },
        "TrackingParams" : (string),
        "AttributionModel" : ("LC"|"LSC"|"FC"|"LYDC"|"LSCCD"|"FCCD"|"LYDCCD"|"AUTO"),
        "PackageBiddingStrategy" : {
            "StrategyId" : (long),
            "StrategyFromCampaignId" : (long),
            "Platforms" : { /* required */
                "SearchResult" : ("YES"|"NO") /* required */,
                "ProductGallery" : ("YES"|"NO") /* required */,
                "Maps" : ("YES"|"NO"),
                "SearchOrganizationList" : ("YES"|"NO"),
                "Network" : ("YES"|"NO") /* required */,
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
**UnifiedCampaignAddItem structure** |  |  |   
`BiddingStrategy` |  UnifiedCampaignStrategyAdd |  Display strategy. |  No if PackageBiddingStrategy is specified  
`Settings` |  array of UnifiedCampaignSetting |  Array of settings that only accept the values YES or NO. |  No  
`CounterIds` |  ArrayOfInteger |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |  No  
`PriorityGoals` |  PriorityGoalsArray |  Priority goals for automatic bid adjustments. If the array is omitted, automatic bid adjustments are used for obtaining the maximum number of engaged sessions (see  |  When passing the `AverageCpaMultipleGoals` or `PayForConversionMultipleGoals` parameter.  
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
`PackageBiddingStrategy` |  UnifiedCampaignPackageBiddingStrategyAdd |  Links a campaign to the specified strategy. You can't pass the following parameters in this field:
  * `BiddingStrategy`.
  * `PriorityGoals`.
  * `CounterIds`.
  * `AttributionModel`.

To pass these parameters, unlink the campaign from the portfolio strategy: specify a new value for `BiddingStrategy` and reset the `PackageBiddingStrategy: null` parameter value. |  No if BiddingStrategy is specified  
`NegativeKeywordSharedSetIds` |  ArrayOfLong, nillable |  IDs of sets of negative keywords. Maximum of 3 items in the array. To get the IDs of sets, use the [NegativeKeywordSharedSets](https://yandex.com/dev/direct/doc/en/campaigns/en/negativekeywordsharedsets/negativekeywordsharedsets).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/negativekeywordsharedsets/get) method. |  No  
**UnifiedCampaignSetting structure** |  |  |   
`Option` |  UnifiedCampaignSettingsEnum |  Setting name:
  * ADD_METRICA_TAG
  * ADD_TO_FAVORITES
  * CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED
  * ENABLE_AREA_OF_INTEREST_TARGETING
  * ENABLE_COMPANY_INFO
  * ENABLE_SITE_MONITORING
  * REQUIRE_SERVICING
  * ALTERNATIVE_TEXTS_ENABLED

|  Yes  
`Value` |  YesNoEnum |  Setting value. |  Yes  
**UnifiedCampaignPackageBiddingStrategyAdd structure** |  |  |   
`StrategyId` |  long |  Portfolio strategy ID. |  No  
`StrategyFromCampaignId` |  long |  ID of the campaign the portfolio strategy was created from. |  No  
`Platforms` |  UnifiedCampaignPlatforms |  Ad placement platform. |  Yes  
**PriorityGoalsArray structure** |  |  |   
`Items` |  array of PriorityGoalsItem |  A set of priority goals and corresponding conversion values. |  Yes  
**PriorityGoalsItem structure** |  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal to prioritize when automatically adjusting bids. For more information about goals, see  To get the list of goals, use the  A value of 12 corresponds to the "Engaged sessions" goal. |  Yes  
`Value` |  long |  The conversion value is a monetary estimation of the advertiser's profit when the goal is completed, in the advertiser's currency, multiplied by 1,000,000. The higher the conversion value, the higher the priority to achieve conversions for this goal. |  Yes  
`IsMetrikaSourceOfValue` |  YesNoEnum |  Priority goal value source: Yandex Metrica goal. The `YES` value is only used for strategies with cost revenue ratio. |  If the BiddingStrategyType parameter is set to AVERAGE_CRR or PAY_FOR_CONVERSION_CRR  
**UnifiedCampaignPlatforms structure** |  |  |   
`SearchResult` |  YesNoEnum |  Search results. |  Yes  
`ProductGallery` |  YesNoEnum |  Product gallery. |  Yes  
`Maps` |  YesNoEnum |  Yandex Maps. |  No  
`SearchOrganizationList` |  YesNoEnum |  List of organizations in search results. |  No  
`Network` |  YesNoEnum |  Yandex Advertising Network. |  Yes  
`DynamicPlaces` |  YesNoEnum |  Dynamic placements in search results. |  No  
**UnifiedCampaignStrategyAdd structure** |  |  |   
`Search` |  UnifiedCampaignSearchStrategyAdd |  Display strategy in search results. |  Yes  
`Network` |  UnifiedCampaignNetworkStrategyAdd |  Display strategy in ad networks. |  Yes  
**UnifiedCampaignSearchStrategyAdd structure** |  |  |   
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

For information about the compatibility of strategies in search results and ad networks, see the section  |  Yes  
`PlacementTypes` |  UnifiedCampaignSearchStrategyPlacementTypes |  Placements in search results. Note When creating a campaign, the "Dynamic placements in search results" placement type takes the same value as the "Search results" type (`SearchResults` field). In the future, we'll add the ability to manage the "Dynamic placements in search results" type through the API. |  No  
`WbMaximumClicks` |  StrategyMaximumClicksAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CLICKS  
`WbMaximumConversionRate` |  StrategyMaximumConversionRateAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CONVERSION_RATE  
`AverageCpc` |  StrategyAverageCpcAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC  
`AverageCpa` |  StrategyAverageCpaAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA  
`AverageCpaMultipleGoals` |  StrategyAverageCpaMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_MULTIPLE_GOALS  
`AverageCrr` |  StrategyAverageCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CRR  
`PayForConversionCrr` |  StrategyPayForConversionCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_CRR  
`PayForConversion` |  StrategyPayForConversionAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
`PayForConversionMultipleGoals` |  StrategyPayForConversionMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
**UnifiedCampaignNetworkStrategyAdd structure** |  |  |   
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

For information about the compatibility of strategies in search results and ad networks, see the section  |  Yes  
`PlacementTypes` |  UnifiedCampaignNetworkStrategyPlacementTypes |  Placements in ad networks. |  No  
`WbMaximumClicks` |  StrategyMaximumClicksAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CLICKS  
`WbMaximumConversionRate` |  StrategyMaximumConversionRateAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to WB_MAXIMUM_CONVERSION_RATE  
`AverageCpc` |  StrategyAverageCpcAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC  
`AverageCpa` |  StrategyAverageCpaAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA  
`AverageCpaMultipleGoals` |  StrategyAverageCpaMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_MULTIPLE_GOALS  
`AverageCrr` |  StrategyAverageCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CRR  
`PayForConversion` |  StrategyPayForConversionAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
`PayForConversionMultipleGoals` |  StrategyPayForConversionMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION  
`PayForConversionCrr` |  StrategyPayForConversionCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_CRR  
**UnifiedCampaignNetworkStrategyPlacementTypes** |  |  |   
`Network` |  YesNoEnum |  Ad networks. |  No  
`Maps` |  YesNoEnum |  Yandex Maps. |  When the `BiddingStrategySearchPlacementTypesMaps` parameter contains a value that isn't Null.  
**StrategyMaximumClicksAdd structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**UnifiedCampaignSearchStrategyPlacementTypes structure** |  |  |   
`SearchResults` |  YesNoEnum |  Search results. |  No  
`ProductGallery` |  YesNoEnum |  Product gallery. |  No  
`DynamicPlaces` |  YesNoEnum |  Dynamic placements in search results. |  No  
`Maps` |  YesNoEnum |  Yandex Maps. |  When the `BiddingStrategyNetworkPlacementTypesMaps` parameter contains a value that isn't Null.  
`SearchOrganizationList` |  YesNoEnum |  List of organizations in search results. |  No  
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
[add: TextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-text-campaign)
Next
[add: SmartCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-smart-campaign)
