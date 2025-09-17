---
title: Image (AdImage) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/adimage
crawled_at: 2025-09-17T15:49:21.927838
---

Servicing
# Image (AdImage)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#service)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#restrictions)
  * [Requirements for images uploaded via the API](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#requirements)
  * [Type of image](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#type)


The Image (AdImage) object contains an image. The _AdImageHash_ parameter is used as the image identifier.
An ad can only have one image (or none at all). You can assign the same image to multiple ads. For more information, see [Images in ads](https://yandex.com/support/direct/efficiency/images.html) in Yandex Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#service)Servicing
Use the [AdImages](https://yandex.com/dev/direct/doc/ref-v5/adimages/adimages.html) service for uploading images as binary data, as well as for deleting images. To upload images asynchronously from a list of URLs, use the [Upload](https://yandex.com/dev/direct/doc/dg-v4/live/AdImage_Upload.html) action for the [AdImage (Live)](https://yandex.com/dev/direct/doc/dg-v4/live/AdImage.html) method in the Live 4 version of the API.
Images can't be edited. If you need to change an image, you must upload a new image and assign it to the ad.
To assign an image to an ad or unassign one from an ad, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service. See [Ad extensions](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/launch-campaign#harness).
An image undergoes review only when it is assigned to an ad. See [Result of reviewing add-ons](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#moderate-addon).
You can delete an image only if it is not assigned to any ads. To get a list of ads that a particular image is assigned to, use the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html) service.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#restrictions)Restrictions
The maximum number of images per advertiser is 1000 + 2 × the number of ads.
To check how many images a client can upload and how many have already been uploaded or are being uploaded, use the [GetLimits](https://yandex.com/dev/direct/doc/dg-v4/live/AdImage_GetLimits.html) action for the [AdImage (Live)](https://yandex.com/dev/direct/doc/dg-v4/live/AdImage.html) method in the Live 4 version of the API.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#requirements)Requirements for images uploaded via the API
  * Allowed image formats: JPG, PNG, GIF.
  * Acceptable image sizes for image ads:
    * 240 × 400, 300 × 250, 300 × 500, 300 × 600, 320 × 50, 320 × 100, 320 × 480, 336 × 280, 480 × 320, 480 × 800, 600 × 500, 600 × 1000, 600 × 1200, 640 × 100, 640 × 200, 640 × 960, 672 × 560, 720 × 1200, 728 × 90, 900 × 750, 900 × 1500, 900 × 1800, 960 × 150, 960 × 300, 960 × 640, 960 × 1440, 960 × 1600, 970 × 250, 1008 × 840, 1200 × 1000, 1200 × 2000, 1200 × 2400, 1280 × 200, 1280 × 400, 1280 × 1920, 1344 × 1120, 1440 × 960, 1456 × 180, 1920 × 1280, 1940 × 500, 2184 × 270, 2910 × 750, 2912 × 360, 3880 × 1000
    * Maximum file size of 512 KB.
  * Acceptable image sizes for other types of ads:
    * When the aspect ratio is from 1:1 to 3:4/4:3 — from 450 to 5000 pixels on a side.
    * When the aspect ratio is 16:9, from 1080 × 607 to 5000 × 2812 pixels.
    * Maximum file size of 10 MB.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#type)Type of image
The type of image (the _Type_ parameter returned by the `get` method) is determined automatically during upload. The types are described in the table:
**Type** |  **Description** |  **Suitable for ad types**  
---|---|---  
REGULAR |  Aspect ratio from 1:1 to 3:4/4:3 Size from 450 to 5000 pixels on each side |  TEXT_AD DYNAMIC_TEXT_AD  
WIDE |  Aspect ratio of 16:9 Size from 1080 × 607 to 5000 × 2812 pixels |  TEXT_AD DYNAMIC_TEXT_AD MOBILE_APP_AD  
FIXED_IMAGE |  240 × 400, 300 × 250, 300 × 500, 300 × 600, 320 × 50, 320 × 100, 320 × 480, 336 × 280, 480 × 320, 480 × 800, 600 × 500, 600 × 1000, 600 × 1200, 640 × 100, 640 × 200, 640 × 960, 672 × 560, 720 × 1200, 728 × 90, 900 × 750, 900 × 1500, 900 × 1800, 960 × 150, 960 × 300, 960 × 640, 960 × 1440, 960 × 1600, 970 × 250, 1008 × 840, 1200 × 1000, 1200 × 2000, 1200 × 2400, 1280 × 200, 1280 × 400, 1280 × 1920, 1344 × 1120, 1440 × 960, 1456 × 180, 1920 × 1280, 1940 × 500, 2184 × 270, 2910 × 750, 2912 × 360, 3880 × 1000. |  IMAGE_AD  
Note
For backward compatibility, the following image types are used:
  * SMALL — Aspect ratio from 1:1 to 3:4; size of 150 pixels on the shorter side.
  * UNFIT — The image type is unknown or unsupported in this version of the API.


Images with this type can't be assigned to an ad.
Hash of the image.
The type of image. See [Image type](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage#type).
Copied
### Was the article helpful?
YesNo
Previous
[vCard](https://yandex.com/dev/direct/doc/en/objects/en/objects/vcard)
Next
[Video (AdVideo)](https://yandex.com/dev/direct/doc/en/objects/en/objects/advideos)
