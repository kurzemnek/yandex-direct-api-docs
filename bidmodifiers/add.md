---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/bidmodifiers/add
crawled_at: 2025-09-17T15:57:01.030375
---

Restrictions
# add
  * [Restrictions](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#samples)


Creates bid adjustments.
###  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#see-also)Learn more
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#restrictions)Restrictions
Maximum of 1 mobile adjustment per campaign or ad group.
Maximum of 1 video extension adjustment per campaign or ad group.
Maximum of 12 gender and age adjustments per campaign or ad group.
Maximum of 100 target audience adjustments per campaign or ad group.
Mobile adjustments can't be created for campaigns and ad groups for mobile app advertising.
You can create adjustments for computers, tablets, and Smart TVs only for groups of Text & Image and display ads.
Video extension adjustments can only be created for campaigns and groups of Text & Image ads.
Group-level adjustments can only be created for unified performance groups.
To learn more about matching the types of bid adjustments to the types of campaigns and ad groups, see 
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "BidModifiers": [{  /* BidModifierAddItem */
      "MobileAdjustment": {  /* MobileAdjustmentAdd */
        "BidModifier": (int), /* required */
        "OperatingSystemType": ( "IOS" | "ANDROID" )
      },
      "TabletAdjustment": {  /* MobileAdjustmentAdd */
        "BidModifier": (int), /* required */
        "OperatingSystemType": ( "IOS" | "ANDROID" )
      },
      "DesktopAdjustment": {  /* DesktopAdjustmentAdd */
        "BidModifier": (int) /* required */
      },
      "DesktopOnlyAdjustment": {  /* DesktopAdjustmentAdd */
        "BidModifier": (int) /* required */
      },
      "DemographicsAdjustments": [{  /* DemographicsAdjustmentAdd */
        "Gender": ( "GENDER_MALE" | "GENDER_FEMALE" ),
        "Age": ( "AGE_0_17" | "AGE_18_24" | "AGE_25_34" | "AGE_35_44" | "AGE_45" | "AGE_45_54" | "AGE_55" ),
        "BidModifier": (int) /* required */
      }, ... ],
      "RetargetingAdjustments": [{  /* RetargetingAdjustmentAdd */
        "RetargetingConditionId": (long), /* required */
        "BidModifier": (int) /* required */
      }, ... ],
      "RegionalAdjustments": [{    /* RegionalAdjustmentAdd */
        "RegionId": (long), /* required */
        "BidModifier": (int) /* required */
      }, ... ],
      "VideoAdjustment": { /* VideoAdjustmentAdd */
        "BidModifier": (int) /* required */
      },
      "SmartAdAdjustment" : { /* SmartAdAdjustmentAdd */
        "BidModifier": (int) /* required */
      },
      "SerpLayoutAdjustments": [{  /* SerpLayoutAdjustmentAdd */
        "SerpLayout": ( "ALONE" | "SUGGEST" ), /* required */
        "BidModifier": (int) /* required */
      }, ... ],
      "IncomeGradeAdjustments": [{  /* IncomeGradeAdjustmentAdd */
        "Grade": ( "VERY_HIGH" | "HIGH" | "ABOVE_AVERAGE" ), /* required */
        "BidModifier": (int) /* required */
      }, ... ],
      "AdGroupAdjustment" : {
        "BidModifier" : (int) /* required */
      }
      "CampaignId": (long),
      "AdGroupId": (long)
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`BidModifiers` |  array of BidModifierAddItem |  Adjustments to add. Maximum of 1000 items in the array. |  Yes  
**BidModifierAddItem structure**  
`CampaignId` |  long |  The campaign ID. Specified when creating bid adjustments at the campaign level. |  Use either `CampaignId` or `AdGroupId`  
`AdGroupId` |  long |  ID of the ad group. Specified when creating bid adjustments at the group level.  
`MobileAdjustment` |  MobileAdjustmentAdd |  Adjustment on mobile phones. |  Use either `MobileAdjustment` or `TabletAdjustment` or `DesktopAdjustment` or `DesktopOnlyAdjustment` or `DemographicsAdjustments` or `RetargetingAdjustments` or `RegionalAdjustments` or `VideoAdjustment` or `SmartAdAdjustment` or `SerpLayoutAdjustments` or `IncomeGradeAdjustments` or `AdGroupAdjustment`.  
`TabletAdjustment` |  TabletAdjustmentAdd |  Adjustment on tablets.  
`DesktopAdjustment` |  DesktopAdjustmentAdd |  Adjustment on desktops and Smart TVs.  
`DesktopOnlyAdjustment` |  DesktopOnlyAdjustmentAdd |  Adjustment only on desktops.  
`DemographicsAdjustments` |  array of DemographicsAdjustmentAdd |  Adjustments for gender and age. Maximum of 12 items in the array.  
`RetargetingAdjustments` |  array of RetargetingAdjustmentAdd |  Adjustments for the target audience. Maximum of 100 items in the array.  
`RegionalAdjustments` |  array of RegionalAdjustmentAdd |  Adjustments by region.  
`VideoAdjustment` |  VideoAdjustmentAdd |  Adjustment for video extensions.  
`SmartAdAdjustment` |  SmartAdAdjustmentAdd |  Bid adjustment for smart ads.  
`SerpLayoutAdjustments` |  array of SerpLayoutAdjustmentAdd |  Adjustments for exclusive placement.  
`IncomeGradeAdjustments` |  array of IncomeGradeAdjustmentAdd |  Adjustments for income.  
`AdGroupAdjustment` |  array of AdGroupAdjustmentAdd |  Group-level adjustments.  
**MobileAdjustmentAdd structure**  
`BidModifier` |  int |  Value of the bid coefficient for serving ads on mobile phones. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`. |  Yes  
`OperatingSystemType` |  OperatingSystemTypeEnum |  The type of operating system. If this parameter is omitted, any operating system is acceptable. |  No  
**TabletAdjustmentAdd structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads on tablets. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`. |  Yes  
`OperatingSystemType` |  OperatingSystemTypeEnum |  The type of operating system. If this parameter is omitted, any operating system is acceptable. |  No  
**DesktopAdjustmentAdd structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads on desktops and Smart TVs. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`. Within a single ad group, you can't set the coefficient to 0 for mobile phones without specifying the OS and simultaneously set it to 0 for computers, tablets, and Smart TVs. |  Yes  
**DesktopOnlyAdjustmentAdd structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads only on desktops. Specified as a percentage:
  * From 0 to 1300 for bid adjustments in all types of campaigns and ad groups.

The bid is multiplied by the value of `BidModifier/100`. Within a single ad group, you can't set the coefficient to 0 for mobile phones without specifying the OS and simultaneously set it to 0 for desktops. |  Yes  
**DemographicsAdjustmentAdd structure**  
`Gender` |  GenderEnum |  The user's gender: GENDER_MALE or GENDER_FEMALE. If you don't specify this parameter, any gender is valid (in this case, please specify the `Age` parameter). |  At least one of the parameters: `Gender` or `Age`.  
`Age` |  AgeRangeEnum |  The user's age group: one of the values AGE_0_17, AGE_18_24, AGE_25_34, AGE_35_44, AGE_45_54 or AGE_55. The value AGE_45 has been deprecated. We recommend creating separate adjustments for AGE_45_54 and AGE_55. If you don't specify this parameter, any age is valid (in this case, please specify the `Gender` parameter). Alert The audience segments that have bid adjustments set for them must not coincide with each other or overlap. For example, you can't set simultaneous adjustments for the AGE_25_34 and the GENDER_MALE+AGE_25_34 groups. |   
`BidModifier` |  int |  The value of the bid coefficient for displaying ads to users of the specified gender and/or age group. Indicated as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
**RetargetingAdjustmentAdd structure**  
`RetargetingConditionId` |  long |  ID of the retargeting list. The list must have the RETARGETING type. See the section  |  Yes  
`BidModifier` |  int |  The value of the bid coefficient for serving ads to users who match the retargeting list. Indicated as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
**RegionalAdjustmentAdd structure**  
`RegionId` |  long |  ID of the region from the reference list of regions. To get the list of regions, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/dictionaries/get) method. |  Yes  
`BidModifier` |  int |  Value of the bid coefficient for displaying ads in the specified region. Indicated as a percentage from 10 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
**VideoAdjustmentAdd structure**  
`BidModifier` |  int |  Value of the bid coefficient for serving ads with video extensions. Indicated as a percentage from 50 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
**SmartAdAdjustmentAdd structure**  
`BidModifier` |  int |  Value of the bid coefficient for serving a smart ad with a single product offer. Indicated as a percentage from 20 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
**SerpLayoutAdjustmentAdd structure**  
`SerpLayout` |  SerpLayoutEnum |  The ad display place:
  * ALONE — Exclusive placement.
  * SUGGEST — Ads in autofill suggestions.

|  Yes  
`BidModifier` |  int |  Value of the bid coefficient for serving ads in the specified placement. It's specified as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
**IncomeGradeAdjustmentAdd structure**  
`Grade` |  IncomeGradeEnum |  Income level:
  * VERY_HIGH
  * HIGH
  * ABOVE_AVERAGE

|  Yes  
`BidModifier` |  int |  Value of the bid coefficient for serving ads for users with a specific income level. It's specified as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
**AdGroupAdjustmentAdd structure**  
`BidModifier` |  int |  The value of the bid coefficient for serving ads from a specific group. It's specified as a percentage from 0 to 1300. The bid is multiplied by the value of `BidModifier/100`. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#output)Response
Alert
  * Adding adjustments for gender and age for the same campaign or ad group is considered a single operation. If one of the coefficients has an error, none of them are created.
  * Adding target audience adjustments for the same campaign or ad group is considered a single operation. If one of the coefficients has an error, none of them are created.
  * Adding regional bid adjustments for the same campaign is considered a single operation. If one of the coefficients has an error, none of them are created.


Response structure in JSON format:
```
{
  "result": { /* result */
    "AddResults": [{  /* MultiIdsActionResult */
      "Ids": [(long), ... ],
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
`AddResults` |  array of MultiIdsActionResult |  Results of adding bid adjustments.  
**MultiIdsActionResult structure**  
`Ids` |  array of long |  IDs of the created adjustments. Returned if there aren't any errors. See the section   
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/add#samples)Examples
**Request example**
```
    {
      "method": "add",
      "params": {
        "BidModifiers": [
          { // 1. Две корректировки по полу и возрасту
            "CampaignId": 10001,
            "DemographicsAdjustments": [
              {
                "Gender": "GENDER_MALE",
                "Age": "AGE_25_34",
                "BidModifier": 101
              },
              {
                "Age": "AGE_45_54",
                "BidModifier": 140
              }
            ]
          },
          { // 2. Корректировки с пересекающимися срезами аудитории
            "CampaignId": 10002,
            "DemographicsAdjustments": [
              {
                "Gender": "GENDER_MALE",
                "Age": "AGE_25_34",
                "BidModifier": 120
              },
              {
                "Age": "AGE_25_34",
                "BidModifier": 170
              }
            ]
          },
          { // 3. Недопустимое значение коэффициента
            "CampaignId": 10003,
            "DemographicsAdjustments": [
              {
                "Gender": "GENDER_MALE",
                "Age": "AGE_25_34",
                "BidModifier": 120
              },
              {
                "Gender": "GENDER_FEMALE",
                "Age": "AGE_35_44",
                "BidModifier": 10000
              }
            ]
          },
          { // 4. Корректировка для целевой аудитории на уровне группы объявлений
            "AdGroupId": 500001,
            "RetargetingAdjustments": [
              {
                "RetargetingConditionId": 2004,
                "BidModifier": 201
              }
            ]
          }
        ]
      }
    }

```

**Response example**
```
    {
      "result" : {
        "AddResults" : [
          { // 1. Созданы две корректировки по полу и возрасту
            "Ids": [ 1003, 1004 ]
          },
          { // 2. Пересекающиеся срезы - ни одна корректировка не создана
            "Errors": [
              {
                "Code": 6000,
                "Message": "Неконсистентное состояние объекта",
                "Details": "Пересекаются условия корректировок в наборе"
              }
            ]
          },
          { // 3. Недопустимое значение - ни одна корректировка не создана
            "Errors": [
              {
                "Code": 5005,
                "Message": "Поле задано неверно",
                "Details": "Значение коэффициента не может быть больше 1300"
              }
            ]
          },
          { // 4. Создана корректировка для целевой аудитории на уровне группы объявлений
            "Ids": [ 1005 ]
          }
        ]
      }
    }

```

Copied
### Was the article helpful?
YesNo
Previous
[BidModifiers: managing bid adjustments](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/bidmodifiers)
Next
[delete](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/delete)
