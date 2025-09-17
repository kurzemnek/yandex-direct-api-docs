---
title: Bid (KeywordBid) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/bid-priority
crawled_at: 2025-09-17T15:55:47.662196
---

Service
# Bid (KeywordBid)
  * [Service](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority#limits)


You can set a bid for a keyword or autotargeting based on the [display strategy](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign-strategies) of your campaign:
  * If the _HIGHEST_POSITION_ display strategy is chosen for search, the `SearchBid` parameter can be specified.
  * If the _MAXIMUM_COVERAGE_ or _MANUAL_CPM_ display strategy is chosen for ad networks, the `NetworkBid` parameter can be specified.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority#service)Service
You can use the 
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority#methods)Methods
Use the 
  * A separate keyword or autotargeting.
  * All keywords and autotargetings in an ad group.
  * All keywords and autotargetings in a campaign.


The 
The 
Alert
  * Bids and prices are passed via the Yandex Direct API as **integer numbers**. The passed value represents the bid or price **multiplied by 1,000,000**.
  * All bids and prices are shown in the advertiser's currency.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority#limits)Restrictions
The minimum and maximum CPC and CPM bids for each currency are listed in the currency reference. To get the list of currencies, use the `Currencies` in the request.
"Manual bid management with optimization" See the 
"Manual bid management with optimization" with separate bid management for Yandex Search and ad networks See the 
"Manual bid management" (for display campaigns) See the 
Copied
### Was the article helpful?
YesNo
Previous
[Keyword](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword)
Next
[Adjustments (BidModifier)](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier)
