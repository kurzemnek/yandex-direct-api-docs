---
title: Allowed fields | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/fields-list
crawled_at: 2025-09-17T15:44:05.452440
---

Allowed fields
# Allowed fields
Fields are specified in the following report parameters:
  * FieldNames: Fields to output in the report (columns).
  * Field in the Filter structure: Fields to use for filtering data in the report.
  * Field in the OrderBy structure: Fields to use for sorting rows in the report.


These parameters allow different sets of fields (see the table below). For example, you can add the CampaignName field to the report as a column, but you can't use it to filter data. Conversely, the Keyword field can only be used to filter data and doesn't appear in the report.
The report type also affects which fields are allowed and how they are applied (see the table below):
  * filter: The field is only used for filtering data, and can't be shown in a report.
  * segment — The field is used for grouping data in the report.
  * metric — The field contains a numeric value based on filters and data groupings.
  * attribute: The field contains a fixed value for the specified segments. Adding this field to the report doesn't create a new grouping.


For example, the CampaignId field for the CUSTOM_REPORT type is a segment: if you add it to the report, data is grouped by campaigns. However, for the ADGROUP_PERFORMANCE_REPORT, CampaignId is an attribute: the data is already grouped by AdGroupId, and the campaign ID is a fixed value for each group.
A dash "–" means that this field can't be used in the parameter or report type.
For field descriptions, see the [Report content](https://yandex.com/dev/direct/doc/en/en/report-format) page.
|  **Parameters** |  **Report types**  
---|---|---  
**Field name** |  **FieldNames** |  **Filter.Field** |  **OrderBy.Field** |  **ACCOUNT_PERFORMANCE_REPORT** |  **AD_PERFORMANCE_REPORT** |  **ADGROUP_PERFORMANCE_REPORT** |  **CAMPAIGN_PERFORMANCE_REPORT** |  **CRITERIA_PERFORMANCE_REPORT** |  **CUSTOM_REPORT** |  **REACH_AND_FREQUENCY_PERFORMANCE_REPORT** |  **SEARCH_QUERY_PERFORMANCE_REPORT**  
AdFormat |  + |  + |  + |  segment |  segment |  segment |  segment |  – |  segment |  – |  –  
AdGroupId |  + |  + |  + |  – |  attribute |  attribute |  – |  attribute |  segment |  segment |  attribute  
AdGroupName |  + |  – |  + |  – |  attribute |  attribute |  – |  attribute |  segment |  segment |  attribute  
AdId |  + |  + |  + |  – |  attribute |  – |  – |  – |  segment |  segment |  segment  
AdNetworkType |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
Age |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  –  
AudienceTargetId |  – |  + |  – |  – |  – |  – |  – |  filter |  filter |  – |  –  
AvgClickPosition |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  – |  metric  
AvgCpc |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
AvgCpm |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric – |   
AvgEffectiveBid |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
AvgImpressionFrequency |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric – |   
AvgImpressionPosition |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  – |  metric  
AvgPageviews |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
AvgTrafficVolume |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
AvgVideoCompleteCost |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric – |   
BounceRate |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
Bounces |  + |  – |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
CampaignId |  + |  + |  + |  – |  attribute |  attribute |  attribute |  attribute |  segment |  segment |  attribute  
CampaignName |  + |  – |  + |  – |  attribute |  attribute |  attribute |  attribute |  segment |  segment |  attribute  
CampaignUrlPath |  + |  – |  + |  – |  attribute |  attribute |  attribute |  attribute |  segment |  segment |  attribute  
CampaignType |  + |  + |  + |  segment |  attribute |  attribute |  attribute |  attribute |  segment |  segment |  attribute  
CarrierType |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
Clicks |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
ClickType |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
ClientLogin |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  segment  
ConversionRate |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
Conversions |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
Cost |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
CostPerConversion |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
CPV |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric – |   
Criteria |  + |  – |  – |  – |  – |  – |  – |  attribute |  segment |  – |  segment  
CriteriaId |  + |  – |  – |  – |  – |  – |  – |  attribute |  segment |  – |  segment  
CriteriaType |  + |  + |  + |  segment |  segment |  segment |  segment |  attribute |  segment |  – |  segment  
Criterion |  + |  – |  – |  – |  – |  – |  – |  attribute |  segment |  – |  segment  
CriterionId |  + |  – |  – |  – |  – |  – |  – |  attribute |  segment |  – |  segment  
CriterionType |  + |  + |  + |  segment |  segment |  segment |  segment |  attribute |  segment |  – |  segment  
Ctr |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
Date |  + |  – |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  segment  
Device |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment – |   
DynamicTextAdTargetId |  – |  + |  – |  – |  – |  – |  – |  filter |  filter |  – |  filter  
ExternalNetworkName |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
Gender |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment – |   
GoalsRoi |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
ImpressionReach |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric – |   
Impressions |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
IncomeGrade |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  segment  
Keyword |  – |  + |  – |  – |  – |  – |  – |  filter |  filter |  – |  filter  
LocationOfPresenceId |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
LocationOfPresenceName |  + |  – |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
MatchedKeyword |  + |  + |  + |  – |  – |  – |  – |  – |  – |  – |  segment  
MatchType |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  segment  
MobilePlatform |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
Month |  + |  – |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  segment  
Placement |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  segment  
Profit |  + |  + |  + |  metric |  metric |  metric |  metric |  metrics |  metric |  metric |  metric  
PurchaseRevenue |  + |  + |  + |  metric |  metric |  metric |  metric |  metrics |  metric |  metric |  metric  
PurchaseProfit |  + |  + |  + |  metric |  metric |  metric |  metric |  metrics |  metric |  metric |  metric  
PurchaseGoalsRoi |  + |  + |  + |  metric |  metric |  metric |  metric |  metrics |  metric |  metric |  metric  
Quarter |  + |  – |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  segment  
Query |  + |  + |  + |  – |  – |  – |  – |  – |  – |  – |  attribute  
Revenue |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
RlAdjustmentId |  + |  + |  + |  – |  – |  – |  – |  segment |  segment |  – |  –  
Sessions |  + |  – |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  –  
Slot |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  –  
SmartAdTargetId |  – |  + |  – |  – |  – |  – |  – |  filter |  filter |  – |  –  
TargetingCategory |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  – |  segment  
TargetingLocationId |  + |  + |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  –  
TargetingLocationName |  + |  – |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  –  
VideoComplete |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoCompleteRate |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoFirstQuartile |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoFirstQuartileRate |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoMidpoint |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoMidpointRate |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoThirdQuartile |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoThirdQuartileRate |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoViews |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
VideoViewsRate |  + |  + |  + |  – |  – |  – |  – |  – |  – |  metric |  –  
Week |  + |  – |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  segment  
WeightedCtr |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
WeightedImpressions |  + |  + |  + |  metric |  metric |  metric |  metric |  metric |  metric |  metric |  metric  
Year |  + |  – |  + |  segment |  segment |  segment |  segment |  segment |  segment |  segment |  segment  
### Was the article helpful?
YesNo
Previous
[Request: report specification](https://yandex.com/dev/direct/doc/en/en/spec)
Next
[Incompatible fields and dependencies](https://yandex.com/dev/direct/doc/en/en/compatibility)
