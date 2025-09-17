---
title: How to manage smart banners | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/smart-ads
crawled_at: 2025-09-17T15:47:18.424436
---

How to manage smart banners
# How to manage smart banners
Smart banners are interactive banners with dynamic content. They are automatically generated from a feed, which is a file with product offers. Smart banners can be targeted at users who viewed products on your site or got engaged with similar products. For more information, see [Smart banners](https://yandex.com/support/direct/smart-banners/about.html) in Yandex.Direct Help.
Alert
Designing creatives is only available in the web interface at this time.
  1. Upload the feed: use the [Feeds.add](https://yandex.com/dev/direct/doc/ref-v5/feeds/add.html) method.
  2. Create a campaign: in the [Campaigns.add](https://yandex.com/dev/direct/doc/ref-v5/campaigns/add.html) method, pass the [SmartCampaign](https://yandex.com/dev/direct/doc/ref-v5/campaigns/add-smart-campaign.html) structure.
For details about working with this type of campaign, see the section [Campaign type](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/campaign#type).
For information about available display strategies, see the section [Display strategies](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/campaign-strategies).
For information about other campaign parameters, see the section [Campaign parameters](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/campaign-params).
  3. Create an ad group: in the [AdGroups.add](https://yandex.com/dev/direct/doc/ref-v5/adgroups/add.html) method, pass the `SmartAdGroup` structure. Enter the feed ID in the group.
  4. Add targeting criteria for smart banners to the group: [SmartAdTargets.add](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/add.html). You can set a bid and/or priority for dynamic ad targets.
  5. Add ads to the group:
    1. Design creatives in Ad Builder in the Yandex Direct web interface. See [Creative Ad Builder for smart banners](https://yandex.com/support/direct/smart-banners/design.html) in the Help for Yandex.Direct.
    2. Get IDs of available creatives with the `SMART_CREATIVE` type: use the [Creatives.get](https://yandex.com/dev/direct/doc/ref-v5/creatives/get.html) method.
    3. Add one or more ads with the `SMART_AD` type: use the [Ads.add](https://yandex.com/dev/direct/doc/ref-v5/ads/add.html) method. Ad parameters must be passed in the `SmartAdBuilderAd` structure.
  6. Submit ads for review: the [Ads.moderate](https://yandex.com/dev/direct/doc/ref-v5/ads/moderate.html) method.


Copied
### Was the article helpful?
YesNo
Previous
[How to work with dynamic ads](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/dynamic-ads)
Next
[Recommendations for registering representatives](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/representatives-recommendations)
