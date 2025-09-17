---
title: Running an advertising campaign | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/launch-campaign
crawled_at: 2025-09-17T15:47:23.182624
---

Creation and review
# Running an advertising campaign
  * [Creation and review](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign#create-campaign)
  * [Stopping and restarting](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign#suspend-resume)
  * [Ad extensions](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign#harness)


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign#create-campaign)Creation and review
  1. Create campaigns: the 
For information about campaign types, see the section [Campaign type](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/campaign#type).
  2. Create ad groups: the 
The group type must match the campaign type.
  3. For a group of text and image ads or a group for advertising mobile apps, add keywords and autotargetings: the 
You can set bids and priorities immediately when creating keywords, or later using the 
  4. For a group of dynamic ads, add dynamic ad targets: the 
  5. Create ads: use the 
You can enhance your ad with add-ons. See [Add-ons to ads](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign#harness).
  6. Submit ads for review: the 


After ads are approved by a moderator, you must transfer funds to the advertising campaign or the shared account. Ads will start being served after payment, but not before the start date of the advertising campaign.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign#suspend-resume)Stopping and restarting
  * Use the 
You can re-enable impressions of previously stopped campaigns using the 
  * Use the 
Use the 
  * Use the 
Use the 
  * Use the 
Use the 


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/launch-campaign#harness)Ad extensions
Depending on the type of ad, you can add a vСard, business profile ID, image, set of sitelinks, callouts, video extension, or Turbo page.
You can include add-ons when creating an ad, or assign the add-ons later after creating the ad.
**Ad extension** |  **Creating** |  **Assigned to ad** |  **Unassigned from ad**  
---|---|---|---  
Business profile |  You can add a business profile or verify your rights to it in the  |  Once an ad extension is created, you can specify its ID in the  |  To unassign an extension, the `nil (null)` value instead of the ID.  
[Image](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/adimage) |  The   
|   
|  You can create a Turbo page in the Turbo Page Builder.  
[A callout](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/adextension) |  |  Once an ad extension is created, you can specify its ID in the  |  You can unassign all the callouts from an ad at once, or selectively. To unassign all the callouts, the `nil (null)` value in the `CalloutSetting` parameter. To unassign a particular callout, specify the callout ID in the `CalloutSetting` parameter and set the action type to `REMOVE`.  
|  Create a video extension in the Ad Builder. To synchronously upload videos by their URL links, use the Add operation from the AdVideos method. |  After creating the video extension in Ad Builder, specify its ID in the `CreativeId` parameter in the `VideoExtension` structure. |  To unassign the video extension, pass `nil (null)` in the `CreativeId` parameter of the `VideoExtension` structure in the . method.  
Note
When an add-on is unassigned from an ad, it is not deleted. To delete an add-on that isn't assigned to any ad, use the `delete` method for the appropriate service.
Copied
### Was the article helpful?
YesNo
Previous
[null (nil) value](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable)
Next
[Negative keywords](https://yandex.com/dev/direct/doc/en/best-practice/en/objects/negative-keywords)
