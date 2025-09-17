---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/bids/get
crawled_at: 2025-09-17T15:54:30.913552
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#samples)


This method returns bids for keywords and autotargetings that match the specified criteria, along with data that can improve bid selection: auction data for display positions in search results, and bids to reach various audience shares in ad networks.
You can get bids regardless of whether your campaign uses a manual or automatic strategy.
Alert
All returned monetary values are integers — the result of multiplying the bid or CPC by 1,000,000.
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#restrictions)Restrictions
The method returns a maximum of 10,000 objects.
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* BidsSelectionCriteria */
      "KeywordIds": [(long), ... ],
      "AdGroupIds": [(long), ... ],
      "CampaignIds": [(long), ... ],
      "ServingStatuses": [( "ELIGIBLE" | "RARELY_SERVED" ), ... ]
    }, /* required */
    "FieldNames": [( "KeywordId" | ... | "AuctionBids" ), ... ], /* required */
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
`SelectionCriteria` |  BidsSelectionCriteria |  Criteria for selecting keywords and autotargetings. |  Yes  
`FieldNames` |  array of BidFieldEnum |  Names of top-level parameters to get. Don't request the parameters `CompetitorsBids`, `SearchPrices`, `MinSearchPrice`, `CurrentSearchPrice`, and `AuctionBids` if impressions in search results are disabled for the campaign (the SERVING_OFF strategy for search results). Don't request the `ContextCoverage` parameter if impressions in ad networks are disabled for the campaign (the SERVING_OFF strategy in ad networks). |  Yes  
`Page` |  LimitOffset |  Structure that defines the page for  |  No  
**BidsSelectionCriteria structure**  
`KeywordIds` |  array of long |  Get bids for the specified keywords and autotargetings. Maximum of 10,000 items in the array. |  One of the parameters: `KeywordIds`, `AdGroupIds`, or `CampaignIds` (or all may be present)  
`AdGroupIds` |  array of long |  Get bids for keywords and autotargetings in the specified ad groups. From 1 to 1000 items in the array.  
`CampaignIds` |  array of long |  Get bids for keywords and autotargetings in the specified campaigns. From 1 to 10 items in the array.  
`ServingStatuses` |  array of ServingStatusEnum |  Get bids for keywords and autotargetings with the specified serving statuses of ad groups. For a description of the statuses, see the section  |  No  
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Bids": [{  /* BidGetItem */
      "CampaignId": (long),
      "AdGroupId": (long),
      "KeywordId": (long),
      "ServingStatus": ( "ELIGIBLE" | "RARELY_SERVED" ),
      "Bid": (long),
      "AutotargetingSearchBidIsAuto" : ("YES"|"NO"),
      "ContextBid": (long),
      "StrategyPriority": "NORMAL", /* nillable */
      "CompetitorsBids": [(long), ... ],
      "SearchPrices": [{  /* SearchPrices */
        "Position": ( "PREMIUMFIRST" | "PREMIUMBLOCK" | "FOOTERFIRST" | "FOOTERBLOCK" ),
        "Price": (long)
      }, ... ],
      "ContextCoverage": {  /* ContextCoverage */
        "Items": [{  /* ContextCoverageItem */
          "Probability": (decimal), /* required */
          "Price": (long) /* required */
        }, ... ]
      }, /* nillable */
      "MinSearchPrice": (long), /* nillable */
      "CurrentSearchPrice": (long), /* nillable */
      "AuctionBids": [{  /* AuctionBidItem */
        "Position": (string),
        "Bid": (long),
        "Price": (long)
      }, ... ]
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`Bids` |  array of BidGetItem |  Bids.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section   
**BidGetItem structure**  
`CampaignId` |  long |  ID of the campaign that the keyword or autotargeting is associated with.  
`AdGroupId` |  long |  ID of the ad group that the keyword or autotargeting is associated with.  
`KeywordId` |  long |  ID of the keyword or autotargeting.  
`ServingStatus` |  ServingStatusEnum |  Serving status for the ad group. For a description of the statuses, see the section   
`Bid` |  long |  Bid in search results.  
`AutotargetingSearchBidIsAuto` |  YesNoEnum |  A flag indicating whether   
`ContextBid` |  long |  Bid in ad networks.  
`StrategyPriority` |  PriorityEnum, nillable |  Priority of the keyword or autotargeting: NORMAL.  
`CompetitorsBids` |  array of long |  Array of minimum bids for this keyword for all positions in Premium Placement and Guaranteed Placement. If the ad group has very few displays (the `ServingStatus` parameter has the value RARELY_SERVED), the parameter isn't returned. Copied For autotargeting, this parameter isn't returned.  
`SearchPrices` |  array of SearchPrices |  Minimum bids for this keyword for display positions in the search. If the ad group has very few displays (the `ServingStatus` parameter has the value RARELY_SERVED), the parameter isn't returned. Copied For autotargeting, this parameter isn't returned.  
`ContextCoverage` |  ContextCoverage, nillable |  Bids for this keyword that allow you to get various percentages of audience coverage in ad networks (forecast). Used as a guide when selecting bids. If the ad group has very few impressions (the `ServingStatus` parameter has the value RARELY_SERVED), it returns null (nil). If the campaign uses the SERVING_OFF or NETWORK_DEFAULT strategy in ad networks, it returns null (nil). For autotargeting, it returns null (nil).  
`MinSearchPrice` |  long, nillable |  The minimum bid set for the advertiser that allows displays in search results. If the ad group has very few impressions (the `ServingStatus` parameter has the value RARELY_SERVED), it returns null (nil). For autotargeting, it returns null (nil).  
`CurrentSearchPrice` |  long, nillable |  Current CPC in search results. This amount can be debited whenever your ad is clicked on a page showing search results for a query that exactly matches the keyword. To learn more, see  If the ad group has very few displays (the `ServingStatus` parameter has the value RARELY_SERVED), it returns null (nil). Copied For autotargeting, it returns null (nil).  
`AuctionBids` |  array of AuctionBidItem |  Auction results for the keyword. If the group only has image ads, this parameter is not returned. If the ad group has very few displays (the `ServingStatus` parameter has the value RARELY_SERVED), the parameter isn't returned. Copied For autotargeting, this parameter isn't returned.  
**SearchPrices structure**  
`Position` |  PositionEnum |  Display position in search results:
  * FOOTERBLOCK — Minimum bid for the 4th position in Guaranteed (for getting into Guaranteed Placement).
  * FOOTERFIRST — Minimum bid for the 1st position in Guaranteed.
  * PREMIUMBLOCK — Minimum bid for the 4th position in Premium Placement (for getting into Premium Placement).
  * PREMIUMFIRST — Minimum bid for the 1st position in Premium Placement.

  
`Price` |  long |  Minimum bid for the specified position.  
**ContextCoverage structure**  
`Items` |  array of ContextCoverageItem |  Bids for this keyword that allow you to get various percentages of audience coverage in ad networks (forecast). Used as a guide when selecting bids.  
**ContextCoverageItem structure**  
`Probability` |  decimal |  The frequency of impressions (the audience coverage) in ad networks. Indicated as a percentage from 0 to 100.  
`Price` |  long |  Bid in ad networks that the specified frequency is forecast for.  
**AuctionBidItem structure**  
`Position` |  string |  Display position: Pmn, where
  * _m_ is the block number (1 is Premium Placement, 2 is Guaranteed Placement).
  * _n_ is the position number within the block.

For example, P12 is the 2nd position in Premium Placement, and P21 is the 1st position in Guaranteed Placement.  
`Bid` |  long |  Minimum bid for the specified position.  
`Price` |  long |  Actual CPC for the specified position.  
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/get#samples)Examples
**Request example**
```
{
  "method" : "get",
  "params" : {
    "SelectionCriteria" : {
      "KeywordIds" : [
        151289987,
        151289988,
        414808783,
        414808784,
        414808785,
        414811825,
        414811826,
        414811827,
        1574449505
      ]
    },
    "FieldNames" : [
      "KeywordId",
      "Bid",
      "ContextBid"
    ]
  }
}

```

**Response example**
```
{
  "result" : {
    "Bids" : [
      {
        "KeywordId" : 414808783,
        "Bid" : 10000,
        "ContextBid" : 0
      },
      {
        "Bid" : 10000,
        "KeywordId" : 414808784,
        "ContextBid" : 0
      },
      {
        "Bid" : 10000,
        "KeywordId" : 414808785,
        "ContextBid" : 0
      },
      {
        "Bid" : 10000,
        "KeywordId" : 1574449505,
        "ContextBid" : 0
      }
    ]
  }
}

```

Copied
### Was the article helpful?
YesNo
Previous
[Bids: managing bids](https://yandex.com/dev/direct/doc/en/bids/en/bids/bids)
Next
[set](https://yandex.com/dev/direct/doc/en/bids/en/bids/set)
