---
title: get | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/vcards/get
crawled_at: 2025-09-17T15:48:36.380676
---

Learn more
# get
  * [Learn more](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#learn-more)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#input)
  * [Response](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#output)
  * [Examples](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#samples)


Returns the vCards that match the specified criteria.
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#learn-more)Learn more
  * [How the "get" method works](https://yandex.com/dev/direct/doc/dg/best-practice/get.html)


##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#restrictions)Restrictions
The method returns a maximum of `page-size` objects.
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#input)Request
Request structure in JSON format:
```
{
  "method": "get",
  "params": { /* params */
    "SelectionCriteria": {   /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    },
    "FieldNames": [( "Id" | "Country" | "City" | "Street" | "House" | "Building" | "Apartment" | "CompanyName" | "ExtraMessage" | "ContactPerson" | "ContactEmail" | "MetroStationId" | "CampaignId" | "Ogrn" | "WorkTime" | "InstantMessenger" | "Phone" | "PointOnMap" ), ... ], /* required */
    "Page": {   /* LimitOffset */
      "Limit": (long),
      "Offset": (long)
    }
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / GetRequest (for SOAP)** |  |  |   
`SelectionCriteria` |  IdsCriteria |  vCard selection criteria. If omitted, all the advertiser's vCards are returned. |  No  
`FieldNames` |  array of VCardFieldEnum |  The names of parameters to get. |  Yes  
`Page` |  [LimitOffset](https://yandex.com/dev/direct/doc/dg/best-practice/get.html#LimitOffset) |  Structure that defines the page for [paginated selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html) of data. |  No  
**IdsCriteria structure** |  |  |   
`Ids` |  array of long |  IDs of vCards to get. A maximum of `ids-select` items in the array. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#output)Response
Response structure in JSON format:
```
{
  "result": {
    "VCards": [{  /* VCardGetItem */
      "Id": (long),
      "CampaignId": (long),
      "Country": (string),
      "City": (string),
      "WorkTime": (string),
      "Phone": {  /* Phone */
        "CountryCode": (string), /* required */
        "CityCode": (string), /* required */
        "PhoneNumber": (string), /* required */
        "Extension": (string)
      },
      "Street": (string), /* nillable */
      "House": (string), /* nillable */
      "Building": (string), /* nillable */
      "Apartment": (string), /* nillable */
      "InstantMessenger": {  /* InstantMessenger */
        "MessengerClient": (string), /* required */
        "MessengerLogin": (string) /* required */
      }, /* nillable */
      "CompanyName": (string), /* nillable */
      "ExtraMessage": (string), /* nillable */
      "ContactEmail": (string), /* nillable */
      "Ogrn": (string), /* nillable */
      "MetroStationId": (long), /* nillable */
      "PointOnMap": {  /*  MapPoint */
        "X": (decimal), /* required */
        "Y": (decimal), /* required */
        "X1": (decimal), /* required */
        "Y1": (decimal), /* required */
        "X2": (decimal), /* required */
        "Y2": (decimal) /* required */
      }, /* nillable */
      "ContactPerson": (string) /* nillable */
    }, ... ],
    "LimitedBy": (long)
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / GetResponse (for SOAP)** |  |   
`VCards` |  array of VCardGetItem |  vCards.  
`LimitedBy` |  long |  Sequential number of the last object returned. It is included if there was a limit on the number of objects in the response. See the section [Paginated data selection](https://yandex.com/dev/direct/doc/dg/best-practice/get.html).  
**VCardGetItem structure** |  |   
`Id` |  long |  vCard ID.  
`CampaignId` |  long |  The campaign ID.  
`Country` |  string |  Country. Maximum of 50 characters.  
`City` |  string |  The city. Maximum of 55 characters.  
`WorkTime` |  string |  The operating hours or client service hours of the business. Set as a string that specifies the range of days of the week, work hours, and minutes. Days of the week are defined by the numbers from 0 to 6, where 0 is Monday and 6 is Sunday. Minutes are set as a multiple of 15: 0, 15, 30 or 45. String format: `"day_from;day_to;hour_from;minute_from;hour_to;minute_to"`. For example, the string `"0;4;10;0;18;0"` sets the following schedule: `0;4` — Monday to Friday `10;0` — from 10:00 `18;0` — to 18:00 The schedule may consist of several strings in this format. For example: "`0;4;10;0;18;0;5;6;11;0;16;0`". Here, in addition to the previous example, the schedule also includes: `5;6` — Saturday and Sunday `11;0` — from 11:00 `16;0` — to 16:00 A 24-hour schedule is set using the string `"0;6;00;00;00;00"`. Maximum of 255 characters.  
`Phone` |  Phone |  Structure that sets the phone number.  
`Street` |  string, nillable |  Street. Maximum of 55 characters.  
`House` |  string, nillable |  House number. Maximum of 30 characters.  
`Building` |  string, nillable |  The building or unit number. Maximum of 10 characters.  
`Apartment` |  string, nillable |  The apartment or office number. Maximum of 100 characters.  
`InstantMessenger` |  InstantMessenger, nillable |  A structure that sets the contact for instant messaging.  
`CompanyName` |  string, nillable |  Name of the organization. Maximum of 255 characters.  
`ExtraMessage` |  string, nillable |  Additional information on the advertised product or service. Maximum of 200 characters.  
`ContactEmail` |  string, nillable |  Email address. Maximum of 255 characters.  
`Ogrn` |  string, nillable |  The OGRN code for a business registered in Russia. Maximum of 255 characters.  
`MetroStationId` |  long, nillable |  ID of the metro station. To get the list of stations, use the [Dictionaries](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/dictionaries.html).[get](https://yandex.com/dev/direct/doc/ref-v5/dictionaries/get.html) method.  
`PointOnMap` |  MapPoint, nillable |  Structure that describes the location of the placemark on the map. If not set, the map is marked at the address that was specified for the client.  
`ContactPerson` |  string, nillable |  Contact person. Maximum of 155 characters.  
**Phone structure** |  |   
`CountryCode` |  string |  The country code for the phone number. Must contain from 1 to 5 characters. Acceptable values:
  * Beginning with the "+" symbol and consisting of digits.
  * The value "8" with the city code "800".

For example, "+7" for Russia.  
`CityCode` |  string |  The area code or city code for the phone number. From 1 to 5 digits. Must not be 0.  
`PhoneNumber` |  string |  The contact phone number. From 5 to 9 digits. When combined with the country code and city code, it is from 8 to 17 digits.  
`Extension` |  string |  The phone extension, if an office PBX system is used. From 1 to 6 digits.  
**InstantMessenger structure** |  |   
`MessengerClient` |  string |  The type of instant messaging system — icq, jabber, skype or mail_agent.  
`MessengerLogin` |  string |  The username (ID) in the instant messaging system. Maximum of 255 characters.  
**MapPoint structure** |  |   
`X` |  decimal |  Longitude of the point. From -180 to 180.  
`Y` |  decimal |  Latitude of the point. From -90 to 90.  
`X1` |  decimal |  Longitude of the lower-left corner of the region on the map. From -180 to 180.  
`Y1` |  decimal |  Latitude of the lower-left corner of the region on the map. From -90 to 90.  
`X2` |  decimal |  Longitude of the upper-right corner of the region on the map. From -180 to 180.  
`Y2` |  decimal |  Latitude of the upper-right corner of the region on the map. From -90 to 90.  
##  [](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/get#samples)Examples
**Request example**
```
    {
      "method": "get",
      "params": {
        "SelectionCriteria" : {
          "Ids" : [ 13070327]
        },
        "FieldNames" : [
          "Country",
          "City",
          "Phone"
        ]
      }
    }

```

**Response example**
```
    {
      "result" : {
        "VCards" : [
          {
            "Phone" : {
              "CityCode" : "812",
              "Extension" : "89",
              "PhoneNumber" : "123-45-67",
              "CountryCode" : "+7"
            },
            "Country" : "Russia",
            "City" : "Moscow"
          }
        ]
      }
    }

```

Copied
### Was the article helpful?
YesNo
Previous
[delete](https://yandex.com/dev/direct/doc/en/vcards/en/vcards/delete)
Next
[Errors and warnings](https://yandex.com/dev/direct/doc/en/vcards/en/concepts/errors-list)
