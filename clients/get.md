---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/clients/get
crawled_at: 2025-09-17T15:42:19.042525
---

get
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/clients/en/clients/get#learn-more)
  * [Request](https://yandex.com/dev/direct/doc/en/clients/en/clients/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/clients/en/clients/get#output)


For an advertiser's representative, returns advertiser parameters and user settings; for an agency's representative, returns agency parameters and user settings.
**Request on behalf of an advertiser's representative**
Any representative of an advertiser can get the advertiser's parameters and their own personal settings.
The advertiser's chief representative can also retrieve the settings of another representative. To do this, they need pass the representative's username in the `Client-Login` request header.
**Request on behalf of an agency's representative**
Any agency representative can also get the advertiser parameters for an agency client and the user settings for the advertiser's representative. To do this, pass the login of the advertiser's representative within the `Client-Login` request header.
Any agency representative can also get the agency parameters and their own personal settings.
The agency's chief representative can also retrieve the settings of another agency representative. To do this, they need to pass the representative's username in the `Client-Login` request header.
##  [](https://yandex.com/dev/direct/doc/en/clients/en/clients/get#learn-more)Learn more
  * [Client](https://yandex.com/dev/direct/doc/dg/objects/client.html)
  * [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html)


##  [](https://yandex.com/dev/direct/doc/en/clients/en/clients/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "FieldNames": [( "AccountQuality" | "Archived" | "ClientId" | "ClientInfo" | "CountryId" | "CreatedAt" | "Currency" | "Grants" | "Bonuses" | "Login" | "Notification" | "OverdraftSumAvailable" | "Phone" | "Representatives" | "Restrictions" | "Settings" | "Type" | "VatRate" | "ForbiddenPlatform" | "AvailableCampaignTypes" ), ... ] /* required */,
    "TinInfoFieldNames" : [ ( "TinType" | "Tin" ), ... ],
    "OrganizationFieldNames": [( "Name" | "EpayNumber" | "RegNumber" | "OksmNumber" | "OkvedCode" ), ... ],
    "ContractFieldNames": [( "Number" | "Date" | "Price" | "Type" | "ActionType" | "SubjectType" ), ... ],
    "ContragentFieldNames": [( "Name" | "Phone" | "EpayNumber" | "RegNumber" | "OksmNumber" ), ... ],
    "ContragentTinInfoFieldNames": [( "TinType" | "Tin" ), ... ]
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)**  
`FieldNames` |  array of ClientFieldEnum |  The names of parameters to get. Alert The response doesn't return the agency parameters `AccountQuality`, `Currency`, `Grants`, `OverdraftSumAvailable`, `Restrictions`, and `Settings`. |  Yes  
`TinInfoFieldNames` |  array of TinInfoFieldEnum |  Names of parameters with the required tax details of the end-advertiser. |  No  
`OrganizationFieldNames` |  array of OrganizationFieldEnum |  Names of parameters with the required details about the organization of the end advertiser. |  No  
`ContractFieldNames` |  array of ContractFieldEnum |  Names of parameters with the required details about the client counterparty contract with the end-advertiser. |  No  
`ContragentFieldNames` |  array of ContragentFieldEnum |  Names of parameters with the required details about the counterparty. |  No  
`ContragentTinInfoFieldNames` |  array of TinInfoFieldEnum |  Names of parameters with the required tax details of the counterparty. |  No  
##  [](https://yandex.com/dev/direct/doc/en/clients/en/clients/get#output)Response
Note
The `Login`, `ClientInfo`, `CreatedAt`, `Notification`, and `Phone` parameters belong to the representative, not to the advertiser or agency:
  * The user on whose behalf the request is made, if the `Client-Login` HTTP header isn't included in the request.
  * The user whose username is specified in the `Client-Login` HTTP header, if the request includes the `Client-Login` HTTP header.


The other parameters are related to the advertiser or the agency, regardless of who the representative is.
Response structure in JSON format:
```
{
  "result": { /* result */
    "Clients": [{  /* ClientGetItem */
      "AccountQuality": (decimal), /* nillable */
      "Archived": ( "YES" | "NO" ),
      "ClientId": (long),
      "ClientInfo": (string),
      "CountryId": (int),
      "CreatedAt": (string),
      "Currency": ( "RUB" | "BYN" | "CHF" | "EUR" | "KZT" | "TRY" | "UAH" | "USD" ),
      "Grants": [{  /* GrantGetItem */
        "Privilege": ( "EDIT_CAMPAIGNS" | "IMPORT_XLS" | "TRANSFER_MONEY" ), /* required */
        "Value": ( "YES" | "NO" ), /* required */
        "Agency": (string)
      }, ... ],
      "Bonuses" : {  /* BonusesGet */
        "AwaitingBonus" : (long) /* required */,
        "AwaitingBonusWithoutNds" : (long) /* required */
      },
      "Login": (string),
      "Notification": {  /* NotificationGet */
        "Lang": ( "RU" | "UK" | "EN" | "TR" ), /* required */
        "SmsPhoneNumber": (string), /* required */
        "Email": (string), /* required */
        "EmailSubscriptions": [{  /* EmailSubscriptionItem */
          "Option": ( "RECEIVE_RECOMMENDATIONS" | "TRACK_MANAGED_CAMPAIGNS" | "TRACK_POSITION_CHANGES" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ]
      },
      "OverdraftSumAvailable": (long),
      "Phone": (string),
      "Representatives": [{  /* Representative */
        "Login": (string), /* required */
        "Email": (string), /* required */
        "Role": ( "CHIEF" | "DELEGATE" | "LIMITED" | "READONLY" | "UNKNOWN" ) /* required */
      }, ... ],
      "Restrictions": [{  /* ClientRestrictionItem */
        "Element": ( "CAMPAIGNS_TOTAL_PER_CLIENT" | "CAMPAIGNS_UNARCHIVED_PER_CLIENT" | "ADGROUPS_TOTAL_PER_CAMPAIGN" | "ADS_TOTAL_PER_ADGROUP" | "KEYWORDS_TOTAL_PER_ADGROUP" | "AD_EXTENSIONS_TOTAL" | "STAT_REPORTS_TOTAL_IN_QUEUE" | "FORECAST_REPORTS_TOTAL_IN_QUEUE" | "WORDSTAT_REPORTS_TOTAL_IN_QUEUE" | "API_POINTS" | "GENERAL_DOMAIN_BLACKLIST_SIZE" | "VIDEO_DOMAIN_BLACKLIST_SIZE" ), /* required */
        "Value": (int) /* required */
      }, ... ],
      "Settings": [{  /* ClientSettingGetItem */
        "Option": ( "CORRECT_TYPOS_AUTOMATICALLY" | "DISPLAY_STORE_RATING" | "SHARED_ACCOUNT_ENABLED" ), /* required */
        "Value": ( "YES" | "NO" ) /* required */
      }, ... ],
      "Type": (string),
      "VatRate": (decimal) /* nillable */,
      "ForbiddenPlatform": ("SEARCH" | "NETWORK" | "NONE"),
      "AvailableCampaignTypes": ("TEXT_CAMPAIGN" | "MOBILE_APP_CAMPAIGN" | "DYNAMIC_TEXT_CAMPAIGN" | "CPM_BANNER_CAMPAIGN" | "SMART_CAMPAIGN" | "CONTENT_PROMOTION" | "BILLING_AGGREGATE" | "UNIFIED_CAMPAIGN" ),
      "TinInfo" : { /* TinInfoGet */
        "TinType" : ( "PHYSICAL" | "FOREIGN_PHYSICAL" | "LEGAL" | "FOREIGN_LEGAL" | "INDIVIDUAL" ),
        "Tin" : (string) /* nillable */
      },
      "ErirAttributes": { /* ErirAttributesGet */
        "Organization": { /* OrganizationGet */
          "Name": (string), /* nillable */
          "EpayNumber": (string), /* nillable */
          "RegNumber": (string), /* nillable */
          "OksmNumber": (string), /* nillable */
          "OkvedCode": (string) /* nillable */
        },
        "Contract": { /* ContractGet */
          "Number": (string), /* nillable */
          "Date": (string), /* nillable */
          "Type": ( "CONTRACT" | "INTERMEDIARY_CONTRACT" | "ADDITIONAL_AGREEMENT" ), /* nillable */
          "ActionType": ( "COMMERCIAL" | "DISTRIBUTION" | "CONCLUDE" | "OTHER" ), /* nillable */
          "SubjectType": ( "REPRESENTATION" | "MEDIATION" | "DISTRIBUTION" | "ORG_DISTRIBUTION" | "OTHER" ), /* nillable */
          "Price": { /* PriceGet */
            "Amount": (decimal), /* required */
            "IncludingVat": ( "YES" | "NO" ) /* required */
          }
        },
        "Contragent": { /* ContragentGet */
          "Name": (string), /* nillable */
          "Phone": (string), /* nillable */
          "EpayNumber": (string), /* nillable */
          "RegNumber": (string), /* nillable */
          "OksmNumber": (string), /* nillable */
          "TinInfo": { /* TinInfoGet */
            "TinType": ( "PHYSICAL" | "FOREIGN_PHYSICAL" | "LEGAL" | "FOREIGN_LEGAL" | "INDIVIDUAL" ),
            "Tin": (string) /* nillable */
          }
        }
      }
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **For an advertiser** |  **For an agency**  
---|---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`Clients` |  array of ClientGetItem |  Advertiser parameters and user settings for the advertiser's representative. |  Agency parameters and user settings for the agency's representative.  
**ClientGetItem structure**  
`AccountQuality` |  decimal, nillable |  Account quality index. |  —  
`Archived` |  YesNoEnum |  Indicates that the advertiser is archived (inactive). |  Indicates that the agency is archived (inactive).  
`ClientId` |  long |  Advertiser ID. |  Agency ID.  
`ClientInfo` |  string |  First and last name of the Yandex Direct user (no more than 255 characters). |  First and last name of the Yandex Direct user (no more than 255 characters).  
`CountryId` |  int |  ID of the advertiser's country from the reference list of regions.  
To get the list of regions, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/clients/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/clients/en/dictionaries/get) method. |  ID of the agency's country from the reference list of regions.  
To get the list of regions, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/clients/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/clients/en/dictionaries/get) method.  
`CreatedAt` |  string |  Date the user was registered in Yandex Direct, in the format YYYY-MM-DD. |  Date the user was registered in Yandex Direct, in the format YYYY-MM-DD.  
`Currency` |  CurrencyEnum |  The advertiser's currency. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/clients/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/clients/en/dictionaries/get) method. |  —  
`Grants` |  array of GrantGetItem |  The advertiser's permissions for campaign management. |  —  
`Bonuses` |  BonusesGet |  The pending bonus to be credited. This parameter can be used only with the RUB currency. |  The pending bonus to be credited. This parameter can be used only with the RUB currency.  
`Login` |  string |  Username of the Yandex Direct user. |  Username of the Yandex Direct user.  
`Notification` |  NotificationGet |  The Yandex Direct user's settings for SMS and email notifications. |  The Yandex Direct user's settings for SMS and email notifications.  
`OverdraftSumAvailable` |  long |  The overdraft limit currently available to the advertiser (see  It's returned as an integer that represents the overdraft limit in the advertiser's currency, multiplied by 1,000,000. |  —  
`Phone` |  string |  Phone number of the Yandex Direct user (255 characters maximum). |  Phone number of the Yandex Direct user (255 characters maximum).  
`Representatives` |  array of Representative |  Advertiser representatives (see  Returns all the representatives for the chief representative, or just the chief representative for a normal representative. |  Agency representatives (see  For the chief representative, returns all the representatives; for all other representatives, returns just the chief representative.  
`Restrictions` |  array of ClientRestrictionItem |  Limits on the number of objects for an advertiser. |  —  
`Settings` |  array of ClientSettingGetItem |  Advertiser settings that only allow YES or NO values. |  —  
`Type` |  string |  Type of client:
  * CLIENT — Direct advertiser.
  * SUBCLIENT: An advertiser that is an agency client.

See [Client](https://yandex.com/dev/direct/doc/dg/objects/client.html). |  Type of client: AGENCY.  
`VatRate` |  decimal, nillable |  The VAT rate of the client who is making the payment, meaning the advertiser or agency. |  The agency's VAT rate.  
`ForbiddenPlatform` |  ForbiddenPlatformEnum |  Blocked sites:
  * SEARCH.
  * NETWORK.
  * NONE.

|   
`AvailableCampaignTypes` |  AvailableCampaignTypesEnum |  Campaign types available by login:
  * TEXT_CAMPAIGN.
  * MOBILE_APP_CAMPAIGN.
  * DYNAMIC_TEXT_CAMPAIGN.
  * CPM_BANNER_CAMPAIGN.
  * SMART_CAMPAIGN.
  * CONTENT_PROMOTION.
  * BILLING_AGGREGATE.
  * UNIFIED_CAMPAIGN.

|   
`TinInfo` |  TinInfoGet |  Tax data of the end-advertiser. |  —  
`ErirAttributes` |  ErirAttributesGet |  Additional advertiser data to label ads with. |  —  
**GrantGetItem structure**  
`Privilege` |  PrivilegeEnum |  Name of the permission:
  * EDIT_CAMPAIGNS: Edit campaigns.
  * IMPORT_XLS: Use files to manage campaigns (see 
  * TRANSFER_MONEY: Transfer funds between campaigns (see 

|  —  
`Value` |  YesNoEnum |  Whether the client has this permission. |  —  
`Agency` |  string |  The name of the advertising agency, if the permission is granted by an agency. |  —  
**BonusesGet structure**  
`AwaitingBonus` |  decimal |  The bonus amount to be credited, with VAT. Returned as an integer multiplied by 1,000,000. |  The bonus amount to be credited, with VAT. Returned as an integer multiplied by 1,000,000.  
`AwaitingBonusWithoutNds` |  decimal |  The bonus amount to be credited, without VAT. Returned as an integer multiplied by 1,000,000. |  The bonus amount to be credited, without VAT. Returned as an integer multiplied by 1,000,000.  
**NotificationGet structure**  
`Lang` |  LangEnum |  Language for notifications. |  Language for notifications.  
`SmsPhoneNumber` |  string |  The phone number for sending SMS notifications from the user's Yandex profile (see  |  The phone number for sending SMS notifications from the user's Yandex profile (see   
`Email` |  string |  The email address for sending notifications related to the account (no more than 255 characters). |  The email address for sending notifications related to the account (no more than 255 characters).  
`EmailSubscriptions` |  array of EmailSubscriptionItem |  Types of notifications to send by email. |  —  
**EmailSubscriptionItem structure**  
`Option` |  EmailSubscriptionEnum |  Type of notification:
  * RECEIVE_RECOMMENDATIONS — Yandex Direct news and recommendations.
  * TRACK_MANAGED_CAMPAIGNS: Notifications for campaigns that have a personal manager.
  * TRACK_POSITION_CHANGES: Warnings about traffic forecasts falling lower than the bid provided at the time of configuration.

|  —  
`Value` |  YesNoEnum |  Whether to send this type of notification. |  —  
**Representative structure**  
`Login` |  string |  Username. |  Username.  
`Email` |  string |  Email address to send notifications to. |  Email address to send notifications to.  
`Role` |  RepresentativeRoleEnum |  The user's role:
  * CHIEF: Chief representative of the advertiser.
  * DELEGATE: An advertiser's representative with full access.
  * READONLY: A representative with read-only access.
  * UNKNOWN: This role isn't supported in this version of the API.

See [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html). |  The user's role:
  * CHIEF: Chief representative of the agency.
  * DELEGATE: Representative of the agency.
  * LIMITED: Representative of the agency who manages clients.
  * UNKNOWN: This role isn't supported in this version of the API.

See [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html).  
**ClientRestrictionItem structure**  
`Element` |  ClientRestrictionEnum |  Name of the restriction:
  * CAMPAIGNS_TOTAL_PER_CLIENT: The maximum number of campaigns per advertiser.
  * CAMPAIGNS_UNARCHIVED_PER_CLIENT: The maximum number of unarchived campaigns per advertiser.
  * ADGROUPS_TOTAL_PER_CAMPAIGN: The maximum number of groups per campaign.
  * ADS_TOTAL_PER_ADGROUP: The maximum number of ads per group.
  * KEYWORDS_TOTAL_PER_ADGROUP: The maximum number of keywords per group.
  * AD_EXTENSIONS_TOTAL: The maximum number of ad extensions per advertiser.
  * STAT_REPORTS_TOTAL_IN_QUEUE: The maximum number of statistical reports being generated simultaneously.
  * FORECAST_REPORTS_TOTAL_IN_QUEUE: The maximum number of budget forecast reports stored on the server.
  * WORDSTAT_REPORTS_TOTAL_IN_QUEUE: The maximum number of search query statistics reports stored on the server.
  * API_POINTS: The daily limit of points.
  * GENERAL_DOMAIN_BLACKLIST_SIZE: The maximum number of sites where ad serving is not allowed.
  * VIDEO_DOMAIN_BLACKLIST_SIZE: The maximum number of sites where serving video ads is not allowed.

|  —  
`Value` |  int |  The limit value. |  —  
**ClientSettingGetItem structure**  
`Option` |  ClientSettingGetEnum |  Setting name:
  * CORRECT_TYPOS_AUTOMATICALLY: Automatically fix errors and typos.
  * DISPLAY_STORE_RATING: Add data from external sources to the ad (see 
  * SHARED_ACCOUNT_ENABLED: The shared account is enabled.

|  —  
`Value` |  YesNoEnum |  Setting value. |  —  
**TinInfoGet structure**  
`TinType` |  TinTypeEnum |  Organization type:
  * LEGAL: A legal entity.
  * PHYSICAL: An individual.
  * INDIVIDUAL: An individual entrepreneur.
  * FOREIGN_LEGAL: A foreign legal entity.
  * FOREIGN_PHYSICAL: A foreign individual.

|  —  
`Tin` |  string |  The taxpayer number or its equivalent in the country of registration. |  —  
**ErirAttributesGet structure**  
`Organization` |  OrganizationGet |  Details about the organization of the end-advertiser. |  —  
`Contract` |  ContractGet |  Details of the contract of the client counterparty with the end-advertiser. |  —  
`Contragent` |  ContragentGet |  Information about the counterparty of the end-advertiser. |  —  
**OrganizationGet structure**  
`Name` |  string |  Organization name. |  —  
`EpayNumber` |  string |  The number of the electronic payment instrument. |  —  
`RegNumber` |  string |  Registration number or its equivalent. |  —  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM. |  —  
`OkvedCode` |  string |  Business category code according to OKVED. |  —  
**ContractGet structure**  
`Number` |  string |  Contract number. |  —  
`Date` |  string |  Contract date in the format YYYY-MM-DD. |  —  
`Type` |  ContractTypeEnum |  Type of contract:
  * CONTRACT: A service contract.
  * INTERMEDIARY_CONTRACT: An intermediary contract.
  * ADDITIONAL_AGREEMENT: An additional agreement. Alert The ADDITIONAL_AGREEMENT value is obsolete and no longer valid.

|  —  
`ActionType` |  ContractActionTypeEnum |  Types of activities of the intermediary representative:
  * COMMERCIAL: Commercial representation.
  * DISTRIBUTION: Ad distribution activities.
  * CONCLUDE: Conclusion of contracts.
  * OTHER: Other activities.

|  —  
`SubjectType` |  ContractSubjectTypeEnum |  Contract subject:
  * REPRESENTATION: Representation activities.
  * MEDIATION: Mediation activities.
  * DISTRIBUTION: A contract for ad distribution.
  * ORG_DISTRIBUTION: A contract for organizing ad distribution.
  * OTHER: Other activities.

|  —  
`Price` |  ContractPrice |  The value of the contract. |  —  
**ContractPrice structure**  
`Amount` |  decimal |  The value of the contract. |  —  
`IncludingVat` |  YesNoEnum |  Whether VAT is included in the contract value. |  —  
**ContragentGet structure**  
`Name` |  string |  Name. |  —  
`Phone` |  string |  Phone number. |  —  
`EpayNumber` |  string |  The number of the electronic payment instrument. |  —  
`RegNumber` |  string |  Registration number or its equivalent. |  —  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM. |  —  
`TinInfo` |  TinInfoGet |  Tax details of the counterparty. |  —  
Copied
### Was the article helpful?
YesNo
Previous
[Clients: managing advertiser parameters and user settings](https://yandex.com/dev/direct/doc/en/clients/en/clients/clients)
Next
[update](https://yandex.com/dev/direct/doc/en/clients/en/clients/update)
