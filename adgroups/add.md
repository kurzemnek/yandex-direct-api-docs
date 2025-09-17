---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adgroups/add
crawled_at: 2025-09-17T15:45:39.427345
---

Learn more
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#samples)


Creates ad groups.
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#learn-more)Learn more
  * [How the "add" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#restrictions)Restrictions
To manage a unified performance group, use this URL: `https://api.direct.yandex.com/v501/`.
You can't add groups to an archived campaign.
Maximum of 1000 groups per method call.
To check the limit on the number of ad groups in a campaign for an advertiser, use the [Clients](https://yandex.com/dev/direct/doc/en/adgroups/en/clients/clients).[get](https://yandex.com/dev/direct/doc/en/adgroups/en/clients/get) or [AgencyClients](https://yandex.com/dev/direct/doc/en/adgroups/en/agencyclients/agencyclients).[get](https://yandex.com/dev/direct/doc/en/adgroups/en/agencyclients/get) method (look for the ADGROUPS_TOTAL_PER_CAMPAIGN element in the Restrictions array).
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "AdGroups": [{  /* AdGroupAddItem */
      "Name": (string), /* required */
      "CampaignId": (long), /* required */
      "RegionIds": [(long), ... ], /* required */
      "NegativeKeywords": { /* ArrayOfString */
        "Items": [(string), ... ] /* required */
      },
      "NegativeKeywordSharedSetIds": { /* ArrayOfLong */
        "Items": [(long), ... ] /* required */
      },
      "TrackingParams": (string),
      "MobileAppAdGroup": {  /* MobileAppAdGroupAdd */
        "StoreUrl": (string), /* required */
        "TargetDeviceType": [( "DEVICE_TYPE_MOBILE" | "DEVICE_TYPE_TABLET" ), ... ], /* required */
        "TargetCarrier": ( "WI_FI_ONLY" | "WI_FI_AND_CELLULAR" ), /* required */
        "TargetOperatingSystemVersion": (string) /* required */
      },
      "DynamicTextAdGroup": [{  /* DynamicTextAdGroupAdd */
        "DomainUrl": (string) /* required */,
        "AutotargetingCategories" : [{  /* AutotargetingCategoriesAdd */
          "Category" : ( "EXACT" | "ALTERNATIVE" | "COMPETITOR" | "BROADER" | "ACCESSORY" ) /* required */,
          "Value" : ( "YES" | "NO" ) /* required */
        }, ...]
      }, ...],
      "DynamicTextFeedAdGroup": [{  /* DynamicTextFeedAdGroupAdd */
        "FeedId": (long) /* required */,
        "AutotargetingCategories" : [{  /* AutotargetingCategoriesAdd */
          "Category" : ( "EXACT" | "ALTERNATIVE" | "COMPETITOR" | "BROADER" | "ACCESSORY" ) /* required */,
          "Value" : ( "YES" | "NO" ) /* required */
        }, ...]
      }, ...],
      "CpmBannerKeywordsAdGroup": {  /* CpmBannerKeywordsAdGroupAdd */
      },
      "CpmBannerUserProfileAdGroup": {  /* CpmBannerUserProfileAdGroupAdd */
      },
      "CpmVideoAdGroup": {  /* CpmVideoAdGroupAdd */
      },
      "SmartAdGroup": {  /* SmartAdGroupAdd */
        "FeedId": (long), /* required */
        "AdTitleSource": (string),
        "AdBodySource": (string)
      },
      "UnifiedAdGroup" : {
        "OfferRetargeting" : ("YES"|"NO") /* required */
      },
      "TextAdGroupFeedParams" : {  /*TextAdGroupFeedParamsAdd */
        "FeedId" : (long) /* required */,
        "FeedCategoryIds" : {
          "Items" : [ (long) ] /* required */
        }
      }
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`AdGroups` |  array of AdGroupAddItem |  The groups to add. |  Yes  
**AdGroupAddItem structure**  
`Name` |  string |  The name of the ad group (from 1 to 255 characters). |  Yes  
`CampaignId` |  long |  ID of the campaign that the group is being added to. |  Yes  
`RegionIds` |  array of long |  Array of IDs of regions where ad impressions are enabled or disabled. The array must contain at least one item. The ID "0" indicates to display ads in all regions. A minus sign before a region ID disables impressions in this region. For example, [1,-219] indicates to display for Moscow and the entire Moscow area, except Chernogolovka. Minus regions can't be used if 0 is set. The array must not consist of only minus regions.  
To get the list of regions, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/adgroups/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/adgroups/en/dictionaries/get) method. |  Yes  
`NegativeKeywords` |  ArrayOfString |  Array of negative keywords that are shared by all the keywords of an ad group. Alert Negative keywords are not allowed in a group of display ads with targeting criteria based on a user profile. A keyword should be specified without the minus sign before the first word. Maximum of 7 words per keyword. The maximum length of each word is 35 characters. The maximum combined length of negative keywords in the array is 4096 characters. Spaces, dashes, and operators are not counted as part of the total length. Note Negative keywords that are shared for all a campaign's ad groups should preferably be set in the campaign parameter of the same name. |  No  
`NegativeKeywordSharedSetIds` |  ArrayOfLong |  IDs of sets of negative keywords. Maximum of 3 items in the array. To get the IDs of sets, use the [NegativeKeywordSharedSets](https://yandex.com/dev/direct/doc/en/adgroups/en/negativekeywordsharedsets/negativekeywordsharedsets).[get](https://yandex.com/dev/direct/doc/en/adgroups/en/negativekeywordsharedsets/get) method. Alert Negative keywords are not allowed in a group of display ads with targeting criteria based on a user profile. |  No  
`TrackingParams` |  string |  GET parameters for tracking traffic sources that are added to the link of all ads in the group (maximum of 1024 characters). May contain  For example: from=direct&ad={ad_id} Image ads, dynamic ads, and smart banners. However, currently it's only used for groups of dynamic ads and smart banners. |  No  
`MobileAppAdGroup` |  MobileAppAdGroupAdd |  Parameters of ad groups for mobile app ads. |  No  
`DynamicTextAdGroup` |  DynamicTextAdGroupAdd |  Parameters of a group of dynamic ads. |  No  
`DynamicTextFeedAdGroup` |  DynamicTextFeedAdGroupAdd |  Parameters of a group of dynamic ads with the FEED subtype. |  No  
`CpmBannerKeywordsAdGroup` |  CpmBannerKeywordsAdGroupAdd |  Parameters for a group of display ads with keywords. To create such a group, specify an empty `CpmBannerKeywordsAdGroup` structure. |  No  
`CpmBannerUserProfileAdGroup` |  CpmBannerUserProfileAdGroupAdd |  Parameters for a group of display ads with targeting criteria based on a user profile. To create such a group, specify an empty `CpmBannerUserProfileAdGroup` structure. |  No  
`CpmVideoAdGroup` |  CpmVideoAdGroupAdd |  Parameters of a group of display video ads in a display campaign. To create such a group, specify an empty `CpmVideoAdGroup` structure. |  No  
`SmartAdGroup` |  SmartAdGroupAdd |  Parameters for ad group of smart banners. |  No  
`UnifiedAdGroup` |  UnifiedAdGroupAdd |  Parameters of a unified performance group: See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). |  No  
`TextAdGroupFeedParams` |  TextAdGroupFeedParams |  Image ads group. |  No  
**MobileAppAdGroupAdd structure**  
`StoreUrl` |  string |  Link to the app in AppStore or Google Play (maximum of 1024 characters). The link must contain the protocol. Not editable. See  Alert All ad groups in the same campaign must have the same app link.  
If groups with different app links were previously created in the campaign, then you are allowed to specify the app link that is shown in your campaign settings in the Yandex Direct web interface. |  Yes  
`TargetDeviceType` |  array of DeviceTypeEnum |  Which devices to show ads on:
  * DEVICE_TYPE_MOBILE — smartphones
  * DEVICE_TYPE_TABLET — tablets

|  Yes  
`TargetCarrier` |  CarrierEnum |  Which types of internet connections to show ads on:
  * WI_FI_ONLY — only Wi-Fi
  * WI_FI_AND_CELLULAR — cellular internet and Wi-Fi

|  Yes  
`TargetOperatingSystemVersion` |  string |  The minimum OS version to display the ad on. For example, 2.3. Note If the minimum OS version in the app store is higher than the one set in this parameter, ads are displayed only for OS versions equal to or higher than the one in the app store. |  Yes  
**DynamicTextAdGroupAdd structure**  
`DomainUrl` |  string |  The domain name of the site to generate dynamic ads for (a maximum of 100 characters). The protocol can be omitted. |  Yes  
`AutotargetingCategories` |  array of AutotargetingCategoriesAddItem |  Targeting categories to be added. |  No  
**DynamicTextFeedAdGroupAdd structure**  
`FeedId` |  long |  ID of the feed on the basis of which dynamic ads must be generated. |  Yes  
`AutotargetingCategories` |  array of AutotargetingCategoriesAddItem |  Targeting categories to be added. |  No  
**AutotargetingCategoriesAddItem structure**  
`Category` |  AutotargetingCategoriesEnum |  Targeting category:
  * EXACT: The targeted queries. The ad matches user queries.
  * ALTERNATIVE: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also match the query in this case.
  * COMPETITOR: Queries mentioning competitors. Searching competitors for the advertised product.
  * BROADER: Broad queries. Queries showing interest in a product exemplified by the ad.
  * ACCESSORY: Related queries. Queries for products that might interest the user in relation to the advertised product or service.

|  Yes  
`Value` |  YesNoEnum |  The flag indicating that the specified targeting category is enabled. All targeting categories are enabled by default. |  Yes  
**SmartAdGroupAdd structure**  
`FeedId` |  long |  The ID of the feed to use for generating smart banners. |  Yes  
`AdTitleSource` |  string |  The name of the feed element to use for the ad title. If omitted, the title is generated automatically. |  No  
`AdBodySource` |  string |  The name of the feed element to use for the ad text. If omitted, the text is generated automatically. |  No  
**UnifiedAdGroupAdd structure**  
`OfferRetargeting` |  YesNoEnum |  Indicates that offer retargeting is enabled. |  Yes  
**TextAdGroupFeedParamsAdd structure**  
`FeedId` |  long |  ID of the feed on the basis of which Text & Image ads must be generated. |  Yes  
`FeedCategoryIds` |  ArrayOfLong |  Image ads must be generated. If no category IDs are specified, all categories from the feed are used. |  No  
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#output)Response
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
`AddResults` |  array of ActionResult |  Results of adding groups.  
**ActionResult structure**  
`Id` |  long |  ID of the created group. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/add#samples)Examples
**Request example**
```
{
  "method" : "add",
  "params" : {
    "AdGroups" : [
      {
        "RegionIds" : [
          0
        ],
        "CampaignId" : 7273721,
        "NegativeKeywords" : {
          "Items" : [
            "куплю"
          ]
        },
        "Name" : "AdGroup #1"
      },
      {
        "RegionIds" : [
          225
        ],
        "CampaignId" : 4193065,
        "NegativeKeywords" : {
          "Items" : [
            "продам"
          ]
        },
        "Name" : "AdGroup #2"
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
      {
        "Id" : 636056397
      },
      {
        "Id" : 636056402
      }
    ]
  }
}

```

**Response with error**
```
{
  "result" : {
    "AddResults" : [
      {
        "Errors" : [
          {
            "Code" : 8800,
            "Details" : "Campaign not found",
            "Message" : "Object not found"
          }
        ]
      },
      {
        "Errors" : [
          {
            "Code" : 5120,
            "Details" : "221 invalid or non-existent region",
            "Message" : "Geo-targeting not set up properly"
          }
        ]
      }
    ]
  }
}

```

Copied
### Was the article helpful?
YesNo
Previous
[AdGroups: operations with ad groups](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/adgroups)
Next
[delete](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete)
