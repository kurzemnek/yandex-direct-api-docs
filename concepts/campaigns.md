---
title: Campaign parameters | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/campaigns
crawled_at: 2025-09-17T15:56:40.980881
---

Campaign parameters
# Campaign parameters
**Parameter name in version Live 4** |  **Parameter name in version 5** |  **Service in version 5**  
---|---|---  
`AdditionalMetrikaCounters` |  `CounterIds` nested in `TextCampaign` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`AddRelevantPhrases` |  Controlled by the presence of the `RelevantKeywords` parameter nested in `TextCampaign`: If this parameter is set, displays are enabled for additional relevant keywords; if it is omitted, they are disabled |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`AgencyName` |  `Agency` nested in `RepresentedBy` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`AutoOptimization` |  No longer relevant |  —  
`BonusDiscount` |  `BalanceBonus`, nested in `CampaignFunds`, nested in `Funds` (if the shared account isn't enabled) |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`CampaignCurrency` |  `Currency` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`CampaignID` |  `Id` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ClickTrackingEnabled` |  `Option` with the value ADD_METRICA_TAG, nested in `Settings`, nested in `TextCampaign` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ConsiderTimeTarget` |  `Option` with the value EXCLUDE_PAUSED_COMPETING_ADS nested in `Settings`, nested in `TextCampaign` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ContextStrategy` |  `Network`, nested in `BiddingStrategy` For the equivalence of nested parameters, see the section [Strategy parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/campaigns#Strategy). |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`Currency` |  Not supported. Bids and costs are always shown in the advertiser's currency. |  —  
`Clicks` |  `Clicks` nested in `Statistics` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`DayBudget` |  `DailyBudget`. For the equivalence of nested parameters, see the section [Daily budget parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/campaigns#DayBudget). |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`DayBudgetEnabled` |  No longer relevant |  —  
`DisabledDomains` |  `ExcludedSites` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`DisabledIps` |  `BlockedIps` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`EmailNotification` |  `EmailSettings` nested in `Notification` For the equivalence of nested parameters, see the section [Email notification parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/campaigns#EmailNotification). |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`EnableRelatedKeywords` |  No longer relevant |  —  
`ExtendedAdTitleEnabled` |  `Option` with the value ENABLE_EXTENDED_AD_TITLE, nested in `Settings`, nested in `TextCampaign` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`FIO` |  `ClientInfo` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`IsActive`, `Status`, `StatusShow`, `StatusArchive`, `StatusActivating`, `StatusModerate` |  `Status`, `StatusPayment`, `StatusClarifications` and `State` (for more information, see [Campaign](https://yandex.com/dev/direct/doc/dg/objects/campaign.html)) |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`Login` |  HTTP header of the `Client-Login request` |  —  
`MaintainNetworkCPC` |  `Option` with the value MAINTAIN_NETWORK_CPC, nested in `Settings`, nested in `TextCampaign` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ManagerName` |  `Manager` nested in `RepresentedBy` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`MinusKeywords` |  `NegativeKeywords` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`MobileBidAdjustment` |  `BidModifier` nested in `MobileAdjustment` |  [BidModifiers](https://yandex.com/dev/direct/doc/ref-v5/bidmodifiers/bidmodifiers.html)  
`Name` |  `Name` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`Rest` |  `Balance`, nested in `CampaignFunds`, nested in `Funds` (if the shared account isn't enabled) |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SmsNotification` |  `SmsSettings` nested in `Notification`. For the equivalence of nested parameters, see the section [SMS notification parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/campaigns#SmsNotification). |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SourceCampaignID` |  `SourceId` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`StartDate` |  `StartDate` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`Strategy` |  `Search` nested in `BiddingStrategy`, nested in `TextCampaign` For the equivalence of nested parameters, see the section [Strategy parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/campaigns#Strategy). |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`TimeTarget` |  `TimeTargeting` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`RelevantPhrasesBudgetLimit` |  `BudgetPercent`, nested in `RelevantKeywords`, nested in `TextCampaign` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`Shows` |  `Impressions` nested in `Statistics` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`StatusBehavior` |  No longer relevant |  —  
`StatusContextStop` |  No longer relevant |  —  
`StatusMetricaControl` |  `Option` with the value ENABLE_SITE_MONITORING, nested in `Settings` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`StatusOpenStat` |  `Option` with the value ADD_OPENSTAT_TAG, nested in `Settings` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`Sum` |  `Sum`, nested in ` CampaignFunds`, nested in `Funds` (if the shared account isn't enabled)  
`Spend`, nested in ` SharedAccountFunds`, nested in `Funds` (if the shared account isn't enabled) |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SumAvailableForTransfer` |  `SumAvailableForTransfer`, nested in `CampaignFunds`, nested in `Funds` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
**Strategy parameters (Strategy and ContextStrategy in version 4)** |  |   
`AverageCPA` |  `AverageCpa` nested in `AverageCpa` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`AveragePrice` |  `AverageCpc` nested in `AverageCpc` or `WeeklyClickPackage` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ContextLimit` |  Controlled by the presence of the `LimitPercent` parameter nested in `NetworkDefault`: If this parameter is set, the budget is limited; if it is omitted, the budget is unlimited |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ContextLimitSum` |  `LimitPercent` nested in `NetworkDefault` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ContextPricePercent` |  `BidPercent` nested in `NetworkDefault` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`GoalID` |  `GoalId` nested in `WbMaximumConversionRate`, `AverageCpa`, or `RoiOptimization` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ClicksPerWeek` |  `ClicksPerWeek` nested in `WeeklyClickPackage` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`MaxPrice` |  `BidCeiling` nested in `WbMaximumClicks`, `WbMaximumConversionRate`, `AverageCpa`, `AverageRoi`, `WeeklyClickPackage` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`Profitability` |  `Profitability` nested in `AverageRoi` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ReserveReturn` |  `ReserveReturn` nested in `AverageRoi` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ROICoef` |  `RoiCoef` nested in `AverageRoi` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`StrategyName` |  `BiddingStrategyType` nested in `Search` or `Network` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`WeeklySumLimit` |  `WeeklySpendLimit` nested in `WbMaximumClicks`, `WbMaximumConversionRate`, `AverageCpc`, `AverageCpa`, `AverageRoi` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
**SMS notification parameters (SmsNotification in version 4)** |  |   
`MetricaSms` |  The MONITORING value in the `Events parameter` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`ModerateResultSms` |  The MODERATION value in the `Events parameter` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`MoneyInSms` |  The MONEY_IN value in the `Events parameter` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`MoneyOutSms` |  The MONEY_OUT value in the `Events parameter` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SmsTimeFrom` |  `TimeFrom` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SmsTimeTo` |  `TimeTo` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
**Email notification parameters (EmailNotification in version 4)** |  |   
`Email` |  `Email` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`MoneyWarningValue` |  `WarningBalance` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SendAccNews` |  `SendAccountNews` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SendWarn` |  `SendWarnings` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`WarnPlaceInterval` |  `CheckPositionInterval` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
**Time targeting parameters (TimeTarget in version 4)** |  |   
`ShowOnHolidays` |  `SuspendOnHolidays` nested in `HolidaysSchedule` Note The Yes value for the `ShowOnHolidays` parameter corresponds to the NO value for the `SuspendOnHolidays` parameter, and vice versa. |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`HolidayShowFrom` |  `StartHour` nested in `HolidaysSchedule` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`HolidayShowTo` |  `EndHour` nested in `HolidaysSchedule` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`DaysHours` and nested `Hours`, `Days`, `BidCoefs` |  `Schedule` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`TimeZone` |  `TimeZone` (higher-level parameter) |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`WorkingHolidays` |  `ConsiderWorkingWeekends` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
**Daily budget parameters (DayBudget in version 4)** |  |   
`Amount` |  `Amount` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
`SpendMode` |  `Mode` |  [Campaigns](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html)  
Copied
### Was the article helpful?
YesNo
Previous
[Method equivalents](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/methods)
Next
[Parameters of groups and ads](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/banners)
