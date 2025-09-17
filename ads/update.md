---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/ads/update
crawled_at: 2025-09-17T15:52:57.153430
---

Restrictions
# update
  * [Restrictions](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#samples)


Changes ad parameters.
###  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#see-also)Learn more
  * [How the "update" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#restrictions)Restrictions
To manage product ads, use the URL: `https://api.direct.yandex.com/v501/`.
Copied
Maximum of 1000 ads per method call.
You can't edit ads with the ARCHIVED status. See [Ad status and state](https://yandex.com/dev/direct/doc/dg/objects/ad.html#status).
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#input)Request
Request structure in JSON format:
```
{
  "method": "update",
  "params": { /* params */
    "Ads": [{  /* AdUpdateItem */
      "Id": (long), /* required */
      "TextAd": {  /* TextAdUpdate */
        "Title": (string),
        "Title2": (string), /* nillable */
        "Text": (string),
        "Href": (string), /* nillable */
        "AgeLabel": ( "AGE_0" | ... | "MONTHS_12" ),
        "DisplayUrlPath": (string), /* nillable */
        "VCardId": (long), /* nillable */
        "AdImageHash": (string), /* nillable */
        "SitelinkSetId": (long), /* nillable */
        "CalloutSetting": {  /* AdExtensionSetting */
          "AdExtensions": [{  /* AdExtensionSettingItem */
            "AdExtensionId": (long), /* required */
            "Operation": ( "ADD" | "REMOVE" | "SET" ) /* required */
          }, ... ] /* required */
        }, /* nillable */
        "VideoExtension": {  /* VideoExtensionUpdateItem */
          "CreativeId": (long) /* nillable */
        },
        "PriceExtension": {  /* PriceExtensionUpdateItem */
          "Price": (long),
          "OldPrice": (long), /* nillable */
          "PriceQualifier": ( "FROM" | "UP_TO" | "NONE" ),
          "PriceCurrency": ( "RUB" | "BYN" | "CHF" | "EUR" | "KZT" | "TRY" | "UAH" | "USD" | "UZS" )
        }, /* nillable */
        "TurboPageId": (long), /* nillable */
        "BusinessId": (long), /* nillable */
        "PreferVCardOverBusiness": ( "YES" | "NO" ),
        "ErirAdDescription" : (string) /* nillable */
      },
      "DynamicTextAd": {  /* DynamicTextAdUpdate */
        "VCardId": (long), /* nillable */
        "AdImageHash": (string), /* nillable */
        "SitelinkSetId": (long), /* nillable */
        "CalloutSetting": {  /* AdExtensionSetting */
          "AdExtensions": [{  /* AdExtensionSettingItem */
            "AdExtensionId": (long), /* required */
            "Operation": ( "ADD" | "REMOVE" | "SET" ) /* required */
          }, ... ] /* required */
        }, /* nillable */
        "Text": (string)
      },
      "MobileAppAd": {  /* MobileAppAdUpdate */
         "Title": (string),
         "Text": (string),
         "TrackingUrl": (string), /* nillable */
         "Action": ( "DOWNLOAD" | "GET" | "INSTALL" | "MORE" | "OPEN" | "UPDATE" | "PLAY" | "BUY_AUTODETECT" ),
         "AdImageHash": (string), /* nillable */
         "Features": [{  /* MobileAppAdFeatureItem */
           "Feature": ( "PRICE" | "ICON" | "CUSTOMER_RATING" | "RATINGS" ), /* required */
           "Enabled": ( "YES" | "NO" ) /* required */
         }, ... ],
         "AgeLabel": ( "AGE_0" | ... | "AGE_18" ),
         "VideoExtension": {  /* VideoExtensionUpdateItem */
           "CreativeId": (long) /* nillable */
         },
         "ErirAdDescription" : (string) /* nillable */
      },
      "TextImageAd": {  /* TextImageAdUpdate */
        "AdImageHash": (string),
        "Href": (string), /* nillable */
        "TurboPageId": (long), /* nillable */
        "ErirAdDescription" : (string) /* nillable */
      },
      "MobileAppImageAd": {  /* MobileAppImageAdUpdate */
        "AdImageHash": (string),
        "TrackingUrl": (string), /* nillable */
        "ErirAdDescription" : (string) /* nillable */
      },
      "MobileAppCpcVideoAdBuilderAd" : {  /* MobileAppCpcVideoAdBuilderAdUpdate */
        "Creative" : { /* AdBuilderAdUpdateItem */
          "CreativeId" : (long) /* required */
        },
        "TrackingUrl" : (string), /* nillable */
        "ErirAdDescription" : (string) /* nillable */
      },
      "TextAdBuilderAd": {  /* TextAdBuilderAdUpdate */
        "Creative": { /* AdBuilderAdUpdateItem */
          "CreativeId": (long) /* required */
        },
        "Href": (string), /* nillable */
        "TurboPageId": (long), /* nillable */
        "ErirAdDescription" : (string) /* nillable */
      },
      "MobileAppAdBuilderAd": {  /* MobileAppAdBuilderAdUpdate */
        "Creative": { /* AdBuilderAdUpdateItem */
          "CreativeId": (long) /* required */
        },
        "TrackingUrl": (string), /* nillable */
        "ErirAdDescription" : (string) /* nillable */
      },
      "CpcVideoAdBuilderAd": {  /* CpcVideoAdBuilderAdUpdate */
        "Creative": { /* AdBuilderAdUpdateItem */
          "CreativeId": (long) /* required */
        },
        "Href": (string),  /* nillable */
        "TurboPageId": (long), /* nillable */
        "ErirAdDescription" : (string) /* nillable */
      },
      "CpmBannerAdBuilderAd": {  /* CpmBannerAdBuilderAdUpdate */
        "Creative": { /* AdBuilderAdUpdateItem */
          "CreativeId": (long) /* required */
        },
        "Href": (string), /* nillable */
        "TrackingPixels": { /* ArrayOfString */
          "Items": [(string), ... ] /* required */
        }, /* nillable */
        "TurboPageId": (long), /* nillable */
        "ErirAdDescription" : (string) /* nillable */
      },
      "CpmVideoAdBuilderAd": {  /* CpmVideoAdBuilderAdUpdate */
        "Creative": { /* AdBuilderAdUpdateItem */
          "CreativeId": (long) /* required */
        },
        "Href": (string),  /* nillable */
        "TrackingPixels": { /* ArrayOfString */
          "Items": [(string), ... ] /* required */
        }, /* nillable */
        "TurboPageId": (long),
        "ErirAdDescription" : (string) /* nillable */
      },
      "SmartAdBuilderAd": {  /* SmartAdBuilderAdUpdate */
        "Creative": { /* AdBuilderAdUpdateItem */
          "CreativeId": (long) /* required */
        },
        "ErirAdDescription" : (string)
      },
      "ShoppingAd" : {
          "SitelinkSetId" : (long) /* nillable */,
          "CalloutSetting" : { /* nillable */
            "AdExtensions" : [{ /* required */
                "AdExtensionId" : (long) /* required */,
                "Operation" : ("ADD"|"REMOVE"|"SET") /* required */
            }, ... ]
          },
          "BusinessId" : (long) /* nillable */,
          "FeedFilterConditions" : { /* nillable */
            "Items" : [{ /* required */
                "Operand" : (string) /* required */,
                "Operator" : ("CONTAINS_ANY"|"EQUALS_ANY"|"EXISTS"|"GREATER_THAN"|"IN_RANGE"|"LESS_THAN"|"NOT_CONTAINS_ALL") /* required */,
                "Arguments" : [ (string) ] /* required */
            }, ... ]
          },
          "TitleSources" : { /* nillable */
              "Items" : [ (string) ] /* required */
          },
          "TextSources" : { /* nillable */
              "Items" : [ (string) ] /* required */
          },
          "DefaultTexts" : [ (string) ]
      },
      "ListingAd" : {
          "SitelinkSetId" : (long) /* nillable */,
          "CalloutSetting" : { /* nillable */
            "AdExtensions" : [{ /* required */
                "AdExtensionId" : (long) /* required */,
                "Operation" : ("ADD"|"REMOVE"|"SET") /* required */
            }, ... ]
          },
          "BusinessId" : (long) /* nillable */,
          "FeedFilterConditions" : { /* nillable */
            "Items" : [{ /* required */
                "Operand" : (string) /* required */,
                "Operator" : ("CONTAINS_ANY"|"EQUALS_ANY"|"EXISTS"|"GREATER_THAN"|"IN_RANGE"|"LESS_THAN"|"NOT_CONTAINS_ALL") /* required */,
                "Arguments" : [ (string) ] /* required */
            }, ... ]
          },
          "TitleSources" : { /* nillable */
              "Items" : [ (string) ] /* required */
          },
          "TextSources" : { /* nillable */
              "Items" : [ (string) ] /* required */
          },
          "DefaultTexts" : [ (string) ]
      }
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / UpdateRequest structure (for SOAP)**  
`Ads` |  array of AdUpdateItem |  Ads to change parameters for. |  Yes  
**AdUpdateItem structure**  
`Id` |  long |  The ID of the ad to change parameters for. |  Yes  
`TextAd` |  TextAdUpdate |  Parameters of a text and image ad. See [Ad type](https://yandex.com/dev/direct/doc/dg/objects/ad.html#types). |  Use either `TextAd` or `MobileAppAd` or `DynamicTextAd` or `TextImageAd` or `MobileAppImageAd` or `MobileAppCpcVideoAdBuilderAd` or `TextAdBuilderAd` or `MobileAppAdBuilderAd` or `CpcVideoAdBuilderAd` or `CpmBannerAdBuilderAd` or `CpmVideoAdBuilderAd` or `SmartAdBuilderAd`.  
`DynamicTextAd` |  DynamicTextAdUpdate |  Parameters of a dynamic ad.  
`MobileAppAd` |  MobileAppAdUpdate |  Parameters of a mobile app ad.  
`TextImageAd` |  TextImageAdUpdate |  Parameters of an image ad that was created from an image (in a group of text and image ads).  
`MobileAppImageAd` |  MobileAppImageAdUpdate |  Parameters of an image ad that was created from an image (in a group of mobile app ads).  
`MobileAppCpcVideoAdBuilderAd` |  MobileAppCpcVideoAdBuilderAdUpdate |  Parameters of a video ad that was created from an image (in a group of ads for mobile apps).  
`TextAdBuilderAd` |  TextAdBuilderAdUpdate |  Parameters of an image ad that was created from a creative (in a group of text and image ads).  
`MobileAppAdBuilderAd` |  MobileAppAdBuilderAdUpdate |  Parameters of an image ad that was created from a creative (in a group of mobile app ads).  
`CpcVideoAdBuilderAd` |  CpcVideoAdBuilderAdUpdate |  Video ad parameters in a “Text & Image ads” campaign.  
`CpmBannerAdBuilderAd` |  CpmBannerAdBuilderAdUpdate |  Display ad parameters.  
`CpmVideoAdBuilderAd` |  CpmVideoAdBuilderAdUpdate |  Parameters of a display video ad in a display campaign.  
`SmartAdBuilderAd` |  SmartAdBuilderAdUpdate |  Smart banner parameters.  
`ShoppingAd` |  ShoppingAdUpdate |  Product ad parameters.  
`ListingAd` |  ListingAdUpdate |  Parameters of an ad for catalog pages.  
**TextAdUpdate structure**  
`Title` |  string |  Title 1. Maximum of 56 characters, counting "narrow" characters. Maximum of 22 characters per word. When using a  Note "Narrow" characters are: `!,.;:"` |  No  
`Title2` |  string, nillable |  Title 2. A maximum of 30 characters not counting “narrow” characters, plus up to 15 “narrow” characters. Maximum of 22 characters per word. When using a  Note "Narrow" characters are: `!,.;:"` |  No  
`Text` |  string |  Ad text. Maximum of 81 characters not counting "narrow" characters, plus up to 15 "narrow" characters. Maximum of 23 characters per word. When using a  Note "Narrow" characters are: `!,.;:"` |  No  
`Href` |  string, nillable |  Link to the advertiser's website. Maximum of 1024 characters. When using a  It must include the protocol and domain name. May contain  |  No  
`AgeLabel` |  AgeLabelEnum |  [Age category.](https://yandex.com/dev/direct/doc/dg/objects/ad.html#age)  
If an ad does not have an age label, this parameter can't be set (the value is ignored). |  No  
`DisplayUrlPath` |  string, nillable |  Display link. Allowed only with the `Href` parameter. Maximum of 20 characters. When using a  It may contain letters, numbers, and the symbols -, №, /, %, #. Spaces, underscores (_), and double characters -- and // are not allowed. See  |  No  
`VCardId` |  long, nillable |  ID of the vCard. The vCard must belong to the same campaign as the ad. |  No  
`AdImageHash` |  string, nillable |  Hash of the image.  
For text and image ads, only images with the REGULAR or WIDE type are acceptable. See [Type of image](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#type). |  No  
`SitelinkSetId` |  long, nillable |  ID of a set of sitelinks. Allowed only with the `Href` or `TurboPageId` parameter. |  No  
`CalloutSetting` |  AdExtensionSetting, nillable |  Callouts for an ad:
  * To edit an existing set of callouts, use the ADD and REMOVE types of actions (see the description for the Operation parameter).
  * To replace an existing set of callouts with a new set, use the SET action.
  * To unassign all callouts, pass the nil (null) value.

|  No  
`VideoExtension` |  VideoExtensionUpdateItem |  Video extension. See  |  No  
`PriceExtension` |  PriceExtensionUpdateItem, nillable |  Price in the ad. |  No  
`TurboPageId` |  long, nillable |  ID of the Turbo page. |  No  
`BusinessId` |  long, nillable |  ID of the business profile on Yandex. To get data from business profiles, use the [Businesses](https://yandex.com/dev/direct/doc/en/ads/en/businesses/businesses).[get](https://yandex.com/dev/direct/doc/en/ads/en/businesses/get) method. A business profile can be linked to an ad only if the YES value is returned for the `IsPublished` parameter. Copied Note The business profile is available at `https://yandex.ru/profile/<profile_id>` |  No  
`PreferVCardOverBusiness` |  YesNoEnum |  Indicates which data source takes priority when displaying an ad: YES — vCard, NO — business profile. Alert This parameter is used if the `VCardID` and `BusinessId` values are specified. If one of these values is deleted, you must set the `PreferVCardOverBusiness` parameter to `NO`. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**AdExtensionSetting structure**  
`AdExtensions` |  array of AdExtensionSettingItem |  Extensions to assign to the ad or unassign from the ad. |  Yes  
**AdExtensionSettingItem structure**  
`AdExtensionId` |  long |  Extension ID. |  Yes  
`Operation` |  AdExtensionTypeEnum |  Type of action with the set of extensions:
  * ADD — Assign the extension to the ad.
  * REMOVE — Unassign the extension from the ad.
  * SET — Replace the set of extensions and assign the extension to the ad as part of the new set. You can use SET with ADD and REMOVE. Make sure all items in the `AdExtensions` array are of the SET type.

See the [examples](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#samples). |  Yes  
**VideoExtensionUpdateItem structure**  
`CreativeId` |  long, nillable |  ID of the creative. To get the ID of a creative, use the [Creatives](https://yandex.com/dev/direct/doc/en/ads/en/creatives/creatives).[get](https://yandex.com/dev/direct/doc/en/ads/en/creatives/get) method. |  Yes  
**PriceExtensionUpdateItem structure**  
`Price` |  long |  The price of a product or service multiplied by 1,000,000. An integer that is a multiple of 10,000 (the price with two digits after the decimal point). Maximum value: 10,000,000,000,000,000. |  No  
`OldPrice` |  long, nillable |  The previous price of a product or service multiplied by 1,000,000. An integer that is a multiple of 10,000. The old price must be higher than the current price. |  No  
`PriceQualifier` |  PriceQualifierEnum |  Text explanation of the price:
  * FROM — "From".
  * UP_TO — "To".
  * NONE — No explanation.

|  No  
`PriceCurrency` |  PriceCurrencyEnum |  The currency that the price is shown in. |  No  
**DynamicTextAdUpdate structure**  
`VCardId` |  long, nillable |  ID of the vCard. The vCard must belong to the same campaign as the ad. |  No  
`AdImageHash` |  string, nillable |  Hash of the image. For dynamic ads, only images of the REGULAR or WIDE type are acceptable. See [Type of image](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#type). |  No  
`SitelinkSetId` |  long, nillable |  ID of a set of sitelinks. |  No  
`CalloutSetting` |  AdExtensionSetting, nillable |  Callouts for an ad:
  * To edit an existing set of callouts, use the ADD and REMOVE types of actions (see the description for the Operation parameter).
  * To replace an existing set of callouts with a new set, use the SET action.
  * To unassign all callouts, pass the nil (null) value.

|  No  
`Text` |  string |  Ad text. Maximum of 81 characters not counting "narrow" characters, plus up to 15 "narrow" characters. Maximum of 23 characters per word. When using a  Note "Narrow" characters are: `!,.;:"` |  No  
**MobileAppAdUpdate structure**  
`Title` |  string |  Title. Maximum of 56 characters, counting "narrow" characters. Maximum of 22 characters per word. When using a  |  No  
`Text` |  string |  Ad text. Maximum of 75 characters, counting "narrow" characters. Maximum of 23 characters per word. When using a  |  No  
`TrackingUrl` |  string, nillable |  Tracking link for tracking app installations. Maximum of 1024 characters. It must include the protocol and domain name. |  No  
`Action` |  MobileAppAdActionEnum |  The button label:
  * DOWNLOAD — "Download"
  * GET — "Get"
  * INSTALL — "Install"
  * MORE — "More"
  * OPEN — "Open"
  * UPDATE — "Update"
  * PLAY — "Play"
  * BUY_AUTODETECT — The text changes based on the app's price: "Buy" if the price is non-zero, or "Free" if the price is set to zero.

|  No  
`AdImageHash` |  string, nillable |  Hash of the image. For mobile app ads, only images of the WIDE type are acceptable. See [Type of image](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#type). |  No  
`Features` |  array of MobileAppAdFeatureItem |  Add-ons that need to be automatically downloaded from the app store and displayed in the ad. |  No  
`AgeLabel` |  MobAppAgeLabelEnum |  Age restriction. |  No  
`VideoExtension` |  VideoExtensionUpdateItem |  Video extension. See  |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**MobileAppAdFeatureItem structure**  
`Feature` |  MobileAppFeatureEnum |  Type of extension:
  * PRICE — price
  * ICON — icon
  * CUSTOMER_RATING — rating
  * RATINGS — number of ratings (shown only if the rating is displayed)

If the add-on type is omitted from the `Features` array, the add-on won't be displayed. |  Yes  
`Enabled` |  YesNoEnum |  Whether to display an add-on in the ad. Note
  * If the add-on couldn't be downloaded from the app store, the YES value is available, but this add-on is not shown when displaying the ad.
  * The number of ratings is only shown together with the average rating: if NO is set for the CUSTOMER_RATING type, but YES is set for RATINGS, the number of ratings is not displayed.

|  Yes  
**TextImageAdUpdate structure**  
`AdImageHash` |  string |  Hash of the image. For image ads, only images of the FIXED_IMAGE type are acceptable. See [Type of image](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#type). |  No  
`Href` |  string, nillable |  Link to the advertiser's website. Maximum of 1024 characters. When using a  It must include the protocol and domain name. May contain  |  No  
`TurboPageId` |  long, nillable |  ID of the Turbo page. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**MobileAppImageAdUpdate structure**  
`AdImageHash` |  string |  Hash of the image. For image ads, only images of the FIXED_IMAGE type are acceptable. See [Type of image](https://yandex.com/dev/direct/doc/dg/objects/adimage.html#type). |  No  
`TrackingUrl` |  string, nillable |  Tracking link for tracking app installations. Maximum of 1024 characters. It must include the protocol and domain name. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**MobileAppCpcVideoAdBuilderAdUpdate structure**  
`Creative` |  AdBuilderAdUpdateItem |  A creative that was created in the Ad Builder. See  |  No  
`TrackingUrl` |  string, nillable |  Tracking link for tracking app installations. Maximum of 1024 characters. It must include the protocol and domain name. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**TextAdBuilderAdUpdate structure**  
`Creative` |  AdBuilderAdUpdateItem |  A creative that was created in the Ad Builder. See  |  No  
`Href` |  string, nillable |  Link to the advertiser's website. Maximum of 1024 characters. When using a  It must include the protocol and domain name. May contain  |  No  
`TurboPageId` |  long, nillable |  ID of the Turbo page. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**MobileAppAdBuilderAdUpdate structure**  
`Creative` |  AdBuilderAdUpdateItem |  A creative that was created in the Ad Builder. See  |  No  
`TrackingUrl` |  string, nillable |  Tracking link for tracking app installations. Maximum of 1024 characters. It must include the protocol and domain name. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**CpcVideoAdBuilderAdUpdate structure**  
`Creative` |  AdBuilderAdUpdateItem |  A creative that was created in the Ad Builder. See the section  |  No  
`Href` |  string, nillable |  Link to the advertiser's website. Maximum of 1024 characters. When using a  It must include the protocol and domain name. May contain  |  No  
`TurboPageId` |  long, nillable |  ID of the Turbo page. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**CpmBannerAdBuilderAdUpdate structure**  
`Creative` |  AdBuilderAdUpdateItem |  A creative that was uploaded in the web interface or created in the Ad Builder. See  |  No  
`Href` |  string, nillable |  Link to the advertiser's website. Maximum of 1024 characters. When using a  It must include the protocol and domain name. May contain  |  No  
`TrackingPixels` |  ArrayOfString, nillable |  Can contain a maximum of two strings:
  * A Yandex Audience pixel (see 
  * An ADFOX tracking tag. The tag must have the `%random%` or `%aw_random%` macro.

The maximum length of each string is 1024 characters. |  No  
`TurboPageId` |  long, nillable |  ID of the Turbo page. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**CpmVideoAdBuilderAdUpdate structure**  
`Creative` |  AdBuilderAdUpdateItem |  A creative that was created in the Ad Builder. See  |  No  
`Href` |  string, nillable |  Link to the advertiser's website. Maximum of 1024 characters. When using a  It must include the protocol and domain name. May contain  |  No  
`TurboPageId` |  long, nillable |  ID of the Turbo page. |  No  
`TrackingPixels` |  ArrayOfString, nillable |  An ADFOX tracking tag. The tag must have the `%random%` or `%aw_random%` macro. Maximum of 1024 characters. |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**SmartAdBuilderAdUpdate structure**  
`Creative` |  AdBuilderAdUpdateItem |  A creative that was created in the Ad Builder. See  |  No  
`ErirAdDescription` |  string |  Ad object description. |  No  
**AdBuilderAdUpdateItem structure**  
`CreativeId` |  long |  ID of the creative. To get the ID of a creative, use the [Creatives](https://yandex.com/dev/direct/doc/en/ads/en/creatives/creatives).[get](https://yandex.com/dev/direct/doc/en/ads/en/creatives/get) method. |  Yes  
**ShoppingAdUpdate structure**  
`SitelinkSetId` |  long |  ID of a set of sitelinks. |  No  
`CalloutSetting` |  CalloutSetting |  CalloutSetting |  No  
`BusinessId` |  long |  ID of the business profile on Yandex. To get data from business profiles, use the [Businesses](https://yandex.com/dev/direct/doc/en/ads/en/businesses/businesses).[get](https://yandex.com/dev/direct/doc/en/ads/en/businesses/get) method. A business profile can be linked to an ad only if the YES value is returned for the `IsPublished` parameter. Copied Note The business profile is available at `https://yandex.ru/profile/<profile_id>` |  No  
`FeedFilterConditions` |  FeedFilterConditionsItem |  Rules for selecting product offers. No more than 30 filters in the array. The total length of the selection rules is a maximum of 65 KB (in JSON). A product offer is selected for ad generation if it meets all the selection rules at the same time. If this parameter is omitted, all product offers from the feed are used for ad generation. |  No  
`TitleSources` |  array of string |  Names of feed fields used to generate ad titles. You can retrieve the acceptable field names through the `TitleAndTextSources` field of the [feeds.get](https://yandex.com/dev/direct/doc/en/ads/en/feeds/get) method. |  No  
`TextSources` |  array of string |  Names of feed fields used to generate ad texts. You can retrieve the acceptable field names through the `TitleAndTextSources` field of the [feeds.get](https://yandex.com/dev/direct/doc/en/ads/en/feeds/get) method. |  No  
`DefaultTexts` |  array of string |  Default texts. You can specify only one value. |  Yes  
**ListingAdUpdate structure**  
`SitelinkSetId` |  long |  ID of a set of sitelinks. |  No  
`CalloutSetting` |  CalloutSetting |  CalloutSetting |  No  
`BusinessId` |  long |  ID of the business profile on Yandex. To get data from business profiles, use the [Businesses](https://yandex.com/dev/direct/doc/en/ads/en/businesses/businesses).[get](https://yandex.com/dev/direct/doc/en/ads/en/businesses/get) method. A business profile can be linked to an ad only if the YES value is returned for the `IsPublished` parameter. Copied Note The business profile is available at `https://yandex.ru/profile/<profile_id>` |  No  
`FeedFilterConditions` |  FeedFilterConditionsItem |  Rules for selecting product offers. No more than 30 filters in the array. The total length of the selection rules is a maximum of 65 KB (in JSON). A product offer is selected for ad generation if it meets all the selection rules at the same time. If this parameter is omitted, all product offers from the feed are used for ad generation. |  No  
`TitleSources` |  array of string |  Names of feed fields used to generate ad titles. You can retrieve the acceptable field names through the `TitleAndTextSources` field of the [feeds.get](https://yandex.com/dev/direct/doc/en/ads/en/feeds/get) method. |  No  
`TextSources` |  array of string |  Names of feed fields used to generate ad texts. You can retrieve the acceptable field names through the `TitleAndTextSources` field of the [feeds.get](https://yandex.com/dev/direct/doc/en/ads/en/feeds/get) method. |  No  
`DefaultTexts` |  array of string |  Default texts. You can specify only one value. |  Yes  
**CalloutSetting structure**  
`AdExtensions` |  AdExtensions |  Extensions for an ad. |  Yes  
**AdExtensions structure**  
`AdExtensionId` |  long |  Extension ID. |  Yes  
`Operation` |  string |  Action.  
Possible values:
  * ADD
  * REMOVE
  * SET

|  Yes  
**FeedFilterConditionsItem structure**  
`Operand` |  string |  Feed parameter. For a description of the fields for each feed type, see  |  Yes  
`Operator` |  StringConditionOperatorEnum |  Comparison operator. For information on the compatibility of feed fields and operators, as well as restrictions on values, see [Rules for selecting product ads](https://yandex.com/dev/direct/doc/dg/objects/ad.html#unified-group-conditions). |  Yes  
`Arguments` |  array of string |  An array of strings to compare the operand to. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "UpdateResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ]
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / UpdateResponse structure (for SOAP)**  
`UpdateResults` |  array of ActionResult |  Results of updating ad parameters.  
**ActionResult structure**  
`Id` |  long |  The ad ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/ads/en/ads/update#samples)Examples
**Making changes to the set of ad extensions**
The callouts with the IDs 111, 112, and 113 were assigned to the ad.
Executing the request will assign the callouts with the IDs 111, 112, 114, and 115 to the ad.
```
    {
      "method": "update",
      "params": {
        "Ads": [{
          "Id": 7654321,
          "TextAd": {
            "CalloutSetting": {
              "AdExtensions": [{
                "AdExtensionId": 114,
                "Operation": "ADD"
              },
              {
                "AdExtensionId": 115,
                "Operation": "ADD"
              },
              {
                "AdExtensionId": 113,
                "Operation": "REMOVE"
              }]
            }
          }
        }]
      }
    }

```

**Replacing the set of extensions**
The callouts with the IDs 111, 112, and 113 were assigned to the ad.
Executing the request will assign the callouts with the IDs 113 and 114 to the ad.
```
    {
      "method": "update",
      "params": {
        "Ads": [{
          "Id": 7654321,
          "TextAd": {
            "CalloutSetting": {
              "AdExtensions": [{
                "AdExtensionId": 113,
                "Operation": "SET"
              },
              {
                "AdExtensionId": 114,
                "Operation": "SET"
              }]
            }
          }
        }]
      }
    }

```

Copied
### Was the article helpful?
YesNo
Previous
[unarchive](https://yandex.com/dev/direct/doc/en/ads/en/ads/unarchive)
Next
[AdVideos: Operations with videos](https://yandex.com/dev/direct/doc/en/ads/en/advideos/advideos)
