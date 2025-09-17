---
title: Statistics | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/stat
crawled_at: 2025-09-17T16:01:04.151416
---

Request parameters
# Statistics
  * [Request parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#spec)
  * [Report fields](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#fields)
  * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#learn-more)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#spec)Request parameters
**Parameter name in Live 4** |  **Parameter name in Reports**  
---|---  
`CampaignID` |  To get statistics on the selected campaign, use the structure ```
<Filter>   <Field>CampaignId</Field>   <Operator>EQUALS</Operator>   <Values>...</Values> </Filter> 

```
See [Filtering data](https://yandex.com/dev/direct/doc/reports/filters.html).  
`StartDate`, `EndDate` |  To get statistics for a specific period, use the parameters `DateFrom` and `DateTo` with `<DateRangeType>CUSTOM_DATE</DateRangeType>`. See [Report period](https://yandex.com/dev/direct/doc/reports/period.html).  
`CompressReport` |  Not supported  
`Currency` |  Not supported. Monetary values are shown in the advertiser's currency.  
`Filter` |  Specify the criteria for filtering data in the `Filter` array. For the equivalents of filter parameters, see the section [Filter parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#Filter). See [Filtering data](https://yandex.com/dev/direct/doc/reports/filters.html).  
`GroupByColumns` |  In the `FieldNames` array, specify the fields to show in the report. For the equivalents of groupings, see the section [Grouping by columns](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#GroupByColumns).  
`GroupByDate` |  In the `FieldNames` array, specify either the `Date`, `Week`, or `Month field.`  
`IncludeDiscount` |  `IncludeDiscount`  
`IncludeVAT` |  `IncludeVAT`  
`Limit` |  Use the structure  
`<Page>   <Limit>...</Limit> </Page>`  
`Offset` |  Not supported  
`OrderBy` |  `OrderBy`  
`TypeResultReport` |  `Format` (only TSV format is supported)  
**Names of fields from GroupByColumns** |   
`clAdjustment` |  `RlAdjustmentId`  
`clAveragePosition` |  `AvgClickPosition`, `AvgImpressionPosition`  
`clBanner` |  `AdId`  
`clCarrierType` |  `CarrierType`  
`clDate` |  `Date`, `Week`, or `Month`  
`clDemographics` |  `Age`, `Gender`  
`clDeviceType` |  `Device`  
`clGeo` |  `TargetingLocationId`  
`clGoalConversionsNum` |  `Conversions`  
`clImage` |  `AdFormat`  
`clMobilePlatform` |  `MobilePlatform`  
`clPage` |  `Placement`, `AdNetworkType`  
`clPhrase` |  `CriterionId`  
`clPositionType` |  `Slot`  
`clROI` |  `GoalsRoi`  
`clStatGoals` |  `AvgPageviews`, `ConversionRate`, `CostPerConversion`  
**Filter parameters** |   
`Age` |  `Age`  
`Banner` |  `AdId`  
`CarrierType` |  `CarrierType`  
`DeviceType` |  `Device`  
`Gender` |  `Gender`  
`Geo` |  `TargetingLocationId`  
`MobilePlatform` |  `MobilePlatform`  
`PageName` |  `Placement`  
`PageType` |  `AdNetworkType`  
`Phrase` |  `Keyword`  
`PositionType` |  `Slot`  
`StatGoals` |  Use the `Goals request parameter`  
`WithImage` |  `AdFormat`  
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#fields)Report fields
**Field name in the Live 4 version** |  **Field names in Reports**  
---|---  
`type` (`phrasesDict` element) |  `CriterionType`  
`value` (`phrasesDict` element) |  `Criterion`, `MatchType`  
`age` |  `Age`  
`bannerID` |  `AdId`  
`carrier_type` |  `CarrierType`  
`clicks` |  `Clicks`  
`clicks_average_position` |  `AvgClickPosition`  
`clicks_context` |  `Clicks` with `AdNetworkType`  
`clicks_search` |   
`device_type` |  `Device`  
`gender` |  `Gender`  
`goal_conversion` |  `ConversionRate`  
`goal_conversions_num` |  `Conversions`  
`goal_cost` |  `CostPerConversion`  
`goal_id` |  Not supported  
`mobile_platform` |  `MobilePlatform`  
`phrase_id` |  `CriterionId` with `CriterionType`  
`placeName` |  `Placement`  
`placeType` |  `AdNetworkType`  
`position_type` |  `Slot`  
`regionID` |  `TargetingLocationId`  
`RetargetingID` |  `CriterionId` with `CriterionType`  
`revenue` |  `Revenue`  
`rl_adjustment_id` |  `RlAdjustmentId`  
`roi` |  `GoalsRoi`  
`session_depth` |  `AvgPageviews`  
`shows` |  `Impressions`  
`shows_average_position` |  `AvgImpressionPosition`  
`shows_context` |  `Impressions` with `AdNetworkType`  
`shows_search` |   
`statDate` |  `Date`, `Week`, `Month`, `Quarter`, or `Year`  
`stat_type` |  `AdFormat`  
`sum` |  `Cost`  
`sum_context` |  `Cost` with `AdNetworkType`  
`sum_search` |   
`WebpageID` |  `CriterionId` with `CriterionType`  
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat#learn-more)Learn more
  * [Example: Reports instead of GetBannersStat (Live)](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat-example)


Copied
### Was the article helpful?
YesNo
Previous
[Parameters of VCards](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/contact-info)
Next
[Parameters of retargetings and retargeting conditions](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/retargetings)
