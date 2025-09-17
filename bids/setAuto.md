---
title: setAuto | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/bids/setAuto
crawled_at: 2025-09-17T15:54:25.367241
---

setAuto
# setAuto
  * [Learn more](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#input)
  * [Response](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#samples)


The automatic bid constructor calculates bids for keywords based on the selected algorithm.
The method sets bids in asynchronous mode and does not return bids. Use the [get](https://yandex.com/dev/direct/doc/en/bids/en/bids/get) method to get bids.
A bid can be set only if a manual strategy is selected in the campaign.
The method doesn't reset the `AutotargetingSearchBidIsAuto`).
If an item in the input array contains bids that are not appropriate for the strategy, these bids are not applied.
  * If the campaign has an automatic strategy selected, an error is returned.
  * If impressions in search results are disabled for the campaign and the `Scope` parameter contains only the SEARCH value, an error is returned. If both values are passed (SEARCH and NETWORK), bids are only updated in ad networks and a warning is displayed.
  * If your campaign uses a manual strategy in search results, you'll receive an error if the bids aren't managed separately in ad networks, or if impressions in ad networks are disabled, but the `Scope` parameter only specifies NETWORK. If both values are passed (SEARCH and NETWORK), bids are only updated in search results and a warning is displayed.


Alert
  * Bids and prices are passed via the Yandex Direct API as **integer numbers**. The passed value represents the bid or price **multiplied by 1,000,000**.
  * All bids and prices are shown in the advertiser's currency.


Calculating bids in search results (Bid)
Calculating bids in ad networks (ContextBid)
To set bids in search results, pass the value SEARCH in the Scope parameter.
The bid calculation uses the values passed in the Position, IncreasePercent, CalculateBy, and MaxBid parameters.
**Position** |  **CalculateBy** |  **Bid calculation formula**  
---|---|---  
FOOTERBLOCK |  VALUE |  Minimum bid for the 4th position in Guaranteed + minimum bid for the 4th position in Guaranteed × `IncreasePercent` / 100, but no greater than `MaxBid`  
DIFF |  Minimum bid for the 4th position in Guaranteed + (minimum bid for the 1st position – minimum bid for the 4th position in Guaranteed) × `IncreasePercent` / 100, but no greater than `MaxBid`  
FOOTERFIRST |  VALUE |  Minimum bid for the 1st position in Guaranteed + Minimum bid for the 1st position in Guaranteed × `IncreasePercent` / 100, but no greater than `MaxBid`  
DIFF |  Minimum bid for the 1st position in Guaranteed + (minimum bid for the 3rd position in Premium – minimum bid for the 1st position in Guaranteed) × `IncreasePercent` / 100, but no greater than `MaxBid`  
PREMIUMBLOCK or P14 |  VALUE |  Minimum bid for the 4th position in Premium + Minimum bid for the 4th position in Premium × `IncreasePercent` / 100, but no greater than `MaxBid`  
DIFF |  Minimum bid for the 4th position in Premium + (minimum bid for the 3rd position in Premium – minimum bid for the 4th position in Premium) × `IncreasePercent` / 100, but no greater than `MaxBid`  
P13 |  VALUE |  Minimum bid for the 3rd position in Premium + Minimum bid for the 3rd position in Premium × `IncreasePercent` / 100, but no greater than `MaxBid`  
DIFF |  Minimum bid for the 3rd position in Premium + (Minimum bid for the 2nd position in Premium – Minimum bid for the 3rd position in Premium) × `IncreasePercent` / 100, but no greater than `MaxBid`  
P12 |  VALUE |  Minimum bid for the 2nd position in Premium + Minimum bid for the 2nd position in Premium × `IncreasePercent` / 100, but no greater than `MaxBid`  
DIFF |  Minimum bid for the 2nd position in Premium + (minimum bid for the 1st position in Premium – minimum bid for the 2nd position in Premium) × `IncreasePercent` / 100, but no greater than `MaxBid`  
PREMIUMFIRST or P11 |  VALUE |  Minimum bid for the 1st position in Premium + minimum bid for the 1st position in Premium × `IncreasePercent` / 100, but no greater than `MaxBid`  
DIFF |  Minimum bid for the 1st position in Premium, but no greater than `MaxBid`  
Note
Over time, competitors' activity might increase the minimum bid for a position, and it will be higher than the advertiser's bid. The higher the markup, the more likely it is that the ad will be shown in the selected position, but expenses are also greater.
You can only set the bid in ad networks for strategies that allow separate management of bids in search results and ad networks.
To set bids in ad networks, pass the value NETWORK in the Scope parameter.
Bid calculation uses the values passed in the ContextCoverage, IncreasePercent, and MaxBid parameters.
Bid calculation formula:
Bid predicted to produce the specified impression frequency + bid predicted to produce the specified impression frequency × `IncreasePercent` / 100,
but no greater than `MaxBid`.
Note
Bid calculation is based on probability, and does not guarantee the desired audience coverage.
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#restrictions)Restrictions
A single request can only set bids for the same type of objects — either for campaigns only, or for groups only, or for keywords only. The method doesn't support setting the bid for autotargeting separately.
Maximum number of objects per method call:
  * Campaigns — 10.
  * Groups — 1000.
  * Keywords — 10,000.


##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#input)Request
Request structure in JSON format:
```
{
  "method": "setAuto",
  "params": { /* params */
    "Bids": [{  /* BidSetAutoItem */
      "CampaignId": (long),
      "AdGroupId": (long),
      "KeywordId": (long),
      "MaxBid": (long),
      "Position": ( "PREMIUMFIRST" | "PREMIUMBLOCK" | "FOOTERFIRST" | "FOOTERBLOCK" | "P11" | "P12" | "P13" | "P14" | "P21" | "P22" | "P23" | "P24" ),
      "IncreasePercent": (int),
      "CalculateBy": ( "VALUE" | "DIFF" ),
      "ContextCoverage": (int),
      "Scope": [( "SEARCH" | "NETWORK" ), ... ] /* required */
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / SetAutoRequest structure (for SOAP)**  
`Bids` |  array of BidSetAutoItem |  Bid calculation parameters |  Yes  
**BidSetAutoItem structure**  
`CampaignId` |  long |  The campaign ID. Specified when updating the bid for all the campaign's keywords. |  Use either `CampaignId` or `AdGroupId` or `KeywordId`  
`AdGroupId` |  long |  ID of the ad group. Specified when the bid needs to be updated for all the group's keywords.  
`KeywordId` |  long |  The keyword ID. Specified when updating the bid for an individual keyword. Alert The autotargeting ID is not allowed.  
`Scope` |  array of ScopeEnum |  Specifies which bids to set. The array may contain the following elements (one or both):
  * SEARCH: Set bids in search results (`Bid`). Bid calculation uses the values passed in the Position, IncreasePercent, CalculateBy, and MaxBid parameters.
  * NETWORK: Set bids in ad networks (`ContextBid`). Bid calculation uses the values passed in the ContextCoverage, IncreasePercent, and MaxBid parameters.

|  Yes  
`MaxBid` |  long |  The bid limit multiplied by 1,000,000. Integer. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the `Currencies` dictionary name in the request. Copied |  No  
`Position` |  PositionEnum |  The display position whose bid is used as the basis for calculating bids in search results. A markup is added to the bid for the selected position (see the `IncreasePercent` and `CalculateBy` parameters). |  If the `Scope` array contains the `Search` value  
`IncreasePercent` |  int |  Markup percent from 0 to 1000. If omitted, markup is not calculated. |  No  
`CalculateBy` |  CalculateByEnum |  The base for calculating the markup:
  * VALUE: Price of the position specified in `Position`.
  * DIFF: Difference between the minimum bid for the position specified in the `Position` parameter and for the next position. When the PREMIUMFIRST (P11) position is selected, there is no next position, and the markup is zero. This is also true when the FOOTERFIRST (P21) position is selected, if the price of the next PREMIUMBLOCK (P14) position is less (rare but possible).

|  If the `Scope` array contains the `Search` value and the `IncreasePercent` parameter is set  
`ContextCoverage` |  int |  The frequency of impressions (the audience coverage) in ad networks. Indicated as a percentage from 0 to 100. A markup is added to the bid that is required to get the selected audience coverage (see the `IncreasePercent` parameter). |  If the `Scope` array contains the `Network` value  
Alert
The `CampaignId`, `AdGroupId`, and `KeywordId` parameters are mutually exclusive. A single request may only contain one of these parameters.
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "SetAutoResults": [{  /* BidActionResult */
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
**result structure (for JSON) / SetAutoResponse structure (for SOAP)**  
`SetAutoResults` |  array of BidActionResult |  The results of the bidding.  
**BidActionResult structure**  
`CampaignId` |  long |  The campaign ID. Returned if there aren't any errors. See the section   
`AdGroupId` |  long |  ID of the ad group. Returned if there aren't any errors. See the section   
`KeywordId` |  long |  Keyword ID. Returned if there aren't any errors. See the section   
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/bids/en/bids/setAuto#samples)Examples
**Request example**
Set the price in search results of the 1st position in Guaranteed + 50% of the difference from Premium, but no greater than 0.25.
```
{
  "method" : "setAuto",
  "params" : {
    "Bids" : [
      {
        "Scope" : [
          "SEARCH"
        ],
        "IncreasePercent" : 50,
        "CalculateBy" : "DIFF",
        "Position" : "FOOTERFIRST",
        "KeywordId" : 1574449505,
        "MaxBid" : 250000
      }
    ]
  }
}

```

**Response example**
```
{
  "result" : {
    "SetAutoResults" : [
      {
        "KeywordId" : 1574449505
      }
    ]
  }
}

```

Copied
### Was the article helpful?
YesNo
Previous
[set](https://yandex.com/dev/direct/doc/en/bids/en/bids/set)
Next
[Businesses: getting business profiles](https://yandex.com/dev/direct/doc/en/bids/en/businesses/businesses)
