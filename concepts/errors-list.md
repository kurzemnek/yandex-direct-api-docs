---
title: Errors and warnings - API reference | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/errors-list
crawled_at: 2025-09-17T15:46:23.944346
---

Errors and warnings  
This section lists codes and descriptions of errors and warnings in response messages from the Yandex Direct API version 5.# Errors
Error code |  Message |  Comments and possible reasons  
---|---|---  
**Server errors** |  |   
52 |  Authorization server temporarily unavailable |  The Yandex Direct API server is temporarily unable to get information from the Yandex.OAuth service. Try calling the method again later.  
1000 |  Server temporarily unavailable |  Internal error on the Yandex Direct API server. Try calling the method again later. If the error persists, contact the support service.  
1001 |  Service initialization error |   
1002 |  Operation error |   
1003 |  Couldn't create a Yandex user account |  An error occurred when creating the account. Try calling the method again later.  
1004 |  Couldn't create client |  An error occurred when creating a client in Yandex Direct. Try calling the method again later. Use a different username to repeat the request.  
1020 |  Internal server error |  The list of available currencies isn't defined. Contact [support](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/.https:/yandex.com/dev/direct/doc/support/troubleshooting/issue).  
**Authentication error** |  |   
53 |  Authorization error |  Invalid OAuth token. For the reasons why a token may become invalid, see [Revoking tokens](https://tech.yandex.com/oauth/doc/dg/reference/token-invalidate-docpage/) in the Yandex OAuth guide.  
**Incomplete app registration** |  |   
58 |  Incomplete registration |  You must [submit a request](https://yandex.com/dev/direct/doc/dg/objects/register.html) for API access and wait for it to be approved.  
**Permission errors** |  |   
54 |  No rights | 
  * The username specified in the request belongs to an advertiser that is not a client of the agency performing the request.
  * The user who a write/edit request is being made on behalf of only has read rights.
  * You need to set a currency for the advertiser's account.
  * The request to the [AgencyClients](https://yandex.com/dev/direct/doc/en/concepts/en/agencyclients/agencyclients) service specifies an access token that was obtained for an advertiser's representative.

  
513 |  Your username is not enabled in Yandex Direct |  The request is on behalf of a user who doesn't have a Yandex Direct account. To register an account, create an advertising campaign in this user's name in the web interface. See also [Access and authorization](https://yandex.com/dev/direct/doc/dg/concepts/access.html).  
3000 |  No API access | 
  * The request is on behalf of a user who doesn't have API access.
  * API access is closed when campaigns are being converted to a currency.
  * The user didn't allow API access from this IP address. See the section [Restricting access by IP address](https://yandex.com/dev/direct/doc/dg/concepts/access.html#restrictions).

  
3001 |  No access to the method |  Access to the [AgencyClients](https://yandex.com/dev/direct/doc/en/concepts/en/agencyclients/agencyclients).[add](https://yandex.com/dev/direct/doc/en/concepts/en/agencyclients/add) method is granted to the agency on request.  
**Restrictions, points** |  |   
152 |  Not enough Yandex units |   
506 |  Exceeded limit on number of connections |  You have reached the maximum number of simultaneous connections to the Yandex Direct server.  
**Unsupported fields, objects, and operations** |  |   
3500 |  Not supported |  Attempt to add bid adjustment is not compatible with the campaign type.  
3600 |  Limited functionality |  Attempt to use the PAY_FOR_CONVERSION or PAY_FOR_CONVERSION_PER_CAMPAIGN strategy.  
**Invalid request parameters** |  |   
4000 |  Invalid request parameters | 
  * The passed parameters for a campaign, group, or ad aren't appropriate for the type of the campaign, group, or ad.
  * Display strategy parameters are set incorrectly: the structure with parameters for the selected strategy is omitted, or the structure specified has parameters for a different strategy.
  * Invalid date format (for example, in the `Timestamp` parameter).
  * Invalid time zone.
  * To optimize conversions for priority goals, specify at least one priority goal other than engaged sessions.
  * To use product categories, you must specify the feed ID.

  
4001 |  Invalid SelectionCriteria filter parameters | 
  * Exceeded the number of IDs in the array.
  * `SelectionCriteria` must have at least one parameter from the set (for example, `Ids`, `AdGroupIds`, and `CampaignIds`).

  
4002 |  Invalid page settings |  Invalid value in the `Limit` or `Offset` parameter.  
4003 |  All required parameters were omitted |  The request must contain at least one parameter from the set, but none of them were specified.  
4004 |  More than one parameter was passed |  Mutually exclusive parameters were specified. Only one of them can be present in the request.  
4005 |  A single type of Id must be used within a request |  Bids are set with IDs of heterogeneous objects (for example, one `Bids` structure has `CampaignId`, but the other structure has `AdGroupId`).  
4006 |  Incompatible operations are entered in the same request |  To edit ad callouts, either use the ADD and REMOVE operations, or use the SET operation.  
**Invalid field value** |  |   
5000 |  Required field |  A required field is empty, or the value consists of spaces.  
5001 |  Exceeded allowed length | 
  * Exceeded the maximum length for the field value.
  * Exceeded total length of sitelink texts.

  
5002 |  Forbidden symbols used | 
  * There is an unallowed character in a keyword, negative keyword, or sitelink.
  * Using operators incorrectly in a keyword, for example, an isolated "!" character.

  
5003 |  Empty value specified |  There is an empty string, for example, in an ad's `Href` parameter.  
5004 |  Invalid format |  Incorrect value for an object field, such as:
  * In the `VCards.add` method:
    * Invalid instant messaging ID in the `MessengerLogin` parameter.
    * Invalid email address in the `ContactEmail` parameter.
    * Invalid business hours in the `WorkTime` parameter.
    * Invalid phone number in the `Phone` structure.
  * In the `AdGroups` service: empty group name.
  * In the `AdImages` service: the type or size of the image file doesn't meet the requirements.

  
5005 |  Field set incorrectly |  Incorrect value for an object field, such as:
  * The object ID isn't a positive integer.
  * In the `VCards.add` method:
    * Unsupported instant messaging platform in the `MessengerClient` parameter.
    * Country code, city code, or phone number omitted in the `Phone` structure.
    * The subway station in the `MetroStationId` parameter is invalid or doesn't match the city.
  * In the `AgencyClients`.`add` method:
    * An invalid currency is specified for the client. You can find the currencies that agencies can use to register clients in the [ClientCurrencies](*ClientCurrencies) parameter of the [{#T}](https://yandex.com/dev/direct/doc/dg-v4/live/GetClientInfo.md) method in the Live 4 version of the API.
    * A prohibited site or an invalid campaign type is specified for the client.
  * The `Clients`.`add` method specifies a prohibited site or an invalid campaign type.
  * In the `Sitelinks` service: the protocol in the link isn't HTTP or HTTPS.
  * In the `Ads` service: the `AdImageHash` field contains an invalid image link, or a link to a non-existant image.
  * In the `AdGroups` service, the `RegionIds` array is empty.
  * In the `Bids` service: the bid value or `ContextCoverage` is outside of the allowed range.
  * In the `Keywords`.`update` method: an attempt to disable all autotargeting categories.

  
5006 |  Invalid use of field | 
  * In the `Campaigns` service:
    * The selected strategy isn't appropriate for the campaign type. See [Display strategies](https://yandex.com/dev/direct/doc/dg/objects/campaign-strategies.html).
    * Invalid domain or IP address.
  * In the `Ads` service:
    * The ad title or text has a word that is too long.
    * Punctuation is used incorrectly in the title or text (a space before a comma).
    * The main link duplicates a sitelink.
  * In the `Sitelinks` service: a sitelink duplicates the main ad link.

  
5007 |  Duplicated element |  Sitelink texts are duplicates, or they link to the same webpage.  
5008 |  All required fields were omitted |  The object must have at least one field specified from the set, but none of them are specified.  
5009 |  More than one field was passed |  The object has mutually exclusive fields specified.  
5010 |  Invalid field length |  The field is too short.  
5100 |  Incorrect template use |  Incorrect use of templates (##) in the ad title and text.  
5120 |  Geotargeting set incorrectly | 
  * The specified region ID does not exist.
  * A region is repeated multiple times.
  * Only negative regions are specified.
  * A negative region was specified that matches a display region.
  * A negative region was specified that is not contained in any of the display regions.

  
5140 |  Keyword contains too many words |  Exceeded the number of words in a keyword.  
5141 |  Incorrect use of stop words |  A keyword consists exclusively of stop words.  
5142 |  Exceeded the maximum word length in a keyword |   
5160 |  Negative keyword can't be a phrase |  Attempt to use a negative keyword with a space in it.  
5161 |  Incorrect use of negative keywords | 
  * A keyword consists exclusively of negative keywords.
  * A negative keyword contains a dot (and is not a decimal number).
  * A negative keyword begins with an apostrophe or ends in an apostrophe.
  * Invalid combination of special symbols in a keyword.
  * A phrase in quotation marks can't consist of negative keywords.
  * You may not specify a negative keyword contained in the original keyword.
  * The total length of keywords exceeds the maximum allowed value.

  
5162 |  Exceed the maximum length of a negative keyword |   
5181 |  You cannot change the advertised application |   
5200 |  Login already in use |  Attempt to create a client with a login name that is already used by another Yandex account.  
**Inconsistent object** |  |   
6000 |  Inconsistent object state | 
  * The type of ad group doesn't correspond to the type of campaign, or the type of ad doesn't correspond to the type of group.
  * Attempt to delete a vCard that is used in an ad.
  * Attempt to delete a set of sitelinks that are used in an ad.
  * An ad specifies a set of sitelinks, but does not specify the main link.
  * An ad doesn't specify a vCard or a main link.
  * Attempt to change the [age label](https://yandex.com/dev/direct/doc/dg/objects/ad.html) when there isn't an age label assigned, or an attempt to set an age label that doesn't correspond to the [ad category](https://yandex.com/dev/direct/doc/dg/objects/ad.html).
  * Attempt to grant an agency client permission to manage campaigns using files but this client doesn't have permission to edit campaigns.
  * Attempt to create a group of display ads with a target based on a user profile that also has negative keywords.

  
6001 |  Wrong object type specified | 
  * Attempt to add a keyword to a group of dynamic ads.
  * Attempt to add autotargeting categories to an unsupported ad group.

  
6100 |  The display region doesn't match the ad text (title, text, sitelinks) |  When trying to change the display region in a group, the ad language was not appropriate for the new region (for example, the ad has Kazakh letters, but geotargeting is being changed to Russia)  
6101 |  Language doesn't match geotargeting |  When adding or modifying ads, display region compatibility was violated (for example, an ad was created in Ukrainian but geotargeting is set to Russia)  
**Object restrictions** |  |   
7000 |  Number of allowed elements exceeded or equal to zero | 
  * Number of sitelinks less than 1 or more than 4
  * Attempt to add more than one audience target to a group of display ads.

  
7001 |  Reached the maximum number of objects | 
  * Reached the maximum number of ad groups in a campaign
  * Reached the maximum number of ads in a group
  * Reached the maximum number of keywords in an ad group

  
7002 |  This tracking system domain isn't supported |   
**Request parsing errors** |  |   
55 |  Operation not found |  Invalid value specified for the `method` key in a JSON request.  
8000 |  Invalid request | 
  * OAuth token omitted.
  * The OAuth token has an invalid format (for example, it contains forbidden characters).
  * The advertiser's username was not specified in a request from an agency.
  * Required parameter omitted.
  * Unknown parameter included.
  * Incorrect parameter type, for example:
    * String instead of number.
    * Single value instead of array.
    * If the parameter has a fixed set of values (for example, `FieldNames`), a value outside of this set will cause an error.
  * Invalid JSON.
  * `method` key omitted in a JSON request.
  * `SOAPAction` header or body omitted in a SOAP request.

  
**Can't perform operation** |  |   
8300 |  Invalid object status | 
  * Attempt to perform an operation with an ad, ad group, or vCard in an archived or deleted campaign.
  * Attempt to submit an ad for review that is not a draft, or is in a group that does not contain display conditions, or is archived.
  * Attempt to delete an ad that is forbidden to delete (for example, the ad has been displayed).
  * Attempt to suspend or resume a draft ad or an archived ad.
  * Attempt to archive an active ad or a draft ad.

  
8301 |  Can't delete object | 
  * Attempt to delete an ad group containing ads or targeting criteria (keywords, audience targets, or dynamic text ad targets).
  * Attempt to delete the only active keyword in a group (if there are no audience targets).
  * Attempt to delete a campaign that can't be deleted (for example, the campaign has funds on it or has an unpaid invoice).

  
8302 |  Displays can't be suspended |  Attempt to suspend the only active keyword in a group (if there are no audience targets).  
8303 |  Object can't be archived | 
  * Attempt to archive a campaign that has funds.
  * Attempt to archive a campaign that hasn't been suspended.
  * Attempt to archive a campaign when the shared account has insufficient funds.

  
8304 |  Object can't be unarchived | 
  * Attempt to unarchive a campaign from the special archive (the CONVERTED state)
  * Attempt to unarchive a campaign that exceeds the limit on the number of active campaigns

  
8305 |  Can't perform action |  Attempt to change the daily budget amount more than 3 times during the same day.  
8312 |  Can't build a report in online mode |  A report with the specified parameters can only be generated in offline mode. Change `processingMode` in the request HTTP header. See [mode](https://yandex.com/dev/direct/doc/reports/mode.html).  
8600 |  Error enabling the shared account |   
**Object not found** |  |   
8800 |  Object not found | 
  * The `Client-Login` HTTP header specifies a non-existent username or the username of an advertiser that doesn't belong to this agency.
  * Specified the ID of an object that is non-existing, deleted, or does not belong to the user (a campaign, group, ad, vCard, or keyword).

  
**Limits on the number of objects in operations in a single request** |  |   
9300 |  Exceeded the limit on the number of objects in operations in a single request |  Exceeded the maximum number of objects in the method's input array  
9301 |  Selection condition is too broad |  Exceeded the maximum number of selected adjustments. The total of the `Limit` and `Offset` values must not exceed 120,000.  
**Dependency of bids on strategies** |  |   
9600 |  The field does not correspond to the set strategy |  The request doesn't have a field that is required in certain conditions (for example, `Bid` in the `Bids.Set` method for manual display strategies).  
9601 |  Bid can't be changed | 
  * An automatic strategy is set in the campaign.
  * Changing bids in ad networks is not allowed, because displays in ad networks are disabled.
  * Changing bids in ad networks is not allowed, because the bid in ad networks depends on the bid in search results for the selected strategy.
  * Changing bids for the search is not allowed, because displays are disabled in search results.

  
**Duplicate objects** |  |   
9800 |  An object can't be in the request more than once |  A single call of the `update`, `set`, or `delete` method contains multiple objects with the same ID.  
9801 |  An object with the specified characteristics already exists |  Attempt to add an adjustment that already exists (for example, repeatedly adding a mobile adjustment or an adjustment for the same target audience).  
9802 |  An item can't be in the list more than once | 
  * In the `Campaigns` service: a duplicate value in the `BlockedIps`, `CounterIds`, or `NegativeKeywords` array, or repeated days in the `Schedule` array.
  * In the `AdGroups` service: a duplicate value in the `TargetDeviceType` array.
  * In the `Ads` service: a duplicate value in the callouts array.

  
**Warning code** |  **Message**  
---|---  
10000 |  The object is in the request more than once  
10020 |  The object is already suspended.  
10021 |  The object is not suspended.  
10022 |  The object is already archived.  
10025 |  The object is already marked as deleted  
10100 |  The specified vCard duplicates a previously created vCard  
10120 |  The specified set of sitelinks duplicates a previously created set  
10140 |  Keyword already exists  
10141 |  New keyword created as the result of updating  
10160 |  Bid won't be applied  
10161 |  Priority won't be applied  
10163 |  Setting won't be changed  
10165 |  Parameter won't be applied  
10175 |  The setting with a higher priority will be used  
10200 |  Ad already paused  
10201 |  Ad not paused  
10202 |  Ad already archived  
10203 |  Ad not archived  
10240 |  Keyword already stopped  
10241 |  Keyword not stopped  
10242 |  Dynamic text ad target is already stopped  
10243 |  Dynamic text ad target is not stopped  
  * [errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/concepts/en/vcards/get)
Next
[Types of strategies](https://yandex.com/dev/direct/doc/en/concepts/en/annex/strategies)
