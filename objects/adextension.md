---
title: Extension (AdExtension) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/adextension
crawled_at: 2025-09-17T15:49:27.043688
---

Servicing
# Extension (AdExtension)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension#service)
  * [Status of an extension](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension#status)
  * [State of an extension](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension#state)


Only one type of extension is currently supported, the callout.
A callout contains additional text for the ad. For more information, see [Callouts](https://yandex.com/support/direct/efficiency/callout.html) in the Help for Yandex.Direct.
You can assign up to 50 callouts to an ad. When the ad is displayed, it shows all the callouts that fit in a single line (66 characters). You can assign the same callout to multiple ads.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension#service)Servicing
Use the [AdExtensions](https://yandex.com/dev/direct/doc/ref-v5/adextensions/adextensions.html) service for creating extensions.
Extensions can't be edited. If you need to change an extension for an ad, create a new extension and assign it to the ad, then unassign the previous extension.
To assign an extension to an ad or unassign one from an ad, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service. See [Ad extensions](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/launch-campaign#harness).
You can delete an extension only if it is not assigned to any ads. To get a list of ads that a particular extension is assigned to, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension#status)Status of an extension
The `Status` parameter reflects the result of reviewing the extension.
**Status** |  **Description**  
---|---  
DRAFT |  The extension has been created but has not yet been submitted for review.  
MODERATION |  The extension is under review.  
ACCEPTED |  The extension was accepted after review.  
REJECTED |  The extension was rejected after review.  
UNKNOWN |  The status is unknown. This value is used for backward compatibility and for displaying statuses that are not supported in this version of the API.  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension#state)State of an extension
The `State` parameter reflects the current state of the extension.
**Status** |  **Description**  
---|---  
ON |  The extension can be displayed.  
DELETED |  The owner deleted the extension. Note The [get](https://yandex.com/dev/direct/doc/ref-v5/adextensions/get.html) method returns an extension in the DELETED state only if the `States` parameter is set to DELETED or the ID of this extension is specified in the `Ids` parameter. If the `Ids` and `States` parameters are both omitted, the method doesn't return extensions in the DELETED state.  
UNKNOWN |  The status is unknown. Used for providing backward compatibility and displaying states that are not supported in this version of the API.  
Copied
### Was the article helpful?
YesNo
Previous
[Creative (Creative)](https://yandex.com/dev/direct/doc/en/objects/en/objects/creative)
Next
[Turbo page (TurboPage)](https://yandex.com/dev/direct/doc/en/objects/en/objects/turbo-page)
