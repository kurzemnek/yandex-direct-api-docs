---
title: Portfolio strategy (Strategy) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/strategy
crawled_at: 2025-09-17T15:56:45.682304
---

Service
# Portfolio strategy (Strategy)
  * [Service](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#service)
    * [Methods](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#methods)
  * [Restrictions](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#restrictions)
  * [Strategy fields](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#fields)
  * [Highlights](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#fetures)
  * [Portfolio strategy status](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#status)


You can use portfolio strategies to combine multiple campaigns of the same type and strategy indicators settings. Use this strategy when you don't have enough conversions to train each campaign. Conversions brought by a portfolio strategy are used to train all the campaigns in this strategy.
Portfolio strategies are also useful for advertisers who need to share a single budget across multiple campaigns with different goals. The budget of a portfolio strategy is shared between the campaigns depending on their effectiveness.
Read more in 
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#service)Service
Use the 
###  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#methods)Methods
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#restrictions)Restrictions
  * A maximum of 100 campaigns per strategy.
  * A maximum of 1500 strategies per client (no more than 500 of them are non-archived).
  * Automatic strategy types supported: AVERAGE_CPA, AVERAGE_CPA_MULTIPLE_GOALS, PAY_FOR_CONVERSION, PAY_FOR_CONVERSION_MULTIPLE_GOALS, WB_MAXIMUM_CONVERSION_RATE, WB_MAXIMUM_CLICKS, AVERAGE_CRR, PAY_FOR_CONVERSION_CRR, AVERAGE_CPC_PER_CAMPAIGN, AVERAGE_CPC_PER_FILTER, AVERAGE_CPA_PER_CAMPAIGN, AVERAGE_CPA_PER_FILTER, PAY_FOR_CONVERSION_PER_CAMPAIGN, PAY_FOR_CONVERSION_PER_FILTER.
  * Campaign types supported: TEXT_CAMPAIGN, DYNAMIC_TEXT_CAMPAIGN, SMART_CAMPAIGN, UNIFIED_CAMPAIGN.
  * You can only add campaigns of the same type to a portfolio strategy.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#fields)Strategy fields
See the section [Display strategies](https://yandex.com/dev/direct/doc/en/objects/en/objects/campaign-strategies).
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#fetures)Highlights
  * To unlink a campaign from a portfolio strategy, specify a new value for `BiddingStrategy` and reset the `PackageBiddingStrategy: null` parameter value. Make sure that you set a relevant budget limit for this campaign.
  * You can't change campaign settings if this campaign is linked to a portfolio strategy. You can only edit the portfolio strategy settings. For more information, see 
  * To create a campaign with a portfolio strategy:
    1. Create a portfolio strategy and get its ID.
    2. Create a campaign and specify the ID of your portfolio strategy in the settings.
Alternatively, you can first create a campaign, get its ID, and link it to a new portfolio strategy.
Moreover, instead of creating a portfolio strategy from scratch, you can use a strategy running in another campaign as a template. To do so, in the 
  * You cannot archive a portfolio strategy that has campaigns linked to it.


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/strategy#status)Portfolio strategy status
The `StatusArchived` parameter shows the status of your portfolio strategy.
**Status** |  **Description**  
---|---  
YES |  The campaign is archived.  
NO |  The campaign is not archived.  
Copied
### Was the article helpful?
YesNo
Previous
[Adjustments (BidModifier)](https://yandex.com/dev/direct/doc/en/objects/en/objects/bidmodifier)
Next
[Audience targets (AudienceTarget)](https://yandex.com/dev/direct/doc/en/objects/en/objects/audience-target)
