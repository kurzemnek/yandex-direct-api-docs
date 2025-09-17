---
title: Parameters of keywords, bids, and position prices | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/phrases
crawled_at: 2025-09-17T15:59:55.620126
---

Parameters of keywords, bids, and position prices
# Parameters of keywords, bids, and position prices
**Parameter name in version Live 4** |  **Parameter name in version 5** |  **Service in version 5**  
---|---|---  
`PhraseID` |  `Id` |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html)  
`Phrase` |  `Keyword` |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html)  
`IsRubric` |  No longer relevant |  —  
`Price` |  `Bid` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`ContextPrice` |  `ContextBid` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`AutoBroker` |  Not supported. When creating keywords using the API, the autobroker is always enabled. |  —  
`UserParams`, with nested `Param1` and `Param2` |  `UserParam1`, `UserParam2` |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html)  
`StatusPhraseModerate` |  `Status` |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html)  
`AutoBudgetPriority` |  `StrategyPriority` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`Clicks`, `Shows` |  `Clicks`, `Impressions` nested in `StatisticsSearch` |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html)  
`ContextClicks`, `ContextShows` |  `Clicks`, `Impressions` nested in `StatisticsNetwork` |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html)  
`Min`, `Max`, `PremiumMin`, `PremiumMax` |  `SearchPrices` array. Names of positions: FOOTERBLOCK, FOOTERFIRST, PREMIUMBLOCK, PREMIUMFIRST. |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`LowCTRWarning`, `LowCTR`, `ContextLowCTR` |  Deprecated |  —  
`Coverage` |  No longer relevant |  —  
`ContextCoverage` |  `ContextCoverage` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`Prices` |  `CompetitorsBids` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`CurrentOnSearch` |  `CurrentSearchPrice` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`MinPrice` |  `MinSearchPrice` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`StatusPaused` |  `State` |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html)  
`Currency` |  Not supported. Bids and costs are always shown in the advertiser's currency. |  —  
`QualityIndex` |  No longer relevant |  —  
**Bid wizard** |  |   
`BannersType` |  No longer relevant |  —  
`PhrasesType` |  `Scope` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`UpdatePhrases`, `UpdateCategories` |  Deprecated |  —  
`MaxPrice` |  `MaxBid` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`PriceBase` |  `Position` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`Proc` |  `IncreasePercent` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`ProcBase` |  `CalculateBy` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`Scope` |  `ContextCoverage` |  [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`DontWaitForPriceUpdate` |  Not supported. The Bid Wizard always updates bids asynchronously |  —  
Copied
### Was the article helpful?
YesNo
Previous
[Parameters of groups and ads](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/banners)
Next
[Parameters of VCards](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/contact-info)
