---
title: Ad target for dynamic ads (DynamicTextAdTarget — Webpage) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/dynamictextadtarget
crawled_at: 2025-09-17T15:46:12.693987
---

Servicing
# Ad target for dynamic ads (DynamicTextAdTarget — Webpage)
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#service)
  * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#restrictions)
  * [Type of dynamic text ad targets](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#types)
  * [Selection rule](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#conditions)
  * [State of dynamic text ad targets](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#status)


A dynamic ad target defines the set of the advertiser's website pages that ads are dynamically generated for. For more information about dynamic ads, see [Dynamic ads](https://yandex.com/support/direct/dynamic-text-ads/about-da.html) in Yandex Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#service)Servicing
Use the [DynamicTextAdTargets](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/dynamictextadtargets.html) service to manage targets for dynamic ads.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#methods)Methods
[add](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/add.html) | [delete](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/delete.html) | [suspend](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/suspend.html) | [resume](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/resume.html) | [get](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/get.html) | [setBids](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/setBids.html)
Dynamic text ad targets can't be edited. If you need to change a targeting condition, you must delete it and create a new one.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#restrictions)Restrictions
A dynamic text ad target can only be added to the DYNAMIC_TEXT_AD_GROUP type of ad group.
Maximum of 50 dynamic ad targets per group.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#types)Type of dynamic text ad targets
There are two types of dynamic text ad targets:
  * PAGES_ALL: “All the website pages”.
  * PAGES_SUBSET: “A group of pages”.
This type of ad target contains the `Conditions` array, which may include up to 10 rules for page filtering. Dynamic ads will be generated for those pages that satisfy all the selection rules.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#conditions)Selection rule
A rule for page selection consists of three parameters:
  * `Operand` — Which page property is matched.
  * `Operator`: Which matching method is used.
  * `Arguments`: An array of strings to match against.


The compatibility of operands and operators is shown in the table below.
**Operand** |  **Description** |  **Applicable operators**  
---|---|---  
DOMAIN |  Domain (any level) |  CONTAINS_ANY
  * `Operand` contains one of the strings from the `Arguments` array.

NOT_CONTAINS_ALL
  * `Operand` doesn't contain any of the strings from the `Arguments` array.

The input is not case sensitive.  
URL |  Link to the product  
PAGE_TITLE |  Page title  
PAGE_CONTENT |  Page content  
OFFERS_LIST_URL |  The URL of a list of offers (a page with a list of products, such as the page for a product category or the page of search results using set parameters) |  EQUALS_ANY
  * `Operand` matches one of the strings in the `Arguments` array.

NOT_EQUALS_ALL
  * `Operand` doesn't match any of the strings in the `Arguments` array.

The protocol (http:// or https://) is ignored during comparison.  
Note
A dynamic ad text target may contain no more than one rule with the OFFERS_LIST_URL operand and the EQUALS_ANY operator, and no more than one rule with the OFFERS_LIST_URL operand and the NOT_EQUALS_ALL operator.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamictextadtarget#status)State of dynamic text ad targets
The `State` parameter reflects the current state of displays for a dynamic ad target.
**State** |  **Description**  
---|---  
ON |  Ad impressions are possible by target.  
OFF |  The dynamic ad target isn't in use.  
SUSPENDED |  Impressions by target for dynamic ads were stopped by the owner (using the [suspend](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/suspend.html) method, or in the web interface).  
DELETED |  The ad target for dynamic ads was deleted by the owner. Note The [get](https://yandex.com/dev/direct/doc/ref-v5/dynamictextadtargets/get.html) method returns a dynamic text ad target in the DELETED state only if the `States` parameter is set to DELETED or the ID of this target is specified in the `Ids` parameter. If both the `Ids` and `States` parameters are omitted, the method doesn't return dynamic text ad targets in the DELETED state.  
UNKNOWN |  Unknown state. Used for providing backward compatibility and displaying states that are not supported in this version of the API.  
Copied
### Was the article helpful?
YesNo
Previous
[Dynamic feed ad target (DynamicFeedAdTarget)](https://yandex.com/dev/direct/doc/en/objects/en/objects/dynamicfeedadtarget)
Next
[Client](https://yandex.com/dev/direct/doc/en/objects/en/objects/client)
