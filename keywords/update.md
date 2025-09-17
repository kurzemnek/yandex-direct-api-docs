---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywords/update
crawled_at: 2025-09-17T15:58:05.342901
---

Learn more
# update
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#output)


Changes the parameters of keywords and autotargetings.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#learn-more)Learn more
  * [How the "update" method works](https://yandex.com/dev/direct/doc/en/best-practice/modify)
  * [How to handle errors](https://yandex.com/dev/direct/doc/en/concepts/errors)
  * [Autotargeting](https://yandex.com/dev/direct/doc/en/best-practice/auto-targeting)


##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#restrictions)Restrictions
Maximum of 1000 objects per method call.
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#input)Request
Request structure in JSON format:
```
{
  "method": "update",
  "params": { /* params */
    "Keywords": [{  /* KeywordUpdateItem */
      "Id": (long), /* required */
      "Keyword": (string),
      "UserParam1": (string), /* nillable */
      "UserParam2": (string), /* nillable */
      "AutotargetingCategories" : [{  /* AutotargetingCategoriesUpdateItem */
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
**params structure (for JSON) / UpdateRequest structure (for SOAP)** |  |  |   
`Keywords` |  array of KeywordUpdateItem |  Keywords and autotargetings to change the parameters for. |  Yes  
**KeywordUpdateItem structure** |  |  |   
`Id` |  long |  ID of the keyword or autotargeting. |  Yes  
`Keyword` |  string |  Keywords. It can contain negative keywords, which are specified with the minus sign before the word, such as _lightning -thunder -rain_. The maximum length of a keyword is 4096 characters. The “!” operator before a negative keyword is not counted in the keyword length (the sequence “-!” is considered one character). Maximum of 7 words per keyword, not counting stop words and negative keywords. Each word can have up to 35 characters, not counting the minus sign before a negative keyword. Alert
  * Changing a keyword may result in the creation of a new keyword. See [Creating a new keyword after editing](https://yandex.com/dev/direct/doc/dg/objects/keyword.html).
  * Updating a keyword may result in its deletion if it becomes a duplicate of another keyword. See [Duplicate keywords](https://yandex.com/dev/direct/doc/dg/objects/keyword.html).

For autotargeting, the value can't be changed. |  No  
`UserParam1` |  string, nillable |  Value of the `{param1}` [substitution variable](https://yandex.com/dev/direct/doc/dg/objects/keyword.html). Maximum of 255 characters. |  No  
`UserParam2` |  string, nillable |  Value of the `{param2}` [substitution variable](https://yandex.com/dev/direct/doc/dg/objects/keyword.html). Maximum of 255 characters. |  No  
`AutotargetingCategories` |  array of AutotargetingCategoriesUpdateItem |  Targeting categories to update. Alert This structure is obsolete and no longer supported. You can't pass both `AutotargetingCategories` and `AutotargetingSettings` at the same time. A validation error will occur if you try to do this. |  No  
`AutotargetingSettings` |  AutotargetingSettingsUpdateItem |  Targeting settings to update. |  No  
**AutotargetingCategoriesUpdateItem structure** |  |  |   
`Category` |  AutotargetingCategoriesEnum |  Targeting category:
  * EXACT: The targeted queries. The ad matches user queries.
  * ALTERNATIVE: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also match the query in this case.
  * COMPETITOR: Queries mentioning competitors. Searching competitors for the advertised product.
  * BROADER: Broad queries. Queries showing interest in a product exemplified by the ad.
  * ACCESSORY: Related queries. Queries for products that might interest the user in relation to the advertised product or service.

Alert This field is deprecated and will soon cease to be supported. The settings specified using the API are converted for the web interface as follows: |  **API** |  **Web interface**  
---|---  
Enabled `EXACT` category. | 
  * If the Exact and Narrow categories are disabled for the group, Exact and Narrow are enabled.
  * If either or both Exact and Narrow are enabled for the group, no changes are made.

  
Disabled `EXACT` category. | 
  * If either or both the Exact and Narrow categories are enabled for the group, Exact and Narrow are disabled.
  * If both Exact and Narrow are disabled for the group, no changes are made.

  
Enabled `COMPETITOR` category (provided it's the only category enabled). |  Enabled Competitors brand mention option + the other brand mention options are disabled + all categories are enabled.  
Enabled `COMPETITOR` category (provided it isn't the only category enabled). |  Enabled Competitors brand mention option.  
Disabled `COMPETITOR` category. |  Disabled Competitors brand mention option.  
Yes  
`Value` |  YesNoEnum |  The flag indicating that the specified targeting category is enabled. All targeting categories are enabled by default. |  Yes  
**AutotargetingSettingsUpdateItem structure** |  |  |   
`Categories` |  AutotargetingSettingsCategoriesFieldNames |  Targeting categories. Available options:
  * Exact: Targeted queries. The ad perfectly matches user queries.
  * Narrow: Narrow queries. The ad is broader than the user's queries.
  * Alternative: Alternative queries. The user is looking for a product that can be replaced by the advertised product. The ad might also match the query in this case.
  * Accessory: Related queries. Queries for products that might interest the user in relation to the advertised product or service.
  * Broader: Broad queries. Queries showing interest in a product exemplified by the ad.

|  No  
`BrandOptions` |  AutotargetingSettingsBrandOptionsFieldNames |  Brand mention settings. Available options:
  * WithoutBrands: Non-branded queries.
  * WithAdvertiserBrand: Queries mentioning the advertiser's brand.
  * WithCompetitorsBrand: Queries mentioning competitor brands.

|  No  
##  [](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/update#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "UpdateResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ]
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / UpdateResponse structure (for SOAP)** |  |   
`UpdateResults` |  array of ActionResult |  Results of changing parameters of keywords and autotargetings.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the changed keyword or autotargeting. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[suspend](https://yandex.com/dev/direct/doc/en/keywords/en/keywords/suspend)
Next
[KeywordsResearch: preprocessing of keywords](https://yandex.com/dev/direct/doc/en/keywords/en/keywordsresearch/keywordsresearch)
