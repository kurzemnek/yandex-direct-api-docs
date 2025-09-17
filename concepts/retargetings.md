---
title: Parameters of retargetings and retargeting conditions | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/retargetings
crawled_at: 2025-09-17T16:01:55.508152
---

Parameters of retargetings
# Parameters of retargetings and retargeting conditions
  * [Parameters of retargetings](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/retargetings#parameters-of-retargetings)
  * [Parameters of retargeting conditions](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/retargetings#parameters-of-retargeting-conditions)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/retargetings#parameters-of-retargetings)Parameters of retargetings
**Parameter name in version Live 4** |  **Parameter name in version 5** |  **Service in version 5**  
---|---|---  
`RetargetingID` |  `Id` |  [AudienceTargets](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/audiencetargets.html)  
`AdID` |  No longer relevant |  —  
`AdGroupID` |  `AdGroupId` |  [AudienceTargets](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/audiencetargets.html)  
`RetargetingConditionID` |  `RetargetingListId` |  [AudienceTargets](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/audiencetargets.html)  
`ContextPrice` |  `ContextPrice` |  [AudienceTargets](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/audiencetargets.html)  
`Currency` |  Not supported. Bids are always indicated in the advertiser's currency. |  —  
`AutoBudgetPriority` |  `StrategyPriority` |  [AudienceTargets](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/audiencetargets.html)  
`StatusPaused` |  `State` |  [AudienceTargets](https://yandex.com/dev/direct/doc/ref-v5/audiencetargets/audiencetargets.html)  
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/retargetings#parameters-of-retargeting-conditions)Parameters of retargeting conditions
**Parameter name in version Live 4** |  **Parameter name in version 5** |  **Service in version 5**  
---|---|---  
`RetargetingConditionID` |  `Id` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`RetargetingConditionName` |  `Name` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`RetargetingConditionDescription` |  `Description` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`Login` |  HTTP header of the `Client-Login request` |  —  
`IsAccessible` |  `IsAvailable` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`RetargetingCondition` |  `Rules` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`Type` |  `Operator` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`Goals` |  `Arguments` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`Time` |  `MembershipLifeSpan` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
`GoalID` |  `ExternalId` |  [RetargetingLists](https://yandex.com/dev/direct/doc/ref-v5/retargetinglists/retargetinglists.html)  
Copied
### Was the article helpful?
YesNo
Previous
[Statistics](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/stat)
Next
[Parameters of clients](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/clients)
