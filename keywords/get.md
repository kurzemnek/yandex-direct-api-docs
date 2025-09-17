---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywords/get
crawled_at: 2025-09-17T15:59:35.821721
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#output)


This method returns parameters for keywords or autotargetings that match the specified criteria: the values of substitution variables, status and state, statistics for impressions and clicks, and bids.
Alert
We don't recommend requesting statistics on impressions and clicks for a large number of keywords: requests like this might take much longer to process.
You can get bids regardless of whether your campaign uses a manual or automatic strategy.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#restrictions)Restrictions
The method returns a maximum of `page-size` objects.
You can't get keywords from archived campaigns.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": {  /* params */
    "SelectionCriteria": {  /* KeywordsSelectionCriteria */
      "Ids": [(long), ... ],
      "AdGroupIds": [(long), ... ],
      "CampaignIds": [(long), ... ],
      "States": [( "OFF" | "ON" | "SUSPENDED" ), ... ],
      "Statuses": [( "ACCEPTED" | "DRAFT" | "REJECTED"), ... ],
      "ServingStatuses": [( "ELIGIBLE" | "RARELY_SERVED" ), ... ],
      "ModifiedSince": (string)
    }, /* required */
    "FieldNames": [( "Id" | "Keyword" | "State" | "Status" | "ServingStatus" | "AdGroupId" | "CampaignId" | "Bid" | "AutotargetingSearchBidIsAuto" | "ContextBid" | "StrategyPriority" | "UserParam1" | "UserParam2" | "Productivity" | "StatisticsSearch" | "StatisticsNetwork" | "AutotargetingCategories" ), ... ], /* required */
    "AutotargetingSettingsCategoriesFieldNames" : [ ("Exact"|"Narrow"|"Alternative"|"Accessory"|"Broader") ],
    "AutotargetingSettingsBrandOptionsFieldNames" : [ ("WithoutBrands"|"WithAdvertiserBrand"|"WithCompetitorsBrand") ],
    "Page": {  /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)** |  |  |   
`SelectionCriteria` |  KeywordsSelectionCriteria |  Criteria for selecting keywords and autotargetings. |  Yes  
`FieldNames` |  array of KeywordFieldEnum |  The names of parameters to get. Alert We don't recommend specifying the `StatisticsSearch` and `StatisticsNetwork` parameters when requesting data for a large number of keywords: requests like this take much longer to process. |  Yes  
`AutotargetingSettingsCategoriesFieldNames` |  array of AutotargetingSettingsCategoriesFieldEnum |  Targeting categories to get. |  No  
`AutotargetingSettingsBrandOptionsFieldNames` |  array of AutotargetingSettingsBrandOptionsFieldEnum |  Brand mention settings to get. |  No  
`Page` |  |  Structure that defines the page for  |  No  
**KeywordsSelectionCriteria structure** |  |  |   
`Ids` |  array of long |  Selects keywords and autotargetings with the specified IDs. From 1 to `ids-select` items in the array. |  One of the parameters: `Ids`, `AdGroupIds`, or `CampaignIds` (or all may be present)  
`AdGroupIds` |  array of long |  Selects keywords and autotargetings from the specified groups. From 1 to `adgroup-ids-select` items in the array. |   
`CampaignIds` |  array of long |  Selects keywords and autotargetings from the specified campaigns. From 1 to `campaign-ids-select` items in the array. |   
`States` |  array of KeywordStatusSelectionEnum |  Selects keywords and autotargetings with the specified states. See  |  No  
`Statuses` |  array of StatusEnum |  Selects keywords and autotargetings with the specified statuses. See  |  No  
`ServingStatuses` |  array of ServingStatusEnum |  Selects keywords and autotargetings with the specified ad group serving statuses. See  |  No  
`ModifiedSince` |  string |  Selects keywords and autotargetings that had changes starting from the specified date. Specified in the format `YYYY-MM-DDThh:mm:ssZ` (following ISO 8601), such as `2015-05-24T23:59:59Z`. |  No  
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/get#output)Response
Note
The response contains only those parameters that were indicated in the `FieldNames` input parameter.
Response structure in JSON format:
```
{
  "result": { /* result */
    "Keywords": [{  /* KeywordGetItem */
      "Id": (long),
      "Keyword": (string),
      "AdGroupId": (long),
      "CampaignId": (long),
      "UserParam1": (string), /* nillable */
      "UserParam2": (string), /* nillable */
      "Bid": (long),
      "AutotargetingSearchBidIsAuto" : ("YES"|"NO"),
      "ContextBid": (long),
      "StrategyPriority": "NORMAL", /* nillable */
      "State": ( "OFF" | "ON" | "SUSPENDED" ),
      "Status": ( "ACCEPTED" | "DRAFT" | "REJECTED" | "UNKNOWN" ),
      "ServingStatus": ( "ELIGIBLE" | "RARELY_SERVED" ),
      "Productivity": null,
      "StatisticsSearch": { /* Statistics */
          "Clicks": (long), /* required */
          "Impressions": (long) /* required */
      },
      "StatisticsNetwork": { /* Statistics */
          "Clicks": (long), /* required */
          "Impressions": (long) /* required */
      },
      "AutotargetingCategories" : { /* nillable */
          "Items" : [{ /* required */
            "Category" : ("EXACT"|"ALTERNATIVE"|"COMPETITOR"|"BROADER"|"ACCESSORY") /* required */,
            "Value" : ("YES"|"NO") /* required */
      }, ...],
      "AutotargetingSettings" : { /* nillable */
        "Categories" : {
            "Exact" : ("YES"|"NO"),
            "Narrow" : ("YES"|"NO"),
            "Alternative" : ("YES"|"NO"),
            "Accessory" : ("YES"|"NO"),
            "Broader" : ("YES"|"NO")
        },
        "BrandOptions" : {
            "WithoutBrands" : ("YES"|"NO"),
            "WithAdvertiserBrand" : ("YES"|"NO"),
            "WithCompetitorsBrand" : ("YES"|"NO")
        }
      }

    }, ... ],
    "LimitedBy": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`Keywords` |  array of KeywordGetItem |  Keywords and autotargetings.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section   
**KeywordGetItem structure** |  |   
`Id` |  long |  ID of the keyword or autotargeting.  
`AdGroupId` |  long |  ID of the ad group that the keyword or autotargeting is associated with.  
`CampaignId` |  long |  ID of the campaign that the keyword or autotargeting is associated with.  
`Keyword` |  string |  Keywords. May contain negative keywords. For autotargeting, the value `---autotargeting` is returned.  
`UserParam1` |  string, nillable |  Value of the `{param1}`  
`UserParam2` |  string, nillable |  Value of the `{param2}`  
`Bid` |  long |  Bid in search results.  
`AutotargetingSearchBidIsAuto` |  YesNoEnum |  A flag indicating whether   
`ContextBid` |  long |  Bid in ad networks.  
`StrategyPriority` |  PriorityEnum, nillable |  Priority of the keyword or autotargeting: NORMAL.  
`Status` |  StatusEnum |  Status of the keyword or autotargeting. For a description of the statuses, see the section   
`ServingStatus` |  ServingStatusEnum |  Serving status for the ad group. For a description of the statuses, see the section   
`State` |  StateEnum |  State of the keyword or autotargeting. For a description of the states, see the section   
`Productivity` |  Productivity, nillable |  This parameter is obsolete. Always returns null (nil).  
`StatisticsSearch` |  Statistics |  Statistics on impressions and clicks for all the group's ads for this keyword or autotargeting in search results. If the ad group has very few impressions (the `ServingStatus` parameter specifies RARELY_SERVED), the parameter isn't returned.  
`StatisticsNetwork` |  Statistics |  Statistics on impressions and clicks for all the group's ads for this keyword in ad networks. If the ad group has very few displays (the `ServingStatus` parameter has the value RARELY_SERVED), the parameter isn't returned. Copied  
`AutotargetingCategories` |  AutotargetingCategories, nillable |  Targeting categories. Alert This field is deprecated and will soon cease to be supported. You can retrieve the targeting settings using the `AutotargetingSettings` structure.  
`AutotargetingSettings` |  AutotargetingSettings, nillable |  Targeting settings.  
**Statistics structure** |  |   
`Clicks` |  long |  Number of clicks on all the group's ads that were shown for this keyword or autotargeting. Calculated for the last 28 days.  
`Impressions` |  long |  Number of impressions for this keyword or autotargeting for all ads in the ad group. Calculated for the last 28 days.  
**AutotargetingCategories structure** |  |   
`Category` |  AutotargetingCategoriesEnum |  Targeting category:
  * EXACT: The targeted queries. The ad matches user queries.
  * ALTERNATIVE: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also match the query in this case.
  * COMPETITOR: Queries mentioning competitors. Searching competitors for the advertised product.
  * BROADER: Broad queries. Queries showing interest in a product exemplified by the ad.
  * ACCESSORY: Related queries. Queries for products that might interest the user in relation to the advertised product or service.

Alert This field is deprecated and will soon cease to be supported. The settings specified in the web interface are converted for the API as follows: |  **Web interface** |  **API**  
---|---  
At least one enabled "Exact" or "Narrow" category. |  Enabled `EXACT` category.  
Enabled Competitors brand mention option (provided it's the only brand mention option enabled). |  Enabled `COMPETITOR` category + the other categories are disabled.  
Enabled Competitors brand mention option (provided it isn't the only brand mention option enabled). |  Enabled `COMPETITOR` category.  
Disabled Competitors brand mention option. |  Disabled `COMPETITOR` category.  
`Value` |  YesNoEnum |  The flag indicating that the specified targeting category is enabled. All targeting categories are enabled by default.  
**AutotargetingSettings structure** |  |   
`Categories` |  AutotargetingSettingsCategoriesFieldNames |  Targeting categories. Available options:
  * Exact: Targeted queries. The ad perfectly matches user queries.
  * Narrow: Narrow queries. The ad is broader than the user's queries.
  * Alternative: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also meet the query in this case.
  * Accessory: Related queries. Queries for products that might interest the user in relation to the advertised product or service.
  * Broader: Broad queries. Queries showing interest in a product exemplified by the ad.

  
`BrandOptions` |  AutotargetingSettingsBrandOptionsFieldNames |  Brand mention settings. Available options:
  * WithoutBrands: Non-branded queries.
  * WithAdvertiserBrand: Queries mentioning the advertiser's brand.
  * WithCompetitorsBrand: Queries mentioning competitor brands.

  
Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/delete)
Next
[resume](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/resume)
