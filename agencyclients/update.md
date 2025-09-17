---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/agencyclients/update
crawled_at: 2025-09-17T15:45:27.353454
---

Learn more
# update
  * [Learn more](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#output)


Changes the parameters of advertisers who are agency clients, and user settings for chief representatives of advertisers.
Note
For requests to the `AgencyClients` service:
  * In the `Authorization` header, specify the access token you obtained for the agency representative.
  * Don't specify the `Client-Login` header.


##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#learn-more)Learn more
  * [Client](https://yandex.com/dev/direct/doc/dg/objects/client.html)
  * [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html)
  * [How the "update" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#restrictions)Restrictions
Maximum of 1000 clients per method call.
##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#input)Request
Note
The `ClientInfo`, `Notification`, and `Phone` parameters belong to the advertiser's chief representative (see [Roles and access of Yandex Direct users](https://yandex.com/dev/direct/doc/dg/objects/roles.html)). The `ClientId`, `Grants`, and `Settings` parameters belong to the advertiser.
Request structure in JSON format:
```
{
  "method": "update",
  "params": { /* params */
    "Clients": [{ /* AgencyClientUpdateItem */
      "ClientId": (long), /* required */
      "ClientInfo": (string),
      "Grants": [{  /* GrantItem */
        "Privilege": ( "EDIT_CAMPAIGNS" | "IMPORT_XLS" | "TRANSFER_MONEY" ), /* required */
        "Value": ( "YES" | "NO" ) /* required */
      }, ... ],
      "Notification": { /* NotificationUpdate */
        "Lang": ( "RU" | "UK" | "EN" | "TR" ),
        "Email": (string),
        "EmailSubscriptions": [{  /* EmailSubscriptionItem */
          "Option": ( "RECEIVE_RECOMMENDATIONS" | "TRACK_MANAGED_CAMPAIGNS" | "TRACK_POSITION_CHANGES" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ]
      },
      "Phone": (string),
      "Settings": [{ /* ClientSettingUpdateItem */
        "Option": ( "DISPLAY_STORE_RATING" | "CORRECT_TYPOS_AUTOMATICALLY" ), /* required */
        "Value": ( "YES" | "NO" ) /* required */
      }, ... ],
      "TinInfo" : { /* TinInfoUpdate */
        "TinType" : ( "PHYSICAL" | "FOREIGN_PHYSICAL" | "LEGAL" | "FOREIGN_LEGAL" | "INDIVIDUAL" ),
        "Tin" : (string) /* nillable */
      }, /* nillable */
      "ErirAttributes": { /* ErirAttributesUpdate */
        "Organization": { /* OrganizationUpdate */
          "Name": (string), /* nillable */
          "EpayNumber": (string), /* nillable */
          "RegNumber": (string), /* nillable */
          "OksmNumber": (string), /* nillable */
          "OkvedCode": (string) /* nillable */
        }, /* nillable */
        "Contract": { /* ContractUpdate */
          "Number": (string), /* nillable */
          "Date": (string), /* nillable */
          "Type": ( "CONTRACT" | "INTERMEDIARY_CONTRACT" | "ADDITIONAL_AGREEMENT" ), /* nillable */
          "ActionType": ( "COMMERCIAL" | "DISTRIBUTION" | "CONCLUDE" | "OTHER" ), /* nillable */
          "SubjectType": ( "REPRESENTATION" | "MEDIATION" | "DISTRIBUTION" | "ORG_DISTRIBUTION" | "OTHER" ), /* nillable */
          "Price": { /* PriceUpdate */
            "Amount": (decimal), /* required */
            "IncludingVat": ( "YES" | "NO" ) /* required */
          } /* nillable */
        }, /* nillable */
        "Contragent": { /* ContragentUpdate */
          "Name": (string), /* nillable */
          "Phone": (string), /* nillable */
          "EpayNumber": (string), /* nillable */
          "RegNumber": (string), /* nillable */
          "OksmNumber": (string), /* nillable */
          "TinInfo": { /* TinInfoUpdate */
            "TinType": ( "PHYSICAL" | "FOREIGN_PHYSICAL" | "LEGAL" | "FOREIGN_LEGAL" | "INDIVIDUAL" ),
            "Tin": (string) /* nillable */
          } /* nillable */
        } /* nillable */
      } /* nillable */
    }] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / UpdateRequest structure (for SOAP)**  
`Clients` |  array of AgencyClientUpdateItem |  The parameters (for agency client advertisers) and user settings (for chief representatives of advertisers) that you need to change. |  Yes  
**AgencyClientUpdateItem structure**  
`ClientId` |  long |  Advertiser ID. |  Yes  
`ClientInfo` |  string |  Client name (maximum of 255 characters). |  No  
`Grants` |  array of GrantItem |  The advertiser's permissions for campaign management. |  No  
`Notification` |  NotificationUpdate |  The Yandex Direct user's settings for SMS and email notifications. |  No  
`Phone` |  string |  Phone number of the Yandex Direct user (50 characters maximum, only numbers allowed, starting with the country code). |  No  
`Settings` |  array of ClientSettingUpdateItem |  Advertiser settings that only allow YES or NO values. |  No  
`TinInfo` |  TinInfoUpdate |  Tax data of the end-advertiser. |  No  
`ErirAttributes` |  ErirAttributesUpdate |  Additional advertiser data to label ads with. |  No  
**GrantItem structure**  
`Privilege` |  PrivilegeEnum |  Name of the permission:
  * EDIT_CAMPAIGNS: Edit campaigns.
  * IMPORT_XLS: Use files to manage campaigns (see 
  * TRANSFER_MONEY: Transfer funds between campaigns (see 

For the IMPORT_XLS permission, you can only set the YES value if the EDIT_CAMPAIGNS permission is also set to YES. Otherwise, an error is returned. For the EDIT_CAMPAIGNS permission, you can only set the NO value if the IMPORT_XLS permission is set to NO. Otherwise, an error is returned. |  Yes  
`Value` |  YesNoEnum |  Whether the client has this permission. |  Yes  
**NotificationUpdate structure**  
`Lang` |  LangEnum |  Language for notifications. |  No  
`Email` |  string |  The email address for sending notifications related to the account (no more than 255 characters). |  No  
`EmailSubscriptions` |  array of EmailSubscriptionItem |  Types of notifications to send by email. |  No  
**EmailSubscriptionItem structure**  
`Option` |  EmailSubscriptionEnum |  Type of notification:
  * RECEIVE_RECOMMENDATIONS — Yandex Direct news and recommendations.
  * TRACK_MANAGED_CAMPAIGNS: Notifications for campaigns that have a personal manager.
  * TRACK_POSITION_CHANGES: Warnings about traffic forecasts falling lower than the bid provided at the time of configuration.

|  Yes  
`Value` |  YesNoEnum |  Whether to send this type of notification. |  Yes  
**ClientSettingUpdateItem structure**  
`Option` |  ClientSettingUpdateEnum |  Setting name:
  * CORRECT_TYPOS_AUTOMATICALLY: Automatically fix errors and typos.
  * DISPLAY_STORE_RATING: Add data from external sources to the ad (see 

|  Yes  
`Value` |  YesNoEnum |  Setting value. |  Yes  
**TinInfoUpdate structure**  
`TinType` |  TinTypeEnum |  Organization type:
  * LEGAL: A legal entity.
  * PHYSICAL: An individual.
  * INDIVIDUAL: An individual entrepreneur.
  * FOREIGN_LEGAL: A foreign legal entity.
  * FOREIGN_PHYSICAL: A foreign individual.

|  No  
`Tin` |  string |  The taxpayer number or its equivalent in the country of registration. |  No  
**ErirAttributesUpdate structure**  
`Organization` |  OrganizationUpdate |  Details about the organization of the end-advertiser. |  No  
`Contract` |  ContractUpdate |  Details of the contract of the client counterparty with the end-advertiser. |  No  
`Contragent` |  ContragentUpdate |  Information about the counterparty of the end-advertiser. |  No  
**OrganizationUpdate structure**  
`Name` |  string |  Organization name (up to 255 characters). |  No  
`EpayNumber` |  string |  The number of the electronic payment instrument (up to 255 characters). |  No  
`RegNumber` |  string |  Registration number or its equivalent (up to 255 characters). |  No  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM (up to 3 characters, numbers only). |  No  
`OkvedCode` |  string |  Business category code according to OKVED. |  No  
**ContractUpdate structure**  
`Number` |  string |  Contract number (up to 255 characters). |  No  
`Date` |  string |  Contract date in YYYY-MM-DD format (no earlier than January 1, 1991). |  No  
`Type` |  ContractTypeEnum |  Type of contract:
  * CONTRACT: A service contract.
  * INTERMEDIARY_CONTRACT: An intermediary contract.
  * ADDITIONAL_AGREEMENT: An additional agreement.

|  No  
`ActionType` |  ContractActionTypeEnum |  Types of activities of the intermediary representative:
  * COMMERCIAL: Commercial representation.
  * DISTRIBUTION: Ad distribution activities.
  * CONCLUDE: Conclusion of contracts.
  * OTHER: Other activities.

|  No  
`SubjectType` |  ContractSubjectTypeEnum |  Contract subject:
  * REPRESENTATION: Representation activities.
  * MEDIATION: Mediation activities.
  * DISTRIBUTION: A contract for ad distribution.
  * ORG_DISTRIBUTION: A contract for organizing ad distribution.
  * OTHER: Other activities.

|  No  
`Price` |  ContractPrice |  Contract price (no more than two decimal digits allowed). |  No  
**ContractPrice structure**  
`Amount` |  decimal |  The value of the contract. |  Yes  
`IncludingVat` |  YesNoEnum |  Whether VAT is included in the contract value. |  Yes  
**ContragentUpdate structure**  
`Name` |  string |  Name (up to 255 characters). |  No  
`Phone` |  string |  Phone number (50 characters maximum, numbers only, starting with the country code). |  No  
`EpayNumber` |  string |  The number of the electronic payment instrument (up to 255 characters). |  No  
`RegNumber` |  string |  Registration number or its equivalent (up to 255 characters). |  No  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM (up to 3 characters, numbers only). |  No  
`TinInfo` |  TinInfoUpdate |  Tax details of the counterparty. |  No  
##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/update#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "UpdateResults": [{  /* ClientsActionResult */
      "ClientId": (long),
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
`UpdateResults` |  array of ClientsActionResult |  The result of changing parameters for agency client advertisers and user settings for chief representatives of advertisers.  
**ClientsActionResult structure**  
`ClientId` |  long |  Advertiser ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get)
Next
[AudienceTargets: managing audience targets](https://yandex.com/dev/direct/doc/en/agencyclients/en/audiencetargets/audiencetargets)
