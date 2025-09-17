---
title: Campaign settings (Option parameter) | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/annex/campaign-options
crawled_at: 2025-09-17T15:38:34.567141
---

Campaign settings (Option parameter)
# Campaign settings (Option parameter)
**Setting name** |  **Description**  
---|---  
ADD_METRICA_TAG |  Automatically add the `yclid` tag with a unique click ID to the ad link. Use this tag to track the performance of your ad campaigns more accurately in Yandex Metrica (see  The default value is YES.  
ADD_OPENSTAT_TAG |  When redirecting to the advertiser's web site, append an OpenStat tag to the URL. The default value is NO.  
ADD_TO_FAVORITES |  Add the campaign to your favorites, in order to filter by it in the web interface. The default value is NO.  
CAMPAIGN_EXACT_PHRASE_MATCHING_ENABLED |  Enables exact keyword matching inside the campaign (see  The default value is NO.  
DAILY_BUDGET_ALLOWED |  This setting is no longer relevant. Always returns YES.  
ENABLE_AREA_OF_INTEREST_TARGETING |  Enable area of interest targeting (enhanced geographical targeting). The default value is YES.  
ENABLE_COMPANY_INFO |  When serving ads on Yandex Maps, add company information from Yandex Business Directory to the ad. The default value is YES.  
ENABLE_EXTENDED_AD_TITLE |  Enable inserting part of the ad text in the title (see [Extended Ad Title in ads](https://yandex.com/support/direct-tooltips/text-substitution.html) in the Help for Yandex Direct). The default value is YES.  
ENABLE_SITE_MONITORING |  Stop displays when the advertiser's site is unavailable (see [Monitoring site availability](https://yandex.com/support/direct/campaigns/site-monitoring.html) in the Help for Yandex Direct). The default value is NO.  
EXCLUDE_PAUSED_COMPETING_ADS |  When calculating forecasted bids, ignore bids in competitors' ads that are paused in accordance with time targeting. The default value is NO.  
MAINTAIN_NETWORK_CPC |  Keep the average CPC in ad networks lower than the average CPC in search results. This setting is only used for the HIGHEST_POSITION search strategy and the NETWORK_DEFAULT strategy in ad networks. For all other strategies, this setting is not used and the passed value is ignored. The default value is YES.  
REQUIRE_SERVICING |  Switch the campaign to being handled by a personal manager. If the advertiser doesn't have any campaigns handled by a manager, you can only set the value to NO. Trying to set it to YES will automatically change it to NO and display a warning. The default value is NO. If the advertiser already has at least one campaign handled by a manager, you can set the value to either YES or NO. The default value is YES. You can't change the value from YES to NO.  
SHARED_ACCOUNT_ENABLED |  The shared account is enabled.  
ALTERNATIVE_TEXTS_ENABLED |  Optimize ad texts for queries. See   
For information on how the set of options depends on the campaign type, see the section [Campaign parameters](https://yandex.com/dev/direct/doc/dg/objects/campaign-params.html).
Copied
### Was the article helpful?
YesNo
Previous
[Types of strategies](https://yandex.com/dev/direct/doc/en/annex/en/annex/strategies)
Next
[How to generate a report](https://yandex.com/dev/direct/doc/en/annex/en/how-to)
