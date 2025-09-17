---
title: Negative keywords | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/negative-keywords
crawled_at: 2025-09-17T15:49:31.662940
---

Negative keywords
# Negative keywords
There are several ways to set negative keywords. All methods can be used simultaneously.
  * List negative keywords at the ad group level in the `NegativeKeywords` parameter and at the campaign level in the `NegativeKeywords` parameter.
  * Create sets of negative keywords using the [NegativeKeywordSharedSets](https://yandex.com/dev/direct/doc/ref-v5/negativekeywordsharedsets/negativekeywordsharedsets.html) service. Enable sets of negative keywords at the ad group level by specifying the set IDs in the `NegativeKeywordSharedSetIds` parameter.
  * Specify individual negative keywords (negative keywords that consist of one word) directly for a keyword in the _Keyword_ parameter.


Moving negative keywords to the group or campaign level makes configuration easier and reduces the risk of exceeding the limit on keyword length (4096 characters).
If a negative keyword that is set on the group or campaign level is completely included in a keyword, the negative keyword isn't applied to this keyword.
For more information about negative keywords, see [Negative keywords](https://yandex.com/support/direct/keywords/negative-keywords.html) and [Negative keyword library](https://yandex.com/support/direct/keywords/negative-keywords-library.html) in Yandex Direct Help.
[*NegativeKeywords]:
Array of negative keywords that are shared by all the keywords of a campaign.
Restriction: This parameter can't be used with display campaigns. A keyword should be specified without the minus sign before the first word.
Maximum of 7 words per keyword. The maximum length of each word is 35 characters. The maximum combined length of negative keywords in the array is 20,000 characters. Spaces, dashes, and operators are not counted as part of the total length.
**Required** : No.
[*NegativeKeywordSharedSetIds]:
IDs of sets of negative keywords. Maximum of 3 items in the array.
To get the IDs of sets, use the [NegativeKeywordSharedSets.get](https://yandex.com/dev/direct/doc/ref-v5/negativekeywordsharedsets/get.html) method.
Restriction: Negative keywords can't be used in groups of display ads that target users based on user profiles.
**Required** : No.
Keywords.
It can contain negative keywords, which are specified with the minus sign before the word, such as lightning -thunder -rain.
The maximum length of a keyword is 4096 characters. The “!” operator before a negative keyword is not counted in the keyword length (the sequence “-!” is considered one character).
Maximum of 7 words per keyword, not counting stop words and negative keywords. Each word can have up to 35 characters, not counting the minus sign before a negative keyword.
If you have negative keywords that apply to all of an ad group's keywords, set them in the [NegativeKeywords](https://yandex.com/dev/direct/doc/ref-v5/adgroups/add.html#input__AdGroupAddItem-NegativeKeywords) parameter for the ad group.
If the value is set to `---autotargeting`, an autotargeting object is created and you can specify an automatic bid (`AutotargetingSearchBidIsAuto`).
**Required** : Yes.
Copied
Copied
### Was the article helpful?
YesNo
Previous
[Running an advertising campaign](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/launch-campaign)
Next
[Autotargeting](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/auto-targeting)
