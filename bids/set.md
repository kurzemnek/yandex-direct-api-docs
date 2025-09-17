---
title: set | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/bids/set
crawled_at: 2025-09-17T15:54:19.783305
---

set
# set
  * [Learn more](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#input)
  * [Response](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#samples)


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


Alert
  * Bids and prices are passed via the Yandex Direct API as **integer numbers**. The passed value represents the bid or price **multiplied by 1,000,000**.
  * All bids and prices are shown in the advertiser's currency.


##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#restrictions)Restrictions
A single request can only set bids for the same type of objects — either for campaigns only, or for groups only, or for keywords and autotargetings only.
Maximum number of objects per method call:
  * Campaigns — 10.
  * Groups — 1000.
  * Keywords and autotargetings — 10,000.


##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#input)Request
Request structure in JSON format:
```
{
  "method": "set",
  "params": { /* params */
    "Bids": [{  /* BidSetItem */
      "CampaignId": (long),
      "AdGroupId": (long),
      "KeywordId": (long),
      "Bid": (long),
      "AutotargetingSearchBidIsAuto" : ("YES"|"NO"),
      "ContextBid": (long),
      "StrategyPriority": ( "LOW" | "NORMAL" | "HIGH" )
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / SetRequest structure (for SOAP)**  
`Bids` |  array of BidSetItem |  Bids. |  Yes  
**BidSetItem structure**  
`CampaignId` |  long |  The campaign ID. Specify it when you want to set the same bid for all keywords and autotargetings in your campaign. |  Use either `CampaignId` or `AdGroupId` or `KeywordId`  
`AdGroupId` |  long |  ID of the ad group. Specify it when you want to set the same bid for all keywords and autotargetings in an ad group.  
`KeywordId` |  long |  The keyword ID. Specified when setting a bid or priority for an individual keyword or autotargeting.  
`Bid` |  long |  The bid on search, multiplied by 1,000,000. Integer. Only for manual strategies. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the `Currencies` dictionary name in the request. Copied |  At least one of the parameters: `Bid`, `ContextBid`, `StrategyPriority`, or `AutotargetingSearchBidIsAuto`  
`AutotargetingSearchBidIsAuto` |  YesNoEnum |  A flag indicating whether  You can specify a manual bid (`Bid`) and enable automatic bids (`AutotargetingSearchBidIsAuto`) at the same time. In that case, automatic bid will be used, and manual bid will be applied if automatic bid is disabled. If you've set a manual bid (`Bid`), the automatic bid value (`AutotargetingSearchBidIsAuto`) is set to NO unless you specify a different automatic bid. If you haven't set a manual bid (`Bid`), the automatic bid value (`AutotargetingSearchBidIsAuto`) is set to YES unless you specify a different automatic bid.  
`ContextBid` |  long |  The bid in ad networks, multiplied by 1,000,000. Integer. Only for manual strategies with independent bid management in ad networks. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the `Currencies` dictionary name in the request. Copied Alert An image ad can be displayed only if the bid is at least as high as the minimum bid for an ad with an image.  
`StrategyPriority` |  PriorityEnum |  Priority of the keyword: LOW, NORMAL or HIGH. Only for automatic strategies. Alert This parameter is not used, and the passed value is ignored.  
Alert
The `CampaignId`, `AdGroupId` and `KeywordId` parameters are mutually exclusive. A single request may only contain one of these parameters.
Copied
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "SetResults": [{  /* BidActionResult */
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
**result structure (for JSON) / SetResponse structure (for SOAP)**  
`SetResults` |  array of BidActionResult |  The results of the bidding.  
**BidActionResult structure**  
`CampaignId` |  long |  The campaign ID. Returned if there aren't any errors. See the section   
`AdGroupId` |  long |  ID of the ad group. Returned if there aren't any errors. See the section   
`KeywordId` |  long |  ID of the keyword or autotargeting. Returned if there aren't any errors. See the section   
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/set#samples)Examples
**Request example**
```
{
  "method" : "set",
  "params" : {
    "Bids" : [
      {
        "StrategyPriority" : "HIGH",
        "CampaignId" : 4193065
      },
      {
        "Bid" : 14000,
        "CampaignId" : 7273721
      }
    ]
  }
}

```

**Response example**
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
[get](https://yandex.com/dev/direct/doc/en/bids/en/bids/get)
Next
[setAuto](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto)
