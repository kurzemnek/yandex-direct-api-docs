---
title: Adjustments (BidModifier) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/bidmodifier
crawled_at: 2025-09-17T15:55:42.445071
---

Servicing
# Adjustments (BidModifier)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#methods)
  * [Types of adjustments](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#types)
  * [Adjustment levels](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#levels)
  * [Acceptable types of bid adjustments by type of campaign and group](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#compatibility)
  * [Disabling adjustments](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#toggle)
  * [How adjustments are applied](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#use)


Adjustments allow advertisers to raise or lower a bid, CPA, or conversion value for specific ad serving criteria. For more information, see [Adjustments](https://yandex.com/support/direct/impressions/bids-adjustment.html) in the Yandex Direct documentation.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#service)Servicing
Use the [BidModifiers](https://yandex.com/dev/direct/doc/ref-v5/bidmodifiers/bidmodifiers.html) service for managing adjustments.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#methods)Methods
[add](https://yandex.com/dev/direct/doc/ref-v5/bidmodifiers/add.html) | [delete](https://yandex.com/dev/direct/doc/ref-v5/bidmodifiers/delete.html) | [get](https://yandex.com/dev/direct/doc/ref-v5/bidmodifiers/get.html) | [set](https://yandex.com/dev/direct/doc/ref-v5/bidmodifiers/set.html) | [toggle](https://yandex.com/dev/direct/doc/ref-v5/bidmodifiers/toggle.html)
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#types)Types of adjustments
You can modify bids using the following types of adjustments:
  * MOBILE_ADJUSTMENT — Adjustment on mobile phones: a coefficient is applied to the bid when serving ads on smartphones.
  * TABLET_ADJUSTMENT — Adjustment on tablets: a coefficient is applied to the bid when serving ads on tablets.
  * DESKTOP_ADJUSTMENT — Adjustment on desktops and Smart TVs: a coefficient is applied to the bid when serving ads on all devices other than smartphones. You cannot use it together with TABLET_ADJUSTMENT and DESKTOPS_ONLY_ADJUSTMENT.
  * DESKTOP_ONLY_ADJUSTMENT — Adjustment desktops only: a coefficient is applied to the bid when serving ads on desktops only.
  * DEMOGRAPHICS_ADJUSTMENT — Adjustments by gender and age: a set of audience segments with specified demographic characteristics and bid coefficients that are applied when serving ads to users from each segment. The segments must not match or overlap within the same set of segments.
  * RETARGETING_ADJUSTMENT — Adjustments for a target audience: a set of retargeting lists and bid coefficients that are applied when serving ads to users who meet a condition. For more information about retargeting lists, see the section [Retargeting list (RetargetingList)](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list).
  * REGIONAL_ADJUSTMENT — Adjustments by display region: a set of regions and bid coefficients that are applied when serving ads in these areas.
  * VIDEO_ADJUSTMENT — Adjustment for video extensions: a bid coefficient that is applied when serving ads with video extensions.
  * SMART_AD_ADJUSTMENT — Adjustment for smart ads: a bid coefficient that is applied when serving ads with a single product offer.
  * SERP_LAYOUT_ADJUSTMENT — Adjustment for exclusive placement: a factor is applied to the bid if the ad gets an exclusive placement or a suggest placement.
  * INCOME_GRADE_ADJUSTMENT — An adjustment for income: a factor is applied to the bid when ads are served for users with a certain income level.
  * AD_GROUP_ADJUSTMENT — A group-level adjustment: a bid coefficient that is applied when serving ads from a certain group (applies only to unified performance groups).


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#levels)Adjustment levels
You can set bid adjustments for device type, gender and age, target audience, and video extensions either on the ad group level or on the campaign level.
Regional bid adjustments can only be set on the campaign level.
In display campaigns, adjustments can only be set on the group level.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#compatibility)Acceptable types of bid adjustments by type of campaign and group
The table below shows the types of bid adjustments you can configure for each type of ad campaign and ad group.
**Campaign type**  
**Group type** |  **Mobile** |  **Tablets** |  **Desktops, Smart TVs** |  **Desktops only** |  **Gender and age** |  **Target audience** |  **Display region** |  **Video extensions** |  **Smart ads** |  **Exclusive placement** |  **Income** |  **Group**  
---|---|---|---|---|---|---|---|---|---|---|---|---  
TEXT_CAMPAIGN  
TEXT_AD_GROUP |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
– |  +  
+ |  –  
– |  +  
+ |  +  
+ |  –  
–  
SMART_CAMPAIGN  
SMART_AD_GROUP |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
– |  –  
– |  +  
+ |  –  
– |  +  
+ |  –  
–  
MOBILE_APP_CAMPAIGN  
MOBILE_APP_AD_GROUP |  –  
– |  –  
– |  –  
– |  –  
– |  +  
+ |  +  
+ |  +  
– |  –  
– |  –  
– |  +  
+ |  +  
+ |  –  
–  
DYNAMIC_TEXT_CAMPAIGN  
DYNAMIC_TEXT_AD_GROUP |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
– |  –  
– |  –  
– |  +  
+ |  +  
+ |  –  
–  
CPM_BANNER_CAMPAIGN  
CPM_BANNER_AD_GROUP,  
subtype KEYWORDS  
CPM_BANNER_AD_GROUP,  
subtype USER_PROFILE  
CPM_VIDEO_AD_GROUP |  –  
+ + – |  –  
– – – |  –  
+ + – |  –  
– – – |  –  
+ – – |  –  
+ – – |  –  
– – – |  –  
– – – |  –  
– – – |  –  
– – – |  –  
– – – |  –  
– – –  
UNIFIED_CAMPAIGN  
UNIFIED_AD_GROUP |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
+ |  +  
– |  +  
+ |  –  
– |  +  
+ |  +  
+ |  –  
+  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#toggle)Disabling adjustments
You can enable or disable the bid adjustments for gender and age, target audience, and region.
This immediately enables or disables the entire set of the selected type of adjustments for a specific ad group, or for a specific campaign.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier#use)How adjustments are applied
  1. If a campaign has a manual bid management strategy set up, adjustments are applied to the bids set by the advertiser.
If a campaign has an automatic strategy set up, Yandex Direct applies the adjustments when managing bids. If strategy parameters specify the maximum bid, adjustments are also applied to this maximum. In other words, the system won't set a bid that is higher than the adjusted maximum bid. If the average CPC or CPA is specified, adjustments are not applied to it.
  2. If an ad group has at least one adjustment set (and this type of adjustment is not disabled), the same type of adjustments set for the campaign are not applied when displaying ads from this group.
  3. If a user is selected by multiple retargeting lists that have adjustments set for them, the largest coefficient is applied.
  4. If adjustments are set for a higher-level region and a lower-level (nested) region, ad displays in the lower-level region use the coefficient for the lower-level region.
  5. Multiple types of adjustments can be applied to a bid simultaneously. In this case, the coefficients are multiplied.
  6. After applying the coefficients, the bid cannot be less than the minimum value or more than the maximum value for the advertiser's currency.


### Was the article helpful?
YesNo
Previous
[Bid and priority (KeywordBid)](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority)
Next
[Portfolio strategy (Strategy)](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy)
