---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywordbids/get
crawled_at: 2025-09-17T15:58:55.021624
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#output)


This method returns bids for keywords and autotargetings that match the specified criteria, along with auction data: bids and actual CPC for various traffic volumes in search results, and bids to reach different audience shares in ad networks.
You can get bids regardless of whether your campaign uses a manual or automatic strategy.
Alert
All returned monetary values are integers — the result of multiplying the bid or CPC by 1,000,000.
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#restrictions)Restrictions
The method returns a maximum of `page-size` objects.
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": { /* KeywordBidsSelectionCriteria */
      "CampaignIds": [(long), ... ],
      "AdGroupIds": [(long), ... ],
      "KeywordIds": [(long), ... ],
      "ServingStatuses": [( "ELIGIBLE" | "RARELY_SERVED" ), ... ]
    }, /* required */
    "FieldNames": [( "KeywordId" | "AdGroupId" | "CampaignId" | "ServingStatus" | "StrategyPriority" ), ... ], /* required */
    "SearchFieldNames": [( "Bid" | "AutotargetingSearchBidIsAuto" | "AuctionBids" ), ... ],
    "NetworkFieldNames": [( "Bid" | "Coverage" ), ... ],
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
`SelectionCriteria` |  KeywordBidsSelectionCriteria |  Criteria for selecting keywords and autotargetings. |  Yes  
`FieldNames` |  array of KeywordBidFieldEnum |  Names of top-level parameters to get. |  Yes  
`SearchFieldNames` |  array of KeywordBidSearchFieldEnum |  Names of search bidding parameters to get. Don't request the `AuctionBids` parameter if impressions in search results are disabled (the SERVING_OFF strategy in Yandex Search). |  No  
`NetworkFieldNames` |  array of KeywordBidNetworkFieldEnum |  Names of ad network bidding parameters to get. Don't request the `Coverage` parameter if impressions in ad networks are disabled (the SERVING_OFF strategy in ad networks). |  No  
`Page` |  |  Structure that defines the page for  |  No  
**KeywordBidsSelectionCriteria structure** |  |  |   
`CampaignIds` |  array of long |  Get bids for keywords and autotargetings in the specified campaigns. From 1 to `campaign-ids-select` items in the array. |  One of the parameters: `KeywordIds`, `AdGroupIds`, or `CampaignIds` (or all may be present)  
`AdGroupIds` |  array of long |  Get bids for keywords and autotargetings in the specified ad groups. From 1 to `adgroup-ids-select` items in the array. |   
`KeywordIds` |  array of long |  Get bids for the specified keywords and autotargetings. A maximum of `ids-select` items in the array. |   
`ServingStatuses` |  array of ServingStatusEnum |  Get bids for keywords and autotargetings with the specified serving statuses of ad groups. For a description of the statuses, see the section  |  No  
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "KeywordBids": [{  /* KeywordBidGetItem */
      "CampaignId": (long),
      "AdGroupId": (long),
      "KeywordId": (long),
      "ServingStatus": ( "ELIGIBLE" | "RARELY_SERVED" ),
      "StrategyPriority": "NORMAL", /* nillable */
      "Search": { /* Search */
        "Bid": (long),
        "AutotargetingSearchBidIsAuto",: ( "YES" | "NO" ),
        "AuctionBids": { /* AuctionBids */
          "AuctionBidItems": [{  /* AuctionBidItem */
            "TrafficVolume": (int), /* required */
            "Bid": (long), /* required */
            "Price": (long) /* required */
          }, ... ]
        } /* nillable */
      },
      "Network": { /* Network */
        "Bid": (long),
        "Coverage": {  /* Coverage */
          "CoverageItems": [{ /* NetworkCoverageItem */
            "Probability": (decimal), /* required */
            "Bid": (long) /* required */
          }, ... ]
        }  /* nillable */
      }
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`KeywordBids` |  array of KeywordBidGetItem |  Bids.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section   
**KeywordBidGetItem structure** |  |   
`CampaignId` |  long |  ID of the campaign that the keyword or autotargeting is associated with.  
`AdGroupId` |  long |  ID of the ad group that the keyword or autotargeting is associated with.  
`KeywordId` |  long |  ID of the keyword or autotargeting.  
`ServingStatus` |  ServingStatusEnum |  Serving status for the ad group. For a description of the statuses, see the section   
`StrategyPriority` |  PriorityEnum, nillable |  Priority of the keyword or autotargeting: NORMAL.  
`Search` |  Search |  Bid and auction data in search.  
`Network` |  Network |  Bid and auction data in ad networks.  
**Search structure** |  |   
`Bid` |  long |  The bid for displays in search results that was set by the advertiser.  
`AutotargetingSearchBidIsAuto` |  YesNoEnum |  A flag indicating whether   
`AuctionBids` |  AuctionBids, nillable |  Bids and actual CPCs in search results for various traffic volumes for this keyword. If the group only has image ads, it returns null (nil). If the ad group has very few impressions (the `ServingStatus` parameter has the value RARELY_SERVED), it returns null (nil). For autotargeting, it returns null (nil).  
**AuctionBids structure** |  |   
`AuctionBidItems` |  array of AuctionBidItem |  Array of bids and actual CPCs in search results for various traffic volumes.  
**AuctionBidItem structure** |  |   
`TrafficVolume` |  int |  Traffic volume.  
`Bid` |  long |  Bid in search for the specified traffic volume.  
`Price` |  long |  The actual CPC for the specified traffic volume.  
**Network structure** |  |   
`Bid` |  long |  The bid for displays in ad networks that was set by the advertiser.  
`Coverage` |  Coverage, nillable |  The bids in ad networks that correspond to various percentages of audience coverage for this keyword.  
If the ad group has very few impressions (the `ServingStatus` parameter has the value RARELY_SERVED), it returns null (nil). If the campaign uses the SERVING_OFF or NETWORK_DEFAULT strategy in ad networks, it returns null (nil). For autotargeting, it returns null (nil).  
**Coverage structure** |  |   
`CoverageItems` |  NetworkCoverageItem |  Array of bids that correspond to various percentages of audience coverage.  
**NetworkCoverageItem structure** |  |   
`Probability` |  decimal |  The frequency of impressions (the audience coverage) in ad networks. Indicated as a percentage from 0 to 100.  
`Bid` |  long |  Bid in ad networks for the specified frequency.  
Copied
### Was the article helpful?
YesNo
Previous
[KeywordBids: managing bids](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/keywordbids)
Next
[set](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set)
