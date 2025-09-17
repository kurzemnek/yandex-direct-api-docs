---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/agencyclients/add
crawled_at: 2025-09-17T15:45:18.879804
---

Learn more
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#output)


Alert
This method isn't supported. Use the 
Registers new advertisers who are agency clients and users who are chief representatives of advertisers.
Note
For requests to the `AgencyClients` service:
  * In the `Authorization` header, specify the access token you obtained for the agency representative.
  * Don't specify the `Client-Login` header.


##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#learn-more)Learn more
##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#restrictions)Restrictions
Maximum of 100 clients per day.
Access to this method is granted 
##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
      "Login": (string), /* required */
      "FirstName": (string), /* required */
      "LastName": (string), /* required */
      "Currency": ( "RUB" | "BYN" | "CHF" | "EUR" | "KZT" | "TRY" | "UAH" | "USD" ), /* required */
      "Grants": [{  /* GrantItem */
        "Privilege": ( "EDIT_CAMPAIGNS" | "IMPORT_XLS" | "TRANSFER_MONEY" ), /* required */
        "Value": ( "YES" | "NO" ) /* required */
      }, ... ],
      "Notification": {  /* NotificationAdd */
        "Lang": ( "RU" | "UK" | "EN" | "TR" ), /* required */
        "Email": (string), /* required */
        "EmailSubscriptions": [{  /* EmailSubscriptionItem */
          "Option": ( "RECEIVE_RECOMMENDATIONS" | "TRACK_MANAGED_CAMPAIGNS" | "TRACK_POSITION_CHANGES" ), /* required */
          "Value": ( "YES" | "NO" ) /* required */
        }, ... ] /* required */
      }, /* required */
      "Settings": [{  /* ClientSettingAddItem */
        "Option": ( "CORRECT_TYPOS_AUTOMATICALLY" | "DISPLAY_STORE_RATING" ), /* required */
        "Value": ( "YES" | "NO" ) /* required */
      }, ... ],
      "TinInfo": { /* TinInfoAdd */
        "TinType": ( "PHYSICAL" | "FOREIGN_PHYSICAL" | "LEGAL" | "FOREIGN_LEGAL" | "INDIVIDUAL" ), /* required */
        "Tin": (string)
      }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)**  
`Login` |  string |  Username of a Yandex Direct user who is the chief representative of an advertiser. This name is used to create a user in Yandex and Yandex Direct, so the username must be unique. The username may include Latin characters, digits, a single hyphen, and a dot. It must start with a letter, end with a letter or number, and contain a maximum of 30 characters. We do not recommend usernames that have dots in them (they should be replaced with hyphens) or uppercase characters. |  Yes  
`FirstName` |  string |  The user's first name (no more than 20 characters). The following characters are not allowed: &=<>. |  Yes  
`LastName` |  string |  The user's last name (no more than 20 characters). The following characters are not allowed: &=<>. |  Yes  
`Currency` |  CurrencyEnum |  The advertiser's currency. |  Yes  
`Grants` |  array of GrantItem |  The advertiser's permissions for campaign management. If omitted, there aren't any permissions. |  No  
`Notification` |  NotificationAdd |  Settings for SMS and email notifications for the advertiser's chief representative. |  Yes  
`Settings` |  array of ClientSettingAddItem |  Advertiser settings that only allow YES or NO values. |  No  
`TinInfo` |  TinInfoAdd |  Tax data of the end-advertiser. |  Yes  
**GrantItem structure**  
`Privilege` |  PrivilegeEnum |  Name of the permission:
  * EDIT_CAMPAIGNS: Edit campaigns.
  * IMPORT_XLS: Use files to manage campaigns (see 
  * TRANSFER_MONEY: Transfer funds between campaigns (see 

If the permission isn't specified, it is created with the value NO. For the IMPORT_XLS permission, you can only set the YES value if the EDIT_CAMPAIGNS permission is also set to YES. Otherwise, an error is returned. |  Yes  
`Value` |  YesNoEnum |  Whether the advertiser has this permission. |  Yes  
**NotificationAdd structure**  
`Lang` |  LangEnum |  Language for notifications. |  Yes  
`Email` |  string |  The email address for sending notifications related to the account. |  Yes  
`EmailSubscriptions` |  array of EmailSubscriptionItem |  Types of notifications to send by email. |  Yes  
**EmailSubscriptionItem structure**  
`Option` |  EmailSubscriptionEnum |  Type of notification:
  * RECEIVE_RECOMMENDATIONS — Yandex Direct news and recommendations.
  * TRACK_MANAGED_CAMPAIGNS: Notifications for campaigns that have a personal manager.
  * TRACK_POSITION_CHANGES: Warnings about traffic forecasts falling lower than the bid provided at the time of configuration.

If the type of notification isn't specified, it is created with the value NO. |  Yes  
`Value` |  YesNoEnum |  Whether to send this type of notification. |  Yes  
**ClientSettingAddItem structure**  
`Option` |  ClientSettingAddEnum |  Setting name:
  * CORRECT_TYPOS_AUTOMATICALLY: Automatically fix errors and typos.
  * DISPLAY_STORE_RATING: Add data from external sources to the ad (see 

If the setting isn't specified, it is created with the value NO. |  Yes  
`Value` |  YesNoEnum |  Setting value. |  Yes  
**TinInfoAdd structure**  
`TinType` |  TinTypeEnum |  Organization type:
  * LEGAL: A legal entity.
  * PHYSICAL: An individual.
  * INDIVIDUAL: An individual entrepreneur.
  * FOREIGN_LEGAL: A foreign legal entity.
  * FOREIGN_PHYSICAL: A foreign individual.

|  Yes  
`Tin` |  string |  The taxpayer number or its equivalent in the country of registration. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/add#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Login": (string),
    "Password":  (string),
    "Email":  (string),
    "ClientId": (long),
    "Warnings": [{  /* ExceptionNotification */
      "Code": (int), /* required */
      "Message": (string), /* required */
      "Details": (string)
    }, ... ],
    "Errors": [{  /* ExceptionNotification */
      "Code": (int), /* required */
      "Message": (string), /* required */
      "Details": (string)
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / AddResponse structure (for SOAP)**  
`Login` |  string |  Username of a Yandex Direct user who is the chief representative of an advertiser. Returned if there aren't any errors. See the section   
`Password` |  string |  Automatically generated password for the user. Returned if there are no errors.  
`Email` |  string |  Email address automatically generated from the username. Returned if there are no errors.  
`ClientId` |  long |  ID of the created advertiser. Returned if there are no errors.  
`Warnings` |  array of ExceptionNotification |  Warnings that occurred during the operation.  
`Errors` |  array of ExceptionNotification |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[AgencyClients: managing agency clients](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/agencyclients)
Next
[get](https://yandex.com/dev/direct/doc/en/agencyclients/en/agencyclients/get)
