---
title: Retargeting list (RetargetingList) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/retargeting-list
crawled_at: 2025-09-17T15:53:55.266422
---

Servicing
# Retargeting list (RetargetingList)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#restrictions)
  * [Goals and segments](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#goals)
  * [Type of retargeting lists](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#types)
  * [Rules for user selection](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#rules)
  * [Scope](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#type)
    * [Learn more](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#learn-more)


A retargeting list defines the criteria for selecting users. Retargeting lists are used in audience targets (see the section [Audience targets (AudienceTarget)](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target)) and in bid adjustments (see the section [Bid adjustments (BidModifier)](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier)).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#service)Servicing
Use the [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html) service for managing retargeting lists.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#methods)Methods
[add](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/add.html) | [update](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/update.html) | [delete](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/delete.html) | [get](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/get.html)
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#restrictions)Restrictions
Maximum of 2,000 retargeting lists per advertiser.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#goals)Goals and segments
To set up a retargeting list, you can use:
  * Goals and segments configured in Yandex Metrica: see the section [What are goals? Types of goals](https://yandex.com/support/metrika/general/goals.html) and [Data segmentation](https://yandex.com/support/metrika/general/segmentation.html) in Yandex.Metrica Help, and [Retargeting & Audiences](https://yandex.com/support/direct/impression-criteria/retargeting-lists.html) in Yandex Direct Help.
  * Segments configured in Yandex Audience: see the Yandex Audience [Help](https://yandex.com/support/audience/).
  * Segments based on [Crypta](https://yandex.com/company/technologies/crypta/) data (demographic and behavior-based segments along with user interest segments): see the section [User profile](https://yandex.com/support/direct/products-cpm-campaign/display-ads-settings.html) in the Help for Yandex Direct.


To get a list of available Yandex.Metrica goals, Yandex.Metrica segments, and Yandex.Audience segments, use the [GetRetargetingGoals (Live)](https://yandex.com/dev/direct/doc/dg-v4/live/GetRetargetingGoals.html) method in the Live 4 version of the API.
To get a list of segments based on Crypta data, use the [Dictionaries](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/dictionaries.html).[get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method:
  * To get the list of demographic and behavior-based segments, specify the `AudienceDemographicProfiles` list name in the request. To get the list of demographic and behavioral characteristics, specify `AudienceCriteriaTypes`.
  * To get the list of user interest segments, specify the `AudienceInterests` list name in the request.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#types)Type of retargeting lists
The type of a retargeting list is set when creating it and can't be changed.
The following types of retargeting lists are currently available:
  * RETARGETING — A retargeting list can contain Yandex Metrica goals, Yandex Metrica segments, and Yandex Audience segments. It can be used in “Text & Image Ads” and “Ads for Mobile Apps” campaigns.
  * AUDIENCE — A retargeting list may contain any types of goals and segments. It can be used in display campaigns. A retargeting list that only contains a selection rule based on short-term interest segments can also be used in “Text & Image Ads” campaigns.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#rules)Rules for user selection
A retargeting list contains rules for user selection (the `Rules` array) that are combined using the AND principle, meaning the retargeting list applies to users who meet all of the rules.
Each selection rule contains a list of goals or segments (the `Arguments` array) and the logical operator (the `Operator` parameter):
  * ALL — The rule is met if the user completed all the goals and is included in all the segments.
  * ANY — The rule is met if the user completed at least one of the goals or the user's session is included in at least one of the segments.
  * NONE — The rule is met if the user didn't complete any of the goals and the user's session isn't included in any of the segments.


For retargeting lists of the RETARGETING type
For retargeting lists of the AUDIENCE type
**Restrictions**
For retargeting lists of the RETARGETING type
For retargeting lists of the AUDIENCE type
  * Retargeting lists can contain from 1 to 50 selection rules based on Yandex Metrica goals, Yandex Metrica segments, and Yandex Audience segments.
  * A selection rule may contain from 1 to 250 goals or segments.


  * A retargeting list must contain at least one rule with the logical operator ALL or ANY.
  * Each selection rule may contain either Yandex Metrica goals, Yandex Metrica segments, and Yandex Audience segments, or demographic segments, or behavior-based segments, or user interest segments.
  * For selection rules based on demographic or behavior-based segments:
    * Each selection rule can only contain segments based on a single characteristic or a single behavior (the _Type_ field returned by the [Dictionaries](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/dictionaries.html).[get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method in the _AudienceDemographicProfiles_ and _AudienceCriteriaTypes_ lists). For example, only segments by revenue.
    * Retargeting lists may contain no more than one selection rule for each demographic characteristic or behavior. For example, no more than one revenue-based selection rule.
    * For some characteristics and behaviors, you can't specify all the segments (the _Rule_ field in the _AudienceCriteriaTypes_ list). For example, the age-based selection rule should not contain all age groups.
    * Only the ANY operator can be used in a selection rule based on a demographic characteristic or behavior.
  * For selection rules based on interest segments:
    * Retargeting lists may include no more than three selection rules based on interest segments.
    * A selection rule may contain no more than 10 interests.
    * An interest-based selection rule can only contain segments with the same interest duration (the _InterestType_ field returned by the [Dictionaries](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/dictionaries.html).[get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method in the _AudienceInterests_ list). For example, only short-term interests.
    * Only the ANY operator can be used in an interest-based selection rule.
  * For selection rules based on goals and segments from Yandex Metrica and Yandex Audience segments:
    * Retargeting lists can contain from 1 to 50 selection rules based on Yandex Metrica goals, Yandex Metrica segments, and Yandex Audience segments.
    * A selection rule may contain from 1 to 250 goals or segments.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#type)Scope
The scope of the retargeting list depends on its type and which kinds of selection rules it has.
The `AvailableForTargetsInAdGroupTypes` and `Scope`parameters returned by the [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html).[get](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/get.html) method describe the scope of the retargeting list:
  * The `AvailableForTargetsInAdGroupTypes` parameter defines the types of groups that can have an audience target added for the specified retargeting list.
  * The `Scope` parameter defines where the retargeting list can be used: only in audience targets, only in bid adjustments, or everywhere.


For retargeting lists of the RETARGETING type
For retargeting lists of the AUDIENCE type
  * If a retargeting list of the RETARGETING type contains at least one rule with the ALL or ANY operator, it can be applied both in bid adjustments and in audience targets.
The `Scope` parameter contains the value FOR_TARGETS_AND_ADJUSTMENTS, and the `AvailableForTargetsInAdGroupTypes` parameter contains the TEXT_AD_GROUP and MOBILE_APP_AD_GROUP values.
  * If a retargeting list consists exclusively of rules with the NONE operator, it can only be used in bid adjustments.
The `Scope` parameter is used for returning the FOR_ADJUSTMENTS_ONLY value, and `AvailableForTargetsInAdGroupTypes` is null (nil).


Alert
  * If you modify a retargeting list that contains at least one rule with the ALL or ANY operator, it still must contain at least one rule with the ALL or ANY operator after your changes.
  * If you modify a retargeting list that consists exclusively of rules with the NONE operator, it must still contain only rules with the NONE operator after your changes.


Otherwise, the edit operation isn't performed, and an error is returned.
Retargeting lists with the AUDIENCE type are only used in audience targets: in the `Scope` parameter always returns FOR_TARGETS_ONLY.
If the retargeting list consists only of a selection rule based on short-term interest segments, the `AvailableForTargetsInAdGroupTypes` parameter has the values TEXT_AD_GROUP, CPM_BANNER_AD_GROUP, and CPM_VIDEO_AD_GROUP. In all other cases, only CPM_BANNER_AD_GROUP and CPM_VIDEO_AD_GROUP.
Alert
  * You can't add audience targeting criteria to CPM_BANNER_AD_GROUP ad groups with the KEYWORDS subtype.
  * Image Ad group, it must still contain only short-term interests after editing.


###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list#learn-more)Learn more
  * [Audience targets (AudienceTarget)](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target)


ID of a demographic or behavioral characteristic (the [TypeId](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html#output__AudienceCriteriaTypesItem-Type) parameter in the AudienceCriteriaTypes structure).
Segments based on demographic and behavioral characteristics for targeting by user profile.
Demographic and behavioral characteristics.
Whether all segments for this characteristic can be specified in a user selection rule (for example, you aren't allowed to specify all age groups, but you can specify all professions).
Type of interest: short-term, long-term, or for any period.
Segments based on user interests for targeting by user profile.
Copied
### Was the article helpful?
YesNo
Previous
[Audience targets (AudienceTarget)](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target)
Next
[Feed (Feed)](https://yandex.com/dev/direct/doc/en/objects/en/objects/feed)
