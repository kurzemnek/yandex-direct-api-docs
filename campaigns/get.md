---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/campaigns/get
crawled_at: 2025-09-17T16:00:51.815270
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#output)
    * [Learn more](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#learn-more1)


Returns the parameters of campaigns that match the specified criteria.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#restrictions)Restrictions
The method returns a maximum of `page-size` objects.
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* CampaignsSelectionCriteria */
      "Ids": [(long), ... ],
      "Types": [( "TEXT_CAMPAIGN" | "MOBILE_APP_CAMPAIGN" | "CPM_BANNER_CAMPAIGN" | "UNIFIED_CAMPAIGN" ), ... ],
      "States": [( "ARCHIVED" | "CONVERTED" | "ENDED" | "OFF" | "ON" | "SUSPENDED" ), ... ],
      "Statuses": [( "ACCEPTED" | "DRAFT" | "MODERATION" | "REJECTED" ), ... ],
      "StatusesPayment": [( "DISALLOWED" | "ALLOWED" ), ... ]
    }, /* required */
    "FieldNames": [( "BlockedIps" | ... | "Type" ), ... ], /* required */
    "TextCampaignFieldNames": [( "CounterIds" | "RelevantKeywords" | "Settings" | "BiddingStrategy" | "PriorityGoals" | "AttributionModel" | "PackageBiddingStrategy" | "CanBeUsedAsPackageBiddingStrategySource" | "NegativeKeywordSharedSetIds" ), ... ],
    "TextCampaignSearchStrategyPlacementTypesFieldNames": [ ( "SearchResults" | "ProductGallery" | "DynamicPlaces") ],
    "MobileAppCampaignFieldNames": [( "Settings" | "BiddingStrategy" | "PackageBiddingStrategy" | "CanBeUsedAsPackageBiddingStrategySource" | "NegativeKeywordSharedSetIds" ), ... ],"PackageBiddingStrategy" | "CanBeUsedAsPackageBiddingStrategySource" | "NegativeKeywordSharedSetIds" ), ... ],
    "DynamicTextCampaignSearchStrategyPlacementTypesFieldNames": [ ( "SearchResults" | "ProductGallery" | "DynamicPlaces") ], 
    "CpmBannerCampaignFieldNames": [( "CounterIds" | "FrequencyCap" | "VideoTarget" | "Settings" | "BiddingStrategy" ), ... ],"CanBeUsedAsPackageBiddingStrategySource" ), ... ],
    "UnifiedCampaignFieldNames" : [ ("CounterIds"|"Settings"|"BiddingStrategy"|"PriorityGoals"|"TrackingParams"|"AttributionModel"|"PackageBiddingStrategy"|"CanBeUsedAsPackageBiddingStrategySource") ],
    "UnifiedCampaignSearchStrategyPlacementTypesFieldNames" : [ ( "SearchResults" | "ProductGallery" | "DynamicPlaces" | "Maps" | "SearchOrganizationList" ) ],
    "UnifiedCampaignPackageBiddingStrategyPlatformsFieldNames": [ ( "SearchResult" | "ProductGallery" | "Maps" | "SearchOrganizationList" | "Network" | "DynamicPlaces" ) ],
    "Page": {  /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)** |  |  |   
`SelectionCriteria` |  CampaignsSelectionCriteria |  Campaign selection criteria. To get all of an advertiser's campaigns, leave `SelectionCriteria` empty. |  No  
`FieldNames` |  array of CampaignFieldEnum |  Names of parameters to get that are common to all types of campaigns. |  Yes  
`TextCampaignFieldNames` |  array of TextCampaignFieldEnum |  Names of the requested parameters for "Text & Image Ads" campaigns. See  Note If a different type of campaign is selected according to `SelectionCriteria`, parameters from `TextCampaignFieldNames` are not returned. |  No  
`TextCampaignSearchStrategyPlacementTypesFieldNames` |  array of TextCampaignSearchStrategyPlacementTypesFieldNames |  Placements for search strategies to get. |  No  
`MobileAppCampaignFieldNames` |  array of MobileAppCampaignFieldEnum |  Names of the requested parameters for "Ads for mobile apps" campaigns. See  Note If a different type of campaign is selected according to `SelectionCriteria`, parameters from `MobileAppCampaignFieldNames` are not returned. |  No  
`CpmBannerCampaignFieldNames` |  array of CpmBannerCampaignFieldEnum |  Names of the requested parameters for display campaigns. See  Note If a different type of campaign is selected according to `SelectionCriteria`, parameters from `CpmBannerCampaignFieldNames` are not returned. |  No  
`UnifiedCampaignFieldNames` |  array of UnifiedCampaignFieldEnum |  Names of the requested parameters for a unified performance campaign. See  Note If a different type of campaign is selected according to `SelectionCriteria`, parameters from `UnifiedCampaignFieldNames` are not returned. |  No  
`UnifiedCampaignSearchStrategyPlacementTypesFieldNames` |  array of UnifiedCampaignSearchStrategyPlacementTypesFieldNames |  Placements for search strategies to get. |  No  
`UnifiedCampaignPackageBiddingStrategyPlatformsFieldNames` |  array of UnifiedCampaignPackageBiddingStrategyPlatformsFieldNames |  Placements for portfolio strategies to get. |  No  
`Page` |  |  Structure that defines the page for  |  No  
**CampaignsSelectionCriteria structure** |  |  |   
`Ids` |  array of long |  Selects campaigns with the specified IDs. Maximum of 1000 items in the array. |  No  
`Types` |  array of CampaignTypeEnum |  Selects campaigns of the specified types. See  |  No  
`States` |  array of CampaignStateEnum |  Selects campaigns with the specified states. For a description of the states, see the section  |  No  
`Statuses` |  array of CampaignStatusSelectionEnum |  Selects campaigns with the specified statuses. For a description of the statuses, see the section  |  No  
`StatusesPayment` |  array of CampaignStatusPaymentEnum |  Selects campaigns with the specified payment statuses. For a description of the statuses, see the section  |  No  
##  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Campaigns": [{  /* CampaignGetItem */
      "Id": (long),
      "Name": (string),
      "StartDate": (string),
      "Type": ( "TEXT_CAMPAIGN" | "MOBILE_APP_CAMPAIGN" | "UNIFIED_CAMPAIGN" | "UNKNOWN" ),
      "Status": ( "ACCEPTED" | "DRAFT" | "MODERATION" | "REJECTED" | "UNKNOWN" ),
      "State": ( "ARCHIVED" | "CONVERTED" | "ENDED" | "OFF" | "ON" | "SUSPENDED" | "UNKNOWN" ),
      "StatusPayment": ( "DISALLOWED" | "ALLOWED" ),
      "StatusClarification": (string),
      "SourceId": (long), /* nillable */
      "Statistics": {  /* Statistics */
        "Clicks": (long), /* required */
        "Impressions": (long) /* required */
      },
      "Currency": ( "RUB" | ... | "USD" ),
      "Funds": {  /* FundsParam */
        "Mode": ( "CAMPAIGN_FUNDS" | "SHARED_ACCOUNT_FUNDS" ), /* required */
        "CampaignFunds": {  /* CampaignFundsParam */
          "Sum": (long), /* required */
          "Balance": (long), /* required */
          "BalanceBonus": (long), /* required */
          "SumAvailableForTransfer": (long)
        },
        "SharedAccountFunds": {  /* SharedAccountFundsParam */
          "Refund": (long),
          "Spend": (long)
        }
      },
      "RepresentedBy": {  /* CampaignAssistant */
        "Manager": (string), /* nillable */
        "Agency": (string) /* nillable */
      },
      "DailyBudget": {  /* DailyBudget */
        "Amount": (long), /* required */
        "Mode": ( "STANDARD" | "DISTRIBUTED" ) /* required */
      }, /* nillable */
      "EndDate": (string), /* nillable */
      "NegativeKeywords": {  /* ArrayOfString */
        "Items": [(string), ... ] /* required */
      }, /* nillable */
      "BlockedIps": {  /* ArrayOfString */
        "Items": [(string), ... ] /* required */
      }, /* nillable */
      "ExcludedSites": {  /* ArrayOfString */
        "Items": [(string), ... ] /* required */
      }, /* nillable */
      "TextCampaign": {  /* TextCampaignGetItem */
        ... text campaign params ...
      },
      "MobileAppCampaign": {  /* MobileAppCampaignGetItem */
        ... mobile app campaign params ...
      },
      "CpmBannerCampaign": {  /* CpmBannerCampaignGetItem */
        ... cpm banner campaign params ...
      },
      "UnifiedCampaign": {  /* SmartCampaignGetItem */
        ... unified campaign params ...
      },
      "ClientInfo": (string), /* nillable */
      "Notification": {  /* Notification */ /* nillable */
        "SmsSettings": {  /* SmsSettings */
          "Events": [( "MONITORING" | ... | "FINISHED" ), ... ],
          "TimeFrom": (string),
          "TimeTo": (string)
        },
        "EmailSettings": {  /* EmailSettings */
          "Email": (string),
          "CheckPositionInterval": (int),
          "WarningBalance": (int),
          "SendAccountNews": ( "YES" | "NO" ),
          "SendWarnings": ( "YES" | "NO" )
        }
      },
      "TimeTargeting": {  /* TimeTargeting */
        "Schedule": {  /* ArrayOfString */
          "Items": [(string), ... ] /* required */
        },
        "ConsiderWorkingWeekends": ( "YES" | "NO" ), /* required */
        "HolidaysSchedule": {  /* TimeTargetingOnPublicHolidays */
          "SuspendOnHolidays": ( "YES" | "NO" ), /* required */
          "BidPercent": (int),
          "StartHour": (int),
          "EndHour": (int)
        } /* nillable */
      },
      "TimeZone": (string)
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`Campaigns` |  array of CampaignGetItem |  Campaigns.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section   
**CampaignGetItem structure** |  |   
`Id` |  long |  The campaign ID.  
`Name` |  string |  Campaign name (maximum of 255 characters).  
`ClientInfo` |  string, nillable |  Client name (maximum of 255 characters). The default value is the name from the advertiser's settings.  
`StartDate` |  string |  Start date for displaying ads, in the format YYYY-MM-DD. Can't be earlier than the current date. Ad impressions begin at 00:00 (UTC+3) regardless of the `TimeZone` parameter. The start time for impressions is affected by the time targeting settings (the `TimeTargeting` parameter). Ad displays are possible only if at least one ad has passed review and funds have been credited to the campaign or shared account. If you set a   
`EndDate` |  string, nillable |  End date for displaying ads, in the format YYYY-MM-DD. Ad impressions end at 00:00 (UTC+3) regardless of the `TimeZone` parameter.  
`TimeTargeting` |  TimeTargeting |  Settings for time targeting and hourly bid adjustments. Specified for the time zone set in the `TimeZone` parameter.  
`TimeZone` |  string |  Time zone of the advertiser's location. Use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method to get a reference list of time zones. The default value is Europe/Moscow.  
`NegativeKeywords` |  ArrayOfString, nillable |  Array of negative keywords that are shared by all the keywords of a campaign. Alert This parameter can't be used with display campaigns. A keyword should be specified without the minus sign before the first word. Maximum of 7 words per keyword. The maximum length of each word is 35 characters. The maximum combined length of negative keywords in the array is 20,000 characters. Spaces, dashes, and operators are not counted as part of the total length.  
`BlockedIps` |  ArrayOfString, nillable |  Array of IP addresses that campaign ads should not be shown to. Maximum of 25 items in the array.  
`ExcludedSites` |  ArrayOfString, nillable |  Array of display places where the ad shouldn't be displayed:
  * Domain names of websites.
  * IDs of mobile apps (the bundle ID for iOS, or the package name for Android).
  * Names of ad exchanges (SSPs). You can get a list of names using the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method.

Maximum of 1000 items in the array. Maximum of 255 characters per array item.  
`DailyBudget` |  DailyBudget, nillable |  Settings for the daily budget of a campaign. Daily budget management is available if a manual display strategy is selected in the campaign. Otherwise, an attempt to set the daily budget results in an error.  
`Notification` |  Notification, nillable |  Settings for SMS and email notifications.  
`Type` |  CampaignTypeGetEnum |  Type of campaign. See   
`Status` |  StatusEnum |  Status of the campaign. See   
`State` |  CampaignStateGetEnum |  Campaign state. See   
`StatusPayment` |  CampaignStatusPaymentEnum |  Campaign payment status. For a description of the statuses, see the section   
`StatusClarification` |  string |  Text explanation of the status.  
`SourceId` |  long, nillable |  ID of the unit-based source campaign, if the current campaign was created automatically when switching the advertiser to a real currency.  
`Statistics` |  Statistics |  Statistics for displays and clicks since the campaign was launched.  
`Currency` |  CurrencyEnum |  Campaign currency. It's the same as the advertiser's currency for all campaigns except campaigns run in Yandex units that were copied when the advertiser switched to a real currency. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method.  
`Funds` |  FundsParam |  Financial indicators of the campaign.  
`RepresentedBy` |  CampaignAssistant |  The Yandex personal manager or agency handling the campaign.  
`TextCampaign` |  TextCampaignGetItem |  Settings for campaigns of the "Text & Image ads" type. For a description of the data structure, see the section [get: TextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-text-campaign).  
`MobileAppCampaign` |  MobileAppCampaignGetItem |  Settings for "Ads for mobile apps" campaigns. For a description of the data structure, see the section [get: MobileAppCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-mobile-app-campaign).  
`CpmBannerCampaign` |  CpmBannerCampaignGetItem |  Settings for display campaigns. For a description of the data structure, see the section [get: CpmBannerCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-cpm-banner-campaign).  
`UnifiedCampaign` |  UnifiedCampaignGetItem |  Settings for unified performance campaigns. For a data structure description, see [get: UnifiedCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-unified-campaign).  
**TimeTargeting structure** |  |   
`Schedule` |  ArrayOfString |  Settings for time targeting and hourly bid adjustments. Maximum of 7 items in the array. Each array item contains 25 comma-separated numbers. The first number is the number of the day of the week: from 1 (Monday) to 7 (Sunday). The next 24 numbers are a sequence of bid coefficients for displaying ads in the corresponding hours. Coefficients are specified as percentages from 0 to 200. The value must be a multiple of 10: If the coefficient is 0, no ads are served during this hour. Example of an array element: 1, 0, 0, 50, 50, 100, 100, 150, 200, 200, 150, 100, 100, 80, 70, 100, 100, 100, 50, 50, 40, 30, 0, 0, 0 Note
  * If the array is missing an element for one of the days of the week, all the bid coefficients are set to 100 for this day.
  * If an automatic display strategy is selected, the coefficient 0 means displays are not allowed, and any other coefficient means displays are allowed (in other words, it is equivalent to 100).

  
`ConsiderWorkingWeekends` |  YesNoEnum |  Whether to change the display schedule when a work day is moved to Saturday or Sunday because of a public holiday. For example, if a work day is moved from Monday to Saturday and the value is YES, on the Saturday work day, ads are displayed according to the Monday schedule, and on the Monday holiday, they are displayed according to the Saturday schedule.  
`HolidaysSchedule` |  TimeTargetingOnPublicHolidays, nillable |  Display settings on public holidays. If the time zone specified in the `TimeZone` parameter is specific to Russia, Ukraine, Belarus, Kazakhstan, or Turkey, that country's holiday calendar will be used. In all other cases, we use the Russian calendar.  
**TimeTargetingOnPublicHolidays structure** |  |   
`SuspendOnHolidays` |  YesNoEnum |  Whether to suspend ads on public holidays: YES — suspend; NO — don't suspend. Note You can specify the `BidPercent`, `StartHour`, and `EndHour` parameters only if the `SuspendOnHolidays` parameter is set to NO.  
`BidPercent` |  int |  The bid coefficient for displays on public holidays. Specified as a percentage from 0 to 200. The value must be a multiple of 10.  
`StartHour` |  int |  The time (in hours) to start displays on public holidays. From 0 to 23.  
`EndHour` |  int |  The time (in hours) to end displays on public holidays. From 0 to 24.  
**DailyBudget structure** |  |   
`Amount` |  long |  The daily campaign budget in the advertiser currency, multiplied by 1,000,000. The minimum daily budget for each currency is listed in the currency reference. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/campaigns/en/dictionaries/get) method.  
`Mode` |  DailyBudgetModeEnum |  Mode for displaying ads:
  * STANDARD — standard
  * DISTRIBUTED — distributed

See   
**Notification structure** |  |   
`SmsSettings` |  SmsSettings |  Settings for sending SMS notifications. The phone number to send notifications to is taken from the advertiser's Yandex profile (see [My numbers](https://yandex.com/support/passport/authorization/phone.html) in Yandex Passport Help). Can't be set for UnifiedCampaign.  
`EmailSettings` |  EmailSettings |  Settings for sending email notifications.  
**SmsSettings structure** |  |   
`Events` |  array of SmsEventsEnum |  Events to notify of by SMS:
  * MONITORING — Pausing and resuming ad displays by site availability monitoring using Metrica data.
  * MODERATION — Ads accepted or rejected after review.
  * MONEY_IN — Funds deposited to the campaign balance (not used when a shared account is enabled).
  * MONEY_OUT — Funds used up on the campaign balance (not used when a shared account is enabled).
  * FINISHED — End of the campaign.

  
`TimeFrom` |  string |  The allowed starting time for sending SMS notifications of campaign events. Specified in the format HH:MM; minutes are set in multiples of 15 (0, 15, 30, 45). For example, 19:45. The default value is 9:00.  
`TimeTo` |  string |  The ending time for sending SMS notifications of campaign events. Specified in the format HH:MM; minutes are set in multiples of 15 (0, 15, 30, 45). For example, 19:45. The default value is 21:00.  
**EmailSettings structure** |  |   
`Email` |  string |  The email address for sending notifications of campaign events. The default value is the advertiser's address.  
`CheckPositionInterval` |  int |  The frequency of checking the traffic forecast: 15, 30 or 60 minutes. The default value is 60. A notification is sent if the traffic forecast is lower than the one that the bid covered at the time of configuration. Can't be set for UnifiedCampaign.  
`WarningBalance` |  int |  The minimal balance; notification is sent when the account balance is reduced to this amount. Set as a percentage of the amount of the last payment, from 1 to 50. The default value is 20. If the client has the shared account enabled, this parameter is not used. Can't be set for UnifiedCampaign.  
`SendAccountNews` |  YesNoEnum |  Whether to send notifications of events related to the campaign. It is set for campaigns that have a personal Yandex manager. For campaigns that are not handled by a personal manager, the passed value is ignored. The default value is NO.  
`SendWarnings` |  YesNoEnum |  Whether to send email notifications. The default value is NO. Can't be set for UnifiedCampaign.  
**Statistics structure** |  |   
`Impressions` |  long |  The number of impressions since the campaign was launched.  
`Clicks` |  long |  The number of clicks since the campaign was launched.  
**FundsParam structure** |  |   
`Mode` |  CampaignFundsEnum |  Type of financial indicators for the campaign:
  * CAMPAIGN_FUNDS: The shared account isn't enabled, and financial indicators are returned in the `CampaignFund` child structure.
  * SHARED_ACCOUNT_FUNDS: The shared account is enabled, and financial indicators are returned in the `SharedAccountFund` child structure.

  
`CampaignFunds` |  [CampaignFundsParam](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#CampaignFundsParam) |  The campaign's financial indicators, if the shared account is not enabled.  
`SharedAccountFunds` |  [SharedAccountFundsParam](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#SharedAccountFundsParam) |  The campaign's financial indicators, if the shared account is enabled.  
**CampaignFundsParam structure** |  |   
`Sum` |  long |  The amount of funds credited to the campaign balance since the campaign was launched, in the advertiser's currency with VAT included.  
`Balance` |  long |  The current balance of the campaign, in the advertiser's currency without VAT.  
`BalanceBonus` |  long |  Discount bonus. This parameter is no longer relevant.  
`SumAvailableForTransfer` |  long |  The amount available for transferring to another campaign, in the advertiser's currency without VAT.  
**SharedAccountFundsParam structure** |  |   
`Refund` |  long |  This parameter is obsolete. Always returns 0.  
`Spend` |  long |  The amount of funds spent on this campaign since its launch, in the advertiser's currency with VAT included.  
**CampaignAssistant structure** |  |   
`Manager` |  string, nillable |  The name of the Yandex personal manager (for campaigns that are handled by a personal manager).  
`Agency` |  string, nillable |  The name of the advertising agency (for campaigns that are handled by an agency).  
###  [](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get#learn-more1)Learn more
  * [get: TextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-text-campaign)
  * [get: UnifiedCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-unified-campaign)
  * [get: MobileAppCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-mobile-app-campaign)


Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/delete)
Next
[get: TextCampaign parameters](https://yandex.com/dev/direct/doc/en/campaigns/en/campaigns/get-text-campaign)
