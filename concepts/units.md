---
title: Restrictions, points | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/units
crawled_at: 2025-09-17T15:42:02.654806
---

Technical limitations
# Restrictions, points
  * [Technical limitations](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#general)
  * [Points](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#units-desc)
    * [How points are awarded](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#units-desc1)
    * [How points are spent](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#spend)


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#general)Technical limitations
A maximum of five simultaneous API requests are allowed per advertiser.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#units-desc)Points
Points are used as a way of regulating the load on the API server. If you don't have enough points, you can't make API requests.
“Points” belong to advertisers and agencies. If an API request is made by an advertiser's representative, the points are deducted from the advertiser. If a request is made by an agency's representative, point deduction depends on the `Use-Operator-Units: true` HTTP header. If this header is specified, the points are deducted from the agency. If it is omitted, they are deducted from the advertiser (the agency's client). It doesn't matter which representative of the advertiser or agency is making the request.
The agency makes its own decision on when to spend its own points, and when to spend a client's points. For example, an agency can use its points to:
  * Create advertising campaigns and ads for a new client who hasn't accumulated enough points yet.
  * Manage campaigns for an active client who has run out of points.


Each response to an API request contains the `Units` HTTP header, which shows the number of points:
Spent when running the request/Available balance/Allowed per day.
**Example:**
```
Units: 10/20828/64000

```

The `Units-Used-Login` HTTP response header specifies the username of the representative of an advertiser or agency whose points were deducted for the request.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#units-desc)How points are awarded
Each advertiser (or agency) is given an individual daily limit of points. This limit depends on the activity of advertising campaigns — the number of impressions and clicks, and resulting expenditures.
If the number of impressions and clicks isn't growing much or the campaign is short of funds, frequent and large API requests create an unreasonable load on the Yandex Direct servers. The daily limit is calculated using a grid of budget thresholds based on statistics for different types of campaigns.
The daily limit is divided among 24 hour-long periods and provided on a sliding window principle. At the beginning of each period, the advertiser or agency is given 1/24 of the daily limit. During the current period, the advertiser or agency can spend 1/24 of the daily limit plus the points that were awarded and not spent during the previous 23 hours.
The start time of the hourly period may vary for different advertisers and agencies, and doesn't necessarily coincide with the beginning of the astronomical hour. For example, the periods may begin at 00:18, 01:18, 02:18, and so on.
###  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/units#spend)How points are spent
Points can be deducted for:
  * A successful method call.
  * A method call that finished with an error.
  * Successfully creating or editing an object.
  * Creating or editing an object that led to an error.
  * Getting an object.


The points deducted **for errors** are the same for all services and methods:
  * 20 points per method call that invokes an error (excluding server errors, such as when the server is unavailable).
  * 20 points per operation to create or edit an object that invokes an error.


Points deducted for **successful method calls** and **successful operations with objects** are listed in the table.
**Servicing** |  **Method** |  **Per call** |  **Per object**  
---|---|---|---  
`AdExtensions` |  `add` |  5 |  1  
|  `delete` |  10 |  1  
|  `get` |  5 |  1  
`AdGroups` |  `add` |  20 |  20  
|  `delete` |  10 |  0  
|  `get` |  15 |  1  
|  `update` |  20 |  20  
`AdImages` |  `add` |  20 |  20  
|  `delete` |  10 |  0  
|  `get` |  15 |  1  
`Ads` |  `add` |  20 |  20  
|  `archive` |  15 |  0  
|  `delete` |  10 |  0  
|  `get` |  15 |  1  
|  `moderate` |  15 |  0  
|  `resume` |  15 |  0  
|  `suspend` |  15 |  0  
|  `unarchive` |  40 |  0  
|  `update` |  20 |  20  
`AgencyClients` |  `add` |  10 |  1  
|  `get` |  10 |  1  
|  `update` |  10 |  1  
`AudienceTargets` |  `add` |  10 |  2  
|  `delete` |  10 |  2  
|  `get` |  1 |  1  
|  `resume` |  10 |  2  
|  `setBids` |  10 |  2  
|  `suspend` |  10 |  2  
`Bids` |  `get` |  15 |  3 points per 2000 keywords _*_  
|  `set` |  25 |  0  
|  `setAuto` |  25 |  0  
`BidModifiers` |  `add` |  15 |  1  
|  `delete` |  15 |  0  
|  `get` |  1 |  0  
|  `set` |  2 |  0  
|  `toggle` |  15 |  0  
`Businesses` |  `get` |  10 |  1  
`Campaigns` |  `add` |  10 |  5  
|  `archive` |  10 |  5  
|  `delete` |  10 |  2  
|  `get` |  10 |  1  
|  `resume` |  10 |  5  
|  `suspend` |  10 |  5  
|  `unarchive` |  10 |  5  
|  `update` |  10 |  3  
`Changes` |  `check` |  10 |  0  
|  `checkCampaigns` |  10 |  0  
|  `checkDictionaries` |  10 |  0  
`Clients` |  `get` |  10 |  0  
|  `update` |  10 |  1  
`Creatives` |  `get` |  15 |  1  
`Dictionaries` |  `get` |  1 |  0  
`DynamicTextAdTargets` |  `add` |  20 |  5  
|  `delete` |  10 |  1  
|  `get` |  15 |  1  
|  `resume` |  10 |  1  
|  `setBids` |  25 |  0  
|  `suspend` |  10 |  1  
`Feeds` |  `add` |  20 |  20  
|  `delete` |  10 |  0  
|  `get` |  15 |  1  
|  `update` |  20 |  20  
`KeywordBids` |  `get` |  15 |  3 points per 2000 keywords _*_  
|  `set` |  25 |  0  
|  `setAuto` |  25 |  0  
`Keywords` |  `add` |  20 |  2  
|  `delete` |  10 |  1  
|  `get` |  15 |  3 points for every 2000 keywords when at least one of these parameters is requested: `Productivity`, `StatisticsSearch`, or ` StatisticsNetwork`.  
Otherwise, 1 point for every 2000 keywords.  
|  `resume` |  15 |  0  
|  `suspend` |  15 |  0  
|  `update` |  20 |  2  
`KeywordsResearch` |  `deduplicate` |  10 |  0  
|  `hasSearchVolume` |  1 |  0  
`Leads` |  `get` |  1 |  1  
`NegativeKeywordSharedSets` |  `add` |  20 |  20  
|  `delete` |  10 |  0  
|  `get` |  15 |  1  
|  `update` |  20 |  20  
`RetargetingLists` |  `add` |  10 |  2  
|  `delete` |  10 |  2  
|  `get` |  1 |  1  
|  `update` |  10 |  2  
`Sitelinks` |  `add` |  20 |  20  
|  `delete` |  10 |  0  
|  `get` |  15 |  1  
`SmartAdTargets` |  `add` |  20 |  5  
|  `delete` |  10 |  1  
|  `get` |  15 |  1  
|  `resume` |  10 |  1  
|  `setBids` |  10 |  0  
|  `suspend` |  10 |  1  
|  `update` |  10 |  1  
`TurboPages` |  `get` |  15 |  1  
`vCards` |  `add` |  20 |  20  
|  `delete` |  10 |  0  
|  `get` |  15 |  1  
Note
If less than 2000 keywords were retrieved using the `Bids.get`, `Keywords.get`, or `KeywordBids.get` method, points are only deducted for the method call.
If less than 2000 keywords were retrieved using the Bids.get, Keywords.get, or KeywordBids.get method, points are only deducted for the method call.
Copied
### Was the article helpful?
YesNo
Previous
[Error handling](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/errors)
Next
[General method properties in the API version 5](https://yandex.com/dev/direct/doc/en/concepts/en/best-practice/principles)
