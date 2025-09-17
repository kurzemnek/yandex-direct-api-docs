---
title: Parameters of groups and ads | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/banners
crawled_at: 2025-09-17T15:58:31.040279
---

Parameters of groups and ads
# Parameters of groups and ads
**Parameter name in version Live 4** |  **Parameter name in version 5** |  **Service in version 5**  
---|---|---  
`AdGroupID` |  `Id` |  [AdGroups](https://yandex.com/dev/direct/doc/ref-v5/adgroups/adgroups.html)  
`AdGroupName` |  `Name` |  [AdGroups](https://yandex.com/dev/direct/doc/ref-v5/adgroups/adgroups.html)  
`BannerID` |  `Id` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`Title` |  `Title` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`Text` |  `Text` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`Href` |  `Href` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`Domain` |  `DisplayDomain` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`Geo` |  `RegionIds` |  [AdGroups](https://yandex.com/dev/direct/doc/ref-v5/adgroups/adgroups.html)  
`ContactInfo` and nested elements |  See [Parameters of VCards](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/contact-info) |  [vCards](https://yandex.com/dev/direct/doc/ref-v5/vcards/vcards.html)  
`Phrases` |  See [Parameters of keywords, bids, and position prices](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/phrases) |  [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html) and [Bids](https://yandex.com/dev/direct/doc/ref-v5/bids/bids.html)  
`StatusActivating`, `StatusArchive`, `StatusBannerModerate`, `StatusShow`, `IsActive` |  `Status`, `StatusClarifications`, and `State` (for more information, see the [Ad](https://yandex.com/dev/direct/doc/dg/objects/ad.html) section) |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`StatusPhrasesModerate` |  `Status` |  [AdGroups](https://yandex.com/dev/direct/doc/ref-v5/adgroups/adgroups.html)  
`StatusPhoneModerate` |  `VCardModeration` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`StatusAdImageModerate` |  `AdImageModeration` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`StatusSitelinksModerate` |  `SitelinksModeration` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`Sitelinks` |  Parameters of sitelink sets |  [Sitelinks](https://yandex.com/dev/direct/doc/ref-v5/sitelinks/sitelinks.html)  
`AdWarnings` |  `AdCategories` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`FixedOnModeration` |  No longer relevant |  —  
`ModerateRejectionReasons` |  `StatusClarification` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`MinusKeywords` |  `NegativeKeywords` |  [AdGroups](https://yandex.com/dev/direct/doc/ref-v5/adgroups/adgroups.html)  
`AgeLabel` |  `AgeLabel` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`AdImageHash` |  `AdImageHash` |  [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html)  
`AutoMinusWords` |  Not supported |  —  
Copied
### Was the article helpful?
YesNo
Previous
[Campaign parameters](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/campaigns)
Next
[Parameters of keywords, bids, and position prices](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/phrases)
