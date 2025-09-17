---
title: Report content | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/report-format
crawled_at: 2025-09-17T15:44:22.917803
---

Report content
# Report content
The report is generated in 
The first row in the report contains the report name that is set in the `ReportName` parameter, along with the start and end dates of the reporting period. This row is not included in the report if the request specifies the HTTP header `skipReportHeader: true`.
The second row contains the names of the fields (columns) that are set in the `FieldNames` parameter. This row is not included in the report if the request specifies the HTTP header `skipColumnHeader: true`.
The following rows contain the statistics (the values for the fields).
The last row in the report contains the number of rows with statistics. This row is not included in the report if the request specifies the HTTP header `skipReportSummary: true`.
The fields are described in the table below.
**Field** |  **Description**  
---|---  
`AdFormat` |  Format of the ad impression:
  * IMAGE: Image ad.
  * TEXT: Text ad.
  * VIDEO: Video ad.
  * SMART_MULTIPLE: Smart banner.
  * SMART_SINGLE: Smart ad.
  * ADAPTIVE_IMAGE: Adaptive image ad.
  * SMART_TILE — Smart tile.

  
`AdGroupId` |  ID of the ad group. It's not shown in the report on campaigns created in the Campaign Wizard.  
`AdGroupName` |  Name of the ad group. It's not shown in the report on campaigns created in the Campaign Wizard.  
`AdId` |  The ad ID. It's not shown in the report on campaigns created in the Campaign Wizard.  
`AdNetworkType` |  The type of advertising place where the ad is shown:
  * SEARCH: In search results.
  * AD_NETWORK: On ad networks.

  
`Age` |  The user's age group: one of the values AGE_0_17, AGE_18_24, AGE_25_34, AGE_35_44, AGE_45, AGE_45_54, AGE_55 or UNKNOWN. Statistics for periods up through 21.08.2018 output the AGE_45 value, and after this date the values AGE_45_54 and AGE_55 are shown. The statistics for a period that includes 21.08.2018 might show some with the AGE_45 value and some with AGE_45_54 or AGE_55.  
`AvgClickPosition` |  Average position where the ad was clicked. Calculated using only clicks on the first page of Yandex search results. The top position is assigned the number 1.  
`AvgCpc` |  Average cost per click.  
`AvgCpm` |  Average price per thousand impressions. Data is only available for display campaigns.  
`AvgEffectiveBid` |  Average bid per click with all adjustments.  
Data is only available for pay-per-click campaigns.  
`AvgImpressionFrequency` |  Average impression frequency per user, up to two decimal places. Data is only available for display campaigns.  
`AvgImpressionPosition` |  Average display position of the ad. Calculated using only displays on the first page of Yandex search results. The top position is assigned the number 1.  
`AvgPageviews` |  The average session depth on the site: the number of pages viewed (according to Yandex Metrica data).  
`AvgTrafficVolume` |  The average volume of traffic from positions that had ad impressions.  
`AvgVideoCompleteCost` |  Average CPV for 100% completed, in rubles.  
`BounceRate` |  The bounce rate compared to the total number of sessions (according to Yandex Metrica data).  
`Bounces` |  Number of bounces (according to Yandex Metrica data).  
`CampaignId` |  The campaign ID.  
`CampaignName` |  The campaign name.  
`CampaignUrlPath` |  The URL specified in the ad campaign settings.  
`CampaignType` |  The type of campaign:
  * TEXT_CAMPAIGN
  * MOBILE_APP_CAMPAIGN
  * DYNAMIC_TEXT_CAMPAIGN
  * SMART_CAMPAIGN
  * MCBANNER_CAMPAIGN
  * CPM_BANNER_CAMPAIGN
  * CPM_DEALS_CAMPAIGN
  * CPM_FRONTPAGE_CAMPAIGN
  * CPM_PRICE
  * UNIFIED_CAMPAIGN See 

  
`CarrierType` |  The type of connection:
  * CELLULAR: Mobile connection.
  * STATIONARY: Wi-Fi or wired internet access.
  * UNKNOWN: The type couldn't be detected.

  
`Clicks` |  The number of clicks.  
`ClickType` |  Which part of the ad was clicked by the user:
  * TITLE: The ad title. A click on the display link is considered a click on the ad. Note For image ads, smart banners, display banners, and search banners, any click on an ad is considered a title click.
  * SITELINK1, SITELINK2, ..., SITELINK8: Sitelinks.
  * VCARD: The virtual business card.
  * CHAT: Live chat with an operator.
  * PHONE: Phone number.
  * MOBILE_APP_ICON — The app icon (for mobile app ads).
  * BUTTON — The download or install button (for mobile app ads).
  * PRODUCT_EXTENSIONS: Product extensions.
  * MARKET: Yandex Market.
  * UNKNOWN

  
`ClientLogin` |  Username of the client's chief representative.  
`ConversionRate` |  The ratio of the number of converted sessions to the number of clicks, as a percentage (according to Yandex Metrica data). It might be greater than 100 because a single click can be the source of multiple sessions. If the request included Yandex Metrica goals (the Goals parameter), the ConversionRate field is replaced with `ConversionRate_<goal_ID>_<attribution_model>` fields.  
`ConversionRate_<goal_id>_<model>` |  The ratio of the number of converted sessions during which the specified goal was reached to the number of clicks. It might be greater than 100 because a single click can be the source of multiple sessions. The name of each field contains the goal ID and the name of the attribution model (the value of the AttributionModels parameter). For example, the ConversionRate_1234567_FC field contains the number of sessions that had a conversion for goal 1234567, when the session source is attributed using the "first click" model. If the request specifies multiple attribution models, the data is output separately for each model. The number of `ConversionRate_<goal_id>_<model>` fields for each attribution model corresponds to the number of goals specified in the Goals parameter.  
`Conversions` |  The number of conversions (according to Yandex Metrica data). If the request included Yandex Metrica goals (the Goals parameter), the Conversions field is replaced with `Conversions_<goal_ID>_<attribution_model>` fields.  
`Conversions_<goal_id>_<model>` |  Number of conversions during which this goal was reached. The name of each field contains the goal ID and the name of the attribution model (the value of the AttributionModels parameter).  
For example, the Conversions_1234567_FC field contains the number of sessions that had a conversion for goal 1234567, when the session source is attributed using the "first click" model. If the request specifies multiple attribution models, the data is output separately for each model. The number of `Conversions_<goal_ID>_<model>` fields for each attribution model corresponds to the number of goals specified in the Goals parameter. Notes. A single session may include conversions for multiple goals, so the total number of converted sessions might be less than the number of converted sessions for separate goals added together.  
`Cost` |  The cost of clicks.  
`CostPerConversion` |  The average cost of converted sessions (according to Yandex Metrica data): the ratio of the cost per click to the number of conversions. If the request included Yandex Metrica goals (the Goals parameter), the CostPerConversion field is replaced with `CostPerConversion_<goal_ID>_<attribution_model>` fields.  
`CostPerConversion_<goal_id>_<model>` |  The average cost of a conversion for the given goal. The name of each field contains the goal ID and the name of the attribution model (the value of the AttributionModels parameter). For example, the CostPerConversion_1234567_FC field contains the number of sessions that had a conversion for goal 1234567, when the session source is attributed using the "first click" model. If the request specifies multiple attribution models, the data is output separately for each model. The number of `CostPerConversion_<goal_ID>_<attribution_model>` fields for each attribution model corresponds to the number of goals specified in the Goals parameter.  
`CPV` |  Average CPV, in rubles.  
`Criteria` |  Name or text of the targeting criteria:
  * For impressions for a keyword or synonym: a keyword with an ID.
  * For autotargeting – the `"---autotargeting"` value.
  * For targeting a related keyword: 
    * an empty value, if the report type is CUSTOM_REPORT.
    * the text of the related keyword, if the report type is SEARCH_QUERY_PERFORMANCE_REPORT.
  * For targeting an audience target: the name of the retargeting list, or the name of a mobile app category.
  * For showing a dynamic ad: the name of the dynamic text ad target, or the name of the filter.
  * For showing smart banners: the name of the filter.

The selection is grouped by CriteriaID implicitly.  
`CriteriaId` |  ID of the targeting criteria:
  * For targeting a keyword or synonym: the keyword ID.
  * For autotargeting: the autotargeting ID.
  * For targeting a related keyword – a dash.
  * For targeting an audience target: the ID of the audience target.
  * For showing a dynamic ad: the ID of the dynamic text ad target, or the ID of the filter.
  * For showing smart banners: the ID of the filter.

It's not shown in the report on campaigns created in the Campaign Wizard.  
`CriteriaType` |  The type of targeting criteria set by the advertiser:
  * KEYWORD: Keyword.
  * AUTOTARGETING: Autotargeting.
  * AUDIENCE_TARGET — Audience target.
  * DYNAMIC_TEXT_AD_TARGET — Dynamic text ad target or filter for dynamic ads.
  * SMART_BANNER_FILTER: Filter for smart banners.

  
`Criterion` |  The name or text of the targeting criteria set by the advertiser:
  * For impressions for a keyword or synonym: a keyword with an ID.
  * For targeting a related keyword: the keyword text, or the value "Automatically added phrase" if the keyword couldn't be determined.
  * For autotargeting: the "---autotargeting" value.
  * For targeting an audience target: the name of the retargeting list, or the name of a mobile app category.
  * For showing a dynamic ad: the name of the dynamic text ad target, or the name of the filter.
  * For showing smart banners: the name of the filter.

The selection is grouped by CriterionID implicitly. We recommend using this field instead of Criteria.  
`CriterionId` |  The ID of the targeting criteria set by the advertiser:
  * For targeting a keyword or synonym: the keyword ID.
  * For targeting a related keyword: the ID of the keyword, or a dash if the keyword couldn't be determined.
  * For autotargeting: the autotargeting ID.
  * For targeting an audience (using a retargeting list or interest in a mobile app category): the ID of the audience target, or a dash if the target was deleted.
  * For a dynamic text ad target generated from site pages: the ID of the dynamic text ad target.
  * For a filter for dynamic ads generated from a feed, or a filter for smart banners, the filter ID.

We recommend using this field instead of CriteriaId. It's not shown in the report on campaigns created in the Campaign Wizard.  
`CriterionType` |  The type of targeting criteria set by the advertiser:
  * KEYWORD: Keyword.
  * AUTOTARGETING: Autotargeting.
  * RETARGETING: Audience target based on a retargeting list.
  * INTERESTS_AND_DEMOGRAPHICS: Audience target based on user profile.
  * MOBILE_APP_CATEGORY: Audience target based on interest in a mobile app category.
  * WEBPAGE_FILTER: Dynamic text ad target for dynamic ads generated based on site pages.
  * FEED_FILTER: Filter for dynamic ads generated from a feed, or a filter for smart banners.
  * OFFER_RETARGETING: Offer retargeting.

We recommend using this field instead of CriteriaType.  
`Ctr` |  CTR as a percent.  
`Date` |  The data statistics are provided for, in the format YYYY-MM-DD.  
`Device` |  The type of device the ad was shown on: DESKTOP, MOBILE or TABLET.  
`ExternalNetworkName` |  The name of the ad exchange (SSP).  
`Gender` |  The user's gender: GENDER_MALE, GENDER_FEMALE or UNKNOWN.  
`GoalsRoi` |  Return on ad spend by conversion value. Calculated as `(Revenue – Cost) / Cost` Up to two decimal places. If the request included Yandex Metrica goals (the Goals parameter), the GoalsRoi field is replaced with `GoalsRoi_<goal_ID>_<attribution_model>`.  
`GoalsRoi_<goal_id>_<model>` |  Return on ad spend by conversion value for the specified goal. Calculated as `(Revenue_<goal_id>_<model> – Cost) / Cost` The name of each field contains the goal ID and the name of the attribution model (the value of the AttributionModels parameter). For example, the GoalsRoi_1234567_FC field contains the ROI for goal 1234567, when the session source is attributed using the "first click" model. If the request specifies multiple attribution models, the data is output separately for each model. The number of `GoalsRoi_<goal_id>_<model>` fields for each attribution model corresponds to the number of goals specified in the Goals parameter.  
`ImpressionReach` |  Reach: the number of unique users who were shown a banner. Data is only available for display campaigns. Note Don't add together the values for the report rows, because the same user might be counted in multiple rows. In particular, the number of unique users for the campaign might be less than the total number of unique users for separate ad groups.  
`Impressions` |  Number of impressions.  
`IncomeGrade` |  User income level:
  * VERY_HIGH: Top 1%.
  * HIGH: 2–5%.
  * ABOVE_AVERAGE: 6–10%.
  * OTHER: Other users.

  
`LocationOfPresenceId` |  ID of the region where the user is located.  
`LocationOfPresenceName` |  Name of the region where the user is located.  
`MatchedKeyword` |  The matched keyword:
  * For targeting a keyword synonym: the synonym text.
  * For targeting a related keyword: the text of the related keyword.
  * For showing a dynamic ad: the text of the keyword that was generated automatically on the main page of the advertised site or product offer from a feed.
  * In other cases: an empty value.

  
`MatchType` |  Keyword match type:
  * RELATED_KEYWORD: Impression for a related keyword.
  * SYNONYM — Impression for the semantic matching of a keyword.
  * KEYWORD: Impression for a keyword.
  * NONE: All other cases.

  
`MobilePlatform` |  OS type: ANDROID, IOS, OTHER or UNKNOWN.  
`Month` |  Date of the start of the month, in the format YYYY-MM-DD.  
`Placement` |  Name of the site where the ad is being displayed.  
`Profit` |  Profit by conversion value. Calculated as the total conversion value for goals minus the cost of clicks.  
`PurchaseRevenue` |  Revenue for purchase goals only. You can specify the goals in the `PurchaseGoals` parameter or use the default logic.   
`PurchaseProfit` |  Profit. Calculated as the total revenue for goals minus the cost of clicks.  
`PurchaseGoalsRoi` |  Return on investment in advertising. Calculated as `(PurchaseProfit – Cost) / Cost` Up to two decimal places.  
`Quarter` |  Date of the start of the quarter, in the format YYYY-MM-DD.  
`Query` |  The search query that triggered the ad.  
`Revenue` |  Conversion value for goals. For priority goals, revenue is calculated based on the conversion values specified in the campaign settings. For other goals, it is calculated using Yandex Metrica data. If the request included Yandex Metrica goals (the Goals parameter), the Revenue field is replaced with `Revenue_<goal_ID>_<attribution_model>`.  
`Revenue_<goal_id>_<model>` |  Conversion value for a specific goal. The name of each field contains the goal ID and the name of the attribution model (the value of the AttributionModels parameter).  
For example, the Revenue_1234567_FC field contains the revenue for goal 1234567, when the session source is attributed using the "first click" model. If the request specifies multiple attribution models, the data is output separately for each model. The number of `Revenue_<goal_ID>_<attribution_model>` fields for each attribution model corresponds to the number of goals specified in the Goals parameter.  
`RlAdjustmentId` |  ID of the retargeting and retargeting criteria used for applying bid adjustments to the target audience.  
`Sessions` |  Number of sessions (according to Yandex Metrica data). For mobile app ads, the number of clicks is shown as the number of visits.  
`Slot` |  The ad display place:
  * ALONE: Exclusive placement.
  * PREMIUMBLOCK: Premium Placement.
  * SUGGEST: Ads in autofill suggestions.
  * PRODUCT_GALLERY: Product gallery.
  * OTHER: Other ad blocks.

  
`TargetingCategory` |  Targeting category:
  * EXACT: The targeted queries. The ad matches user queries.
  * ALTERNATIVE: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also match the query in this case.
  * COMPETITOR: Queries mentioning competitors. Searching competitors for the advertised product.
  * BROADER: Broad queries. Queries showing interest in a product exemplified by the ad.
  * ACCESSORY: Related queries. Queries for products that might interest the user in relation to the advertised product or service.

This field is deprecated and will soon cease to be supported. The settings specified using the API are converted for the web interface as follows: |  API |  Web interface  
---|---  
EXACT category is enabled. |  Enabled "Exact" and "Narrow" categories.  
COMPETITOR category is enabled (provided it's the only category enabled). |  Enabled "Competitors" brand mention option + the other brand mention options are disabled + all categories are enabled.  
Enabled COMPETITOR category (provided it isn't the only category enabled). |  Enabled "Competitors" brand mention option.  
COMPETITOR category is disabled. |  "Competitors" brand mention option is disabled.  
`TargetingLocationId` |  ID of the targeting region. If extended geotargeting is used, the ID may differ from the user's actual location. See   
`TargetingLocationName` |  Name of the targeting region.  
`VideoComplete` |  Views to 100%.  
`VideoCompleteRate` |  Rate of 100% views.  
`VideoFirstQuartile` |  Views to 25%.  
`VideoFirstQuartileRate` |  Rate of 25% views.  
`VideoMidpoint` |  Views to 50%.  
`VideoMidpointRate` |  Rate of 50% views.  
`VideoThirdQuartile` |  Views to 75%.  
`VideoThirdQuartileRate` |  Rate of 75% views.  
`VideoViews` |  Views  
`VideoViewsRate` |  View rate, %  
`Week` |  Date of the start of the week (Monday), in the format YYYY-MM-DD.  
`WeightedCtr` |  Weighted CTR as a percent. Calculated as `(Clicks / WeightedImpressions) × 100%`.  
`WeightedImpressions` |  Weighted impressions. Each impression is counted with the weight `TrafficVolume / 100`, where TrafficVolume is the traffic volume from the position where an impression occurred. So `WeightedImpressions = Impressions × AvgTrafficVolume / 100`.  
`Year` |  Date of the start of the year, in the format YYYY-MM-DD.  
Copied
### Was the article helpful?
YesNo
Previous
[Incompatible fields and dependencies](https://yandex.com/dev/direct/doc/en/en/compatibility)
Next
[Online and offline reports](https://yandex.com/dev/direct/doc/en/en/mode)
