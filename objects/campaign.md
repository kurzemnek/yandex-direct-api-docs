---
title: Campaign | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/campaign
crawled_at: 2025-09-17T15:49:06.285604
---

Service
# Campaign
  * [Service](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#restrictions)
  * [Campaign type](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#type)
  * [Display strategies](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#strategy)
  * [Monetary parameters](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#currency-limits)
  * [Campaign status and state](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#status)


The Campaign object contains an advertising campaign's settings and summary statistics.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#service)Service
Use the 
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#methods)Methods
To manage a unified performance campaign, use this URL: `https://api.direct.yandex.com/v501/`.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#restrictions)Restrictions
To get the limit on the number of campaigns for an advertiser, use the method _Restrictions_ array).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#type)Campaign type
The campaign type is set when creating a campaign and can't be changed.
The campaign type determines the type for child [ad groups](https://yandex.com/dev/direct/doc/en/objects/en/objects/adgroup). You can only add the corresponding type of groups to the campaign.
Part of the campaign parameters are shared across all types of campaigns, and part of them depend on the type of campaign. The parameters that depend on the campaign type are passed in a child structure with the corresponding name.
The following types of campaigns are currently available:
  * TEXT_CAMPAIGN: Campaign of the "Text & Image ads" type.
To create or edit this type of campaign, you must pass the campaign parameters in the `TextCampaign` structure for the 
When getting campaign parameters, list the names of parameters that are shared across all campaign types in the `FieldNames` input parameter, and list the names of parameters that are specific to this campaign type in the `TextCampaignFieldNames` input parameter of the
  * UNIFIED_CAMPAIGN: Unified performance campaign.
To create or edit this type of campaign, use the `UnifiedCampaign` structure. Parameters are described in 
When getting campaign parameters, list the names of the parameters shared across all campaign types in the `FieldNames` input parameter, and list the names of parameters specific to this campaign type in the `UnifiedCampaignFieldNames` input parameter of the 
  * SMART_CAMPAIGN: Campaign of the "Smart banners" type. For more information about smart banners, see 
To create or edit this type of campaign, use the `SmartCampaign` structure. Parameters are described in 
When getting campaign parameters, list the names of parameters that are shared across all campaign types in the `FieldNames` input parameter, and list the names of parameters that are specific to this campaign type in the `SmartCampaignFieldNames` input parameter of the 
  * DYNAMIC_TEXT_CAMPAIGN: Campaign of the "Dynamic ads" type. For more information about dynamic ads, see 
To create or edit this type of campaign, use the `DynamicTextCampaign` structure. Parameters are described in the sections 
When getting campaign parameters, list the names of parameters that are shared across all campaign types in the `FieldNames` input parameter, and list the names of parameters that are specific to this campaign type in the `DynamicTextCampaignFieldNames` input parameter of the 
  * MOBILE_APP_CAMPAIGN: Campaign of the "Ads for Mobile Apps" type. For more information about ads for mobile apps, see 
To create or edit this type of campaign, use the `MobileAppCampaign` structure. Parameters are described in the sections 
When getting campaign parameters, list the names of parameters that are shared across all campaign types in the `FieldNames` input parameter, and list the names of parameters that are specific to this campaign type in the `MobileAppCampaignFieldNames` input parameter of the 
  * MCBANNER_CAMPAIGN: Campaign of the "Search banner" type. For more information about banners in search results, see 
This type of campaign only allows getting statistics via the Yandex Direct API.
  * CPM_BANNER_CAMPAIGN: Campaign of the "Display campaign" type. For more information about display campaigns, see 
To create or edit this type of campaign, use the `CpmBannerCampaign` structure. Parameters are described in the sections 
When getting campaign parameters, list the names of parameters that are shared across all campaign types in the `FieldNames` input parameter, and list the names of parameters that are specific to this campaign type in the `CpmBannerCampaignFieldNames` input parameter of the 
  * CPM_DEALS_CAMPAIGN: Campaign of the "Display campaign with deals" type. For more information about deals, see 
This type of campaign only allows getting statistics via the Yandex Direct API.
  * CPM_FRONTPAGE_CAMPAIGN: Campaign of the "Display campaign on the Yandex Home page" type. For more information about this campaign type, see 
This type of campaign only allows getting statistics via the Yandex Direct API.
  * CPM_PRICE: Campaign of the "Fixed CPM campaign" type. For more information about this type of campaign, see 
This type of campaign only allows getting statistics via the Yandex Direct API.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#strategy)Display strategies
See the section [Display strategies](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign-strategies).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#currency-limits)Monetary parameters
Alert
All monetary campaign parameters (daily budget, weekly budget, and average price for automatic strategies) are passed via the Yandex Direct API as integer numbers. The passed value is a monetary value in the advertiser's currency, multiplied by 1,000,000.
Limits on monetary parameters are listed for each currency in the currency reference. To get the list of currencies, use the 
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign#status)Campaign status and state
The `State` parameter reflects the current state of displays in the campaign.
**State** |  **Description**  
---|---  
CONVERTED |  The campaign was run in Yandex units before the advertiser switched to a real currency. It is currently in a special archive and available only for read access. Note The `States` parameter is set to CONVERTED or the ID of this campaign is specified in the `Ids` parameter. If the `Ids` and `States` parameters are both omitted, the method doesn't return a campaign in the CONVERTED state.  
ARCHIVED |  The campaign has been archived using the   
SUSPENDED |  The owner has stopped the campaign using the   
ENDED |  The campaign ended (the end date has passed).  
ON |  The campaign is active and ads can be displayed.  
OFF |  The campaign is inactive (draft, pending review, rejected, no funds on the campaign or on the shared account, or no active ads).  
UNKNOWN |  Used for providing backward compatibility and displaying states that are not supported in this version of the API.  
The `Status` parameter reflects the overall result of reviewing the campaign objects.
**Status** |  **Description**  
---|---  
DRAFT |  The campaign has been created but has not yet been submitted for review.  
MODERATION |  The campaign is under review.  
ACCEPTED |  At least one of the campaign's ads was accepted after review.  
REJECTED |  All of the campaign's ads were rejected after review.  
UNKNOWN |  This value is used for backward compatibility and for displaying statuses that are not supported in this version of the API.  
The `StatusPayment` parameter indicates whether the campaign is ready for payments.
**Payment status** |  **Description**  
---|---  
DISALLOWED |  Payment is not allowed (or only   
ALLOWED |  The campaign was accepted after review, or the shared account is enabled.  
**For an advertiser**
Limits on the number of objects for an advertiser.
**For an agency**
—
Copied
### Was the article helpful?
YesNo
Previous
[Main objects](https://yandex.com/dev/direct/doc/en/objects/en/objects/objects)
Next
[Display strategies](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign-strategies)
