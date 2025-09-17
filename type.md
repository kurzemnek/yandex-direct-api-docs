---
title: Report type | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/type
crawled_at: 2025-09-17T15:37:54.964055
---

Report type
# Report type
In the _ReportType_ parameter, specify the type of report. The report type affects which fields are available and how the data is grouped.
For example, if you set the SEARCH_QUERY_PERFORMANCE_REPORT type, the report data will be grouped by `AdGroupId` and `Query`. Note that when you group data by certain fields, those fields aren't added automatically to the report. The report contains only the fields that are listed in the _FieldNames_ parameter.
The most general report type is CUSTOM_REPORT. It doesn't add any groupings.
The table lists the report types.
**Report type** |  **Description** |  **Adds data grouping** |  **Fields not allowed**  
---|---|---|---  
ACCOUNT_PERFORMANCE_REPORT |  Statistics for the advertiser's account |  – |  See section [Allowed fields](https://yandex.com/dev/direct/doc/en/en/fields-list)  
CAMPAIGN_PERFORMANCE_REPORT |  Statistics for campaigns |  _CampaignId_ |  See section [Allowed fields](https://yandex.com/dev/direct/doc/en/en/fields-list)  
ADGROUP_PERFORMANCE_REPORT |  Statistics for ad groups |  _AdGroupId_ |  See section [Allowed fields](https://yandex.com/dev/direct/doc/en/en/fields-list)  
AD_PERFORMANCE_REPORT |  Statistics for ads |  _AdId_ |  _AudienceTargetId_ , _Criteria_ , _CriteriaId_ , _Criterion_ , _CriterionId_ , _DynamicTextAdTargetId_ , _Keyword_ , _Query_ , _RlAdjustmentId_ , _SmartAdTargetId_  
CRITERIA_PERFORMANCE_REPORT |  Statistics for targeting criteria |  _AdGroupId_ , _CriteriaId_ , _CriteriaType_ |  _AdFormat_ , _AdId_ , _Placement_ , _Query_  
CUSTOM_REPORT |  Statistics with custom groupings |  – |  _Query_  
REACH_AND_FREQUENCY_PERFORMANCE_REPORT |  Statistics for display campaigns. The report only contains data for display campaigns and ignores all other types of campaigns. |  In the report request, set the _FieldNames_ value to `CampaignId` |  See section [Allowed fields](https://yandex.com/dev/direct/doc/en/en/fields-list)  
SEARCH_QUERY_PERFORMANCE_REPORT |  Statistics for search queries |  _AdGroupId_ , _Query_ |  See section [Allowed fields](https://yandex.com/dev/direct/doc/en/en/fields-list)  
Note
All the report types use single attribution: each impression and click is attributed to only one targeting criteria, region, user age, etc.
Report type.  
**Required** Yes
Names of fields (columns) that will be in the report. To see which fields you can specify, see the sections [Available fields](https://yandex.com/dev/direct/doc/en/en/fields-list) and [Incompatible fields and dependencies](https://yandex.com/dev/direct/doc/en/en/compatibility). For the REACH_AND_FREQUENCY_PERFORMANCE_REPORT report type, the CampaignId field is required.  
**Required** Yes
The campaign ID
ID of the ad group. It's not shown in the report on campaigns created in the Campaign Wizard.
The ad ID. It's not shown in the report on campaigns created in the Campaign Wizard.
ID of the audience target. See the section [Audience target (AudienceTarget)](https://yandex.com/dev/direct/doc/dg/objects/audience-target.html).
Name or text of the targeting criteria:
  * For impressions for a keyword or synonym: a keyword with an ID.
  * For autotargeting: the “---autotargeting” value.
  * For targeting a related keyword: 
    * an empty value, if the report type is CUSTOM_REPORT.
    * the text of the related keyword, if the report type is SEARCH_QUERY_PERFORMANCE_REPORT.
  * For targeting an audience target: the name of the retargeting list, or the name of a mobile app category.
  * For showing a dynamic ad: the name of the dynamic text ad target, or the name of the filter.
  * For showing smart banners: the name of the filter.  
  
The selection is grouped by `CriteriaID` implicitly.


Copied
ID of the targeting criteria:
  * For targeting a keyword or synonym – the keyword ID.
  * For autotargeting: the autotargeting ID.
  * For targeting a related keyword – a dash.
  * For targeting an audience target – the ID of the audience target.
  * For showing a dynamic ad – the ID of the audience target for dynamic ads, or the ID of the filter.
  * For showing smart banners – the ID of the filter.  
  
It's not shown in the report on campaigns created in the Campaign Wizard.


The name or text of the targeting criteria set by the advertiser:
  * For impressions for a keyword or synonym: a keyword with an ID.
  * For targeting a [related keyword](https://yandex.com/support/direct/keywords/related-keywords.html) – the keyword text, or the value “Automatically added phrase” if the keyword couldn't be determined.
  * For autotargeting: the “---autotargeting” value.
  * For targeting an audience target: the name of the retargeting list, or the name of a mobile app category.
  * For showing a dynamic ad: the name of the dynamic text ad target, or the name of the filter.
  * For showing smart banners: the name of the filter.  
  
The selection is grouped by `CriterionID` implicitly. We recommend using this field instead of `Criteria`.


Copied
The ID of the targeting criteria set by the advertiser:
  * For targeting a keyword or synonym: the keyword ID.
  * For targeting a related keyword: the ID of the keyword, or a dash if the keyword couldn't be determined.
  * For autotargeting: the autotargeting ID.
  * For targeting an audience (using a retargeting list or interest in a mobile app category): the ID of the audience target, or a dash if the target was deleted.
  * For a dynamic text ad target generated from site pages: the ID of the dynamic text ad target.
  * For a filter for dynamic ads generated from a feed, or a filter for smart banners, the filter ID.  
  
We recommend using this field instead of `CriteriaId`. It's not shown in the report on campaigns created in the Campaign Wizard.


Copied
The ID of the audience target for dynamic ads, or the ID of the filter for dynamic ads. See the section [Ad target for dynamic ads (DynamicTextAdTarget — Webpage)](https://yandex.com/dev/direct/doc/dg/objects/dynamictextadtarget.html)
The keyword text.
The search query that triggered the ad.
ID of the retargeting and retargeting criteria used for applying bid adjustments to the target audience.
The ID of the filter for smart banners.
The type of targeting criteria set by the advertiser:
  * KEYWORD — Keyword.
  * AUTOTARGETING — Autotargeting.
  * AUDIENCE_TARGET — Audience target.
  * DYNAMIC_TEXT_AD_TARGET — Audience target for dynamic ads or the filter for dynamic ads.
  * SMART_BANNER_FILTER — Filter for smart banners.


Format of the ad impression:
  * IMAGE: Image ad.
  * TEXT — A text ad.
  * VIDEO: Video ad.
  * SMART_MULTIPLE — Smart banner.
  * SMART_SINGLE — Smart ad.
  * ADAPTIVE_IMAGE: Adaptive image ad.
  * SMART_TILE — Smart tile.


Name of the site where the ad is being displayed.
Copied
### Was the article helpful?
YesNo
Previous
[Report period](https://yandex.com/dev/direct/doc/en/en/period)
Next
[Report fields](https://yandex.com/dev/direct/doc/en/en/fields)
