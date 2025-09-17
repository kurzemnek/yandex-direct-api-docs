---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/audiencetargets/get
crawled_at: 2025-09-17T15:50:05.336239
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#output)


Returns the parameters of audience targets.
You can get bids and priorities regardless of whether a manual or automatic strategy is selected in the campaign.
Alert
All returned monetary values are integers — the result of multiplying the bid by 1,000,000.
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#learn-more)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* AudienceTargetSelectionCriteria */
      "Ids": [(long), ... ],
      "AdGroupIds": [(long), ... ],
      "CampaignIds": [(long), ... ],
      "RetargetingListIds": [(long), ... ],
      "InterestIds": [(long), ... ],
      "States": [( "ON" | "SUSPENDED" ), ... ]
    }, /* required */
    "FieldNames": [( "Id" | "AdGroupId" | "CampaignId" | "RetargetingListId" | "InterestId" | "ContextBid" | "StrategyPriority" | "State" ), ... ], /* required */
    "Page": {  /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)**  
`SelectionCriteria` |  AudienceTargetSelectionCriteria |  Criteria for selecting audience targets. |  Yes  
`FieldNames` |  array of AudienceTargetFieldEnum |  The names of parameters to get. |  Yes  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page) of data. |  No  
**AudienceTargetSelectionCriteria structure**  
`Ids` |  array of long |  Selects audience targets with the specified IDs. From 1 to 10,000 items in the array. |  At least one of the parameters: `Ids`, `AdGroupIds`, `CampaignIds`, `RetargetingListIds`, or `InterestIds` (all may be present)  
`AdGroupIds` |  array of long |  Selects audience targets in the specified ad groups. From 1 to 1000 items in the array.  
`CampaignIds` |  array of long |  Selects audience targets in the specified campaigns. From 1 to 100 items in the array.  
`RetargetingListIds` |  array of long |  Selects audience targets with the specified retargeting lists. From 1 to 1000 items in the array.  
`InterestIds` |  array of long |  Selects audience targets with the specified interests. From 1 to 1000 items in the array.  
`States` |  array of AudienceTargetStateEnum |  Selects audience targets with the specified states. See [State of an audience target](https://yandex.com/dev/direct/doc/dg/objects/audience-target.html#state). |  No  
##  [](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AudienceTargets": [{  /* AudienceTargetGetItem */
      "Id": (long),
      "AdGroupId": (long),
      "CampaignId": (long),
      "RetargetingListId": (long),  /* nillable */
      "InterestId": (long),  /* nillable */
      "State": ( "ON" | "SUSPENDED" | "UNKNOWN" ),
      "ContextBid": (long),
      "StrategyPriority": ( "LOW" | "NORMAL" | "HIGH" )
   }, ... ],
   "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`AudienceTargets` |  array of AudienceTargetGetItem |  Audience targets.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page).  
**AudienceTargetGetItem structure**  
`Id` |  long |  ID of the audience target.  
`AdGroupId` |  long |  ID of the ad group that the audience target belongs to.  
`CampaignId` |  long |  ID of the campaign that the audience target belongs to.  
`RetargetingListId` |  long, nillable |  ID of the retargeting list.  
`InterestId` |  long, nillable |  ID of an app category interest.  
`ContextBid` |  long |  The bid in ad networks, multiplied by 1,000,000.  
`StrategyPriority` |  PriorityEnum |  Priority: LOW, NORMAL or HIGH.  
`State` |  StateEnum |  State of an audience target. See [State of an audience target](https://yandex.com/dev/direct/doc/dg/objects/audience-target.html#state).  
Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/delete)
Next
[resume](https://yandex.com/dev/direct/doc/en/audiencetargets/en/audiencetargets/resume)
