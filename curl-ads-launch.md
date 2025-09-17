---
title: Stop and start ads | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/curl-ads-launch
crawled_at: 2025-09-17T15:38:58.873583
---

Stop
# Stop and start ads
  * [Stop](https://yandex.com/dev/direct/doc/en/en/curl-ads-launch#stop)
  * [Start](https://yandex.com/dev/direct/doc/en/en/curl-ads-launch#start)


Uses the cURL utility
This example shows how to stop serving ads using the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html).[suspend](https://yandex.com/dev/direct/doc/ref-v5/ads/suspend.html) method and restart using the [Ads](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.html).[resume](https://yandex.com/dev/direct/doc/ref-v5/ads/resume.html) method. For instance, you can pause and resume ads based on product inventory levels. This helps you avoid wasting money on out-of-stock items.
To use the examples, specify the OAuth token and ad IDs in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login.
##  [](https://yandex.com/dev/direct/doc/en/en/curl-ads-launch#stop)Stop
```
curl \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Client-Login: CLIENT_LOGIN' \
  -d '{ "method": "suspend",
  "params": {
    "SelectionCriteria": {
      "Ids": [ID_1,ID_2,...,ID_N]
    }
  }
}' https://api.direct.yandex.com/json/v5/ads

```

##  [](https://yandex.com/dev/direct/doc/en/en/curl-ads-launch#start)Start
```
curl \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Client-Login: CLIENT_LOGIN' \
  -d '{ "method": "resume",
  "params": {
    "SelectionCriteria": {
      "Ids": [ID_1,ID_2,...,ID_N]
    }
  }
}' https://api.direct.yandex.com/json/v5/ads

```

Note
For cURL in Windows, replace all single quotes with double quotes, and escape double quotes in JSON code. For example: `-d "{\"method\"`...
Copied
### Was the article helpful?
YesNo
Previous
[Add tags to an ad URL](https://yandex.com/dev/direct/doc/en/en/curl-ads-keywords-modify)
Next
[Setting bids](https://yandex.com/dev/direct/doc/en/en/curl-bids)
