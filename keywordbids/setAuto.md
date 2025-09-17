---
title: setAuto | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywordbids/setAuto
crawled_at: 2025-09-17T15:59:07.569490
---

setAuto
# setAuto
  * [Learn more](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#samples)


Sets bids for keywords on search depending on the desired traffic volume, or bids in ad networks depending on the desired frequency of impressions (audience share).
Bid calculation formula:
In search results
In ad networks
The bid that corresponds to the traffic volume [TargetTrafficVolume](*TargetTrafficVolume) × (1 + [IncreasePercent](*IncreasePercent) / 100),
but no more than [BidCeiling](*BidCeiling).
Over time, competitors' activity might increase the bid for a certain traffic volume, and it will go higher than the advertiser's bid. The higher the markup, the higher the traffic volume, but spending also increases.
The bid that corresponds to the impression frequency [TargetCoverage](*TargetCoverage) × (1 + [IncreasePercent](*IncreasePercent) / 100),
but no more than [BidCeiling](*BidCeiling).
Over time, competitors' activity might increase the bid for the desired coverage, and it will be higher than the advertiser's bid. The higher the markup, the higher the frequency of impressions, but spending also might increase.
The method does not return the assigned bids, but you can get them using the [get](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/get) method.
The method doesn't reset the `AutotargetingSearchBidIsAuto`).
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#learn-more)Learn more
  * [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)


##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#restrictions)Restrictions
You can specify the bid for search results only if the campaign uses the HIGHEST_POSITION strategy for impressions in search results. Otherwise, an error is returned.
You can specify the bid for ad networks only if the campaign uses the MAXIMUM_COVERAGE or MANUAL_CPM strategy for impressions in ad networks. Otherwise, an error is returned.
A single request can only set bids for the same type of objects — either for campaigns only, or for groups only, or for keywords only.
The method doesn't support setting the bid for autotargeting separately. Changing bids in search for all the keywords in an ad group or campaign may affect the autotargeting bid.
Maximum number of objects per method call:
  * Campaigns: A maximum of `campaign-ids-select`
  * Groups: A maximum of `adgroup-ids-select`
  * Keywords: A maximum of `ids-select`.


##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#input)Request
Request structure in JSON format:
```
{
  "method": "setAuto",
  "params": { /* params */
    "KeywordBids": [{  /* KeywordBidSetAutoItem */
      "CampaignId": (long),
      "AdGroupId": (long),
      "KeywordId": (long),
      "BiddingRule": { /* BiddingRule */
        "SearchByTrafficVolume": { /* SearchByTrafficVolume */
          "TargetTrafficVolume": (int), /* required */
          "IncreasePercent": (int),
          "BidCeiling": (long)
        },
        "NetworkByCoverage": { /* NetworkByCoverage */
          "TargetCoverage": (int), /* required */
          "IncreasePercent": (int),
          "BidCeiling": (long)
        }
      } /* required */
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / SetAutoRequest structure (for SOAP)** |  |  |   
`KeywordBids` |  array of KeywordBidSetAutoItem |  Bid calculation parameters |  Yes  
**KeywordBidSetAutoItem structure** |  |  |   
`CampaignId` |  long |  The campaign ID. Specified when updating the bid for all the campaign's keywords. |  Use either `CampaignId` or `AdGroupId` or `KeywordId`  
`AdGroupId` |  long |  ID of the ad group. Specified when the bid needs to be updated for all the group's keywords. |   
`KeywordId` |  long |  The keyword ID. Specified when updating the bid for an individual keyword. Alert The autotargeting ID is not allowed. |   
`BiddingRule` |  BiddingRule |  Parameters for calculating bids. |  Yes  
**BiddingRule structure** |  |  |   
`SearchByTrafficVolume` |  SearchByTrafficVolume |  Parameters for calculating bids in search results. |  Use either `SearchByTrafficVolume` or `NetworkByCoverage`  
`NetworkByCoverage` |  NetworkByCoverage |  Parameters for calculating bids in ad networks. |   
**SearchByTrafficVolume structure** |  |  |   
`TargetTrafficVolume` |  int |  The desired traffic volume in search results. Indicated as a percentage from 5 to 100. A markup is added to the bid that corresponds to the selected traffic volume (see the `IncreasePercent` parameter). |  Yes  
`IncreasePercent` |  int |  Markup percent from 0 to 1000. If omitted, markup is not calculated. |  No  
`BidCeiling` |  long |  The bid limit multiplied by 1,000,000. Integer. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/keywordbids/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/keywordbids/en/dictionaries/get) method and specify the `Currencies` dictionary name in the request. Copied |  No  
**NetworkByCoverage structure** |  |  |   
`TargetCoverage` |  int |  The desired frequency of impressions (the audience coverage) in ad networks. Indicated as a percentage from 0 to 100. A markup is added to the bid that corresponds to the selected impression frequency (see the `IncreasePercent` parameter). |  Yes  
`IncreasePercent` |  int |  Markup percent from 0 to 1000. If omitted, markup is not calculated. |  No  
`BidCeiling` |  long |  The bid limit multiplied by 1,000,000. Integer. Specified in the advertiser's currency. Restrictions are listed in the currency reference. To get it, use the `Currencies` dictionary name in the request. Copied |  No  
Alert
The `CampaignId`, `AdGroupId`, and `KeywordId` parameters are mutually exclusive. A single request may only contain one of these parameters.
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "SetAutoResults": [{  /* KeywordBidActionResult */
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
**result structure (for JSON) / SetAutoResponse structure (for SOAP)** |  |   
`SetAutoResults` |  array of KeywordBidActionResult |  The results of the bidding.  
**KeywordBidActionResult structure** |  |   
`CampaignId` |  long |  The campaign ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) (if it was specified in the request).  
`AdGroupId` |  long |  ID of the ad group. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) (if it was specified in the request).  
`KeywordId` |  long |  Keyword ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) (if it was specified in the request).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/setAuto#samples)Examples
**Request example**
Sets the bid in search for all keywords in an ad group to get the traffic volume of 75, increased by 10%, but not more than 12.
```
    {
      "method": "setAuto",
      "params": {
        "KeywordBids": [{
          "AdGroupId": 636056397,
          "BiddingRule": {
            "SearchByTrafficVolume": {
              "TargetTrafficVolume": 75,
              "IncreasePercent": 10,
              "BidCeiling": 12000000,
            }
          }
        }]
      }
    }

```

**Response example**
```
    {
      "result" : {
        "SetAutoResults" : [
          {
            "AdGroupId" : 636056397
          }
        ]
      }
    }

```

Copied
### Was the article helpful?
YesNo
Previous
[set](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywordbids/set)
Next
[Keywords: managing keywords and autotargetings](https://yandex.com/dev/direct/doc/en/keywordbids/en/keywords/keywords)
