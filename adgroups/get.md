---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/adgroups/get
crawled_at: 2025-09-17T15:46:03.094777
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#samples)


Returns parameters of groups that match the specified criteria.
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#learn-more)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#restrictions)Restrictions
To manage a unified performance group, use this URL: `https://api.direct.yandex.com/v501/`.
The method returns a maximum of 10,000 objects.
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* AdGroupsSelectionCriteria */
      "CampaignIds": [(long), ... ],
      "Ids": [(long), ... ],
      "Types": [( "TEXT_AD_GROUP" | "MOBILE_APP_AD_GROUP" | "DYNAMIC_TEXT_AD_GROUP" | "CPM_BANNER_AD_GROUP" | "CPM_VIDEO_AD_GROUP" | "SMART_AD_GROUP" | "UNIFIED_AD_GROUP" ), ... ],
      "Statuses": [( "ACCEPTED" | "DRAFT" | "MODERATION" | "PREACCEPTED" | "REJECTED" ), ... ],
      "ServingStatuses": [( "ELIGIBLE" | "RARELY_SERVED" ), ... ],
      "AppIconStatuses": [( "ACCEPTED" | "MODERATION" | "REJECTED" ), ... ],
      "NegativeKeywordSharedSetIds": [(long), ... ]
    }, /* required */
    "FieldNames": [( "CampaignId" | ... | "Type" ), ... ], /* required */
    "MobileAppAdGroupFieldNames": [( "StoreUrl" | ... | "AppIconModeration" ), ... ],
    "DynamicTextAdGroupFieldNames": [( "DomainUrl" | "DomainUrlProcessingStatus" | "AutotargetingCategories" ), ... ],
    "DynamicTextFeedAdGroupFieldNames": [( "Source" | "FeedId" | "SourceType" | "SourceProcessingStatus" | "AutotargetingCategories" ), ... ],
    "SmartAdGroupFieldNames": [( "FeedId" | "AdTitleSource" | "AdBodySource" ), ... ],
    "TextAdGroupFeedParamsFieldNames": [ ( "FeedId" | "FeedCategoryIds" ) ],
    "UnifiedAdGroupFieldNames" : [ ("OfferRetargeting") ],
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
`SelectionCriteria` |  AdGroupsSelectionCriteria |  Group selection criteria. |  Yes  
`FieldNames` |  array of AdGroupFieldEnum |  Names of top-level parameters to get. |  Yes  
`MobileAppAdGroupFieldNames` |  array of MobileAppAdGroupFieldEnum |  Names of parameters to get for a mobile app ad group. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). Note If a different type of group is selected according to `SelectionCriteria`, parameters from `MobileAppAdGroupFieldNames` are not returned. |  No  
`DynamicTextAdGroupFieldNames` |  array of DynamicTextAdGroupFieldEnum |  Names of parameters for a group of dynamic ads that has a website as the data source. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). Note If a different type of group is selected according to `SelectionCriteria`, parameters from `DynamicTextAdGroupFieldNames` are not returned. |  No  
`DynamicTextFeedAdGroupFieldNames` |  array of DynamicTextFeedAdGroupFieldEnum |  Names of parameters for a group of dynamic ads that has a feed as the data source. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). Note If a different type of group is selected according to `SelectionCriteria`, parameters from `DynamicTextFeedAdGroupFieldNames` are not returned. |  No  
`SmartAdGroupFieldNames` |  array of SmartAdGroupFieldEnum |  The names of parameters for a smart banner group. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). Note If a different type of group is selected according to `SelectionCriteria`, parameters from `SmartAdGroupFieldNames` are not returned. |  No  
`TextAdGroupFeedParamsFieldNames` |  array of TextAdGroupFeedParamsFieldEnum |  Names of parameters for a group of Text & Image ads that has a feed as the data source. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). Note If a different type of group is selected according to `SelectionCriteria`, parameters from `TextAdGroupFeedParamsFieldNames` are not returned. |  No  
`UnifiedAdGroupFieldNames` |  array of UnifiedAdGroupFieldEnum |  Parameter names of a unified performance group. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). Note If a different type of group is selected according to `SelectionCriteria`, parameters from `UnifiedAdGroupFieldNames` are not returned. |  No  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page) of data. |  No  
**AdGroupsSelectionCriteria structure**  
`CampaignIds` |  array of long |  Selects groups of the specified campaigns. From 1 to 10 items in the array. |  At least one of the `CampaignIds` or `Ids` parameters or both  
`Ids` |  array of long |  Selects groups with the specified IDs. From 1 to 10,000 items in the array.  
`Types` |  array of AdGroupTypesEnum |  Selects groups of the specified types. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types). |  No  
`Statuses` |  array of AdGroupStatusSelectionEnum |  Selects groups with the specified statuses. See [Group status](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#status). |  No  
`ServingStatuses` |  array of ServingStatusEnum |  Selects groups with the specified ad serving statuses. See [Serving status for the ad group](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#serving-status). |  No  
`AppIconStatuses` |  array of AdGroupAppIconStatusSelectionEnum |  Selects groups based on results of app icon review:
  * ACCEPTED — Accepted after review.
  * MODERATION — Currently under review.
  * REJECTED — Rejected.

If this parameter is set, only groups for mobile app advertising will be received. Don't set it if you need to get other types of groups. |  No  
`NegativeKeywordSharedSetIds` |  array of long |  Selects ad groups that use at least one of the specified sets of negative keywords. |  No  
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AdGroups": [{  /* AdGroupGetItem */
      "Id": (long),
      "Name": (string),
      "CampaignId": (long),
      "RegionIds": [(long), ... ],
      "RestrictedRegionIds": {  /* ArrayOfLong */
        "Items": [(long), ... ] /* required */
      }, /* nillable */
      "NegativeKeywords": {  /* ArrayOfString */
        "Items": [(string), ... ] /* required */
      }, /* nillable */
      "NegativeKeywordSharedSetIds": { /* ArrayOfLong */
        "Items": [(long), ... ] /* required */
      }, /* nillable */
      "TrackingParams": (string),
      "Status": ( "ACCEPTED" | "DRAFT" | "MODERATION" | "PREACCEPTED" | "REJECTED" ),
      "ServingStatus": ( "ELIGIBLE" | "RARELY_SERVED" ),
      "Type": ( "TEXT_AD_GROUP" | "MOBILE_APP_AD_GROUP" | "DYNAMIC_TEXT_AD_GROUP"
                | "CPM_BANNER_AD_GROUP" | "CPM_VIDEO_AD_GROUP" | "SMART_AD_GROUP" ),
      "Subtype": ( "WEBPAGE" | "FEED" | "NONE" | "KEYWORDS" | "USER_PROFILE" ),
      "MobileAppAdGroup": {  /* MobileAppAdGroupGet */
        "StoreUrl": (string),
        "TargetDeviceType": [( "DEVICE_TYPE_MOBILE" | "DEVICE_TYPE_TABLET" ), ... ],
        "TargetCarrier": ( "WI_FI_ONLY" | "WI_FI_AND_CELLULAR" ),
        "TargetOperatingSystemVersion": (string),
        "AppIconModeration": {  /* ExtensionModeration */
          "Status": ( "ACCEPTED" | "MODERATION" | "REJECTED" ), /* required */
          "StatusClarification": (string)
        }, /* nillable */
        "AppOperatingSystemType": ( "IOS" | "ANDROID" | "OS_TYPE_UNKNOWN" ),
        "AppAvailabilityStatus": ( "UNPROCESSED" | "AVAILABLE" | "NOT_AVAILABLE" )
      },
      "DynamicTextAdGroup": [{  /* DynamicTextAdGroupGet */
        "DomainUrl": (string),
        "DomainUrlProcessingStatus": ( "EMPTY_RESULT" | "PROCESSED" | "UNKNOWN" | "UNPROCESSED" ),
        "AutotargetingCategories" : { /* nillable */
          "Items" : [{ /* required */
            "Category" : ("EXACT"|"ALTERNATIVE"|"COMPETITOR"|"BROADER"|"ACCESSORY") /* required */,
            "Value" : ("YES"|"NO") /* required */
          }, ...]
        }, ...]
      }, ...],
      "DynamicTextFeedAdGroup": [{  /* DynamicTextFeedAdGroupGet */
        "Source": (string),
        "FeedId": (long),
        "SourceType": ( "RETAIL_FEED" | "UNKNOWN" ),
        "SourceProcessingStatus": ( "EMPTY_RESULT" | "PROCESSED" | "UNKNOWN" | "UNPROCESSED" ),
        "AutotargetingCategories" : { /* nillable */
          "Items" : [{ /* required */
            "Category" : ("EXACT"|"ALTERNATIVE"|"COMPETITOR"|"BROADER"|"ACCESSORY") /* required */,
            "Value" : ("YES"|"NO") /* required */
          }, ...]
        }, ...]
      }, ...],
      "SmartAdGroup": { /* SmartAdGroupGet */
        "FeedId": (long),
        "AdTitleSource": (string), /* nillable */
        "AdBodySource": (string) /* nillable */
      },
      "TextAdGroupFeedParams" : {  /* TextAdGroupFeedParamsGet */
        "FeedId" : (long) /* nillable */,
        "FeedCategoryIds" : { /* nillable */
          "Items" : [ (long) ] /* required */
        }
      },
      "UnifiedAdGroup" : {
        "OfferRetargeting" : ("YES"|"NO")
      }
    }, ... ],
  "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`AdGroups` |  array of AdGroupGetItem |  Groups of ads.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page).  
**AdGroupGetItem structure**  
`Id` |  long |  ID of the ad group.  
`Name` |  string |  Name of the group.  
`CampaignId` |  long |  The campaign ID.  
`RegionIds` |  array of long |  IDs of regions where ad impressions are enabled or disabled. The ID "0" indicates to display ads in all regions. A minus sign before a region ID disables impressions in this region. For example, [1,-219] indicates to display for Moscow and the entire Moscow area, except Chernogolovka.  
`RestrictedRegionIds` |  ArrayOfLong, nillable |  IDs of regions where ads won't be served due to legal restrictions.  
`NegativeKeywords` |  ArrayOfString, nillable |  Negative keywords that are shared by all the ad group's keywords.  
`NegativeKeywordSharedSetIds` |  ArrayOfLong, nillable |  IDs of sets of negative keywords. Maximum of 3 items in the array.  
`TrackingParams` |  string |  GET parameters for tracking traffic sources that are added to the link of all ads in the group (maximum of 1024 characters). May contain  For example: from=direct&ad={ad_id} Image ads, dynamic ads, and smart banners. However, currently it's only used for groups of dynamic ads and smart banners.  
`Status` |  StatusEnum |  Group status. See [Group status](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#status).  
`ServingStatus` |  ServingStatusEnum |  Serving status for the ad group. See [Serving status for the ad group](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#serving-status).  
`Type` |  AdGroupTypesEnum |  Type of ad group. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types).  
`Subtype` |  AdGroupSubtypeEnum |  The subtype of ad group. For a group with a type other than DYNAMIC_TEXT_AD_GROUP or CPM_BANNER_AD_GROUP, the value NONE is returned.  
`MobileAppAdGroup` |  MobileAppAdGroupGet |  Parameters of groups for mobile app advertising.  
`DynamicTextAdGroup` |  DynamicTextAdGroupGet |  Parameters for a group of dynamic ads that has a website as the data source.  
`DynamicTextFeedAdGroup` |  DynamicTextFeedAdGroupGet |  Parameters for a group of dynamic ads that has a feed as the data source.  
`SmartAdGroup` |  SmartAdGroupGet |  Parameters for ad group of smart banners.  
`TextAdGroupFeedParams` |  TextAdGroupFeedParamsGet |  Parameters of a Text & Image ads group.  
`UnifiedAdGroup` |  UnifiedAdGroupGet |  Parameters of a unified performance group. See [Group type](https://yandex.com/dev/direct/doc/dg/objects/adgroup.html#types).  
**MobileAppAdGroupGet structure**  
`StoreUrl` |  string |  Link to the app in AppStore or Google Play (maximum of 1024 characters). The link must contain the protocol. Not editable. See  Alert All ad groups in the same campaign must have the same app link.  
If groups with different app links were previously created in the campaign, then you are allowed to specify the app link that is shown in your campaign settings in the Yandex Direct web interface.  
`TargetDeviceType` |  array of DeviceTypeEnum |  Which devices to show ads on:
  * DEVICE_TYPE_MOBILE — smartphones
  * DEVICE_TYPE_TABLET — tablets

  
`TargetCarrier` |  CarrierEnum |  Which types of internet connections to show ads on:
  * WI_FI_ONLY — only Wi-Fi
  * WI_FI_AND_CELLULAR — cellular internet and Wi-Fi

  
`TargetOperatingSystemVersion` |  string |  The minimum OS version to display the ad on. For example, 2.3. Note If the minimum OS version in the app store is higher than the one set in this parameter, ads are displayed only for OS versions equal to or higher than the one in the app store.  
`AppIconModeration` |  ExtensionModeration |  Result of reviewing the mobile app icon.  
`AppOperatingSystemType` |  MobileOperatingSystemTypeEnum |  Type of operating system (detected automatically based data from the app store):
  * IOS — iOS.
  * ANDROID — Android.
  * OS_TYPE_UNKNOWN — Data hasn't been received from the app store yet.

  
`AppAvailabilityStatus` |  AppAvailabilityStatusEnum |  Whether the app is available in the app store:
  * AVAILABLE — The app is available.
  * NOT_AVAILABLE — The app isn't available.
  * UNPROCESSED — Data hasn't been received from the app store yet.

  
**ExtensionModeration structure**  
`Status` |  ModerationStatusEnum |  Result of reviewing the mobile app icon:
  * ACCEPTED — Accepted after review.
  * MODERATION — Currently under review.
  * REJECTED — Rejected.

  
`StatusClarification` |  string |  Text explanation of the status and/or reasons for rejection after review.  
**DynamicTextAdGroupGet structure**  
`DomainUrl` |  string |  The domain name of the site to generate dynamic ads for (a maximum of 100 characters). The protocol can be omitted.  
`DomainUrlProcessingStatus` |  SourceProcessingStatusEnum |  Status of generating dynamic ads:
  * UNPROCESSED — Ad generation has not finished.
  * PROCESSED — Ads have been created.
  * EMPTY_RESULT — No ads could be created.

  
`AutotargetingCategories` |  array of AutotargetingCategoriesGetItem |  Targeting categories to be added.  
**AutotargetingCategories structure**  
`Category` |  AutotargetingCategoriesEnum |  Targeting category:
  * EXACT: The targeted queries. The ad matches user queries.
  * ALTERNATIVE: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also match the query in this case.
  * COMPETITOR: Queries mentioning competitors. Searching competitors for the advertised product.
  * BROADER: Broad queries. Queries showing interest in a product exemplified by the ad.
  * ACCESSORY: Related queries. Queries for products that might interest the user in relation to the advertised product or service.

  
`Value` |  YesNoEnum |  The flag indicating that the specified targeting category is enabled. All targeting categories are enabled by default.  
**DynamicTextFeedAdGroupGet structure**  
`Source` |  string |  The feed ID.  
`FeedId` |  long |  The feed ID.  
`SourceType` |  SourceTypeGetEnum |  The type of data source. Currently, only the RETAIL_FEED value is available.  
`SourceProcessingStatus` |  SourceProcessingStatusEnum |  Status of generating dynamic ads:
  * UNPROCESSED — Ad generation has not finished.
  * PROCESSED — Ads have been created.
  * EMPTY_RESULT — No ads could be created.

  
`AutotargetingCategories` |  array of AutotargetingCategoriesGetItem |  Targeting categories to be added.  
**SmartAdGroupGet structure**  
`FeedId` |  long |  ID of the feed to use for generating smart banners.  
`AdTitleSource` |  string, nillable |  The name of the feed element to use for the ad title. If omitted, the title is generated automatically.  
`AdBodySource` |  string, nillable |  The name of the feed element to use for the ad text. If omitted, the text is generated automatically.  
**TextAdGroupFeedParamsGet structure**  
`FeedId` |  long |  ID of the feed on the basis of which Text & Image ads must be generated.  
`FeedCategoryIds` |  ArrayOfLong |  Image ads must be generated. If no category IDs are specified, all categories from the feed are used.  
**UnifiedAdGroupGet structure**  
`OfferRetargeting` |  YesNoEnum |  Indicates that offer retargeting is enabled.  
##  [](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/get#samples)Examples
**Request example**
```
{
  "method" : "get",
  "params" : {
    "SelectionCriteria" : {
      "CampaignIds" : [
        2991372,
        4193065,
        4193084,
        7273721
      ],
      "Statuses" : [ "DRAFT" ]
    },
    "FieldNames" : [
      "Id",
      "Name",
      "CampaignId",
      "Status",
      "RegionIds",
      "NegativeKeywords"
    ]
  }
}

```

**Response example**
```
{
  "result" : {
    "AdGroups" : [
      {
        "Id" : 45625656,
        "Status" : "DRAFT",
        "CampaignId" : 4193065,
        "RegionIds" : [
          225
        ],
        "NegativeKeywords" : null,
        "Name" : "AdGroup #1"
      },
      {
        "Id" : 198171138,
        "Status" : "DRAFT",
        "CampaignId" : 7273721,
        "RegionIds" : [
          225
        ],
        "NegativeKeywords" : null,
        "Name" : "AdGroup #2"
      },
      {
        "Id" : 636056252,
        "Status" : "DRAFT",
        "CampaignId" : 7273721,
        "RegionIds" : [
          0
        ],
        "NegativeKeywords" : {
          "Items" : [
            "куплю"
          ]
        },
        "Name" : "AdGroup #3"
      }
    ]
  }
}

```

Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/delete)
Next
[update](https://yandex.com/dev/direct/doc/en/adgroups/en/adgroups/update)
