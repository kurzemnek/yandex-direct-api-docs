---
title: Autotargeting | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/auto-targeting
crawled_at: 2025-09-17T15:52:39.404482
---

Autotargeting
# Autotargeting
  * [Add](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#add)
  * [Edit](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#update)
  * [Set the bid](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#set)
  * [Pause, start, delete](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#suspend)
  * [Get](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#get)
  * [Statistics](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#stat)


You can use autotargeting technology to serve ads without configuring keywords. The ad text and the landing page are matched to the search query, the user's interests, or the site content where it is served. For more information, see [Autotargeting](https://yandex.com/support/direct/features/autotargeting.html) in Yandex Direct Help.
The autotargeting criteria are the same as for a keyword and have the same parameters (except that you can't edit the phrase).
Autotargeting can be used in `TEXT_AD_GROUP` and `MOBILE_APP_AD_GROUP` types of ad groups.
  * When you use the [AdGroups.add](https://yandex.com/dev/direct/doc/ref-v5/adgroups/add.html) method, all created groups automatically include the `---autotargeting` keyword.
  * Ad groups served on Yandex Search or both Yandex Search and the Yandex Advertising Network, are created with autotargeting enabled. You will get a validation error if you try to disable it.
  * In campaigns served in the Yandex Advertising Network, ad groups are created with autotargeting disabled. You can enable or disable this keyword as needed. To enable autotargeting in such a group:
    * Once an ad group is created, get the `---autotargeting` keyword using the [Keywords.get](https://yandex.com/dev/direct/doc/ref-v5/keywords/get.html) method and enable it using the [Keywords.resume](https://yandex.com/dev/direct/doc/ref-v5/keywords/resume.html) method.
    * Alternatively, you can get the `---autotargeting` keyword using the [Keywords.add](https://yandex.com/dev/direct/doc/ref-v5/keywords/add.html) method (this enables the previously disabled keyword).
  * You can't delete the `---autotargeting` keyword using the [Keywords.delete](https://yandex.com/dev/direct/doc/ref-v5/keywords/delete.html) method. When called, this method disables autotargeting in those campaigns where it is possible.


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#add)Add
Use the [Keywords.add](https://yandex.com/dev/direct/doc/ref-v5/keywords/add.html) method to add autotargeting to an ad group. To do this, specify the special value `---autotargeting` in the `Keyword` parameter.
You can only add one autotargeting to an ad group. If you add multiple autotargetings to an ad group in the same request, an error is returned for each autotargeting.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#update)Edit
Use the [Keywords.update](https://yandex.com/dev/direct/doc/ref-v5/keywords/update.html) method to change `UserParam1` and `UserParam2` for autotargeting. You can't change the `Keyword` parameter.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#set)Set the bid
Use the [KeywordBids.set](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/set.html) method to set the bid and priority for autotargeting.
When changing bids for all the keywords in an ad group or campaign, the [KeywordBids.setAuto](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/setAuto.html) method may affect the autotargeting bid. The method doesn't support setting the bid for autotargeting separately.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#suspend)Pause, start, delete
The [Keywords.suspend](https://yandex.com/dev/direct/doc/ref-v5/keywords/suspend.html) and [Keywords.resume](https://yandex.com/dev/direct/doc/ref-v5/keywords/resume.html) methods pause and resume impressions for autotargeting.
Use the [Keywords.delete](https://yandex.com/dev/direct/doc/ref-v5/keywords/delete.html) method to remove autotargeting from an ad group. You can add it again later.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#get)Get
Use the [Keywords.get](https://yandex.com/dev/direct/doc/ref-v5/keywords/get.html) method to get the same parameters for autotargeting as for a keyword. The value `---autotargeting` is returned in the `Keyword` parameter.
Use the [KeywordBids.get](https://yandex.com/dev/direct/doc/ref-v5/keywordbids/get.html) method to get the same parameters for the autotargeting as for a keyword, except `Search.AuctionBids` and `Network.Coverage`.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/auto-targeting#stat)Statistics
Use the `Reports` service to get statistics on impressions and clicks for autotargeting. Autotargeting parameters are output to the following report fields:
**Field** |  **Value**  
---|---  
`Criteria`, `Criterion` |  `---autotargeting`  
`CriteriaId`, `CriterionId` |  ID of the autotargeting.  
`CriteriaType` |  AUTOTARGETING  
To select data only for autotargeting, filter by `CriteriaType`:
```
<Filter>
  <Field>CriteriaType</Field>
  <Operator>EQUALS</Operator>
  <Values>AUTOTARGETING</Values>
</Filter>

```

Copied
### Was the article helpful?
YesNo
Previous
[Negative keywords](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/negative-keywords)
Next
[Tracking changes](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/check-changes)
