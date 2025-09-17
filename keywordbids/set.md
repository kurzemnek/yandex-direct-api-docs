---
title: set | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywordbids/set
crawled_at: 2025-09-17T15:59:01.783224
---

set
# set
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#output)
  * [Example](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#samples)


Sets fixed bids for keywords and autotargetings.
You can set a bid for:
  * A separate keyword or autotargeting.
  * All keywords and autotargetings in an ad group.
  * All keywords and autotargetings in a campaign.


You can set a bid based on your campaign's 
  * If you've chosen the HIGHEST_POSITION display strategy for Yandex Search, you can specify the `SearchBid` parameter.
  * If you've chosen the MAXIMUM_COVERAGE or MANUAL_CPM display strategy for ad networks, you can specify the `NetworkBid` parameter.


If an item in the input array contains parameters that are not appropriate for the strategy, the values of these parameters are not changed.
  * If an item in the input array contains parameters that both match and don't match the strategy, the operation only changes the values of the parameters that match the strategy, and a warning is returned.
  * If an item in the input array only contains parameters that don't match the strategy, the operation doesn't run and an error is returned.


##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#restrictions)Restrictions
A single request can only set bids for the same type of objects — either for campaigns only, or for groups only, or for keywords and autotargetings only.
Maximum number of objects per method call:
  * Campaigns: A maximum of `campaign-ids-select`
  * Groups: A maximum of `adgroup-ids-select`
  * Keywords and autotargetings: no more than `ids-select`.


##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#input)Request
Request structure in JSON format:
```
{
  "method": "set",
  "params": { /* params */
    "KeywordBids": [{  /* KeywordBidSetItem */
      "CampaignId": (long),
      "AdGroupId": (long),
      "KeywordId": (long),
      "SearchBid": (long),
      "AutotargetingSearchBidIsAuto" : ("YES"|"NO"),
      "NetworkBid": (long),
      "StrategyPriority": ( "LOW" | "NORMAL" | "HIGH" )
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / SetRequest structure (for SOAP)** |  |  |   
`KeywordBids` |  array of KeywordBidSetItem |  Bids. |  Yes  
**KeywordBidSetItem structure** |  |  |   
`CampaignId` |  long |  The campaign ID. Specify it when you want to set the same bid for all keywords and autotargetings in your campaign. |  Use either `CampaignId` or `AdGroupId` or `KeywordId`  
`AdGroupId` |  long |  ID of the ad group. Specify it when you want to set the same bid for all keywords and autotargetings in an ad group. |   
`KeywordId` |  long |  The keyword ID. Specified when setting a bid or priority for an individual keyword or autotargeting. |   
`SearchBid` |  long |  The bid on search, multiplied by 1,000,000. Integer. Only for manual strategies. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the `Currencies` dictionary name in the request. Copied |  At least one of the parameters: `SearchBid`, `NetworkBid`, `StrategyPriority`, or `AutotargetingSearchBidIsAuto`  
`AutotargetingSearchBidIsAuto` |  YesNoEnum |  A flag indicating whether  You can specify a manual bid (`SearchBid`) and enable automatic bids (`AutotargetingSearchBidIsAuto`) at the same time. In that case, automatic bid will be used, and manual bid will be applied if automatic bid is disabled. If only a manual bid (`SearchBid`) is specified:
  * For an operation specifying `CampaignId` or `AdGroupId`, the automatic bid value won't be reset after this method is used.
  * For an operation specifying `KeywordId`, the automatic bid value will be set to NO. If you want to keep this setting, you need to specify it for the operation with `KeywordId`.

|   
`NetworkBid` |  long |  The bid in ad networks, multiplied by 1,000,000. Integer. Only for manual strategies with independent bid management in ad networks. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the `Currencies` dictionary name in the request. Copied Alert An image ad can be displayed only if the bid is at least as high as the minimum bid for an ad with an image. |   
`StrategyPriority` |  PriorityEnum |  Priority of the keyword: LOW, NORMAL or HIGH. Only for automatic strategies. Alert This parameter is not used, and the passed value is ignored. |   
Alert
The `CampaignId`, `AdGroupId` and `KeywordId` parameters are mutually exclusive. A single request may only contain one of these parameters.
Copied
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "SetResults": [{  /* KeywordBidActionResult */
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ],
      "CampaignId": (long),
      "AdGroupId": (long),
      "KeywordId": (long)
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / SetResponse structure (for SOAP)** |  |   
`SetResults` |  array of KeywordBidActionResult |  The results of the bidding.  
**KeywordBidActionResult structure** |  |   
`CampaignId` |  long |  The campaign ID. Returned if there aren't any errors. See the section   
`AdGroupId` |  long |  ID of the ad group. Returned if there aren't any errors. See the section   
`KeywordId` |  long |  ID of the keyword or autotargeting. Returned if there aren't any errors. See the section   
`Warnings` |  array of  |  Warnings that occurred during the operation.  
`Errors` |  array of  |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set#samples)Example
**Request**
```
    {
      "method" : "set",
      "params" : {
        "KeywordBids" : [
          {
            "StrategyPriority" : "HIGH",
            "CampaignId" : 4193065
          },
          {
            "SearchBid" : 14000,
            "CampaignId" : 7273721
          }
        ]
      }
    }

```

**Response**
```
    {
      "result" : {
        "SetResults" : [
          {
            "CampaignId" : 4193065
          },
          {
            "CampaignId" : 7273721
          }
        ]
      }
    }

```

Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get)
Next
[setAuto](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto)
