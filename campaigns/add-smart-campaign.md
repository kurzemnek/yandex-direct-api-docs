---
title: add: SmartCampaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/add-smart-campaign
crawled_at: 2025-09-17T16:02:43.266012
---

add: SmartCampaign parameters
# add: SmartCampaign parameters
Request structure in JSON format:
```
{
  "method": "add",
  "params": {
    "Campaigns": [{  /* CampaignAddItem */
      ...
      "SmartCampaign": { /* SmartCampaignAddItem */
        "BiddingStrategy": { /* SmartCampaignStrategyAdd */
          "Search": { /* SmartCampaignSearchStrategy */
            "BiddingStrategyType": ( "AVERAGE_CPC_PER_CAMPAIGN" | ... | "SERVING_OFF" ), /* required */
            "AverageCpcPerCampaign": { /* StrategyAverageCpcPerCampaignAdd */
              "AverageCpc": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long),
            },
            "AverageCpcPerFilter": { /* StrategyAverageCpcPerFilterAdd */
              "FilterAverageCpc": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long)
            },
            "AverageCpaPerCampaign" : { /* StrategyAverageCpaPerCampaignAdd */
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
            "AverageCpaPerFilter": {  /* StrategyAverageCpaPerFilterAdd */
              "FilterAverageCpa": (long), /* required */
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
            "AverageRoi": { /* StrategyAverageRoiAdd */
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
            "PayForConversionCrr": {  /* StrategyPayForConversionCrrAdd */
              "Crr": (int), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "PayForConversionPerCampaign" : { /* StrategyPayForConversionPerCampaignAdd */
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
            "PayForConversionPerFilter" : { /* StrategyPayForConversionPerFilterAdd */
              "Cpa" : (long) /* required */,
              "GoalId" : (long) /* required */,
              "WeeklySpendLimit" : (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            }
          }, /* required */
          "Network": { /* SmartCampaignNetworkStrategyAdd */
            "BiddingStrategyType": ( "AVERAGE_CPC_PER_CAMPAIGN" | ... | "SERVING_OFF" ), /* required */
            "AverageCpcPerCampaign": { /* StrategyAverageCpcPerCampaignAdd */
              "AverageCpc": (long), /* required */
              "WeeklySpendLimit": (long),
              "BidCeiling": (long)
            },
            "AverageCpcPerFilter": { /* StrategyAverageCpcPerFilterAdd */
              "FilterAverageCpc": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              },
              "BidCeiling": (long)
            },
            "AverageCpaPerCampaign" : { /* StrategyAverageCpaPerCampaignAdd */
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
            "AverageCpaPerFilter": {  /* StrategyAverageCpaPerFilter */
              "FilterAverageCpa": (long), /* required */
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
            "AverageRoi": { /* StrategyAverageRoiAdd */
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
            "PayForConversionCrr": {  /* StrategyPayForConversionCrrAdd */
              "Crr": (int), /* required */
              "GoalId": (long), /* required */
              "WeeklySpendLimit": (long),
              "CustomPeriodBudget": {
                "SpendLimit": (long),
                "StartDate": (string),
                "EndDate": (string),
                "AutoContinue": ("YES" | "NO")
              }
            },
            "PayForConversionPerCampaign" : { /* StrategyPayForConversionPerCampaignAdd */
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
            "PayForConversionPerFilter" : { /* StrategyPayForConversionPerFilterAdd */
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
            "NetworkDefault": {  /* StrategyNetworkDefaultAdd */
            }
          } /* required */
        }, /* required */
        "Settings": [{ /* SmartCampaignSetting */
          "Option": ( "ADD_TO_FAVORITES" | "REQUIRE_SERVICING" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ],
        "CounterId": (long), /* required */
        "PriorityGoals": { /* PriorityGoalsArray */
          "Items": [{ /* PriorityGoalsItem */
            "GoalId": (long), /* required */
            "Value": (long), /* required */
            "IsMetrikaSourceOfValue": ( "YES" | "NO" )
          }, ... ] /* required */
        },
        "TrackingParams" : (string),
        "AttributionModel": ( "FC" | "LC" | "LSC" | "LYDC" | "FCCD" | "LSCCD" | "LYDCCD" | "AUTO" ),
        "PackageBiddingStrategy" : {
          "StrategyId": (long),
          "StrategyFromCampaignId": (long),
          "Platforms" : { /* required */
            "Search" : ( "YES" | "NO" ) /* required */,
            "Network" : ( "YES"| "NO" ) /* required */
          }
        }
      }
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**SmartCampaignAddItem structure** |  |  |   
`BiddingStrategy` |  SmartCampaignStrategyAdd |  Display strategy. |  No if PackageBiddingStrategy is specified  
`Settings` |  array of SmartCampaignSetting |  Array of settings that only accept the values YES or NO. |  No  
`CounterId` |  long |  ID of the Yandex Metrica tag installed on the advertiser's site (see  |  Yes  
`PriorityGoals` |  PriorityGoalsArray |  Priority goals for automatic bid adjustments. If the array is omitted, automatic bid adjustments are used for obtaining the maximum number of engaged sessions (see  You can't add more than 30 priority goals. |  No  
`TrackingParams` |  string |  URL parameters for templates. |  No  
`AttributionModel` |  AttributionModelEnum |  The attribution model used for optimizing conversions (see  Possible values:
  * FC — First click.
  * LC — Last click.
  * LSC — Last significant (non-direct) click.
  * LYDC — Last click from Yandex Direct.

The default value is LYDC. |  No  
`PackageBiddingStrategy` |  SmartCampaignPackageBiddingStrategyAdd |  Links a campaign to the specified strategy. You can't pass the following parameters in this field:
  * `BiddingStrategy`.
  * `PriorityGoals`.
  * `CounterIds`.
  * `AttributionModel`.

To pass these parameters, unlink the campaign from the portfolio strategy: specify a new value for `BiddingStrategy` and reset the `PackageBiddingStrategy: null` parameter value. |  No if BiddingStrategy is specified  
**SmartCampaignSetting structure** |  |  |   
`Option` |  SmartCampaignSettingsEnum |  Setting name:
  * ADD_TO_FAVORITES
  * REQUIRE_SERVICING

|  Yes  
`Value` |  YesNoEnum |  Setting value. |  Yes  
**PackageBiddingStrategyAdd structure** |  |  |   
`StrategyId` |  long |  Portfolio strategy ID. |   
`StrategyFromCampaignId` |  long |  ID of the campaign the portfolio strategy was created from. |  No  
`Platforms` |  SmartCampaignpPlatforms |  Ad placement platform. |  Yes  
**SmartCampaignPlatforms structure** |  |  |   
`Search` |  YesNoEnum |  Search results. |  Yes  
`Network` |  YesNoEnum |  Yandex Advertising Network. |  Yes  
**PriorityGoalsArray structure** |  |  |   
`Items` |  array of PriorityGoalsItem |  A set of priority goals and corresponding conversion values. |  Yes  
**PriorityGoalsItem structure** |  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal to prioritize when automatically adjusting bids. For more information about goals, see  To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. A value of 12 corresponds to the "Engaged sessions" goal. |  Yes  
`Value` |  long |  The conversion value is a monetary estimation of the advertiser's profit when the goal is completed, in the advertiser's currency, multiplied by 1,000,000. The higher the conversion value, the higher the priority to achieve conversions for this goal. |  Yes  
`IsMetrikaSourceOfValue` |  YesNoEnum |  Priority goal value source: Yandex Metrica goal. The `YES` value is only used for strategies with cost revenue ratio. |  If the BiddingStrategyType parameter is set to AVERAGE_CRR or PAY_FOR_CONVERSION_CRR  
**SmartCampaignStrategyAdd structure** |  |  |   
`Search` |  SmartCampaignSearchStrategyAdd |  Display strategy in search results. |  Yes  
`Network` |  SmartCampaignNetworkStrategyAdd |  Display strategy in ad networks. |  Yes  
**SmartCampaignSearchStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  SmartCampaignSearchStrategyTypeEnum |  The type of display strategy in search results:
  * AVERAGE_CPA_PER_CAMPAIGN
  * AVERAGE_CPA_PER_FILTER
  * AVERAGE_CPC_PER_CAMPAIGN
  * AVERAGE_CPC_PER_FILTER
  * AVERAGE_ROI
  * AVERAGE_CRR
  * PAY_FOR_CONVERSION_CRR
  * PAY_FOR_CONVERSION_PER_CAMPAIGN
  * PAY_FOR_CONVERSION_PER_FILTER
  * SERVING_OFF

|  Yes  
`AverageCpaPerCampaign` |  StrategyAverageCpaPerCampaignAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_PER_CAMPAIGN  
`AverageCpaPerFilter` |  StrategyAverageCpaPerFilterAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_PER_FILTER  
`AverageCpcPerCampaign` |  StrategyAverageCpcPerCampaignAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC_PER_CAMPAIGN  
`AverageCpcPerFilter` |  StrategyAverageCpcPerFilterAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC_PER_FILTER  
`AverageRoi` |  StrategyAverageRoiAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_ROI  
`AverageCrr` |  StrategyAverageCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CRR  
`PayForConversionCrr` |  StrategyPayForConversionCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_CRR  
`PayForConversionPerCampaign` |  StrategyPayForConversionPerCampaignAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_PER_CAMPAIGN.  
`PayForConversionPerFilter` |  StrategyPayForConversionPerFilterAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_PER_FILTER  
**SmartCampaignNetworkStrategyAdd structure** |  |  |   
`BiddingStrategyType` |  SmartCampaignNetworkStrategyTypeEnum |  The type of display strategy in ad networks:
  * AVERAGE_CPA_PER_CAMPAIGN
  * AVERAGE_CPA_PER_FILTER
  * AVERAGE_CPC_PER_CAMPAIGN
  * AVERAGE_CPC_PER_FILTER
  * AVERAGE_ROI
  * AVERAGE_CRR
  * PAY_FOR_CONVERSION_CRR
  * NETWORK_DEFAULT
  * PAY_FOR_CONVERSION_PER_CAMPAIGN
  * PAY_FOR_CONVERSION_PER_FILTER
  * SERVING_OFF

|  Yes  
`AverageCpaPerCampaign` |  StrategyAverageCpaPerCampaignAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_PER_CAMPAIGN  
`AverageCpaPerFilter` |  StrategyAverageCpaPerFilterAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPA_PER_FILTER  
`AverageCpcPerCampaign` |  StrategyAverageCpcPerCampaignAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC_PER_CAMPAIGN  
`AverageCpcPerFilter` |  StrategyAverageCpcPerFilterAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CPC_PER_FILTER  
`AverageRoi` |  StrategyAverageRoiAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to AVERAGE_ROI  
`AverageCrr` |  StrategyAverageCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to AVERAGE_CRR  
`PayForConversionCrr` |  StrategyPayForConversionCrrAdd |  Parameters of the strategy  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_CRR  
`PayForConversionPerCampaign` |  StrategyPayForConversionPerCampaignAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_PER_CAMPAIGN.  
`PayForConversionPerFilter` |  StrategyPayForConversionPerFilterAdd |  Parameters of the  |  When the `BiddingStrategyType` parameter is set to PAY_FOR_CONVERSION_PER_FILTER  
`NetworkDefault` |  StrategyNetworkDefaultAdd |  Settings for impressions in ad networks based on the settings for search. Pass an empty structure for this strategy. |  When the `BiddingStrategyType` parameter is set to NETWORK_DEFAULT  
**StrategyAverageCpaPerCampaignAdd structure** |  |  |   
`AverageCpa` |  long |  The average goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCpaPerFilterAdd structure** |  |  |   
`FilterAverageCpa` |  long |  The average default goal cost per filter in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
|  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCpcPerCampaignAdd structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyAverageCpcPerFilterAdd structure** |  |  |   
`FilterAverageCpc` |  long |  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyAverageRoiAdd structure** |  |  |   
`ReserveReturn` |  int |  The maximum percentage of saved funds that can be returned to advertising (spent) if the forecasted return on investment exceeds the value of the `RoiCoef` parameter. A value from 0 to 100 as a multiple of ten: 0, 10, 20... 100. |  Yes  
`RoiCoef` |  long |  The desired average return on investment per week. The value represents the ratio between sales profits and ad costs, multiplied by 1,000,000. The value must be an integer. If the value is not a multiple of 10,000, the last 4 digits are reset to zero (which is the same as discarding extra decimal digits). |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. Подробнее о целях см. раздел  The value 13 indicates priority goals. Allowed if the array specifies at least one goal that is different from engaged sessions. To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`Profitability` |  long |  The percentage of revenue that is the cost value of products or services. The value is a percentage multiplied by 1,000,000. The value must be an integer between 0 and 100,000,000 (which corresponds to 100%). If the value is not a multiple of 10,000, the last 4 digits are reset to zero (which is the same as discarding extra decimal digits). |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCrrAdd structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  If the field is omitted, a default value is set for the strategy (it's calculated based on the strategy settings). To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyPayForConversionCrrAdd structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyPayForConversionPerCampaignAdd structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyPayForConversionPerFilterAdd structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the [GetStatGoals](https://yandex.com/dev/direct/doc/dg-v4/live/GetStatGoals.md) method in version 4 or Live 4 of the API. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method. |  No  
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
[add: UnifiedCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-unified-campaign)
Next
[add: DynamicTextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/add-dynamic-text-campaign)
