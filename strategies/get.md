---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/strategies/get
crawled_at: 2025-09-17T16:01:45.998486
---

Request
# get
  * [Request](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/get#output)


Gets information about a portfolio strategy.
##  [](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/get#input)Request
Request structure in JSON format:
```

      "params" : { /* required */
        "Page" : {
            "Limit" : (long),
            "Offset" : (long)
        },
        "SelectionCriteria" : { /* required */
            "Ids" : [ (long) ],
            "Types" : [ ("AVERAGE_CPC"|"AVERAGE_CPA"|"PAY_FOR_CONVERSION"|"WB_MAXIMUM_CONVERSION_RATE"|"WB_MAXIMUM_CLICKS"|"AVERAGE_CRR"|"PAY_FOR_CONVERSION_CRR"|"AVERAGE_CPC_PER_CAMPAIGN"|"AVERAGE_CPC_PER_FILTER"|"AVERAGE_CPA_PER_CAMPAIGN"|"AVERAGE_CPA_PER_FILTER"|"PAY_FOR_CONVERSION_PER_CAMPAIGN"|"PAY_FOR_CONVERSION_PER_FILTER"|"UNKNOWN") ],
            "IsArchived" : ("YES"|"NO")
        },
        "FieldNames" : [ ("Id"|"AttributionModel"|"CounterIds"|"PriorityGoals"|"Type"|"Name"|"StatusArchived") ] /* required */,
        "StrategyMaximumClicksFieldNames" : [ ("WeeklySpendLimit"|"BidCeiling"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyMaximumConversionRateFieldNames" : [ ("WeeklySpendLimit"|"BidCeiling"|"GoalId"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyAverageCpcFieldNames" : [ ("AverageCpc"|"WeeklySpendLimit"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyAverageCpaFieldNames" : [ ("AverageCpa"|"GoalId"|"WeeklySpendLimit"|"BidCeiling"|"ExplorationBudget"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyAverageCpaMultipleGoalsFieldNames" : [ ("WeeklySpendLimit"|"BidCeiling"|"ExplorationBudget"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyPayForConversionFieldNames" : [ ("Cpa"|"GoalId"|"WeeklySpendLimit"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyPayForConversionMultipleGoalsFieldNames" : [ ("GoalId"|"WeeklySpendLimit"|"CustomPeriodBudget") ],
        "StrategyAverageCpaPerCampaignFieldNames" : [ ("AverageCpa"|"GoalId"|"WeeklySpendLimit"|"BidCeiling"|"ExplorationBudget"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyPayForConversionPerCampaignFieldNames" : [ ("Cpa"|"GoalId"|"WeeklySpendLimit"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyPayForConversionPerFilterFieldNames" : [ ("Cpa"|"GoalId"|"WeeklySpendLimit"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyAverageCpaPerFilterFieldNames" : [ ("FilterAverageCpa"|"GoalId"|"WeeklySpendLimit"|"BidCeiling"|"ExplorationBudget"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyAverageCpcPerCampaignFieldNames" : [ ("AverageCpc"|"WeeklySpendLimit"|"BidCeiling"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyAverageCpcPerFilterFieldNames" : [ ("FilterAverageCpc"|"WeeklySpendLimit"|"BidCeiling"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyAverageCrrFieldNames" : [ ("Crr"|"GoalId"|"WeeklySpendLimit"|"ExplorationBudget"|"CustomPeriodBudget"|"BudgetType") ],
        "StrategyPayForConversionCrrFieldNames" : [ ("Crr"|"GoalId"|"WeeklySpendLimit"|"CustomPeriodBudget"|"BudgetType") ]
    }

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)** |  |  |   
`Page` |  |  Structure that defines the page for  |  No  
`SelectionCriteria` |  SelectionCriteria |  Criteria for selecting portfolio strategies. To get all of an advertiser's portfolio strategies, leave `SelectionCriteria` empty. |  No  
`FieldNames` |  array of CampaignFieldEnum |  Names of parameters to get that are common to all portfolio strategies. |  Yes  
`StrategyMaximumClicksFieldNames` |  array for StrategyMaximumClicksFieldNames |  Names of parameters for a WB_MAXIMUM_CLICKS strategy. |  No  
`StrategyMaximumConversionRateFieldNames` |  array for StrategyMaximumConversionRateFieldNames |  Names of parameters for a WB_MAXIMUM_CONVERSION_RATE strategy. |  No  
`StrategyAverageCpcFieldNames` |  array for StrategyAverageCpcFieldNames |  Names of parameters for an AVERAGE_CPC strategy. |  No  
`StrategyAverageCpaFieldNames` |  array for StrategyAverageCpaFieldNames |  Names of parameters for an AVERAGE_CPA strategy. |  No  
`StrategyAverageCpaMultipleGoalsFieldNames` |  array of StrategyAverageCpaMultipleGoalsFieldNames |  Names of parameters for an "AVERAGE_CPA_MULTIPLE_GOALS" strategy. |  No  
`StrategyPayForConversionFieldNames` |  array for StrategyPayForConversionFieldNames |  Names of parameters for a PAY_FOR_CONVERSION strategy. |  No  
`StrategyPayForConversionMultipleGoalsFieldNames` |  array of StrategyPayForConversionMultipleGoalsFieldNames |  Names of parameters for a "PAY_FOR_CONVERSION_MULTIPLE_GOALS" strategy. |  No  
`StrategyAverageCpaPerCampaignFieldNames` |  array for StrategyAverageCpaPerCampaignFieldNames |  Names of parameters for an AVERAGE_CPA_PER_CAMPAIGN strategy. |  No  
`StrategyPayForConversionPerCampaignFieldNames` |  array for StrategyPayForConversionPerCampaignFieldNames |  Names of parameters for a PAY_FOR_CONVERSION_PER_CAMPAIGN strategy. |  No  
`StrategyPayForConversionPerFilterFieldNames` |  array for StrategyPayForConversionPerFilterFieldNames |  Names of parameters for a PAY_FOR_CONVERSION_PER_FILTER strategy. |  No  
`StrategyAverageCpaPerFilterFieldNames` |  array for StrategyAverageCpaPerFilterFieldNames |  Names of parameters for an AVERAGE_CPA_PER_FILTER strategy. |  No  
`StrategyAverageCpcPerCampaignFieldNames` |  array for StrategyAverageCpcPerCampaignFieldNames |  Names of parameters for an AVERAGE_CPC_PER_CAMPAIGN strategy. |  No  
`StrategyAverageCpcPerFilterFieldNames` |  array for StrategyAverageCpcPerFilterFieldNames |  Names of parameters for an AVERAGE_CPC_PER_FILTER strategy. |  No  
`StrategyAverageCrrFieldNames` |  array for StrategyAverageCrrFieldNames |  Names of parameters for an AVERAGE_CRR strategy. |  No  
`StrategyPayForConversionCrrFieldNames` |  array for StrategyPayForConversionCrrFieldNames |  Names of parameters for a PAY_FOR_CONVERSION_CRR strategy. |  No  
**SelectionCriteria structure** |  |  |   
`Ids` |  array of long |  Selects strategies with the specified IDs. Maximum of 1000 items in the array. |  No  
`Types` |  array for StrategyTypeEnum |  Selects strategies with the specified types. See  |  No  
`IsArchived` |  YesNoEnum |  Selects archived or non-archived strategies. |  No  
##  [](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/get#output)Response
Response structure in JSON format:
```

    "params" : { /* required */
        "Strategies" : [{ /* required */
            "Id" : (long),
            "AttributionModel" : ("LC"|"LSC"|"FC"|"LYDC"|"LSCCD"|"FCCD"|"LYDCCD"),
            "Type" : (string),
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
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
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
                  "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
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
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
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
                  "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
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
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
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
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
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
                  "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
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
                  "IsMinimumExplorationBudgetCustom" : ("YES"|"NO") /* required */
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
                "BudgetType": ("WEEKLY_BUDGET" | "CUSTOM_PERIOD_BUDGET") /* nillable */
            }
        } ]
    }


```

**Parameter** |  **Type** |  **Description** |   
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)** |  |  |   
Strategies |  array of StrategiesGetItem |  Portfolio strategy |   
**StrategiesGetItem structure** |  |  |   
`Id` |  long |  Portfolio strategy ID. |   
`AttributionModel` |  AttributionModelEnum |  The attribution model used for optimizing conversions (see  Possible values:
  * FC — First click.
  * LC — Last click.
  * LSC — Last significant (non-direct) click.
  * LYDC — Last click from Yandex Direct.
  * LSCCD — Last significant (non-direct) cross-device click.
  * FCCD — First cross-device click.
  * LYDCCD — Last Yandex Direct cross-device click.

The default value is LYDC. |   
`Type` |  long |  Strategy type. See  |   
`Name` |  String |  Portfolio strategy name. |   
`CounterIds` |  ArrayOfInteger |  The IDs of Yandex Metrica tags installed on the advertiser's website (see  |   
`PriorityGoals` |  PriorityGoalsArray |  Priority goals for automatic bid adjustments. If the array is omitted, automatic bid adjustments are used for obtaining the maximum number of engaged sessions (see  You can't add more than 30 priority goals. |   
`WbMaximumClicks` |  StrategyMaximumClicksGet |  Parameters of the  |   
`WbMaximumConversionRate` |  StrategyMaximumConversionRateGet |  Parameters of the  |   
`AverageCpc` |  StrategyAverageCpcGet |  Parameters of the  |   
`AverageCpa` |  StrategyAverageCpaGet |  Parameters of the  |   
`AverageCrr` |  StrategyAverageCrrGet |  Parameters of the strategy  |   
`PayForConversionCrr` |  StrategyPayForConversionCrrGet |  Parameters of the strategy  |   
`PayForConversion` |  StrategyPayForConversionGet |  Parameters of the  |   
`AverageCpaPerCampaign` |  StrategyAverageCpaPerCampaignGet |  Parameters of the  |   
`PayForConversionPerCampaign` |  StrategyPayForConversionPerCampaignGet |  Parameters of the  |   
`PayForConversionPerFilter` |  StrategyPayForConversionPerFilterGet |  Parameters of the  |   
`AverageCpaPerFilter` |  StrategyAverageCpaPerFilterGet |  Parameters of the  |   
`AverageCpcPerCampaign` |  StrategyAverageCpcPerCampaignGet |  Parameters of the  |   
`AverageCpcPerFilter` |  StrategyAverageCpcPerFilterGet |  Parameters of the  |   
**PriorityGoalsArray structure** |  |  |   
`Items` |  array of PriorityGoalsItem |  A set of priority goals and corresponding conversion values. |   
**PriorityGoalsItem structure** |  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal to prioritize when automatically adjusting bids. For more information about goals, see  To get the list of goals, use the  A value of 12 corresponds to the "Engaged sessions" goal. |   
`Value` |  long |  The conversion value is a monetary estimation of the advertiser's profit when the goal is completed, in the advertiser's currency, multiplied by 1,000,000. The higher the conversion value, the higher the priority to achieve conversions for this goal. |   
`IsMetrikaSourceOfValue` |  YesNoEnum |  Priority goal value source: Yandex Metrica goal. The `YES` value is only used for strategies with cost revenue ratio. |   
**StrategyMaximumClicksGet structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
**StrategyMaximumConversionRateGet structure** |  |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  The value 13 indicates priority goals. Allowed if the PriorityGoals array specifies at least one goal that is different from engaged sessions. To get the list of goals, use the  |   
**StrategyAverageCpcGet structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyAverageCpaGet structure** |  |  |   
`AverageCpa` |  long |  The average goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  |   
**StrategyAverageCrrGet structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  |   
**StrategyPayForConversionGet structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyPayForConversionCrrGet structure** |  |  |   
`Crr` |  int |  Average cost revenue ratio. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyAverageCpaPerCampaignGet structure** |  |  |   
`AverageCpa` |  long |  The average goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  |   
**StrategyPayForConversionPerCampaignGet structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyPayForConversionPerFilterGet structure** |  |  |   
`Cpa` |  long |  The goal cost in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum CPA values are listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency must be at least the value of the `Cpa` parameter multiplied by 20. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
**StrategyAverageCpaPerFilterGet structure** |  |  |   
`FilterAverageCpa` |  long |  The average default goal cost per filter in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
|  |  |   
`GoalId` |  long |  ID of the Yandex Metrica goal. For more information about goals, see  To get the list of goals, use the  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
`ExplorationBudget` |  ExplorationBudget |  Minimum budget. Read more in  |   
**StrategyAverageCpcPerCampaignGet structure** |  |  |   
`AverageCpc` |  long |  The average CPC in the advertiser's currency, multiplied by 1,000,000. The minimum value for the average cost is listed by currency in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
**StrategyAverageCpcPerFilterGet structure** |  |  |   
`FilterAverageCpc` |  long |  |   
`WeeklySpendLimit` |  long |  The weekly budget in the advertiser's currency, multiplied by 1,000,000. The minimum weekly budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. |   
`CustomPeriodBudget` |  CustomPeriodBudget |  Budget for a custom period. For more information, see  When creating a campaign, you can't specify both this parameter and `WeeklySpendLimit`. |   
`BudgetType` |  BudgetTypeEnum |  Type of budget:
  * WEEKLY_BUDGET — Weekly budget.
  * CUSTOM_PERIOD_BUDGET — Budget for a custom period.

|   
`BidCeiling` |  long |  The maximum bid in the advertiser's currency, multiplied by 1,000,000. The minimum and maximum bid for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/strategies/en/dictionaries/get) method. Note We don't recommend setting the maximum bid, as this may reduce the effectiveness of the strategy. |   
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
[archive](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/archive)
Next
[unarchive](https://yandex.com/dev/direct/doc/en/strategies/en/strategies/unarchive)
