---
title: How to work with display campaigns | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/cpm-banner
crawled_at: 2025-09-17T15:51:57.564175
---

Manage campaigns
# How to work with display campaigns
  * [Manage campaigns](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#feed)
    * [Display banners](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#feed1)
    * [Video ads](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#video-ads)
  * [Getting statistics](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#stat)
  * [Request example](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#request-example)


Display campaigns are ad campaigns where payment is based on Yandex Direct impressions (not clicks). Ads are displayed in the Yandex Advertising Network on desktops and mobile devices, as well as on digital billboards.
A display campaign can include ad groups with different formats. The Yandex Direct API currently supports display banners and video display ads. For more information about these formats, see [Display banners](https://yandex.com/support/direct/products-cpm-campaign/about.html) and [Video advertising](https://yandex.com/support/direct/products-cpm-campaign-video/about.html) in Yandex Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#feed)Manage campaigns
Alert
To design creatives in Ad Builder or upload creatives, you must use the web interface at this time.
  1. Create a campaign with the `CPM_BANNER_CAMPAIGN` type: pass the [CpmBannerCampaign](https://yandex.com/dev/direct/doc/ref-v5/campaigns/add-cpm-banner-campaign.html) structure in the [Campaigns.add](https://yandex.com/dev/direct/doc/ref-v5/campaigns/add.html) method.
For details about working with this type of campaign, see the section [Campaign type](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/campaign#type).
For information about available display strategies, see the section [Display strategies](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/campaign-strategies).
For information about other campaign parameters, see the section [Campaign parameters](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/campaign-params).
  2. You can add groups of display banners and groups of video ads to a display campaign.


###  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#feed)Display banners
  1. Create an ad group.
In a group of display banners, you can use either a user profile target or keywords. Depending on what impression criteria you plan to add, choose the group subtype:
     * To create a group with an audience target based on a user profile, use the [AdGroups.add](https://yandex.com/dev/direct/doc/ref-v5/adgroups/add.html) method to pass an empty `CpmBannerUserProfileAdGroup` structure.
Note
Negative keywords are not allowed in a group with an audience target based on a user profile.
     * To create a group with keywords, use the [AdGroups.add](https://yandex.com/dev/direct/doc/ref-v5/adgroups/add.html) method to pass an empty `CpmBannerKeywordsAdGroup` structure.
You cannot change the group subtype in the future.
  2. Add impression criteria to the group.
User profile
Keywords
    1. Get reference lists of Crypta segments based on demographic and behavioral characteristics, as well as lists of Crypta user interest segments: use the [Dictionaries.get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method and specify `AudienceDemographicProfiles` and `AudienceInterests` in the request.
    2. Create a user profile: use the [RetargetingLists.add](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/add.html) method.
The user profile is implemented as a retargeting list of the `AUDIENCE` type. For more information about the profile, see the section [Retargeting list (RetargetingList)](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/retargeting-list).
    3. Add a user profile to the ad group: the [AudienceTargets.add](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/add.html) method.
If a manual display strategy is selected in the campaign, you can set a bid on the user profile immediately when adding the profile to an ad group or later using the [AudienceTargets.setBids](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/setBids.html) method.
Add keywords: use the [Keywords.add](https://yandex.com/dev/direct/doc/ref-v5/keywords/add.html) method.
You can set bids and priorities immediately when creating keywords, or later using the [KeywordBids.set](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/set.html) or [KeywordBids.setAuto](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/setAuto.html) method.
Aautotargeting can't be added to a group of display ads.
  3. Add ads to the group:
    1. Design creatives in Ad Builder or upload existing creatives in the Yandex Direct web interface. See [How to launch a display campaign](https://yandex.com/support/direct/products-cpm-campaign/create.html) in the Help for Yandex Direct.
    2. Get IDs of available creatives with the `HTML5_CREATIVE` and `IMAGE_CREATIVE` type: use the [Creatives.get](https://yandex.com/dev/direct/doc/ref-v5/creatives/get.html) method.
    3. Add one or more ads with the `CPM_BANNER_AD` type to the group by using the [Ads.add](https://yandex.com/dev/direct/doc/ref-v5/ads/add.html) method. Pass the ad parameters in the `CpmBannerAdBuilderAd` structure.
  4. Submit ads for review: the [Ads.moderate](https://yandex.com/dev/direct/doc/ref-v5/ads/moderate.html) method.


###  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#video-ads)Video ads
  1. Create an ad group: use the [Groups.add](https://yandex.com/dev/direct/doc/ref-v5/adgroups/add.html) method to pass an empty `CpmVideoAdGroup` structure.
  2. Add a user profile target to the group.
    1. Get reference lists of Crypta segments based on demographic and behavioral characteristics, as well as lists of Crypta user interest segments: use the [Dictionaries.get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method and specify `AudienceDemographicProfiles` and `AudienceInterests` in the request.
    2. Create a user profile: use the [RetargetingLists.add](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/add.html) method.
The user profile is implemented as a retargeting list of the `AUDIENCE` type. For more information about the profile, see the section [Retargeting list (RetargetingList)](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/retargeting-list).
    1. Add a user profile to the ad group: the [AudienceTargets.add](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/add.html) method.
If a manual display strategy is selected in the campaign, you can set a bid on the user profile immediately when adding the profile to an ad group or later using the [AudienceTargets.setBids](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/setBids.html) method.
  3. Add ads to the group:
    1. Design creatives in Ad Builder in the Yandex Direct web interface. See [Video advertising / How to launch](https://yandex.com/support/direct/products-cpm-campaign-video/create.html) in Yandex Direct Help.
    2. Get IDs of available creatives with the `CPM_VIDEO_CREATIVE` type: use the [Creatives.get](https://yandex.com/dev/direct/doc/ref-v5/creatives/get.html) method.
    3. Add one or more ads with the `CPM_VIDEO_AD` type: use the [Ads.add](https://yandex.com/dev/direct/doc/ref-v5/ads/add.html) method. Pass the ad parameters in the `CpmVideoAdBuilderAd` structure.
  4. Submit ads for review: the [Ads.moderate](https://yandex.com/dev/direct/doc/ref-v5/ads/moderate.html) method.


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#stat)Getting statistics
To get statistics for display campaigns, use [Reports](https://yandex.com/dev/direct/doc/reports/reports.html). The report can provide the average CPM, the average frequency of impressions per user, and the number of unique users who were shown a banner.
In the report request, specify:
  * In the `Type` parameter — the REACH_AND_FREQUENCY_PERFORMANCE_REPORT report type.
  * In the `Filter` structure — one or multiple IDs of display campaigns. A filter by campaign is required for this type of report.
  * In the `FieldNames` array, add the `CampaignId`, `AvgCpm`, `AvgImpressionFrequency`, and `ImpressionReach` values.


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/cpm-banner#request-example)Request example
```
curl \
  -H 'Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f' \
  -H 'Accept-Language: en' \
  -H 'Client-Login: agrom' \
  -H 'returnMoneyInMicros: false' \
  -d '{
    "params": {
      "SelectionCriteria": {
        "Filter": [{
          "Field": "CampaignId",
          "Operator": "IN",
          "Values": [ "10012", "10017" ]
        }]
      },
      "FieldNames": [ "CampaignId", "Impressions", "Clicks", "Cost", "AvgCpm", "AvgImpressionFrequency", "ImpressionReach" ],
      "OrderBy": [{
        "Field": "CampaignId"
      }],
      "ReportName": "Display campaigns",
      "ReportType": "REACH_AND_FREQUENCY_PERFORMANCE_REPORT",
      "DateRangeType": "LAST_WEEK",
      "Format": "TSV",
      "IncludeVAT": "YES",
      "IncludeDiscount": "YES"
    }
  }' \
  https://api.direct.yandex.com/json/v5/reports

```

Copied
### Was the article helpful?
YesNo
Previous
[Statistics and analysis](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/statistics)
Next
[How to work with dynamic ads](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/dynamic-ads)
