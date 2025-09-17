---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/strategies/update
crawled_at: 2025-09-17T15:59:44.444040
---

Request
# update
  * [Request](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#output)


Updates a portfolio strategy.
##  [](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#input)Request
Request structure in JSON format:
```

    "params" : { /* required */
        "Strategies" : [{ /* required */
            "Id": (long), /* required */
            "AttributionModel" : ("LC"|"LSC"|"FC"|"LYDC"|"LSCCD"|"FCCD"|"LYDCCD"),
            "Name" : (string) /* required */,
            "CounterIds" : {
                "Items" : [ (long) ] /* required */
            },
            "PriorityGoals" : {
                "Items" : [{ /* required */
                    "GoalId" : (long) /* required */,
                    "Value" : (long) /* required */,
                    "IsMetrikaSourceOfValue" : ("YES"|"NO")
                } ]
            },
            "WbMaximumClicks" : {
                "WeeklySpendLimit" : (long) /* required */,
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "BidCeiling" : (long)
            },
            "WbMaximumConversionRate" : {
                "WeeklySpendLimit" : (long) /* required */,
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "BidCeiling" : (long),
                "GoalId" : (long) /* required */
            },
            "AverageCpc" : {
                "AverageCpc" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
            },
            "AverageCpa" : {
                "AverageCpa" : (long) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "BidCeiling" : (long),
                "ExplorationBudget" : { /* nillable */
                  "MinimumExplorationBudget" : (long) /* required */,
                  "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
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
                  "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
                }
            },
            "PayForConversion" : {
                "Cpa" : (long) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
            },
            "PayForConversionMultipleGoals" : {,
                "WeeklySpendLimit" : (long),
                "CustomPeriodBudget": {
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
            },
            "AverageCpaPerCampaign" : {
                "AverageCpa" : (long) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "BidCeiling" : (long),
                "ExplorationBudget" : { /* nillable */
                  "MinimumExplorationBudget" : (long) /* required */,
                  "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
                }
            },
            "PayForConversionPerCampaign" : {
                "Cpa" : (long) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
            },
            "PayForConversionPerFilter" : {
                "Cpa" : (long) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
            },
            "AverageCpaPerFilter" : {
                "FilterAverageCpa" : (long) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "BidCeiling" : (long),
                "ExplorationBudget" : { /* nillable */
                  "MinimumExplorationBudget" : (long) /* required */,
                  "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
                }
            },
            "AverageCpcPerCampaign" : {
                "AverageCpc" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "BidCeiling" : (long)
            },
            "AverageCpcPerFilter" : {
                "FilterAverageCpc" : (long),
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "BidCeiling" : (long)
            },
            "AverageCrr" : {
                "Crr" : (integer) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
                "ExplorationBudget" : { /* nillable */
                  "MinimumExplorationBudget" : (long) /* required */,
                  "IsMinimumExplorationBudgetCustom" : ("YES") /* required */
                }
            },
            "PayForConversionCrr" : {
                "Crr" : (integer) /* required */,
                "GoalId" : (long) /* required */,
                "WeeklySpendLimit" : (long), /* nillable */
                "CustomPeriodBudget": { /* nillable */
                  "SpendLimit": (long),
                  "StartDate": (string),
                  "EndDate": (string),
                  "AutoContinue": ("YES" | "NO")
                },
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */,
            }
        } ]
    }


```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)** |  |  |   
Strategies |  array of StrategiesUpdateItem |  Portfolio strategy |  Yes  
**StrategiesUpdateItem structure** |  |  |   
`Id` |  long |  Portfolio strategy ID. |  Yes  
`AttributionModel` |  AttributionModelEnum |  The attribution model used for optimizing conversions (see  Possible values:
  * FC — First click.
  * LC — Last click.
  * LSC — Last significant (non-direct) click.
  * LYDC — Last click from Yandex Direct.
  * LSCCD — Last significant (non-direct) cross-device click.
  * FCCD — First cross-device click.
  * LYDCCD — Last Yandex Direct cross-device click.

The default value is LYDC. |  No  
`Name` |  String |  Portfolio strategy name. |  Yes  
`CounterIds` |  ArrayOfInteger |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |  No  
`PriorityGoals` |  PriorityGoalsArray |  Priority goals for automatic bid adjustments. If the array is omitted, automatic bid adjustments are used for obtaining the maximum number of engaged sessions (see  You can't add more than 30 priority goals. |  When passing the `AverageCpaMultipleGoals` or `PayForConversionMultipleGoals` parameter.  
`WbMaximumClicks` |  StrategyMaximumClicksUpdate |  Parameters of the  |  No  
`WbMaximumConversionRate` |  StrategyMaximumConversionRateUpdate |  Parameters of the  |  No  
`AverageCpc` |  StrategyAverageCpcUpdate |  Parameters of the  |  No  
`AverageCpa` |  StrategyAverageCpaUpdate |  Parameters of the  |  No  
`AverageCpaMultipleGoals` |  StrategyAverageCpaMultipleGoalsAdd |  Parameters of the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  No  
`AverageCrr` |  StrategyAverageCrrUpdate |  Parameters of the strategy  |  No  
`PayForConversionCrr` |  StrategyPayForConversionCrrUpdate |  Parameters of the strategy  |  No  
`PayForConversion` |  StrategyPayForConversionUpdate |  Parameters of the  |  No  
`PayForConversionMultipleGoals` |  StrategyPayForConversionMultipleGoalsAdd |  Parameters of the   
Be sure to simultaneously pass the `PriorityGoals` array with at least two priority goals, and specify the target CPA for each goal as the `Value`. |  No  
`AverageCpaPerCampaign` |  StrategyAverageCpaPerCampaignUpdate |  Parameters of the  |  No  
`PayForConversionPerCampaign` |  StrategyPayForConversionPerCampaignUpdate |  Parameters of the  |  No  
`PayForConversionPerFilter` |  StrategyPayForConversionPerFilterUpdate |  Parameters of the  |  No  
`AverageCpaPerFilter` |  StrategyAverageCpaPerFilterUpdate |  Parameters of the  |  No  
`AverageCpcPerCampaign` |  StrategyAverageCpcPerCampaignUpdate |  Parameters of the  |  No  
`AverageCpcPerFilter` |  StrategyAverageCpcPerFilterUpdate |  Parameters of the  |  No  
**PriorityGoalsArray structure** |  |  |   
`Items` |  array of PriorityGoalsItem |  A set of priority goals and corresponding conversion values. |  Yes  
**PriorityGoalsItem structure** |  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal to prioritize when automatically adjusting bids. For more information about goals, see  To get the list of goals, use the  A value of 12 corresponds to the "Engaged sessions" goal. |  Yes  
`Value` |  long |  The conversion value is a monetary estimation of the advertiser's profit when the goal is completed, in the advertiser's currency, multiplied by 1,000,000. The higher the conversion value, the higher the priority to achieve conversions for this goal. |  Yes  
`IsMetrikaSourceOfValue` |  YesNoEnum |  Priority goal value source: Yandex Metrica goal. The `YES` value is only used for strategies with cost revenue ratio. |  If the BiddingStrategyType parameter is set to AVERAGE_CRR or PAY_FOR_CONVERSION_CRR  
**StrategyMaximumClicksUpdate structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyMaximumConversionRateUpdate structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  The value 13 indicates priority goals. Allowed if the PriorityGoals array specifies at least one goal that is different from engaged sessions. To get the list of goals, use the  |  Yes  
**StrategyAverageCpcUpdate structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
**StrategyAverageCpaUpdate structure** |  |  |   
`AverageCpa` |  long |  The average goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  [ExplorationBudget](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#ExplorationBudget) |  Minimum budget. Read more in  If the field is not set, the minimum budget won't change. To set the default value, pass `ExplorationBudget=NULL`. To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCpaMultipleGoalsUpdate structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  [ExplorationBudget](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#ExplorationBudget) |  Minimum budget. Read more in  If the field is not set, the minimum budget won't change. To set the default value, pass `ExplorationBudget=NULL`. To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCrrUpdate structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`ExplorationBudget` |  [ExplorationBudget](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#ExplorationBudget) |  Minimum budget. Read more in  If the field is not set, the minimum budget won't change. To set the default value, pass `ExplorationBudget=NULL`. To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyPayForConversionUpdate structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
**StrategyPayForConversionMultipleGoalsUpdate structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
**StrategyAverageCpaPerCampaignUpdate structure** |  |  |   
`AverageCpa` |  long |  The average goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  [ExplorationBudget](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#ExplorationBudget) |  Minimum budget. Read more in  If the field is not set, the minimum budget won't change. To set the default value, pass `ExplorationBudget=NULL`. To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyPayForConversionPerCampaignUpdate structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
**StrategyPayForConversionPerFilterUpdate structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
**StrategyAverageCpaPerFilterUpdate structure** |  |  |   
`FilterAverageCpa` |  long |  The average default goal cost per filter in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
|  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
`ExplorationBudget` |  [ExplorationBudget](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#ExplorationBudget) |  Minimum budget. Read more in  If the field is not set, the minimum budget won't change. To set the default value, pass `ExplorationBudget=NULL`. To set a custom minimum budget, use the `MinimumExplorationBudget` parameter and set `IsMinimumExplorationBudgetCustom="YES"`. If `IsMinimumExplorationBudgetCustom` is `NO`, the operation raises an error. |  No  
**StrategyAverageCpcPerCampaignUpdate structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyAverageCpcPerFilterUpdate structure** |  |  |   
`FilterAverageCpc` |  long |  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |  No  
**StrategyPayForConversionCrrUpdate structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |  Yes  
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |  Yes  
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |  No  
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |  No  
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

If the budget type is changed while editing the campaign, the original type must be passed with a NULL value. For example, if you change the budget type from weekly to custom period, make sure to pass NULL in the "WeeklySpendLimit" field. |  No  
**ExplorationBudget structure** |  |  |   
`MinimumExplorationBudget` |  long |  Minimum budget value. Acceptable value: between 0 and the weekly budget (if set). |  Yes, if the request includes the `ExplorationBudget` structure.  
`IsMinimumExplorationBudgetCustom` |  YesNoEnum |  A flag indicating a custom minimum budget. |  Yes, if the request includes the `ExplorationBudget` structure.  
**CustomPeriodBudget structure** |  |  |   
`SpendLimit` |  long |  Budget size for a custom period. |  Yes  
`StartDate` |  string |  Start of the budget period. |  Yes  
`EndDate` |  string |  End of the budget period. |  Yes  
`AutoContinue` |  YesNoEnum |  Flag to autocontinue the budget period. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/update#output)Response
Response structure in JSON format:
```
{
  "result" : { /* required */
        "UpdateResults" : [{
            "Warnings" : [{
                "Code" : (integer) /* required */,
                "Message" : (string) /* required */,
                "Details" : (string)
            } ],
            "Errors" : [{
                "Code" : (integer) /* required */,
                "Message" : (string) /* required */,
                "Details" : (string)
            } ],
            "Id" : (long)
        } ]
    }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / UpdateResponse structure (for SOAP)** |  |   
`UpdateResults` |  array of ActionResult |  What happens when a portfolio strategy is added.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the portfolio strategy that was created. Returned if there aren't any errors. See the section   
`Warnings` |  array of  |  Warnings that occurred during the operation.  
`Errors` |  array of  |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[unarchive](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/unarchive)
Next
[TurboPages: getting parameters of Turbo pages](https://yandex.com/dev/direct/doc/en/strategies/en/turbopages/turbopages)
