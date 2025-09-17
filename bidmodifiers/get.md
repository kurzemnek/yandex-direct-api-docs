---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/bidmodifiers/get
crawled_at: 2025-09-17T15:57:11.194876
---

Restrictions
# get
  * [Restrictions](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get#output)


Returns parameters of adjustments that match the specified criteria.
###  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get#see-also)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)
  * [Adjustments (BidModifier)](https://yandex.com/dev/direct/doc/dg/objects/bidmodifier.html)


##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
The total of the `Limit` and `Offset` values must not exceed 120,000 (if you don't specify the `Limit` value, make sure that the `Offset` value doesn't exceed 110,000).
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* BidModifiersSelectionCriteria */
      "CampaignIds": [(long), ... ],
      "AdGroupIds": [(long), ... ],
      "Ids": [(long), ... ],
      "Types": [( "MOBILE_ADJUSTMENT" | "TABLET_ADJUSTMENT" | "DESKTOP_ADJUSTMENT" | "DESKTOP_ONLY_ADJUSTMENT" | "DEMOGRAPHICS_ADJUSTMENT" | "RETARGETING_ADJUSTMENT" | "REGIONAL_ADJUSTMENT" | "VIDEO_ADJUSTMENT" | "SMART_AD_ADJUSTMENT" | "SERP_LAYOUT_ADJUSTMENT" | "INCOME_GRADE_ADJUSTMENT" | "AD_GROUP_ADJUSTMENT" ), ... ],
      "Levels": [( "CAMPAIGN" | "AD_GROUP" ), ... ] /* required */
    }, /* required */
    "FieldNames": [( "Id" | "CampaignId" | "AdGroupId" | "Level" | "Type" ), ... ], /* required */
    "MobileAdjustmentFieldNames": [( "BidModifier" | "OperatingSystemType" ), ... ],
    "TabletAdjustmentFieldNames": [( "BidModifier" | "OperatingSystemType" ), ... ],
    "DesktopAdjustmentFieldNames": [( "BidModifier" )],
    "DesktopOnlyAdjustmentFieldNames": [( "BidModifier" )],
    "DemographicsAdjustmentFieldNames": [( "Gender" | "Age" | "BidModifier" | "Enabled" ), ... ],
    "RetargetingAdjustmentFieldNames": [( "RetargetingConditionId" | "BidModifier" | "Accessible" | "Enabled" ), ... ],
    "RegionalAdjustmentFieldNames": [( "RegionId" | "BidModifier" | "Enabled" ), ... ],
    "VideoAdjustmentFieldNames": [( "BidModifier" )],
    "SmartAdAdjustmentFieldNames": [( "BidModifier" )],
    "SerpLayoutAdjustmentFieldNames": [( "SerpLayout" | "BidModifier" | "Enabled" ), ... ],
    "IncomeGradeAdjustmentFieldNames": [( "Grade" | "BidModifier" | "Enabled" ), ... ],
    "AdGroupAdjustmentFieldNames" : [ ("BidModifier") ],
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
`SelectionCriteria` |  BidModifiersSelectionCriteria |  Criteria for selecting adjustments. |  Yes  
`FieldNames` |  array of BidModifierFieldEnum |  Names of top-level parameters to get. |  Yes  
`MobileAdjustmentFieldNames` |  array of MobileAdjustmentFieldEnum |  Names of mobile adjustment parameters to get. |  No  
`TabletAdjustmentFieldNames` |  array of TabletAdjustmentFieldEnum |  Names of parameters to get for bid adjustments on tablets. |  No  
`DesktopAdjustmentFieldNames` |  array of DesktopAdjustmentFieldEnum |  Names of parameters to get for bid adjustments on desktops and Smart TVs. |  No  
`DesktopOnlyAdjustmentFieldNames` |  array of DesktopOnlyAdjustmentFieldEnum |  Names of parameters to get for bid adjustments only on desktops. |  No  
`DemographicsAdjustmentFieldNames` |  array of DemographicsAdjustmentFieldEnum |  Names of gender and age adjustment parameters to get. |  No  
`RetargetingAdjustmentFieldNames` |  array of RetargetingAdjustmentFieldEnum |  Names of parameters to get for adjustments for a target audience. |  No  
`RegionalAdjustmentFieldNames` |  array of RegionalAdjustmentFieldEnum |  Names of regional bid adjustment parameters to get. |  No  
`VideoAdjustmentFieldNames` |  array of VideoAdjustmentFieldEnum |  Names of parameters to get for video extension adjustments. |  No  
`SmartAdAdjustmentFieldNames` |  array of SmartAdAdjustmentFieldEnum |  Names of parameters to get for smart ad adjustments. |  No  
`SerpLayoutAdjustmentFieldNames` |  array of SerpLayoutAdjustmentFieldEnum |  Names of parameters to get for bid adjustments on exclusive placement. |  No  
`IncomeGradeAdjustmentFieldNames` |  array of IncomeGradeAdjustmentFieldEnum |  Names of parameters to get for bid adjustments on income. |  No  
`AdGroupAdjustmentFieldNames` |  array of AdGroupAdjustmentFieldEnum |  Names of requested parameters for group-level bid adjustments. |  No  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  No  
**BidModifiersSelectionCriteria**  
`CampaignIds` |  array of long |  Selects adjustments set for the specified campaigns and/or child groups. From 1 to 10 items in the array. |  At least one of the parameters: `CampaignIds`, `AdGroupIds`, or `Ids`  
`AdGroupIds` |  array of long |  Selects adjustments set for the specified groups. From 1 to 1000 items in the array.  
`Ids` |  array of long |  Selects adjustments with the specified IDs. From 1 to 10,000 items in the array.  
`Types` |  array of BidModifierTypeEnum |  Selects the specified types of adjustments. See [Types of adjustments](https://yandex.com/dev/direct/doc/dg/objects/bidmodifier.html#types). |  No  
`Levels` |  array of BidModifierLevelEnum |  Selects the specified levels of adjustments:
  * CAMPAIGN — Adjustments set for campaigns.
  * AD_GROUP — Adjustments set for ad groups.

|  Yes  
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "BidModifiers": [{  /* BidModifierGetItem */
      "CampaignId": (long),
      "AdGroupId": (long), /* nillable */
      "Id": (long),
      "Level": ( "CAMPAIGN" | "AD_GROUP" ),
      "Type": ( "MOBILE_ADJUSTMENT" | "TABLET_ADJUSTMENT" | "DESKTOP_ADJUSTMENT" | "DESKTOP_ONLY_ADJUSTMENT" | "DEMOGRAPHICS_ADJUSTMENT" | "RETARGETING_ADJUSTMENT" | "REGIONAL_ADJUSTMENT" | "VIDEO_ADJUSTMENT" | "SMART_AD_ADJUSTMENT" | "SERP_LAYOUT_ADJUSTMENT" | "INCOME_GRADE_ADJUSTMENT" | "AD_GROUP_ADJUSTMENT" ),
      "MobileAdjustment": {  /* MobileAdjustmentGet */
        "BidModifier": (int),
        "OperatingSystemType": ( "IOS" | "ANDROID" )
      },
      "TabletAdjustment": {  /* MobileAdjustmentGet */
        "BidModifier": (int), /* required */
        "OperatingSystemType": ( "IOS" | "ANDROID" )
      },
      "DesktopAdjustment": {  /* DesktopAdjustmentGet */
        "BidModifier": (int)
      },
      "DesktopOnlyAdjustment": {  /* DesktopAdjustmentGet */
        "BidModifier": (int) /* required */
      },
      "DemographicsAdjustment": {  /* DemographicsAdjustmentGet */
        "Gender": ( "GENDER_MALE" | "GENDER_FEMALE" ), /* nillable */
        "Age": ( "AGE_0_17" | "AGE_18_24" | "AGE_25_34" | "AGE_35_44" | "AGE_45" | "AGE_45_54" | "AGE_55" ), /* nillable */
        "BidModifier": (int),
        "Enabled": ( "YES" | "NO" )
      },
      "RetargetingAdjustment": {  /* RetargetingAdjustmentGet */
        "RetargetingConditionId": (long),
        "BidModifier": (int),
        "Accessible": ( "YES" | "NO" ),
        "Enabled": ( "YES" | "NO" )
      },
      "RegionalAdjustment": {  /* RegionalAdjustmentGet */
        "RegionId": (long),
        "BidModifier": (int),
        "Enabled": ("YES"|"NO")
      },
      "VideoAdjustment": {  /* VideoAdjustmentGet */
        "BidModifier": (int)
      },
      "SmartAdAdjustment" : { /* SmartAdAdjustmentGet */
        "BidModifier": (int)
      },
      "SerpLayoutAdjustment": {  /* SerpLayoutAdjustmentGet */
        "SerpLayout": ( "ALONE" | "SUGGEST" ),
        "BidModifier": (int),
        "Enabled": ( "YES" | "NO" )
      },
      "IncomeGradeAdjustment": {  /* IncomeGradeAdjustmentGet */
        "Grade": ( "VERY_HIGH" | "HIGH" | "ABOVE_AVERAGE" ),
        "BidModifier": (int),
        "Enabled": ( "YES" | "NO" )
      },
      "AdGroupAdjustment" : {
        "BidModifier" : (integer)
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`BidModifiers` |  array of BidModifierGetItem |  Bid adjustments.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
**BidModifierGetItem structure**  
`CampaignId` |  long |  ID of the campaign that the adjustment is set for, or the ID of the campaign that belongs to the ad group that the adjustment is set for.  
`AdGroupId` |  long, nillable |  ID of the ad group that the adjustment is set for.  
`Id` |  long |  Bid adjustment ID.  
`Level` |  BidModifierLevelEnum |  Level of the adjustment: set for a campaign, or for an ad group.  
`Type` |  BidModifierTypeEnum |  Type of bid adjustment.  
`MobileAdjustment` |  MobileAdjustmentGet |  Mobile adjustment parameters.  
`TabletAdjustment` |  TabletAdjustmentGet |  Parameters for bid adjustments on tablets.  
`DesktopAdjustment` |  DesktopAdjustmentGet |  Parameters for bid adjustments on desktops and Smart TVs.  
`DesktopOnlyAdjustment` |  DesktopOnlyAdjustmentGet |  Parameters for bid adjustments on desktops only.  
`VideoAdjustment` |  VideoAdjustmentGet |  Parameters for the bid adjustment for video extensions.  
`DemographicsAdjustment` |  DemographicsAdjustmentGet |  Parameters for the bid adjustment for gender and age.  
`RetargetingAdjustment` |  RetargetingAdjustmentGet |  Parameters for the bid adjustment for a target audience.  
`RegionalAdjustment` |  RegionalAdjustmentGet |  Parameters for the regional bid adjustment.  
`SmartAdAdjustment` |  SmartAdAdjustmentGet |  Parameters for the smart banner adjustment.  
`IncomeGradeAdjustment` |  IncomeGradeAdjustmentGet |  Parameters for the income adjustment.  
`SerpLayoutAdjustment` |  SerpLayoutAdjustmentGet |  Parameters for the exclusive placement adjustment.  
`AdGroupAdjustment` |  AdGroupAdjustmentGet |  Parameters for group-level bid adjustments.  
**MobileAdjustmentGet structure**  
`BidModifier` |  int |  Value of the bid coefficient for serving ads on mobile phones. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`.  
`OperatingSystemType` |  OperatingSystemTypeEnum |  The type of operating system. If this parameter is omitted, any operating system is acceptable.  
**TabletAdjustmentGet structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads on tablets. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`.  
`OperatingSystemType` |  OperatingSystemTypeEnum |  The type of operating system. If this parameter is omitted, any operating system is acceptable.  
**DesktopAdjustmentGet structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads on desktops and Smart TVs. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`. Within a single ad group, you can't set the coefficient to 0 for mobile phones without specifying the OS and simultaneously set it to 0 for computers, tablets, and Smart TVs.  
**DesktopOnlyAdjustmentGet structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads only on desktops. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`. Within a single ad group, you can't set the coefficient to 0 for mobile phones without specifying the OS and simultaneously set it to 0 for desktops.  
**DemographicsAdjustmentGet structure**  
`Gender` |  GenderEnum, nillable |  The user's gender: GENDER_MALE or GENDER_FEMALE. If the parameter is omitted, any gender is assumed.  
`Age` |  AgeRangeEnum, nillable |  The user's age group: one of the values AGE_0_17, AGE_18_24, AGE_25_34, AGE_35_44, AGE_45_54 or AGE_55. The value AGE_45 has been deprecated. We recommend creating separate adjustments for AGE_45_54 and AGE_55. If the parameter is omitted, any age is assumed.  
`BidModifier` |  int |  The value of the bid coefficient for displaying ads to users of the specified gender and/or age group. Indicated as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
`Enabled` |  YesNoEnum |  Whether the set of demographics adjustments is enabled or disabled.  
**RetargetingAdjustmentGet structure**  
`RetargetingConditionId` |  long |  ID of the retargeting list. The list must have the RETARGETING type. See the section [Retargeting list (RetargetingList)](https://yandex.com/dev/direct/doc/dg/objects/retargeting-list.html).  
`BidModifier` |  int |  The value of the bid coefficient for serving ads to users who match the retargeting list. Indicated as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
`Accessible` |  YesNoEnum |  Indicates that all goals and segments in the retargeting list are available to the advertiser. The value NO means that one or more goals or segments are not available.  
`Enabled` |  YesNoEnum |  Whether the set of target audience adjustments is enabled or disabled.  
**RegionalAdjustmentGet structure**  
`RegionId` |  long |  ID of the region from the reference list of regions. To get the list of regions, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/dictionaries/get) method.  
`BidModifier` |  int |  Value of the bid coefficient for displaying ads in the specified region. Indicated as a percentage from 10 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
`Enabled` |  YesNoEnum |  Whether the set of regional bid adjustments is enabled or disabled.  
**VideoAdjustmentGet structure**  
`BidModifier` |  int |  Value of the bid coefficient for serving ads with video extensions. Indicated as a percentage from 50 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
**SmartAdAdjustmentGet structure**  
`BidModifier` |  int |  Value of the bid coefficient for serving a smart ad with a single product offer. Indicated as a percentage from 20 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
**SerpLayoutAdjustmentGet structure**  
`SerpLayout` |  SerpLayoutEnum |  The ad display place:
  * ALONE — Exclusive placement.
  * SUGGEST — Ads in autofill suggestions.

  
`BidModifier` |  int |  Value of the bid coefficient for serving ads in the specified placement. It's specified as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
`Enabled` |  YesNoEnum |  Whether the set of adjustments for exclusive placement is enabled or disabled.  
**IncomeGradeAdjustmentGet structure**  
`Grade` |  IncomeGradeEnum |  Income level:
  * VERY_HIGH
  * HIGH
  * ABOVE_AVERAGE

  
`BidModifier` |  int |  Value of the bid coefficient for serving ads for users with a specific income level. It's specified as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
`Enabled` |  YesNoEnum |  A set of income adjustments is enabled or disabled.  
**AdGroupAdjustmentGet structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads from a specific group. It's specified as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`.  
Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete)
Next
[set](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/set)
