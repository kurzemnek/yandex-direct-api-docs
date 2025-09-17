---
title: Dynamic feed ad target (DynamicFeedAdTarget) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/dynamicfeedadtarget
crawled_at: 2025-09-17T15:48:23.313105
---

Servicing
# Dynamic feed ad target (DynamicFeedAdTarget)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#restrictions)
  * [Type of product offer selection](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#types)
  * [Selection rule](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#conditions)
  * [Examples](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#examples)
  * [State of dynamic text ad targets](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#status)


A dynamic ad target defines the set of the advertiser's website pages that ads are dynamically generated for. For more information about dynamic ads, see [Dynamic ads](https://yandex.com/support/direct/dynamic-text-ads/about-da.html) in Yandex.Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#service)Servicing
Use the [DynamicFeedAdTargets](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/dynamicfeedadtargets.html) service to manage targets for dynamic ads.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#methods)Methods
[add](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/add.html) | [delete](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/delete.html) | [suspend](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/suspend.html) | [resume](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/resume.html) | [get](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/get.html) | [setBids](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/setBids.html)
Dynamic text ad targets can't be edited. If you need to change a targeting condition, you must delete it and create a new one.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#restrictions)Restrictions
A dynamic text ad target can only be added to the DYNAMIC_TEXT_AD_GROUP type of ad group.
Maximum of 50 dynamic ad targets per group.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#types)Type of product offer selection
There are two types of selection:
  * ITEMS_ALL — “Select all”.
Dynamic ads will be generated for all product offers from your feed.
  * ITEMS_SUBSET — “A group of pages”.
The filter contains up to 10 selection rules. Dynamic ads are generated only for those product offers that meet all the selection rules at the same time.


Note
For the Yandex Realty feed and Flights feed in Google Ads, only the ITEMS_ALL type is available.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#conditions)Selection rule
The selection rule consists of three parameters:
  * `Operand` — The feed field.
  * `Operator` — The comparison operator.
  * `Arguments` — An array of values to compare the field value in the feed with.


For a description of the fields for each type of feed, see 
The compatibility of feed fields and operators depends on the feed:
Retail sales, other business: Yandex Market feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
categoryId |  GREATER_THAN, LESS_THAN |  One number  
EQUALS_ANY |  Maximum 20,000 numbers  
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#range-sample).  
id |  GREATER_THAN, LESS_THAN |  One number  
EQUALS_ANY |  Max 50 numbers  
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#range-sample).  
market_category typePrefix vendor |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
description model name |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
url |  EQUALS,CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
oldprice price |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#range-sample).  
EXISTS |  Pass the value 1  
adult manufacturer_warranty pickup store |  EQUALS_ANY |  Acceptable values:
  * 0
  * 1

  
EXISTS |  Pass the value 1  
age |  EQUALS_ANY |  Acceptable values: integer from 0 to 12, 16, or 18.  
EXISTS |  Pass the value 1  
Hotels: Google Ads "Hotels and rentals" feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
Rsis |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#range-sample).  
Description max_score name location url |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
class |  EQUALS_ANY |  Acceptable values:
  * 1
  * 2
  * 3
  * 4
  * 5

  
EXISTS |  Pass the value 1  
OfferID Score |  GREATER_THAN, LESS_THAN |  Single integer  
EQUALS_ANY |  Max 50 integers  
RANGE |  Max 10 ranges or integers. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#range-sample).  
Automobiles: Auto.ru feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
body_type color folder_id mark_id |  CONTAINS_ANY, NOT_CONTAINS_ALL, |  Max 50 lines, max 175 characters per line  
wheel |  CONTAINS_ANY |  Recommended values:
  * left
  * right

  
metallic |  EQUALS_ANY |  Recommended values:
  * yes
  * no

  
availability |  EQUALS_ANY |  Recommended values:
  * in stock
  * on order

  
year |  EQUALS_ANY |  Max 10 numbers  
url |  CONTAINS_ANY, NOT_CONTAINS_ALL, EQUALS_ANY |  Max 50 lines, max 175 characters per line  
price |  GREATER_THAN, LESS_THAN |  Single integer  
EQUALS_ANY |  Max 50 integers  
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#range-sample).  
Realty: Yandex Realty feed
This feed doesn't use selection rules.
Flights: Google Ads "Flights" feed
This feed doesn't use selection rules.
Other business: universal feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
url |  EQUALS_ANY, CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
description name |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
price oldprice |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#range-sample).  
Other business: Google Ads "Custom" feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
category description name second_title |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
url |  EQUALS_ANY, CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
price sale_price |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
IN_RANGE |  Up to 10 ranges, up to 2 decimal places  
EQUALS_ANY |  Up to 50 values, up to 2 decimal places  
Other business: Google Ads "Travel" feed
**Feed field** |  **The operators** |  **Restrictions on values**  
---|---|---  
Category destination origin Title |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
url |  EQUALS_ANY, CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
price sale_price |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
IN_RANGE |  Up to 10 ranges, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#examples)Examples
**The value contains one of the specified rows** :
```
    {
      "Operand": "mark_id",
      "Operator": "CONTAINS_ANY",
      "Arguments": ["Audi","Opel"]
    }

```

**Range: price from 111 to 222 or 3000 to 10000** :
```
    {
      "Operand": "price",
      "Operator": "IN_RANGE",
      "Arguments": ["111-222", "3000-10000"]
    }

```

**Value from the list** :
```
    {
      "Operand": "wheel",
      "Operator": "EQUALS_ANY",
      "Arguments": ["левый"]
    }

```

##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget#status)State of dynamic text ad targets
The `State` parameter reflects the current state of displays for a dynamic ad target.
**State** |  **Description**  
---|---  
ON |  Ad impressions are possible by target.  
OFF |  The dynamic ad target isn't in use.  
SUSPENDED |  Impressions by target for dynamic ads were stopped by the owner (using the [suspend](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/suspend.html) method, or in the web interface).  
DELETED |  The ad target for dynamic ads was deleted by the owner. Note The [get](https://yandex.com/dev/direct/doc/ref-v5/dynamicfeedadtargets/get.html) method returns a dynamic text ad target in the DELETED state only if the `States` parameter is set to DELETED or the ID of this target is specified in the `Ids` parameter. If both the `Ids` and `States` parameters are omitted, the method doesn't return dynamic text ad targets in the DELETED state.  
UNKNOWN |  Unknown state. Used for providing backward compatibility and displaying states that are not supported in this version of the API.  
Copied
### Was the article helpful?
YesNo
Previous
[Filter — targeting criteria for smart banners (SmartAdTarget)](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget)
Next
[Ad target for dynamic ads (DynamicTextAdTarget — Webpage)](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget)
