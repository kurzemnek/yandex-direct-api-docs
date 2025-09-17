---
title: Audience targets (AudienceTarget) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/audience-target
crawled_at: 2025-09-17T15:55:37.635412
---

Targeting by retargeting list
# Audience targets (AudienceTarget)
  * [Targeting by retargeting list](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#retargeting-list)
  * [Targeting by app category](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#interest)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#restrictions)
    * [Targeting by retargeting list](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#restrictions-retarget-list)
    * [Targeting by mobile app categories](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#restrictions-mobile-app-cats)
  * [State of an audience target](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#state)
    * [Learn more](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#learn-more)


Audience targets allow you to display ads to users who meet the specified criteria. Audience targets link an ad group to either a retargeting list or audience interest in a mobile app category. You can set a bid and/or priority for an audience target.
Alert
Displays for audience targets are only available in ad networks (the Yandex Advertising Network and external networks).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#retargeting-list)Targeting by retargeting list
Ads can be shown to users who meet the criteria in a retargeting list. To do this, the audience target should specify the ad group (`AdGroupId`) and the retargeting list (`RetargetingListId`).
You can use the same retargeting list in multiple audience targets that are assigned to different groups of ads.
![retargeting](https://yandex.com/dev/direct/doc/en/objects/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_images/retargeting.png)
For more information about retargeting lists, see the section [Retargeting list (RetargetingList)](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#interest)Targeting by app category
Targeting by audience interests is only available for mobile app ads.
Ads can be shown to users who are interested in a specific category of mobile apps. To do this, the audience target should specify the ad group (`AdGroupId`) and the interest (`InterestId`).
To get the list of app categories, use the [Dictionaries](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/dictionaries.html).[get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method and specify the dictionary name `Interests` in the request.
For more information about targeting ads by audience interests, see [Targeting by mobile app interests](https://yandex.com/support/direct/mobile/interest-targeting.html) in Yandex Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#service)Servicing
Use the [AudienceTargets](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/audiencetargets.html) service for managing audience targets.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#methods)Methods
[add](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/add.html) | [delete](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/delete.html) | [suspend](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/suspend.html) | [resume](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/resume.html) | [get](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/get.html) | [setBids](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/setBids.html)
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#restrictions)Restrictions
Maximum of 50 audience targets in the TEXT_AD_GROUP and MOBILE_APP_AD_GROUP types of ad groups.
Maximum of 1 audience targeting criteria with the AUDIENCE type in a TEXT_AD_GROUP type of ad group.
Maximum of one audience target in an ad group with the CPM_BANNER_AD_GROUP type and USER_PROFILE subtype.
Maximum of one audience target in an ad group with the CPM_VIDEO_AD_GROUP type.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#restrictions-retarget-list)Targeting by retargeting list
Audience targeting criteria based on retargeting criteria can be added to the types of ad groups that are specified in the `AvailableForTargetsInAdGroupTypes` parameter for retargeting.
You can't add audience targeting criteria to CPM_BANNER_AD_GROUP ad groups with the KEYWORDS subtype.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#restrictions-mobile-app-cats)Targeting by mobile app categories
Audience targets by interests (mobile app categories) can only be added to an ad group with the MOBILE_APP_AD_GROUP type.
You can only use interests that have the `IsTargetable` parameter set to YES in the reference list.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#state)State of an audience target
The `State` parameter reflects the current state of displays for the audience target.
**State** |  **Description**  
---|---  
ON |  Ads can be served for an audience target.  
SUSPENDED |  Ad serving for the audience target was stopped by the owner (using the [suspend](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/suspend.html) method, or in the web interface).  
UNKNOWN |  Unknown state. Used for providing backward compatibility and displaying states that are not supported in this version of the API.  
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target#learn-more)Learn more
  * [Retargeting list (RetargetingList)](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list)


Copied
### Was the article helpful?
YesNo
Previous
[Portfolio strategy (Strategy)](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy)
Next
[Retargeting list (RetargetingList)](https://yandex.com/dev/direct/doc/en/objects/en/objects/retargeting-list)
