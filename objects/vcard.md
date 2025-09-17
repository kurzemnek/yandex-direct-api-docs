---
title: vCard | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/vcard
crawled_at: 2025-09-17T15:52:16.613472
---

Servicing
# vCard
The virtual business card (VCard) object contains the advertiser's contact information. For more information, see [vCards](https://yandex.com/support/direct/efficiency/vcards.html) in the Help for Yandex.Direct.
An ad can only have one vCard (or none). You can add the same vCard to multiple ads.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/vcard#service)Servicing
Use the [VCards](https://yandex.com/dev/direct/doc/ref-v5/vcards/vcards.html) service for creating and deleting vCards.
You can't edit vCards. If you need to change the vCard, create a new one and assign it to the ad.
To add a vCard to an ad or remove it from an ad, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service. See [Ad extensions](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/launch-campaign#harness).
A vCard undergoes review only when it is assigned to an ad. See [Result of reviewing add-ons](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#moderate-addon).
You can delete a vCard only if it is not assigned to any ads. To get a list of ads that a particular vCard is assigned to, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service.
### Was the article helpful?
YesNo
Previous
[Set of sitelinks (SitelinksSet)](https://yandex.com/dev/direct/doc/en/objects/en/objects/sitelink)
Next
[Image (AdImage)](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage)
