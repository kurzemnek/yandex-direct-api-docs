---
title: Add tags to an ad URL | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/curl-ads-keywords-modify
crawled_at: 2025-09-17T15:38:51.476930
---

Change keyword parameters
# Add tags to an ad URL
  * [Change keyword parameters](https://yandex.com/dev/direct/doc/en/en/curl-ads-keywords-modify#change-keyword-parameters)
  * [Add a parameter to the ad URL](https://yandex.com/dev/direct/doc/en/en/curl-ads-keywords-modify#add-a-parameter-to-the-ad-url)


Uses the cURL utility.
This example shows how to append custom tags to an ad URL. The tag values are specified in the `UserParam1` parameter for keywords using the [Keywords](https://yandex.com/dev/direct/doc/ref-v5/keywords/keywords.html).[update](https://yandex.com/dev/direct/doc/ref-v5/keywords/update.html) method. The tag is appended to the ad URL using the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html).[update](https://yandex.com/dev/direct/doc/ref-v5/ads/update.html) method. For example, this allows you to pass keyword IDs from your internal system or include other attributes that help you track ad performance.
To use the examples, change the input data to specify the OAuth token and the IDs of ads and keywords, and edit the URL. If you're submitting a request on behalf of an agency, be sure to include the client's login.
##  [](https://yandex.com/dev/direct/doc/en/en/curl-ads-keywords-modify#change-keyword-parameters)Change keyword parameters
```
curl \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Client-Login: CLIENT_LOGIN' \
  -d '{ "method": "update",
  "params": {
    "Keywords": [{
      "Id": KEYWORD_1_ID,
      "UserParam1": "VALUE_1"
    },
    {
      "Id": KEYWORD_2_ID,
      "UserParam1": "VALUE_2"
    }]
  }
}' https://api.direct.yandex.com/json/v5/keywords

```

##  [](https://yandex.com/dev/direct/doc/en/en/curl-ads-keywords-modify#add-a-parameter-to-the-ad-url)Add a parameter to the ad URL
```
curl \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Client-Login: CLIENT_LOGIN' \
  -d '{ "method": "update",
  "params": {
    "Ads": [{
      "Id": AD_1_ID,
      "TextAd": {
        "Href": "https://www.site.com/1/?utm_source=yandex-direct&utm_term={param1}"
      }
    },
    {  
      "Id": AD_2_ID,
      "TextAd": {
        "Href": "https://www.site.com/2/?utm_source=yandex-direct&utm_term={param1}"
      }
    }]   
  }
}' https://api.direct.yandex.com/json/v5/ads

```

Result: The first link in the ad leads to `https://www.site.com/1/?utm_source=yandex-direct&utm_term=VALUE_1` when the ad is served for keyword 1, and to `https://www.site.com/1/?utm_source=yandex-direct&utm_term=VALUE_2` when the ad is served for keyword 2.
Note
For cURL in Windows, replace all single quotes with double quotes, and escape double quotes in JSON code. For example: `-d "{\"method\"`...
Copied
Copied
### Was the article helpful?
YesNo
Previous
[Change the strategy](https://yandex.com/dev/direct/doc/en/en/curl-campaigns-strategy)
Next
[Stop and start ads](https://yandex.com/dev/direct/doc/en/en/curl-ads-launch)
