---
title: Filter — targeting criteria for smart banners (SmartAdTarget) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/smartadtarget
crawled_at: 2025-09-17T15:50:53.556569
---

Servicing
# Filter — targeting criteria for smart banners (SmartAdTarget)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#restrictions)
  * [Type of product offer selection](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#types)
  * [Selection rule](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#conditions)
  * [Examples](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#examples)
  * [Filter status](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#status)


The filter defines a set of product offers from the feed that are used for dynamically generating smart banners. For more information about filters, see [Configuring filters](https://yandex.com/support/direct/smart-banners/configuring-filters.html) in the Help for Yandex.Direct.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#service)Servicing
Use the [SmartAdTargets](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/smartadtargets.html) service for managing filters.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#methods)Methods
[add](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/add.html) | [update](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/update.html) | [setBids](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/setBids.html) | [delete](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/delete.html) | [suspend](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/suspend.html) | [resume](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/resume.html) | [get](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/get.html)
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#restrictions)Restrictions
The filter can only be added to a SMART_AD_GROUP type of ad group.
Maximum of 50 filters per group.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#types)Type of product offer selection
There are two types of selection:
  * ITEMS_ALL — “Select all”.
Smart banners are generated for all product offers from the feed.
  * ITEMS_SUBSET — “A group of pages”.
The filter contains up to 10 selection rules. Smart banners are generated only for those product offers that meet all the selection rules at the same time.


Note
For the Yandex Realty feed and Flights feed in Google Ads, only the ITEMS_ALL type is available.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#conditions)Selection rule
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
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#range-sample).  
id |  GREATER_THAN, LESS_THAN |  One number  
EQUALS_ANY |  Max 50 numbers  
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#range-sample).  
market_category typePrefix vendor |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
EXISTS |  Pass the value 1  
description model name |  CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
url |  EQUALS,CONTAINS_ANY, NOT_CONTAINS_ALL |  Max 50 lines, max 175 characters per line  
oldprice price |  GREATER_THAN, LESS_THAN |  Single number, up to 2 decimal places  
EQUALS_ANY |  Max 50 numbers, up to 2 decimal places  
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#range-sample).  
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
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#range-sample).  
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
RANGE |  Max 10 ranges or integers. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#range-sample).  
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
RANGE |  Max 10 ranges. See [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#range-sample).  
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
RANGE |  Max 10 ranges, up to 2 decimal places. See the [example](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#range-sample).  
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
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#examples)Examples
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

##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/smartadtarget#status)Filter status
The `State` parameter displays the current state of impressions that match the filter.
**State** |  **Description**  
---|---  
ON |  Impressions are possible using this filter.  
OFF |  Filter is not applied.  
SUSPENDED |  Impressions using this filter were stopped by the owner (either via the [suspend](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/suspend.html) method or the web interface).  
DELETED |  The filter was deleted by the owner. Note The [get](https://yandex.com/dev/direct/doc/ref-v5/smartadtargets/get.html) method returns the filter in the DELETED state only if the `States` parameter is set to DELETED or the ID of this filter is specified in the `Ids` parameter. If both the `Ids` and `States` parameters are omitted, the method doesn't return filters in the DELETED state.  
UNKNOWN |  Unknown state. Used for providing backward compatibility and displaying states that are not supported in this version of the API.  
Copied
### Was the article helpful?
YesNo
Previous
[Feed (Feed)](https://yandex.com/dev/direct/doc/en/objects/en/objects/feed)
Next
[Dynamic feed ad target (DynamicFeedAdTarget)](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget)
