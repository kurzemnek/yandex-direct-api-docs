---
title: toggle | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/bidmodifiers/toggle
crawled_at: 2025-09-17T15:57:20.627247
---

Request
# toggle
  * [Request](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/toggle#input)
  * [Response](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/toggle#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/toggle#samples)


Enables or disables a set of adjustments.
###  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/toggle#see-also)Learn more
  * [How methods that change data work](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/toggle#input)Request
Request structure in JSON format:
```
{
  "method": "toggle",
  "params": { /* params */
    "BidModifierToggleItems": [{  /* BidModifierToggleItem */
      "CampaignId": (long),
      "AdGroupId": (long),
      "Type": ( "DEMOGRAPHICS_ADJUSTMENT" | "RETARGETING_ADJUSTMENT" | "REGIONAL_ADJUSTMENT" | "SERP_LAYOUT_ADJUSTMENT" | "INCOME_GRADE_ADJUSTMENT" ), /* required */
      "Enabled": ( "YES" | "NO" ) /* required */
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / ToggleRequest structure (for SOAP)**  
`BidModifierToggleItems` |  array of BidModifierToggleItem |  Sets of adjustments to enable or disable. Maximum of 1000 items in the array. |  Yes  
**BidModifierToggleItem structure**  
`CampaignId` |  long |  The campaign ID. Specified when enabling or disabling adjustments at the campaign level. |  Use either `CampaignId` or `AdGroupId`  
`AdGroupId` |  long |  ID of the ad group. Specified when enabling or disabling adjustments at the group level.  
`Type` |  BidModifierTypeEnum |  Types of adjustments to be enabled or disabled: DEMOGRAPHICS_ADJUSTMENT, RETARGETING_ADJUSTMENT, REGIONAL_ADJUSTMENT, SERP_LAYOUT_ADJUSTMENT, or INCOME_GRADE_ADJUSTMENT. |  Yes  
`Enabled` |  YesNoEnum |  YES — enable the set of adjustments; NO — disable the set of adjustments. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/toggle#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "ToggleResults": [{  /* ToggleResult */
      "CampaignId": (long),
      "AdGroupId": (long),
      "Type": ( "DEMOGRAPHICS_ADJUSTMENT" | "RETARGETING_ADJUSTMENT" | "REGIONAL_ADJUSTMENT" | "SERP_LAYOUT_ADJUSTMENT" | "INCOME_GRADE_ADJUSTMENT" ), /* required */
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
**result structure (for JSON) / ToggleResponse structure (for SOAP)**  
`ToggleResults` |  array of ToggleResult |  Results of enabling or disabling adjustments.  
**ToggleResult structure**  
`CampaignId` |  long |  The campaign ID. Returned if the operation completed successfully (if it was specified in the request).  
`AdGroupId` |  long |  ID of the ad group. Returned if the operation completed successfully (if it was specified in the request).  
`Type` |  BidModifierTypeEnum |  Type of adjustments that were enabled or disabled.  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/toggle#samples)Examples
**Example of disabling gender and age adjustments at the campaign level**
```
    {
      "method": "toggle",
      "params": {
        "BidModifierToggleItems": [
          {
            "CampaignId": 10001,
            "Type": "DEMOGRAPHICS_ADJUSTMENT",
            "Enabled": "NO"
          }
        ]
      }
    }

```

Copied
### Was the article helpful?
YesNo
Previous
[set](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/bidmodifiers/set)
Next
[Campaigns: managing campaigns](https://yandex.com/dev/direct/doc/en/bidmodifiers/en/campaigns/campaigns)
