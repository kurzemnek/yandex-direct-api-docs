---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/audiencetargets/add
crawled_at: 2025-09-17T15:49:46.225110
---

Learn more
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#output)


Creates audience targets and sets bids and priorities for the created targets.
Alert
  * Bids and prices are passed via the Yandex Direct API as **integer numbers**. The passed value represents the bid or price **multiplied by 1,000,000**.
  * All bids and prices are shown in the advertiser's currency.


How bids and priorities are applied
The bid or priority is used depending on which display strategy is selected in the campaign:
  * If you've set a manual strategy for your campaign, the `ContextBid` parameter is used.
  * If your campaign has an automatic strategy, the `StrategyPriority` parameter is used: ads targeting audiences with higher priority get more traffic if possible, and are paused last when the budget runs low.


If there **isn't a parameter appropriate to the strategy** , the default value is preserved.
  * If the strategy is manual but the bid isn't specified, the minimum bid is set by default (it depends on the advertiser's currency).
  * If the strategy is automatic but the priority isn't specified, the average priority is set by default.


If **a parameter is specified that isn't appropriate for the strategy** , its value is saved.
  * If the strategy is manual but the priority is specified, this priority value will be applied later when the strategy is switched to an automatic one.
  * If the strategy is automatic but a bid is specified, this bid value **will not be applied** : if the strategy switches from automatic to manual, the bid will be set according to an automatic algorithm.


##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#learn-more)Learn more
  * [Audience targets (AudienceTarget)](https://yandex.com/dev/direct/doc/dg/objects/audience-target.html)


##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#restrictions)Restrictions
Maximum of 1000 audience targets per method call.
For other restrictions, see the section [Restrictions](https://yandex.com/dev/direct/doc/dg/objects/audience-target.html#restrictions).
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "AudienceTargets": [{  /* AudienceTargetAddItem */
      "AdGroupId": (long), /* required */
      "RetargetingListId": (long),
      "InterestId": (long),
      "ContextBid": (long),
      "StrategyPriority": ( "LOW" | "NORMAL" | "HIGH" )
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`AudienceTargets` |  array of AudienceTargetAddItem |  Audience targets to add. |  Yes  
**AudienceTargetAddItem structure**  
`AdGroupId` |  long |  ID of the group to add the audience target to. |  Yes  
`RetargetingListId` |  long |  ID of the retargeting list. The scope of the retargeting list must match the type of ad group. See [Scope](https://yandex.com/dev/direct/doc/dg/objects/retargeting-list.html#type). The ID must be unique within the ad group: you can't have two audience targets with identical retargeting list IDs. |  Use either `RetargetingListId` or `InterestId`  
`InterestId` |  long |  ID of an app category interest. To get the list of app categories, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/audiencetargets/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/audiencetargets/en/dictionaries/get) method and specify the dictionary name `Interests` in the request. You can only use interests that have the `IsTargetable` parameter set to YES in the dictionary. This parameter can only be used with the MOBILE_APP_AD_GROUP type of ad group. The ID must be unique within the ad group (you can't have two audience targets with identical interest IDs).  
`ContextBid` |  long |  The bid in ad networks, multiplied by 1,000,000. Integer. Only used for a manual strategy. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the `Currencies` dictionary name in the request. Copied The default value is the minimum bid. Alert An image ad can be displayed only if the bid is at least as high as the minimum bid for an ad with an image. |  No  
`StrategyPriority` |  PriorityEnum |  The priority of the audience target: LOW, NORMAL or HIGH. Only used for an automatic strategy. The default value is NORMAL. |  No  
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/add#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AddResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ]
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / AddResponse structure (for SOAP)**  
`AddResults` |  array of ActionResult |  Results of adding audience targets.  
**ActionResult structure**  
`Id` |  long |  The ID of a created audience target. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[AudienceTargets: managing audience targets](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/audiencetargets)
Next
[delete](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/delete)
