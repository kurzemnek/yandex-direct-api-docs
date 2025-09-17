---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywords/add
crawled_at: 2025-09-17T15:57:59.736521
---

add
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#output)


Creates keywords and autotargetings.
Alert
The method doesn't save duplicates of keywords. See 
You can set a bid based on your campaign's strategy:
  * If your campaign uses a manual strategy, you can specify the `Bid` parameter. If the strategy allows you to manage bids for ad networks separately, you can specify `Bid` and `ContextBid`.
If an item in the input array contains parameters that are not appropriate for the strategy, the values of these parameters are saved and a warning is issued.
  * If you've set up an automatic strategy for your campaign but specified the `Bid` and/or `ContextBid` parameter when creating keywords, these bid values **won't be applied**. When the strategy changes from automatic to manual, the bid will be selected by an automatic algorithm.
  * If you've set up a manual strategy for your campaign that allows you to manage bids in ad networks separately, but you've specified the `ContextBid` parameter when creating keywords, this bid value will be applied later when the strategy changes to a manual strategy that allows you to manage bids separately.


If the strategy allows for setting bids but the bid is not specified, the default setting is:
  * For a keyword – The minimum bid.
  * For autotargeting for `ContextBid`: A bid calculated from bids for keywords in the ad group (if the group has no keywords, the minimum bid is used).
  * For autotargeting for `Bid`: An automatic bid. If automatic bid is disabled: A bid calculated based on bids for keywords in the ad group (a manual bid is always calculated, but it's only used when automatic bid is disabled). If there are no keywords in the ad group, the minimum bid is used.


All targeting categories are enabled by default.
Categories for which neither "YES" nor "NO" is explicitly specified are considered enabled.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#restrictions)Restrictions
Maximum of 1000 objects per method call.
Maximum of 1 autotargeting per ad group.
You cannot add keywords to an ad group that has the CPM_BANNER_AD_GROUP type and USER_PROFILE subtype, or to a DYNAMIC_TEXT_AD_GROUP type of ad group.
You cannot add autotargetings to an ad group with the DYNAMIC_TEXT_AD_GROUP or CPM_BANNER_AD_GROUP type.
To check the limit on the number of keywords per ad group for an advertiser, use the [get](https://yandex.com/dev/direct/doc/en/keywords/en/clients/get) or 
For restrictions on the number of words and characters in a keyword, see the 
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": {  /* params */
    "Keywords": [{  /* KeywordAddItem */
      "Keyword": (string), /* required */
      "AdGroupId": (long), /* required */
      "Bid": (long),
      "AutotargetingSearchBidIsAuto" : ("YES" | "NO"),
      "ContextBid": (long),
      "StrategyPriority":  ( "LOW" | "NORMAL" | "HIGH" ),
      "UserParam1": (string),
      "UserParam2": (string),
      "AutotargetingCategories" : [{  /* AutotargetingCategoriesAddItem */
          "Category" : ("EXACT"|"ALTERNATIVE"|"COMPETITOR"|"BROADER"|"ACCESSORY") /* required */,
          "Value" : ("YES"|"NO") /* required */
      }, ...],
      "AutotargetingSettings" : {
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
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)** |  |  |   
`Keywords` |  array of KeywordAddItem |  Keywords and autotargetings to add. |  Yes  
**KeywordAddItem structure** |  |  |   
`AdGroupId` |  long |  ID of the group to add the keyword or autotargeting to. |  Yes  
`Keyword` |  string |  Keywords. It can contain negative keywords, which are specified with the minus sign before the word, such as _lightning -thunder -rain_. The maximum length of a keyword is 4096 characters. The "!" operator before a negative keyword doesn't count toward the keyword length (the sequence "-!" is considered a single character). Maximum of 7 words per keyword, not counting stop words and negative keywords. Each word can have up to 35 characters, not counting the minus sign before a negative keyword. Note If you have negative keywords that apply to all of an ad group's keywords, set them in the [NegativeKeywords](*NegativeKeywords) parameter for the ad group. If the value is set to `---autotargeting`, an autotargeting object is created, and you can specify an automatic bid (`AutotargetingSearchBidIsAuto`). |  Yes  
`Bid` |  long |  The bid on search, multiplied by 1,000,000. Integer. Only for manual strategies. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/keywords/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/keywords/en/dictionaries/get) method and specify the `Currencies` dictionary name in the request. |  No  
`AutotargetingSearchBidIsAuto` |  YesNoEnum |  A flag indicating whether  You can specify a manual bid (`Bid`) and enable automatic bids (`AutotargetingSearchBidIsAuto`) at the same time. In that case, automatic bid will be used, and manual bid will be applied if automatic bid is disabled. If you've set a manual bid (`Bid`), the automatic bid value (`AutotargetingSearchBidIsAuto`) is set to NO unless you specify a different automatic bid. If you haven't set a manual bid (`Bid`), the automatic bid value (`AutotargetingSearchBidIsAuto`) is set to YES unless you specify a different automatic bid. |  No  
`ContextBid` |  long |  The bid in ad networks, multiplied by 1,000,000. Integer. Only for manual strategies with independent bid management in the Yandex Advertising Network. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/keywords/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/keywords/en/dictionaries/get) method and specify the `Currencies` dictionary name in the request. Alert An image ad can be displayed only if the bid is at least as high as the minimum bid for an ad with an image. |  No  
`StrategyPriority` |  PriorityEnum |  Priority of the keyword or autotargeting: LOW, NORMAL or HIGH. Only for automatic strategies. Alert This parameter is not used, and the passed value is ignored. |  No  
`UserParam1` |  string |  Value of the `{param1}` |  No  
`UserParam2` |  string |  Value of the `{param2}` |  No  
`AutotargetingCategories` |  array of [AutotargetingCategoriesAddItem](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#AutotargetingCategoriesAddItem) |  Targeting categories to be added. Alert This structure is deprecated and will soon cease to be supported. You can't pass both `AutotargetingCategories` and `AutotargetingSettings` at the same time. A validation error will occur if you try to do this. |  No  
`AutotargetingSettings` |  [AutotargetingSettingsAddItem](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#AutotargetingSettingsAddItem) |  Targeting settings to add. |  No  
**AutotargetingCategoriesAddItem structure** |  |  |   
`Category` |  AutotargetingCategoriesEnum |  Targeting category:
  * EXACT: The targeted queries. The ad matches user queries.
  * ALTERNATIVE: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also match the query in this case.
  * COMPETITOR: Queries mentioning competitors. Searching competitors for the advertised product.
  * BROADER: Broad queries. Queries showing interest in a product exemplified by the ad.
  * ACCESSORY: Related queries. Queries for products that might interest the user in relation to the advertised product or service.

Alert This field is deprecated and will soon cease to be supported. The settings specified using the API are converted for the web interface as follows: |  **API** |  **Web interface**  
---|---  
Enabled `EXACT` category. |  Enabled "Exact" and "Narrow" categories.  
Enabled `COMPETITOR` category (provided it's the only category enabled). |  Enabled Competitors brand mention option + the other brand mention options are disabled + all categories are enabled.  
Enabled `COMPETITOR` category (provided it isn't the only category enabled). |  Enabled Competitors brand mention option.  
Disabled `COMPETITOR` category. |  Disabled Competitors brand mention option.  
Yes  
`Value` |  YesNoEnum |  The flag indicating that the specified targeting category is enabled. All targeting categories are enabled by default. |  Yes  
**AutotargetingSettingsAddItem structure** |  |  |   
`Categories` |  AutotargetingSettingsCategoriesFieldNames |  Targeting categories. Available options:
  * Exact: Targeted queries. The ad perfectly matches user queries.
  * Narrow: Narrow queries. The ad is broader than the user's queries.
  * Alternative: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also meet the query in this case.
  * Accessory: Related queries. Queries for products that might interest the user in relation to the advertised product or service.
  * Broader: Broad queries. Queries showing interest in a product exemplified by the ad.

|  No  
`BrandOptions` |  AutotargetingSettingsBrandOptionsFieldNames |  Brand mention settings. Available options:
  * WithoutBrands: Non-branded queries.
  * WithAdvertiserBrand: Queries mentioning the advertiser's brand.
  * WithCompetitorsBrand: Queries mentioning competitor brands.

|  No  
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/add#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "AddResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ...  ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ]
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / AddResponse structure (for SOAP)** |  |   
`AddResults` |  array of ActionResult |  Results of adding keywords or autotargetings.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the created keyword or autotargeting. Returned if there aren't any errors. See the section   
`Warnings` |  array of  |  Warnings that occurred during the operation.  
`Errors` |  array of  |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[Keywords: managing keywords and autotargetings](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/keywords)
Next
[delete](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/delete)
