---
title: Recommendations for registering representatives | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/representatives-recommendations
crawled_at: 2025-09-17T15:44:37.433839
---

Separate app representative
# Recommendations for registering representatives
  * [Separate app representative](https://yandex.com/dev/direct/doc/en/objects/en/objects/representatives-recommendations#separate-app-representative)
  * [Different representatives for different apps](https://yandex.com/dev/direct/doc/en/objects/en/objects/representatives-recommendations#different-representatives-for-different-apps)


##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/representatives-recommendations#separate-app-representative)Separate app representative
We recommend registering a separate representative of the advertiser or agency for working in an app. If you are using the same username in the web interface and the app, you need to change the password often for security reasons. When you change the password, you need to issue a new OAuth token. If the username is only used in the app rather than in the browser, the risk of compromise is minimal, and you can change the password less frequently.
It is particularly useful to create a separate representative if the app doesn't interact with the user (for example, a script updates bids automatically). In this case, it is difficult to issue a new token for the app.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/representatives-recommendations#different-representatives-for-different-apps)Different representatives for different apps
If you use several different apps for working with Yandex.Direct (such as apps that perform different tasks or were created by different developers), we recommend creating a separate representative for each app. If you have problems with some app (for example, the token was compromised, or it's spending too many points), you need to revoke the token only from the app's representative.
####  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/representatives-recommendations#learn-more)Learn more
  * [Client](https://yandex.com/dev/direct/doc/en/objects/en/objects/client)
  * [Roles and access of Yandex.Direct users](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles)


### Was the article helpful?
YesNo
Previous
[How to manage smart banners](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/smart-ads)
Next
[For agencies](https://yandex.com/dev/direct/doc/en/objects/en/best-practice/agency)
