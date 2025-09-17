---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/agencyclients/get
crawled_at: 2025-09-17T15:42:32.570872
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get#learn-more)
  * [Request](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get#output)


Returns a list of advertisers who are agency clients, their parameters, and settings for each advertiser's chief representative.
Note
For requests to the `AgencyClients` service:
  * In the `Authorization` header, specify the access token you obtained for the agency representative.
  * Don't specify the `Client-Login` header.


##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get#learn-more)Learn more
  * [Client](https://yandex.com/dev/direct/doc/dg/objects/client.html)
  * [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html)
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {  /* AgencyClientsSelectionCriteria */
      "Logins": [(string), ... ],
      "Archived": ( "YES" | "NO" )
    }, /* required */
    "FieldNames": [( "AccountQuality" | "Archived" | "ClientId" | "ClientInfo" | "CountryId" | "CreatedAt" | "Currency" | "Grants" | "Bonuses" | "Login" | "Notification" | "OverdraftSumAvailable" | "Phone" | "Representatives" | "Restrictions" | "Settings" | "Type" | "VatRate" | "ForbiddenPlatform" | "AvailableCampaignTypes" ), ... ], /* required */
    "TinInfoFieldNames" : [( "TinType" | "Tin"), ... ],
    "OrganizationFieldNames": [( "Name" | "EpayNumber" | "RegNumber" | "OksmNumber" | "OkvedCode" ), ... ],
    "ContractFieldNames": [( "Number" | "Date" | "Price" | "Type" | "ActionType" | "SubjectType" ), ... ],
    "ContragentFieldNames": [( "Name" | "Phone" | "EpayNumber" | "RegNumber" | "OksmNumber" ), ... ],
    "ContragentTinInfoFieldNames": [( "TinType" | "Tin" ), ... ],
    "Page": {  /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)** |   
`SelectionCriteria` |  AgencyClientsSelectionCriteria |  Client selection criteria. To retrieve parameters for all of the agency's clients, specify an empty `SelectionCriteria` structure. |  Yes  
`FieldNames` |  array of AgencyClientFieldEnum |  The names of parameters to get. |  Yes  
`TinInfoFieldNames` |  array of TinInfoFieldEnum |  Names of parameters with the required tax details of the end-advertiser. |  No  
`OrganizationFieldNames` |  array of OrganizationFieldEnum |  Names of parameters with the required details about the organization of the end advertiser. |  No  
`ContractFieldNames` |  array of ContractFieldEnum |  Names of parameters with the required details about the client counterparty contract with the end-advertiser. |  No  
`ContragentFieldNames` |  array of ContragentFieldEnum |  Names of parameters with the required details about the counterparty. |  No  
`ContragentTinInfoFieldNames` |  array of TinInfoFieldEnum |  Names of parameters with the required tax details of the counterparty. |  No  
`Page` |  LimitOffset |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page) of data. |  No  
**AgencyClientsSelectionCriteria structure** |   
`Logins` |  array of string |  Selects clients with the specified representative usernames. Maximum of 10,000 items in the array. |  No  
`Archived` |  YesNoEnum |  Selects clients based on whether they are archived: YES – archived clients, NO – active clients. |  No  
##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get#output)Response
Note
  * The `Login`, `ClientInfo`, `CreatedAt`, `Notification`, and `Phone` parameters belong to the advertiser's chief representative (see [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html)). The other parameters relate to the advertiser.
  * If the `Logins` parameter in the request specifies the username of a representative other than the chief representative, the response contains the username of the advertiser's chief representative instead of the username from the request.
  * If the `Logins` parameter in the request specifies usernames of multiple representatives for the same advertiser, this advertiser (and their chief representative) is only listed once in the response.
  * All the advertiser's representatives are listed in the `Representatives` parameter.


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
        }, ... ] /* required */
      },
      "OverdraftSumAvailable": (long),
      "Phone": (string),
      "Representatives": [{  /* Representative */
        "Login": (string), /* required */
        "Email": (string), /* required */
        "Role": ( "CHIEF" | "DELEGATE" | "READONLY" | "UNKNOWN" ) /* required */
      }, ... ],
      "Restrictions": [{  /* ClientRestrictionItem */
        "Element": ( "CAMPAIGNS_TOTAL_PER_CLIENT" | "CAMPAIGNS_UNARCHIVED_PER_CLIENT" | "ADGROUPS_TOTAL_PER_CAMPAIGN" | "ADS_TOTAL_PER_ADGROUP" | "KEYWORDS_TOTAL_PER_ADGROUP" | "AD_EXTENSIONS_TOTAL" | "STAT_REPORTS_TOTAL_IN_QUEUE" | "FORECAST_REPORTS_TOTAL_IN_QUEUE" | "WORDSTAT_REPORTS_TOTAL_IN_QUEUE" | "API_POINTS" | "GENERAL_DOMAIN_BLACKLIST_SIZE" | "VIDEO_DOMAIN_BLACKLIST_SIZE" ), /* required */
        "Value": (int) /* required */
      }, ... ],
      "Settings": [{  /* ClientSettingGetItem */
        "Option": ( "CORRECT_TYPOS_AUTOMATICALLY" | "DISPLAY_STORE_RATING" | "SHARED_ACCOUNT_ENABLED"  ), /* required */
        "Value": ( "YES" | "NO" ) /* required */
      }, ... ],
      "Type": (string),
      "VatRate": (decimal), /* nillable */
      "ForbiddenPlatform": ("SEARCH" | "NETWORK" | "NONE"),
      "AvailableCampaignTypes": ("TEXT_CAMPAIGN" | "MOBILE_APP_CAMPAIGN" | "DYNAMIC_TEXT_CAMPAIGN" | "CPM_BANNER_CAMPAIGN" | "SMART_CAMPAIGN" | "CONTENT_PROMOTION" | "BILLING_AGGREGATE" | "UNIFIED_CAMPAIGN" ),
      "TinInfo": { /* TinInfoGet */
        "TinType": ( "PHYSICAL" | "FOREIGN_PHYSICAL" | "LEGAL" | "FOREIGN_LEGAL" | "INDIVIDUAL" ),
        "Tin": (string) /* nillable */
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
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)**  
`Clients` |  array of ClientGetItem |  Advertisers – agency clients and their chief representatives.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#page).  
**ClientGetItem structure**  
`AccountQuality` |  decimal, nillable |  Account quality index.  
`Archived` |  YesNoEnum |  Indicates that the advertiser is archived (inactive).  
`ClientId` |  long |  Advertiser ID.  
`ClientInfo` |  string |  Client name (maximum of 255 characters).  
`CountryId` |  int |  ID of the advertiser's country from the reference list of regions. To get the list of regions, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/agencyclients/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/agencyclients/en/dictionaries/get) method.  
`CreatedAt` |  string |  Date the user was registered in Yandex Direct, in the format YYYY-MM-DD.  
`Currency` |  CurrencyEnum |  The advertiser's currency. To get the list of currencies, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/agencyclients/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/agencyclients/en/dictionaries/get) method.  
`Grants` |  array of GrantGetItem |  The advertiser's permissions for campaign management.  
`Bonuses` |  BonusesGet |  The pending bonus to be credited. This parameter can be used only with the RUB currency.  
`Login` |  string |  Username of the Yandex Direct user.  
`Notification` |  NotificationGet |  The Yandex Direct user's settings for SMS and email notifications.  
`OverdraftSumAvailable` |  long |  The overdraft limit currently available to the advertiser (see  It's returned as an integer that represents the overdraft limit in the advertiser's currency, multiplied by 1,000,000.  
`Phone` |  string |  Phone number of the Yandex Direct user (50 characters maximum, only numbers allowed, starting with the country code).  
`Representatives` |  array of Representative |  Representatives of the advertiser. See [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html).  
`Restrictions` |  array of ClientRestrictionItem |  Limits on the number of objects for an advertiser.  
`Settings` |  array of ClientSettingGetItem |  Advertiser settings that only allow YES or NO values.  
`Type` |  string |  Client type: SUBCLIENT.  
`VatRate` |  decimal, nillable |  The agency's VAT rate.  
`ForbiddenPlatform` |  ForbiddenPlatformEnum |  Blocked sites:
  * SEARCH.
  * NETWORK.
  * NONE.

  
`AvailableCampaignTypes` |  AvailableCampaignTypesEnum |  Campaign types available by login:
  * TEXT_CAMPAIGN.
  * MOBILE_APP_CAMAIGN.
  * DYNAMIC_TEXT_CAMPAIGN.
  * CPM_BANNER_CAMPAIGN.
  * SMART_CAMPAIGN.
  * CONTENT_PROMOTION.
  * BILLING_AGGREGATE.
  * UNIFIED_CAMPAIGN.

  
`TinInfo` |  TinInfoGet |  Tax data of the end-advertiser.  
`ErirAttributes` |  ErirAttributesGet |  Additional advertiser data to label ads with.  
**GrantGetItem structure**  
`Privilege` |  PrivilegeEnum |  Name of the permission:
  * EDIT_CAMPAIGNS: Edit campaigns.
  * IMPORT_XLS: Use files to manage campaigns (see 
  * TRANSFER_MONEY: Transfer funds between campaigns (see 

  
`Value` |  YesNoEnum |  Whether the client has this permission.  
`Agency` |  string |  The name of the advertising agency, if the permission is granted by an agency.  
**BonusesGet structure**  
`AwaitingBonus` |  long |  The bonus amount to be credited, with VAT. Returned as an integer multiplied by 1,000,000.  
`AwaitingBonusWithoutNds` |  long |  The bonus amount to be credited, without VAT. Returned as an integer multiplied by 1,000,000.  
**NotificationGet structure**  
`Lang` |  LangEnum |  Language for notifications.  
`SmsPhoneNumber` |  string |  The phone number for sending SMS notifications from the user's Yandex profile (see   
`Email` |  string |  The email address for sending notifications related to the account (no more than 255 characters).  
`EmailSubscriptions` |  array of EmailSubscriptionItem |  Types of notifications to send by email.  
**EmailSubscriptionItem structure**  
`Option` |  EmailSubscriptionEnum |  Type of notification:
  * RECEIVE_RECOMMENDATIONS — Yandex Direct news and recommendations.
  * TRACK_MANAGED_CAMPAIGNS: Notifications for campaigns that have a personal manager.
  * TRACK_POSITION_CHANGES: Warnings about traffic forecasts falling lower than the bid provided at the time of configuration.

  
`Value` |  YesNoEnum |  Whether to send this type of notification.  
**Representative structure**  
`Login` |  string |  Username.  
`Email` |  string |  Email address to send notifications to.  
`Role` |  RepresentativeRoleEnum |  The user's role:
  * CHIEF: Chief representative of the advertiser.
  * DELEGATE: An advertiser's representative with full access.
  * READONLY: A representative with read-only access.
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

  
`Value` |  int |  The limit value.  
**ClientSettingGetItem structure**  
`Option` |  ClientSettingGetEnum |  Setting name:
  * CORRECT_TYPOS_AUTOMATICALLY: Automatically fix errors and typos.
  * DISPLAY_STORE_RATING: Add data from external sources to the ad (see 
  * SHARED_ACCOUNT_ENABLED: The shared account is enabled.

  
`Value` |  YesNoEnum |  Setting value.  
**TinInfoGet structure**  
`TinType` |  TinTypeEnum |  Organization type:
  * LEGAL: A legal entity.
  * PHYSICAL: An individual.
  * INDIVIDUAL: An individual entrepreneur.
  * FOREIGN_LEGAL: A foreign legal entity.
  * FOREIGN_PHYSICAL: A foreign individual.

  
`Tin` |  string |  The taxpayer number or its equivalent in the country of registration.  
**ErirAttributesGet structure**  
`Organization` |  OrganizationGet |  Details about the organization of the end-advertiser.  
`Contract` |  ContractGet |  Details of the contract of the client counterparty with the end-advertiser.  
`Contragent` |  ContragentGet |  Information about the counterparty of the end-advertiser.  
**OrganizationGet structure**  
`Name` |  string |  Organization name (up to 255 characters).  
`EpayNumber` |  string |  The number of the electronic payment instrument (up to 255 characters).  
`RegNumber` |  string |  Registration number or its equivalent (up to 255 characters).  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM (up to 3 characters, numbers only).  
`OkvedCode` |  string |  Business category code according to OKVED.  
**ContractGet structure**  
`Number` |  string |  Contract number (up to 255 characters).  
`Date` |  string |  Contract date in YYYY-MM-DD format (no earlier than January 1, 1991).  
`Type` |  ContractTypeEnum |  Type of contract:
  * CONTRACT: A service contract.
  * INTERMEDIARY_CONTRACT: An intermediary contract.
  * ADDITIONAL_AGREEMENT: An additional agreement.

  
`ActionType` |  ContractActionTypeEnum |  Types of activities of the intermediary representative:
  * COMMERCIAL: Commercial representation.
  * DISTRIBUTION: Ad distribution activities.
  * CONCLUDE: Conclusion of contracts.
  * OTHER: Other activities.

  
`SubjectType` |  ContractSubjectTypeEnum |  Contract subject:
  * REPRESENTATION: Representation activities.
  * MEDIATION: Mediation activities.
  * DISTRIBUTION: A contract for ad distribution.
  * ORG_DISTRIBUTION: A contract for organizing ad distribution.
  * OTHER: Other activities.

  
`Price` |  ContractPrice |  Contract price (no more than two decimal digits allowed).  
**ContractPrice structure**  
`Amount` |  decimal |  The value of the contract.  
`IncludingVat` |  YesNoEnum |  Whether VAT is included in the contract value.  
**ContragentGet structure**  
`Name` |  string |  Name (up to 255 characters).  
`Phone` |  string |  Phone number (50 characters maximum, numbers only, starting with the country code).  
`EpayNumber` |  string |  The number of the electronic payment instrument (up to 255 characters).  
`RegNumber` |  string |  Registration number or its equivalent (up to 255 characters).  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM (up to 3 characters, numbers only).  
`TinInfo` |  TinInfoGet |  Tax details of the counterparty.  
Copied
### Was the article helpful?
YesNo
Previous
[add](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add)
Next
[update](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update)
