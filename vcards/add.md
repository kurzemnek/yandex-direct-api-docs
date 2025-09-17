---
title: add | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/vcards/add
crawled_at: 2025-09-17T15:53:21.530046
---

Learn more
# add
  * [Learn more](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#input)
  * [Response](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#samples)


Creates virtual business cards.
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#learn-more)Learn more
  * [How the "add" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#restrictions)Restrictions
Maximum of 1000 vCards per method call.
A vCard can't be added if the campaign is archived.
If the vCards have identical information, only one vCard is created.
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#input)Request
Request structure in JSON format:
```
{
  "method": "add",
  "params": { /* params */
    "VCards": [{  /* VCardAddItem */
      "CampaignId": (long), /* required */
      "Country": (string), /* required */
      "City": (string), /* required */
      "CompanyName": (string), /* required */
      "WorkTime": (string), /* required */
      "Phone": {  /* Phone */
        "CountryCode": (string), /* required */
        "CityCode": (string), /* required */
        "PhoneNumber": (string), /* required */
        "Extension": (string)
      }, /* required */
      "Street": (string),
      "House": (string),
      "Building": (string),
      "Apartment": (string),
      "InstantMessenger": {  /* InstantMessenger */
        "MessengerClient": (string), /* required */
        "MessengerLogin": (string) /* required */
      },
      "ExtraMessage": (string),
      "ContactEmail": (string),
      "Ogrn": (string),
      "MetroStationId": (long),
      "PointOnMap": {  /* MapPoint */
        "X": (decimal), /* required */
        "Y": (decimal), /* required */
        "X1": (decimal), /* required */
        "Y1": (decimal), /* required */
        "X2": (decimal), /* required */
        "Y2": (decimal) /* required */
      },
      "ContactPerson": (string)
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / AddRequest structure (for SOAP)** |  |  |   
`VCards` |  array of VCardAddItem |  The vCards to add. |  Yes  
**VCardAddItem structure** |  |  |   
`CampaignId` |  long |  The campaign ID. |  Yes  
`Country` |  string |  Country. Maximum of 50 characters. |  Yes  
`City` |  string |  The city. Maximum of 55 characters. |  Yes  
`CompanyName` |  string |  Name of the organization. Maximum of 255 characters. |  Yes  
`WorkTime` |  string |  The operating hours or client service hours of the business. Set as a string that specifies the range of days of the week, work hours, and minutes. Days of the week are defined by the numbers from 0 to 6, where 0 is Monday and 6 is Sunday. Minutes are set as a multiple of 15: 0, 15, 30 or 45. String format: `"day_from;day_to;hour_from;minute_from;hour_to;minute_to"`. For example, the string `"0;4;10;0;18;0"` sets the following schedule: `0;4` — Monday to Friday `10;0` — from 10:00 `18;0` — to 18:00 The schedule may consist of several strings in this format. For example: "`0;4;10;0;18;0;5;6;11;0;16;0`". Here, in addition to the previous example, the schedule also includes: `5;6` — Saturday and Sunday `11;0` — from 11:00 `16;0` — to 16:00 A 24-hour schedule is set using the string `"0;6;00;00;00;00"`. Maximum of 255 characters. |  Yes  
`Phone` |  Phone |  Structure that sets the phone number. |  Yes  
`Street` |  string |  Street. Maximum of 55 characters. |  No  
`House` |  string |  House number. Maximum of 30 characters. |  No  
`Building` |  string |  The building or unit number. Maximum of 10 characters. |  No  
`Apartment` |  string |  The apartment or office number. Maximum of 100 characters. |  No  
`InstantMessenger` |  InstantMessenger |  A structure that sets the contact for instant messaging. |  No  
`ExtraMessage` |  string |  Additional information on the advertised product or service. Maximum of 200 characters. |  No  
`ContactEmail` |  string |  Email address. Maximum of 255 characters. |  No  
`Ogrn` |  string |  The OGRN code for a business registered in Russia. Maximum of 255 characters. |  No  
`MetroStationId` |  long |  ID of the metro station. To get the list of stations, use the [Dictionaries](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/dictionaries.html).[get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method. |  No  
`PointOnMap` |  MapPoint |  Structure that describes the location of the placemark on the map. If not set, the map is marked at the address that was specified for the client. |  No  
`ContactPerson` |  string |  Contact person. Maximum of 155 characters. |  No  
**Phone structure** |  |  |   
`CountryCode` |  string |  The country code for the phone number. Must contain from 1 to 5 characters. Acceptable values:
  * Beginning with the "+" symbol and consisting of digits.
  * The value "8" with the city code "800".

For example, "+7" for Russia. |  Yes  
`CityCode` |  string |  The area code or city code for the phone number. From 1 to 5 digits. Must not be 0. |  Yes  
`PhoneNumber` |  string |  The contact phone number. From 5 to 9 digits. When combined with the country code and city code, it is from 8 to 17 digits. |  Yes  
`Extension` |  string |  The phone extension, if an office PBX system is used. From 1 to 6 digits. |  No  
**InstantMessenger structure** |  |  |   
`MessengerClient` |  string |  The type of instant messaging system — icq, jabber, skype or mail_agent. |  Yes  
`MessengerLogin` |  string |  The username (ID) in the instant messaging system. Maximum of 255 characters. |  Yes  
**MapPoint structure** |  |  |   
`X` |  decimal |  Longitude of the point. From -180 to 180. |  Yes  
`Y` |  decimal |  Latitude of the point. From -90 to 90. |  Yes  
`X1` |  decimal |  Longitude of the lower-left corner of the region on the map. From -180 to 180. |  Yes  
`Y1` |  decimal |  Latitude of the lower-left corner of the region on the map. From -90 to 90. |  Yes  
`X2` |  decimal |  Longitude of the upper-right corner of the region on the map. From -180 to 180. |  Yes  
`Y2` |  decimal |  Latitude of the upper-right corner of the region on the map. From -90 to 90. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "AddResults": [{  /* ActionResult */
      "Id": (long),
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
    }, ... ]
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / AddResponse structure (for SOAP)** |  |   
`AddResults` |  array of ActionResult |  Results of adding vCards.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the created vCard. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/add#samples)Examples
**Request example**
```
    {
      "method" : "add",
      "params" : {
        "VCards" : [
          {
            "Phone" : {
              "CityCode" : "812",
              "Extension" : "89",
              "PhoneNumber" : "123-45-67",
              "CountryCode" : "+7"
            },
            "WorkTime" : "0;3;10;0;18;0;4;6;10;0;11;0",
            "Country" : "Russia",
            "CompanyName" : "Some Company DvKqXuiphd",
            "CampaignId" : 4193065,
            "PointOnMap" : {
              "X" : 39.724068,
              "Y" : 47.222555,
              "X1" : 39.722020,
              "Y1" : 47.221160,
              "X2" : 39.726116,
              "Y2" : 47.223951,

            },
            "City" : "Moscow"
          }
        ]
      }
    }

```

**Response example**
```
    {
      "result" : {
        "AddResults" : [
          {
            "Id" : 13070322
          }
        ]
      }
    }

```

**Sample response with a warning**
If the vCard being added is a duplicate of a previously created one, the new vCard is not created and a warning is issued.
```
{
  "result" : {
    "AddResults" : [
      {
        "Id" : 13070292,
        "Warnings" : [
          {
            "Code" : 10100,
            "Message" : "The card indicated duplicates a card created earlier"
          }
        ]
      }
    ]
  }
}

```

Copied
### Was the article helpful?
YesNo
Previous
[VCards: operations with vCards](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/vcards)
Next
[delete](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/delete)
