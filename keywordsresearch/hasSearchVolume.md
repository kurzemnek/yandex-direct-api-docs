---
title: hasSearchVolume | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywordsresearch/hasSearchVolume
crawled_at: 2025-09-17T15:55:16.819650
---

Restrictions
# hasSearchVolume
  * [Restrictions](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/hasSearchVolume#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/hasSearchVolume#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/hasSearchVolume#output)


Generates an approximate forecast of impressions for the specified keywords and regions, broken down by device type. Used when selecting keywords.
##  [](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/hasSearchVolume#restrictions)Restrictions
Each advertiser can send a maximum of 20 requests every 60 seconds to the Reports service.
##  [](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/hasSearchVolume#input)Request
Request structure in JSON format:
```
{
  "method": "hasSearchVolume",
  "params": { /* params */
    "SelectionCriteria": {  /* HasSearchVolumeSelectionCriteria */
      "Keywords": [(string), ... ], /* required */
      "RegionIds": [(long), ... ] /* required */
    }, /* required */
    "FieldNames": [( "Keyword" | "RegionIds" | "AllDevices" | "MobilePhones" | "Tablets" | "Desktops" ), ... ] /* required */
  } 
}

```

Parameters are described below.
**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / HasSearchVolumeRequest (for SOAP)** |  |  |   
`SelectionCriteria` |  HasSearchVolumeSelectionCriteria |  The keywords and regions to get a forecast for. |  Yes  
`FieldNames` |  array of HasSearchVolumeFieldEnum |  The names of parameters to get. |  Yes  
**HasSearchVolumeSelectionCriteria structure** |  |  |   
`Keywords` |  array of string |  Keywords. From 1 to 10,000 items in the array. Duplicate strings are not allowed. A keyword may contain operators. The maximum length of a keyword is 4096 characters. The “!” operator before a negative keyword is not counted in the keyword length (the sequence “-!” is considered one character). Maximum of 7 words per keyword, not counting stop words and negative keywords. Each word can have up to 35 characters, not counting the minus sign before a negative keyword. |  Yes  
`RegionIds` |  array of long |  IDs of regions where ad impressions are enabled or disabled. The ID "0" indicates to display ads in all regions. A minus sign before a region ID disables impressions in this region. For example, [1,-219] indicates to display for Moscow and the entire Moscow area, except Chernogolovka. Minus regions can't be used if 0 is set. The array must not consist of only minus regions.  
To get the list of regions, use the [Dictionaries](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/dictionaries/dictionaries).[get](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/dictionaries/get) method. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/hasSearchVolume#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "HasSearchVolumeResults": [{  /* HasSearchVolumeItem */
      "Keyword": (string),
      "RegionIds": [(long), ... ],
      "AllDevices": ( YES | NO ),
      "MobilePhones": ( YES | NO ),
      "Tablets": ( YES | NO ),
      "Desktops": ( YES | NO )
    }, ... ],
  }
}

```

Parameters are described below.
**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / HasSearchVolumeResponse (for SOAP)** |  |   
`HasSearchVolumeResults` |  array of HasSearchVolumeItem |  Forecast of impressions.  
**HasSearchVolumeItem structure** |  |   
`Keyword` |  string |  The keyword from the request.  
`RegionIds` |  array of long |  Region IDs from the request.  
`AllDevices` |  YesNoEnum |  Whether there are impressions.  
`MobilePhones` |  YesNoEnum |  Whether there are impressions on mobile phones.  
`Tablets` |  YesNoEnum |  Whether there are impressions on tablets.  
`Desktops` |  YesNoEnum |  Whether there are impressions on desktop browsers.  
Copied
### Was the article helpful?
YesNo
Previous
[deduplicate](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/deduplicate)
Next
[Leads: receiving form data from Turbo pages](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/leads/leads)
