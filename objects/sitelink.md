---
title: Set of sitelinks (SitelinksSet) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/sitelink
crawled_at: 2025-09-17T15:53:59.916151
---

Services
# Set of sitelinks (SitelinksSet)
The SitelinksSet object contains from 1 to 8 additional links. For more information, see [Sitelinks](https://yandex.com/support/direct/efficiency/quick-links.html) in Yandex.Direct Help.
An ad can only have one set of sitelinks (or none). The same set of sitelinks can be assigned to multiple ads.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/sitelink#service)Services
Use the [Sitelinks](https://yandex.com/dev/direct/doc/ref-v5/sitelinks/sitelinks.html) service for creating and deleting sets of sitelinks.
Sitelinks cannot be edited. If you need to change sitelinks, create a new set and assign it to the ad.
Use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service for assigning a set of sitelinks to an ad or unassigning it from an ad. See [Ad extensions](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/launch-campaign#harness).
A set of sitelinks undergoes review only when it is assigned to an ad. See [Result of reviewing add-ons](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#moderate-addon).
A set of sitelinks can be deleted only if it is not assigned to any ads. To get a list of ads that a particular set is assigned to, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service.
### Was the article helpful?
YesNo
Previous
[Ad](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad)
Next
[vCard](https://yandex.com/dev/direct/doc/en/objects/en/objects/vcard)
