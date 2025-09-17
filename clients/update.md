---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/clients/update
crawled_at: 2025-09-17T15:45:00.730396
---

Learn more
# update
  * [Learn more](https://yandex.com/dev/direct/doc/en/clients/en/clients/update#learn-more)
  * [Request](https://yandex.com/dev/direct/doc/en/clients/en/clients/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/clients/en/clients/update#output)


Changes the advertiser parameters and the user settings for the advertiser's representative.
Any representative of an advertiser can edit the advertiser's parameters and their own personal settings.
The advertiser's chief representative can also edit the settings of another representative. To do this, they need to pass the representative's username in the `Client-Login` request header.
##  [](https://yandex.com/dev/direct/doc/en/clients/en/clients/update#learn-more)Learn more
  * [How the "update" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/clients/en/clients/update#input)Request
Note
The `ClientInfo`, `Notification`, and `Phone` parameters belong to the user who is a representative of the advertiser:
  * The user on whose behalf the request is made, if the request is in the name of any representative of the advertiser and the `Client-Login` HTTP header isn't included in the request.
  * The user whose username is specified in the `Client-Login` HTTP header, if the request is in the name of the advertiser's chief representative and the request includes the `Client-Login` HTTP header.


The `Settings` parameter belongs to the advertiser regardless of who the representative is.
Request structure in JSON format:
```
{
  "method": "update",
  "params": { /* params */
    "Clients": [{ /* ClientUpdateItem */
      "ClientInfo": (string),
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
        "Option": ( "CORRECT_TYPOS_AUTOMATICALLY" | "DISPLAY_STORE_RATING" ), /* required */
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
`Clients` |  array of ClientUpdateItem |  Advertiser parameters and user settings to change. |  Yes  
**ClientUpdateItem structure**  
`ClientInfo` |  string |  First and last name of the Yandex Direct user (no more than 255 characters). |  No  
`Notification` |  NotificationUpdate |  The Yandex Direct user's settings for SMS and email notifications. |  No  
`Phone` |  string |  Phone number of the Yandex Direct user (255 characters maximum). |  No  
`Settings` |  array of ClientSettingUpdateItem |  Advertiser settings that only allow YES or NO values. |  No  
`TinInfo` |  TinInfoUpdate |  Tax data of the end-advertiser. |  No  
`ErirAttributes` |  ErirAttributesUpdate |  Additional advertiser data to label ads with. |  No  
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
`Name` |  string |  Organization name. |  No  
`EpayNumber` |  string |  The number of the electronic payment instrument. |  No  
`RegNumber` |  string |  Registration number or its equivalent. |  No  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM. |  No  
`OkvedCode` |  string |  Business category code according to OKVED. |  No  
**ContractUpdate structure**  
`Number` |  string |  Contract number. |  No  
`Date` |  string |  Contract date in the format YYYY-MM-DD. |  No  
`Type` |  ContractTypeEnum |  Type of contract:
  * CONTRACT: A service contract.
  * INTERMEDIARY_CONTRACT: An intermediary contract.
  * ADDITIONAL_AGREEMENT: An additional agreement. Alert The ADDITIONAL_AGREEMENT value is obsolete and no longer valid.

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
`Price` |  ContractPrice |  The value of the contract. |  No  
**ContractPrice structure**  
`Amount` |  decimal |  The value of the contract. |  Yes  
`IncludingVat` |  YesNoEnum |  Whether VAT is included in the contract value. |  Yes  
**ContragentUpdate structure**  
`Name` |  string |  Name. |  No  
`Phone` |  string |  Phone number. |  No  
`EpayNumber` |  string |  The number of the electronic payment instrument. |  No  
`RegNumber` |  string |  Registration number or its equivalent. |  No  
`OksmNumber` |  string |  Legal entity's code of the country of registration according to OKSM. |  No  
`TinInfo` |  TinInfoUpdate |  Tax details of the counterparty. |  No  
##  [](https://yandex.com/dev/direct/doc/en/clients/en/clients/update#output)Response
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
`UpdateResults` |  array of ClientsActionResult |  The result of changing advertiser parameters and user settings.  
**ClientsActionResult structure**  
`ClientId` |  long |  Advertiser ID. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/clients/en/clients/get)
Next
[Creatives: getting creatives](https://yandex.com/dev/direct/doc/en/clients/en/creatives/creatives)
