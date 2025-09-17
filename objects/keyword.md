---
title: Keyword | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/keyword
crawled_at: 2025-09-17T15:54:04.910048
---

Servicing
# Keyword
  * [Servicing](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#restrictions)
  * [Status and state of a keyword](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#status)
    * [Learn more](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#learn-more)
  * [Substitution variables](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#userparams)
  * [Creating a new keyword after editing](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#update)
  * [Duplicate keywords](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#duplicate)


A keyword determines which search queries on Yandex will trigger an ad impression, as well as the topics of pages and user interests that the ad will be displayed for in ad networks (the Yandex Advertising Network and external networks). For more information, see [Keywords](https://yandex.com/support/direct/keywords/keywords.html) in the Help for Yandex Direct.
A keyword may contain negative keywords. You can also set negative keywords at the ad group level and at the campaign level. See [Negative keywords](https://yandex.com/dev/direct/doc/en/objects/en/objects/negative-keywords).
A keyword can contain refining operators. See [Symbols and operators](https://yandex.com/support/direct/keywords/symbols-and-operators.html) in Yandex Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#service)Servicing
Use the [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html) service for managing keywords.
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#methods)Methods
[add](https://yandex.com/dev/direct/doc/ref-v5/keywords/add.html) | [update](https://yandex.com/dev/direct/doc/ref-v5/keywords/update.html) | [delete](https://yandex.com/dev/direct/doc/ref-v5/keywords/delete.html) | [suspend](https://yandex.com/dev/direct/doc/ref-v5/keywords/suspend.html) | [resume](https://yandex.com/dev/direct/doc/ref-v5/keywords/resume.html) | [get](https://yandex.com/dev/direct/doc/ref-v5/keywords/get.html)
Note
Use the [KeywordBids](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/keywordbids.html) service for setting bids and priorities on keywords. See also [Bid and priority (KeywordBid)](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#restrictions)Restrictions
You cannot add keywords to an ad group of the CPM_BANNER_AD_GROUP type and USER_PROFILE subtype, as well as an ad group of the DYNAMIC_TEXT_AD_GROUP type.
To get the limit on the number of keywords per ad group for an advertiser, use the [Clients](https://yandex.com/dev/direct/doc/ref-v5/clients/clients.html).[get](https://yandex.com/dev/direct/doc/ref-v5/clients/get.html) or [AgencyClients](https://yandex.com/dev/direct/doc/ref-v5/agencyclients/agencyclients.html).[get](https://yandex.com/dev/direct/doc/ref-v5/agencyclients/get.html) method (see the KEYWORDS_TOTAL_PER_ADGROUP element in the _Restrictions_ array).
For restrictions on the number of words and characters in a keyword, see the section [Quantitative restrictions](https://yandex.com/support/direct/troubleshooting/interface.html#limitations) in the Help for Yandex Direct.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#status)Status and state of a keyword
The `Status` parameter reflects the results of reviewing a keyword.
**Status** |  **Description**  
---|---  
DRAFT |  New keyword: not yet submitted for review, or currently under review. If a campaign has at least one ad that is active or submitted for review, new keywords are automatically submitted for review.  
ACCEPTED |  The keyword was accepted after review.  
REJECTED |  The keyword was rejected after review.  
UNKNOWN |  The status is unknown. This value is used for backward compatibility and for displaying statuses that are not supported in this version of the API.  
The `State` parameter reflects whether displays were suspended for the keyword.
**State** |  **Description**  
---|---  
ON |  Ad displays for the keyword are enabled.  
SUSPENDED |  Ad displays were suspended by the owner using the [suspend](https://yandex.com/dev/direct/doc/ref-v5/keywords/suspend.html) method or in the web interface.  
OFF |  The keyword has not been submitted for review yet, or was rejected after review.  
The `ServingStatus` parameter reflects the ad group serving status. See [Ad group serving status](https://yandex.com/dev/direct/doc/en/objects/en/objects/adgroup#serving-status).
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#learn-more)Learn more
  * [How can I tell if there are active displays for a keyword?](https://yandex.com/dev/direct/doc/support/troubleshooting/faq.html#faq__keyword-running)


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#userparams)Substitution variables
The ad link and sitelinks can use the substitution variables `{param1}` and `{param2}`. They are substituted with the values specified in the keyword parameters `UserParam1` and `UserParam2`. This allows you to modify links depending on the keyword used to select and display the ad. For more information about substitution variables, see [Transferring ad data in URLs](https://yandex.com/support/direct/statistics/url-tags.html) in Yandex Direct Help.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#update)Creating a new keyword after editing
A new keyword may be created as the result of editing a keyword. For example, this may happen if you delete or replace a keyword or delete a negative keyword, or add or remove the **!** or **+** operator.
If a new keyword is created, the [update](https://yandex.com/dev/direct/doc/ref-v5/keywords/update.html) method returns the ID of the new keyword and a warning.
Statistics will still be available for the “old” keyword, but displays will be stopped for it, and you will not be able to work with it anymore.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#duplicate)Duplicate keywords
Duplicates are keywords that differ only in their word forms and auxiliary parts of speech, such as _exchange dollars to rubles_ and _exchanging rubles and dollars_.
The [add](https://yandex.com/dev/direct/doc/ref-v5/keywords/add.html) and [update](https://yandex.com/dev/direct/doc/ref-v5/keywords/update.html) methods automatically delete duplicate keywords within an ad group:
  * If two keywords that are duplicates are passed in the input array of the `add` method, a single keyword is created, identical IDs are returned in the method response, and a warning is issued for one of the keywords.
  * If the input array of the `add` method passes a keyword that duplicates an existing one, the new keyword isn't created, and the method response returns the ID of the existing keyword with a warning.
  * If editing a keyword using the `update` method caused the keyword to become a duplicate of an existing one, the edited keyword is deleted and the method response returns the ID of the existing keyword with a warning.
  * If editing two keywords using the `update` method causes the keywords to become duplicates, one of them is deleted. The response for it returns the ID of the other keyword with a warning.
Example
![keywords-update](https://yandex.com/dev/direct/doc/en/objects/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_images/keywords-update.png)
  * If editing two keywords using the `update` method causes the keywords to become duplicates and [a new keyword is created](https://yandex.com/dev/direct/doc/en/objects/en/objects/keyword#update), the method returns the ID of the new keyword and warnings: for one of the keywords in the request, that a new keyword was created, and for the other, that the same keyword exists.
Example
![keywords-update2](https://yandex.com/dev/direct/doc/en/objects/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_images/keywords-update2.png)


**For an advertiser**  
Limits on the number of objects for an advertiser.  
**For an agency**  
—
Copied
### Was the article helpful?
YesNo
Previous
[Turbo page (TurboPage)](https://yandex.com/dev/direct/doc/en/objects/en/objects/turbo-page)
Next
[Bid and priority (KeywordBid)](https://yandex.com/dev/direct/doc/en/objects/en/objects/bid-priority)
