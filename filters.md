---
title: Filtering data | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/filters
crawled_at: 2025-09-17T15:38:08.940873
---

Filtering data
# Filtering data
  * [Filter by ClientLogin](https://yandex.com/dev/direct/doc/en/en/filters#filter-by-clientlogin)
  * [Filter by Age](https://yandex.com/dev/direct/doc/en/en/filters#filter-by-age)
  * [Filters for targeting criteria](https://yandex.com/dev/direct/doc/en/en/filters#filters-for-targeting-criteria)
  * [RlAdjustmentId filter](https://yandex.com/dev/direct/doc/en/en/filters#rladjustmentid-filter)
  * [Filters for monetary values](https://yandex.com/dev/direct/doc/en/en/filters#filters-for-monetary-values)


To filter data in the report, use the Filter structure. Each filter is a set of criteria for selecting data. Filters are combined with AND, so the report shows data that meets all the filter criteria. A filter consists of three parameters:
  * Field — Which field to compare the values of.
  * Operator — How to compare.
  * Values — An array of symbols to compare with.


For example, to make the report only show rows that have more than 10 conversions, use the filter
JSON
XML
```
"Filter": [{
"Field": "Conversions",
"Operator": "GREATER_THAN",
"Values": ["10"]
}]

```

```
<Filter>
<Field>Conversions</Field>
<Operator>GREATER_THAN</Operator>
<Values>10</Values>
</Filter>

```

The table below shows how operators correspond to fields.
**Field name** |  **Operators allowed**  
---|---  
AdNetworkType |  EQUALS, IN  
CampaignId  
CampaignType  
ClientLogin  
AdFormat |  EQUALS, IN, NOT_EQUALS, NOT_IN  
AdGroupId  
AdId  
Age  
AudienceTargetId  
CarrierType  
ClickType  
CriteriaType  
CriterionType  
Device  
DynamicTextAdTargetId  
ExternalNetworkName  
Gender  
IncomeGrade  
LocationOfPresenceId  
MatchType  
MobilePlatform  
Placement  
RlAdjustmentId  
Slot  
SmartAdTargetId  
TargetingCategory  
TargetingLocationId |  EQUALS, IN, GREATER_THAN, LESS_THAN  
Clicks  
Conversions  
ImpressionReach |  GREATER_THAN, LESS_THAN  
Impressions  
AvgClickPosition  
AvgCpc  
AvgCpm  
AvgEffectiveBid  
AvgImpressionFrequency  
AvgImpressionPosition  
AvgPageviews  
AvgTrafficVolume  
BounceRate  
ConversionRate  
Cost  
CostPerConversion  
Ctr  
GoalsRoi  
Profit  
Revenue  
WeightedCtr  
WeightedImpressions  
Keyword |  EQUALS, IN, NOT_EQUALS, NOT_IN, STARTS_WITH_IGNORE_CASE, STARTS_WITH_ANY_IGNORE_CASE, DOES_NOT_START_WITH_IGNORE_CASE, DOES_NOT_START_WITH_ALL_IGNORE_CASE  
MatchedKeyword  
Query  
##  [](https://yandex.com/dev/direct/doc/en/en/filters#filter-by-clientlogin)Filter by ClientLogin
In the ClientLogin filter, you can specify only the client usernames available to the manager account.
  * If the filter is not set for the field, the username from the `Client-Login` HTTP header is used by default. If the header is missing, the username is taken from the OAuth token.
  * If the filter for the `ClientLogin` field exists, the maximum number of rows in the report is 500,000 (the same value is used by default).


##  [](https://yandex.com/dev/direct/doc/en/en/filters#filter-by-age)Filter by Age
In the Age field, statistics for periods up to 08/21/2018 will display the value AGE_45, and after that date, the values AGE_45_54 and AGE_55.
To get statistics for all users age 45 and over regardless of the report period, we recommend specifying all three values in the Age filter:
JSON
XML
```
"Filter": [{
"Field": "Age",
"Operator": "IN",
"Values": ["AGE_45", "AGE_45_54", "AGE_55"]
}]

```

```
<Filter>
<Field>Age</Field>
<Operator>IN</Operator>
<Values>AGE_45</Values>
<Values>AGE_45_54</Values>
<Values>AGE_55</Values>
</Filter>

```

If not all of these age segments are specified in the filter, the statistics for the period that includes the date 21.08.2018 may be incomplete. For example, if only the values AGE_45_54 and AGE_55 are specified, the report will not include users whose age group is defined as AGE_45.
If the filter specifies AGE_45 and does not specify AGE_45_54 and AGE_55, the report won't be generated for a period after 21.08.2018 and an error message will be returned.
##  [](https://yandex.com/dev/direct/doc/en/en/filters#filters-for-targeting-criteria)Filters for targeting criteria
The following fields aren't output to the report. They are only used for filtering data. These fields are mutually exclusive; only one of them can be present in the Filter array.
**Field** |  **Description** |  **Comment**  
---|---|---  
`Keyword` |  The keyword text. |  The keyword text is shown in the `Criterion` field in the report, and the keyword ID is shown in the `CriterionId` field.  
`AudienceTargetId` |  ID of the audience target. See [the section Audience target (AudienceTarget)](https://yandex.com/dev/direct/doc/dg/objects/audience-target.html). |  The ID of the audience target is shown in the `CriterionId` field. The `Criterion` field shows the name of the retargeting list. Filtering by `AudienceTargetId` is available for data starting from December 8, 2017.  
`DynamicTextAdTargetId` |  The ID of the audience target for dynamic ads, or the ID of the filter for dynamic ads. See the section [Ad target for dynamic ads (DynamicTextAdTarget — Webpage)](https://yandex.com/dev/direct/doc/dg/objects/dynamictextadtarget.html) |  The ID of the dynamic text ad target is shown in the `CriterionId` field in the report, and the name is shown in the `Criterion` field.  
`SmartAdTargetId` |  The ID of the filter for smart banners. |  The ID of the smart banner filter is shown in the `CriterionId` field in the report, and the name is shown in the `Criterion` field.  
##  [](https://yandex.com/dev/direct/doc/en/en/filters#rladjustmentid-filter)RlAdjustmentId filter
The `RIAdjustmentId` filter can have the value NONE, which means that bid adjustments for a target audience weren't applied.
In particular, if you only want the report to show data with bid adjustments for a target audience, use this filter:
JSON
XML
```
"Filter": [{
"Field": "RlAdjustmentId",
"Operator": "NOT_EQUALS",
"Values": ["NONE"]
}]

```

```
<Filter>
<Field>RlAdjustmentId</Field>
<Operator>NOT_EQUALS</Operator>
<Values>NONE</Values>
</Filter>

```

##  [](https://yandex.com/dev/direct/doc/en/en/filters#filters-for-monetary-values)Filters for monetary values
All monetary values in filters should be specified as **integers** : the amount in the currency, **multiplied by 1,000,000** (regardless of the `returnMoneyInMicros: false` header).
Copied
### Was the article helpful?
YesNo
Previous
[Monetary values](https://yandex.com/dev/direct/doc/en/en/money)
Next
[HTTP headers](https://yandex.com/dev/direct/doc/en/en/headers)
