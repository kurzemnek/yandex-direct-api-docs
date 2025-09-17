---
title: HTTP headers | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/headers
crawled_at: 2025-09-17T15:37:45.968502
---

Request headers
# HTTP headers
  * [Request headers](https://yandex.com/dev/direct/doc/en/en/headers#request)
    * [processingMode](https://yandex.com/dev/direct/doc/en/en/headers#processingmode)
    * [returnMoneyInMicros: false](https://yandex.com/dev/direct/doc/en/en/headers#returnmoneyinmicros-false)
    * [skipReportHeader: true](https://yandex.com/dev/direct/doc/en/en/headers#skipreportheader-true)
    * [skipColumnHeader: true](https://yandex.com/dev/direct/doc/en/en/headers#skipcolumnheader-true)
    * [skipReportSummary: true](https://yandex.com/dev/direct/doc/en/en/headers#skipreportsummary-true)
    * [Accept-Encoding: gzip](https://yandex.com/dev/direct/doc/en/en/headers#accept-encoding-gzip)
  * [Response headers](https://yandex.com/dev/direct/doc/en/en/headers#response)
    * [retryIn](https://yandex.com/dev/direct/doc/en/en/headers#retryin)
    * [reportsInQueue](https://yandex.com/dev/direct/doc/en/en/headers#reportsinqueue)


##  [](https://yandex.com/dev/direct/doc/en/en/headers#request)Request headers
You can specify the following headers in addition to the [Authorization](https://yandex.com/dev/direct/doc/dg/concepts/headers.html#authorization), [Accept-Language](https://yandex.com/dev/direct/doc/dg/concepts/headers.html#accept-language), and [Client-Login](https://yandex.com/dev/direct/doc/dg/concepts/headers.html#client-login) headers:
###  [](https://yandex.com/dev/direct/doc/en/en/headers#processingmode)processingMode
The mode for generating the report: `online`, `offline` or `auto`. If you omit this header, it is interpreted as `auto`. The modes are described in the section [Online and offline reports](https://yandex.com/dev/direct/doc/en/en/mode).
###  [](https://yandex.com/dev/direct/doc/en/en/headers#returnmoneyinmicros-false)returnMoneyInMicros: false
If you specify this header, monetary values in the report are returned in the currency with up to two decimal points. If you omit this header, monetary values are returned as integers – the amount in the currency, multiplied by 1,000,000.
###  [](https://yandex.com/dev/direct/doc/en/en/headers#skipreportheader-true)skipReportHeader: true
Don't include the row with the report name and the date range in the report.
###  [](https://yandex.com/dev/direct/doc/en/en/headers#skipcolumnheader-true)skipColumnHeader: true
Don't include the row with the field names in the report.
###  [](https://yandex.com/dev/direct/doc/en/en/headers#skipreportsummary-true)skipReportSummary: true
Don't include the row with the number of data rows in the report.
###  [](https://yandex.com/dev/direct/doc/en/en/headers#accept-encoding-gzip)Accept-Encoding: gzip
If the header is specified, gzip compression is used.
##  [](https://yandex.com/dev/direct/doc/en/en/headers#response)Response headers
If the report is generated in offline mode, the following header is returned in addition to the [RequestId](https://yandex.com/dev/direct/doc/dg/concepts/headers.html#request-id) header:
###  [](https://yandex.com/dev/direct/doc/en/en/headers#retryin)retryIn
The recommended interval in seconds for checking the report status.
###  [](https://yandex.com/dev/direct/doc/en/en/headers#reportsinqueue)reportsInQueue
The number of offline reports waiting to be generated (maximum of 5 reports per advertiser).
Copied
### Was the article helpful?
YesNo
Previous
[Filtering data](https://yandex.com/dev/direct/doc/en/en/filters)
Next
[Request: report specification](https://yandex.com/dev/direct/doc/en/en/spec)
