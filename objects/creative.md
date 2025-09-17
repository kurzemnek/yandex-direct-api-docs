---
title: Creative (Creative) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/creative
crawled_at: 2025-09-17T15:52:28.666018
---

Servicing
# Creative (Creative)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/creative#service)
  * [Type of creative](https://yandex.com/dev/direct/doc/en/objects/en/objects/creative#types)


The Creative object contains the parameters of a creative that was created in Ad Builder.
The same creative can be used in multiple ads.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/creative#service)Servicing
You can build creatives only in the Yandex Direct web interface, an exception are creatives for video extensions that can be created in the [Creatives](https://yandex.com/dev/direct/doc/ref-v5/creatives/creatives.html) service by the [add](https://yandex.com/dev/direct/doc/ref-v5/creatives/add.html) method. You can't edit creatives.
To get creatives, use the [Creatives](https://yandex.com/dev/direct/doc/ref-v5/creatives/creatives.html) service and the [get](https://yandex.com/dev/direct/doc/ref-v5/creatives/get.html) method.
To create an ad with a creative, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html).[add](https://yandex.com/dev/direct/doc/ref-v5/ads/add.html) method. To replace the creative in an ad, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html).[update](https://yandex.com/dev/direct/doc/ref-v5/ads/update.html) method.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/creative#types)Type of creative
The following types of creatives are currently available in the Yandex Direct API:
**Type of creative** |  **Suitable for ad types** |  **Description**  
---|---|---  
IMAGE_CREATIVE |  IMAGE_AD with subtypes TEXT_AD_BUILDER_AD and MOBILE_APP_AD_BUILDER_AD CPM_BANNER_AD |  Image creative. See [Creative Ad Builder](https://yandex.com/support/direct/products-image-ads/builder.html) in Yandex Direct Help.  
HTML5_CREATIVE |  CPM_BANNER_AD |  HTML5 banner or image banner in JPG, PNG or GIF format, uploaded as a file.  
VIDEO_EXTENSION_CREATIVE |  TEXT_AD |  Creative for video extensions. See [Creative Ad Builder for video extensions](https://yandex.com/support/direct/features/video-extension-builder.html) in Yandex Direct Help.  
CPC_VIDEO_CREATIVE |  CPC_VIDEO_AD |  Creative for video ads in the “Text & Image Ads” campaigns. See the section [Video ads / Creative Ad Builder](https://yandex.com/support/direct/products-video-ads/builder.html) in the Help for Yandex Direct.  
CPM_VIDEO_CREATIVE |  CPM_VIDEO_AD |  Creative for video ads in display campaigns. See [Video advertising / How to launch](https://yandex.com/support/direct/products-cpm-campaign-video/create.html) in Yandex Direct Help.  
SMART_CREATIVE |  SMART_AD |  Creative for smart banners in the “Smart banners” campaigns. See [Smart banners](https://yandex.com/support/direct/smart-banners/about.html) in Yandex Direct Help.  
### Was the article helpful?
YesNo
Previous
[Video (AdVideo)](https://yandex.com/dev/direct/doc/en/objects/en/objects/advideos)
Next
[Extension (AdExtension)](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension)
