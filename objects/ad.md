---
title: Ad | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/ad
crawled_at: 2025-09-17T15:52:04.490282
---

Learn more
# Ad
  * [Learn more](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#learn-more)
  * [Service](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#restrictions)
  * [Ad type](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#types)
  * [Ad status and state](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#status)
  * [Special category](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#classification)
  * [Age label](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#age)
  * [Ad extensions](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#addons)
    * [Bids for images and video extensions](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#addons1)
    * [Result of reviewing add-ons](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#moderate-addon)
  * [Rules for selecting product ads.](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#unified-group-conditions)
  * [Examples](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#examples)
  * [Ad labeling](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#ad-labeling)


An ad consists of advertising materials. The set of parameters for an ad depends on its type.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#learn-more)Learn more
  * [Running an advertising campaign](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/launch-campaign).


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#service)Service
Use the 
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#methods)Methods
To manage product ads, use this URL: `https://api.direct.yandex.com/v501/`.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#restrictions)Restrictions
The ad type must match the group type. See the table in [Ad type](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#types).
Operations with ads are not possible in archived campaigns.
To get the limit on the number of ads per group for an advertiser, use the method _Restrictions_ array).
For restrictions on ad parameters, see 
Note
  * An ad in Belarusian can only be added to a group that has the display region restricted to Belarus.
  * An ad in Kazakh can only be added to a group that has the display region restricted to Kazakhstan.
  * An ad in Turkish can only be added to a group that has the display region restricted to Turkey.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#types)Ad type
The ad type is set when creating an ad and can't be changed.
The following types of ads are currently available:
  * TEXT_AD: A Text & Image (regular) ad.
The ad contains a title and ad text, as well as a link to the advertised website. You can also include a Turbo page, display link, image, video extension, price, [sitelinks](https://yandex.com/dev/direct/doc/en/objects/en/objects/sitelink), [ad callouts](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension), and the ID of your business profile in Yandex Maps. If the Turbo page, vCard, or business profile ID is included, the website link is optional. The ad can be automatically assigned an [age label](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#age). In this case, you can change the label.
To create or edit a Text & Image ad, use the `TextAd` structure.
To get the ad parameters (other than price parameters), list the parameter names in the `TextAdFieldNames` input parameter for the `TextAdPriceExtensionFieldNames` input parameter.
  * SMART_AD: A smart banner.
The ad contains a creative that was created in Ad Builder.
To create or edit an ad, use the `SmartAdBuilderAd` structure.
To get the ad parameters, list the parameter names in the `SmartAdBuilderAdFieldNames` input parameter of the 
  * MOBILE_APP_AD: An ad for advertising mobile apps.
The ad contains a title, text, and age restriction, as well as a label for the button to download or install. You can also add an image, specify a tracking link to track installs, and include a set of add-ons that need to be downloaded from the app store (icon, rating, and so on). For more information about ads for mobile apps, see 
To create or edit an ad for mobile app advertising, use the `MobileAppAd` structure.
To get the parameters of a mobile ad, list the parameter names in the `MobileAppAdFieldNames` input parameter of the 
  * DYNAMIC_TEXT_AD: A dynamic ad.
The ad contains text. You can also include an [image](https://yandex.com/dev/direct/doc/en/objects/en/objects/adimage), a [set of sitelinks](https://yandex.com/dev/direct/doc/en/objects/en/objects/sitelink), and [callouts](https://yandex.com/dev/direct/doc/en/objects/en/objects/adextension) in an ad. For more information about dynamic ads, see 
To create or edit a dynamic ad, use the `DynamicTextAd` structure.
To get the ad parameters, list the parameter names in the `DynamicTextAdFieldNames` input parameter for the 
  * IMAGE_AD: An image ad.
There are four subtypes of image ads:
    * TEXT_IMAGE_AD
The ad contains an image and a link to the advertised website and/or Turbo page.
To create or edit an ad, use the `TextImageAd` structure.
To get the ad parameters, list the parameter names in the `TextImageAdFieldNames` input parameter for the 
    * MOBILE_APP_IMAGE_AD
The ad contains an image. You can also add a tracking link to the ad to track app installs.
To create or edit an ad, use the `MobileAppImageAd` structure.
To get the ad parameters, list the parameter names in the `MobileAppImageAdFieldNames` input parameter for the 
    * TEXT_AD_BUILDER_AD
The ad contains a creative that was designed in Ad Builder, as well as a link to the advertised website and/or Turbo page.
To create or edit an ad, use the `TextImageAd` structure.
To get the ad parameters, list the parameter names in the `TextAdBuilderAdFieldNames` input parameter for the 
    * MOBILE_APP_AD_BUILDER_AD
The ad contains a creative that was created in Ad Builder. You can also add a tracking link to the ad to track app installs.
To create or edit an ad, use the `MobileAppImageAd` structure.
To get the ad parameters, list the parameter names in the `MobileAppAdBuilderAdFieldNames` input parameter for the 
Alert
Image ads are only displayed in ad networks (the Yandex Advertising Network and external networks); they are not displayed in search results.
Displays of image ads are possible only if the bid on a keyword or audience target meets the minimum CPC for an ad containing an image, which you can find on the 
For more information about image ads, see 
  * CPC_VIDEO_AD: A video ad (in a "Text & Image Ads" or "Ads for mobile apps" campaign).
The ad contains a creative that was designed in Ad Builder, as well as a link to the advertised website and/or Turbo page.
To create or edit an ad, use the `CpcVideoAdBuilderAd` structure.
To get the ad parameters, list the parameter names in the `CpcVideoAdBuilderAdFieldNames` input parameter of the 
The "Ads for mobile apps" campaigns use a separate subtype for video ads — MOBILE_APP_CPC_VIDEO_AD_BUILDER_AD.
    * **MOBILE_APP_CPC_VIDEO_AD_BUILDER_AD**
Such an ad contains a creative that was created in Ad Builder. You can also add a tracking link to the ad to track app installs.
To create or edit an ad, use the `MobileAppCpcVideoAdBuilderAd` structure.
To get the ad parameters, list the parameter names in the `MobileAppCpcVideoAdBuilderAdFieldNames` input parameter of the 
  * CPM_BANNER_AD: A display banner.
The ad contains a creative that was uploaded in the web interface or designed in the Ad Builder, as well as a link to the advertised website and/or Turbo page. You can also add a Yandex Audience pixel and an ADFOX impression tag to your ads.
To create or edit an ad, use the `CpmBannerAdBuilderAd` structure.
To get the ad parameters, list the parameter names in the `CpmBannerAdBuilderAdFieldNames` input parameter of the 
  * CPM_VIDEO_AD: A display video ad in a display campaign.
The ad contains a creative that was designed in Ad Builder, as well as a link to the advertised website and/or Turbo page. You can also add an ADFOX impression tag to an ad.
To create or edit an ad, pass the parameters in the `CpmBannerAdBuilderAd` structure for the 
To get the ad parameters, list the parameter names in the `CpmBannerAdBuilderAdFieldNames` input parameter of the 
  * SHOPPING_AD: A product ad in a "unified performance campaign".
To create or edit an ad, use the `ShoppingAd` structure.
To get the ad parameters, list the parameter names in the `ShoppingAdFieldNames` input parameter of the 
  * LISTING_AD: An ad for catalog pages in a "unified performance campaign".
To create or edit an ad, use the `ListingAd` structure.
To retrieve ad parameters, list the parameter names in the `ListingAdFieldNames` input parameter of the 


The `Type`, `Subtype`, `Status`, `State`, `StatusClarification`, `AdCategories`, and `AgeLabel` parameters are common to all types of ads. To get these parameters, list the desired parameter names in the `FieldNames` input parameter for the 
The table below shows how ad types correspond to group types.
**Group type** |  **Possible types of ads**  
---|---  
TEXT_AD_GROUP |  TEXT_AD, IMAGE_AD, subtypes TEXT_IMAGE_AD, TEXT_AD_BUILDER_AD, CPC_VIDEO_AD  
SMART_AD_GROUP |  SMART_AD  
MOBILE_APP_AD_GROUP |  MOBILE_APP_AD, IMAGE_AD, subtypes MOBILE_APP_IMAGE_AD, MOBILE_APP_AD_BUILDER_AD, CPC_VIDEO_AD, subtype MOBILE_APP_CPC_VIDEO_AD_BUILDER_AD  
DYNAMIC_TEXT_AD_GROUP |  DYNAMIC_TEXT_AD  
CPM_BANNER_AD_GROUP |  CPM_BANNER_AD  
CPM_VIDEO_AD_GROUP |  CPM_VIDEO_AD  
UNIFIED_AD_GROUP |  TEXT_AD, IMAGE_AD, subtypes TEXT_IMAGE_AD, TEXT_AD_BUILDER_AD, SHOPPING_AD, LISTING_AD  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#status)Ad status and state
The `State` parameter reflects the current state of the ad.
**State** |  **Description**  
---|---  
SUSPENDED |  Ad displays were stopped by the owner using the   
OFF_BY_MONITORING |  Ad displays are automatically stopped by   
ON |  The ad is active, belongs to an active campaign, and can be served (if the campaign has funds, time targeting settings allow impressions, and so on).  
OFF |  The ad is inactive (a draft, pending review, or rejected), or belongs to an inactive or suspended campaign.  
ARCHIVED |  The ad has been archived (using the   
The `Status` parameter reflects the result of reviewing the ad.
**Status** |  **Description**  
---|---  
DRAFT |  The ad has been created but has not yet been submitted for review.  
MODERATION |  The ad is under review.  
PREACCEPTED |  The ad has been automatically accepted for displays, but will be further reviewed by a moderator.  
ACCEPTED |  The ad was accepted after review.  
REJECTED |  The ad was rejected after review.  
Note
If the ad was edited, and the new version is pending review (the MODERATION status) or was immediately rejected after review (the REJECTED status), the previous version of the ad continues being displayed if it was not suspended. In this case, the ad has the ON status.
If the new version of the ad was automatically accepted for display after editing (PREACCEPTED), and then it was rejected (REJECTED), displays of the previous version will not be resumed.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#classification)Special category
During the review, an ad can be assigned a label stating that the advertised product or service belongs to a special category. In this case, the ad is given the `AdCategories` parameter, which cannot be changed.
For certain categories, ad displays are forbidden. For others, ads are served with a special warning in accordance with the legislation of the Russian Federation.
To get the reference list of special categories, use the 
These categories cannot be changed, assigned, or removed via the API. If you disagree with the category assigned, contact the 
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#age)Age label
The `AgeLabel` parameter contains the age-appropriate category of the advertised product if this category is required to be specified by the federal law of the Russian Federation "About advertising". Assigning the age category depends on the ad type.
TEXT_AD
MOBILE_APP_AD
The value of the age label depends on whether the ad belongs to the [special category](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#classification) BABY_FOOD:
  * For ads that belong to the BABY_FOOD category, it is the age of the infant in months: "MONTHS_0", "MONTHS_1", "MONTHS_2", ..., "MONTHS_12".
  * For all other ads, it is the age that the informational product is appropriate for. Possible values: "AGE_0", "AGE_6", "AGE_12", "AGE_16", "AGE_18".


If an ad does not have an age label, this parameter can't be set (the `update` method ignores the parameter value).
Alert
The API can only be used to change the value of the age category if the ad has one. In order to change whether an ad has or doesn't have an age category, contact the 
An age label is assigned to all ads. Possible values: "AGE_0", "AGE_6", "AGE_12", "AGE_16", "AGE_18".
The label can be specified when creating the ad. Default value: "AGE_18". You can change the value of the label when editing the ad, but you can't remove the label.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#addons)Ad extensions
You can use the 
Video extensions are only displayed in ad networks (the Yandex Advertising Network and external networks); they are not displayed in search results.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#addons)Bids for images and video extensions
An image or video extension can be displayed only if the bid for the keyword or audience target meets the minimum CPC for an ad containing an image, which you can find on the 
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#moderate-addon)Result of reviewing add-ons
The vCard, image, video extension, and sitelinks are not reviewed in isolation, but together with the ad. They are sent for moderation automatically if the ad is under moderation or already passed moderation.
The `VCardModeration` structure), image (`AdImageModeration` structure), sitelinks (`SitelinksModeration` structure), or video extension (`Status` parameter in the `VideoExtension` structure).
**Review status** |  **Description**  
---|---  
DRAFT |  The ad extension has not been submitted for review.  
MODERATION |  The ad extension is under review.  
ACCEPTED |  The ad extension was accepted after review. The ad will contain the add-on when it is shown.  
REJECTED |  The ad extension was rejected after review.  
UNKNOWN |  The status is unknown. This value is used for backward compatibility and for displaying statuses that are not supported in this version of the API.  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#unified-group-conditions)Rules for selecting product ads.
The selection rule consists of three parameters:
  * `Operand` — The feed field.
  * `Operator` — The comparison operator.
  * `Arguments` — An array of values to compare the field value in the feed with.


For a description of the fields for each type of feed, see 
The compatibility of feed fields and operators depends on the feed:
Retail sales, other business: Yandex Market feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
categoryId |  GREATER_THAN, LESS_THAN |  One number  
EQUALS_ANY |  Maximum 20,000 numbers  
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#range-sample).  
id |  GREATER_THAN, LESS_THAN |  One number  
EQUALS_ANY |  Max 50 numbers  
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#range-sample).  
market_category typePrefix vendor |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
description model name |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
url |  EQUALS,CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
oldprice price |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#range-sample).  
EXISTS |  Pass the value 1  
adult manufacturer_warranty pickup store |  EQUALS_ANY |  Acceptable values:
  * 0
  * 1

  
EXISTS |  Pass the value 1  
age |  EQUALS_ANY |  Acceptable values: integer from 0 to 12, 16, or 18.  
EXISTS |  Pass the value 1  
Hotels: Google Ads "Hotels and rentals" feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
Rsis |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#range-sample).  
Description max_score name location url |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
class |  EQUALS_ANY |  Acceptable values:
  * 1
  * 2
  * 3
  * 4
  * 5

  
EXISTS |  Pass the value 1  
OfferID Score |  GREATER_THAN, LESS_THAN |  Single integer  
EQUALS_ANY |  Max 50 integers  
RANGE |  Max 10 ranges or integers. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#range-sample).  
Automobiles: Auto.ru feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
body_type color folder_id mark_id |  CONTAINS_ANY, NOT_CONTAINS_ALL, |  Max 50 lines, max 175 characters per line  
wheel |  CONTAINS_ANY |  Recommended values:
  * left
  * right

  
metallic |  EQUALS_ANY |  Recommended values:
  * yes
  * no

  
availability |  EQUALS_ANY |  Recommended values:
  * in stock
  * on order

  
year |  EQUALS_ANY |  Max 10 numbers  
url |  CONTAINS_ANY, NOT_CONTAINS_ALL, EQUALS_ANY |  Max 50 lines, max 175 characters per line  
price |  GREATER_THAN, LESS_THAN |  Single integer  
EQUALS_ANY |  Max 50 integers  
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#range-sample).  
Realty: Yandex Realty feed
This feed doesn't use selection rules.
Flights: Google Ads "Flights" feed
This feed doesn't use selection rules.
Other business: universal feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
url |  EQUALS_ANY, CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
description name |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
price oldprice |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#range-sample).  
Other business: Google Ads "Custom" feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
category description name second_title |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
url |  EQUALS_ANY, CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
price sale_price |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
IN_RANGE |  Up to 10 ranges, up to 2 decimal places  
EQUALS_ANY |  Up to 50 values, up to 2 decimal places  
Other business: Google Ads "Travel" feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
Category destination origin Title |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
url |  EQUALS_ANY, CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
price sale_price |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
IN_RANGE |  Up to 10 ranges, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#examples)Examples
**The value contains one of the specified rows** :
```
    {
      "Operand": "mark_id",
      "Operator": "CONTAINS_ANY",
      "Arguments": ["Audi","Opel"]
    }

```

**Range: price from 111 to 222 or 3000 to 10000** :
```
    {
      "Operand": "price",
      "Operator": "IN_RANGE",
      "Arguments": ["111-222", "3000-10000"]
    }

```

**Value from the list** :
```
    {
      "Operand": "wheel",
      "Operator": "EQUALS_ANY",
      "Arguments": ["левый"]
    }

```

##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/ad#ad-labeling)Ad labeling
The `ErirAdDescription` parameter contains a description of an ad object.
The `AutogeneratedErirAdDescription` contains an automatically generated description of an ad object.
For more information about ad labeling, see 
**For an advertiser**
Limits on the number of objects for an advertiser.
**For an agency**
—
Copied
### Was the article helpful?
YesNo
Previous
[Ad group](https://yandex.com/dev/direct/doc/en/objects/en/objects/adgroup)
Next
[Set of sitelinks (SitelinksSet)](https://yandex.com/dev/direct/doc/en/objects/en/objects/sitelink)
