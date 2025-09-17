---
title: PHP examples for JSON | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-json-curl
crawled_at: 2025-09-17T15:48:46.235034
---

Verify the SSL certificate
# PHP examples for JSON
PHP 5 using JSON with the cURL library
  * [Get campaigns](https://yandex.com/dev/direct/doc/en/en/php5-curl-campaigns)
  * [Create ads](https://yandex.com/dev/direct/doc/en/en/php5-curl-ads)
  * [Get statistics for any dates](https://yandex.com/dev/direct/doc/en/en/php5-curl-stat1)
  * [Get statistics for a selection of rows](https://yandex.com/dev/direct/doc/en/en/php5-curl-stat2)


##  [](https://yandex.com/dev/direct/doc/en/en/php5-json-curl#php-ssl)Verify the SSL certificate
When using the SSL protocol with PHP prior to version 5.6.0, verification of the remote server's SSL certificate might be disabled by default, which may lead to man-in-the-middle attacks. If verification is enabled, you may need to specify the path to the certification authority's root certificate.
We recommend enabling verification and, if necessary, setting the path to the CA root certificate file on the local computer.
The Yandex Direct API servers use an SSL certificate issued by the CERTUM certification authority. You can download the root certificate from the CA's website: **Certum root certificates** and click the link **Download: PEM** (for the `CA.pem` file).
Each example includes a section with instructions on enabling SSL certificate verification and setting the path to the root certificate.
Copied
### Was the article helpful?
YesNo
Previous
[Handle error 152 Insufficient points](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-points)
Next
[Get campaigns](https://yandex.com/dev/direct/doc/en/en/php5-curl-campaigns)
