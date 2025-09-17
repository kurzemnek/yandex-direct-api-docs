---
title: Online and offline reports | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/mode
crawled_at: 2025-09-17T15:38:20.934594
---

Choosing the mode
# Online and offline reports
  * [Choosing the mode](https://yandex.com/dev/direct/doc/en/en/mode#choosing-the-mode)
    * [processingMode: online](https://yandex.com/dev/direct/doc/en/en/mode#processingmode-online)
    * [processingMode: offline](https://yandex.com/dev/direct/doc/en/en/mode#processingmode-offline)
    * [processingMode: auto](https://yandex.com/dev/direct/doc/en/en/mode#processingmode-auto)
  * [How to check whether an offline report is ready](https://yandex.com/dev/direct/doc/en/en/mode#how-to-check-whether-an-offline-report-is-ready)
    * [Learn more](https://yandex.com/dev/direct/doc/en/en/mode#learn-more)


##  [](https://yandex.com/dev/direct/doc/en/en/mode#choosing-the-mode)Choosing the mode
The Yandex Direct server can create a report in either online or offline mode, depending on the parameters and the amount of data in the report. You can set the mode in the HTTP processingMode header in the request:
###  [](https://yandex.com/dev/direct/doc/en/en/mode#processingmode-online)processingMode: online
This generates a report in online mode. If the report is created successfully, it is returned in the response body. If the report can't be generated in online mode, an error is returned.
###  [](https://yandex.com/dev/direct/doc/en/en/mode#processingmode-offline)processingMode: offline
This puts the request in a queue to generate the report in offline mode. To check whether the report is ready, send repeated requests with the same parameters (see How to check whether an offline report is ready). The recommended interval for checking the report status is shown in the HTTP retryIn header in the response. If the report is created successfully, the server returns the report in the response body.
###  [](https://yandex.com/dev/direct/doc/en/en/mode#processingmode-auto)processingMode: auto
The server automatically selects the mode for generating the report. If the report is created successfully in online mode, it is returned in the response body. If the report can't be created in online mode, it is added to the offline queue. Your application must support both modes.
If you omit this header, it is interpreted as auto.
Note
Reports with the SEARCH_QUERY_PERFORMANCE_REPORT type can only be generated in offline mode.
##  [](https://yandex.com/dev/direct/doc/en/en/mode#how-to-check-whether-an-offline-report-is-ready)How to check whether an offline report is ready
Steps for `auto` mode:
  1. Send a request to generate a report. Specify the HTTP `processingMode: auto` header in the request.
The server response contains one of the following HTTP codes:
     * 200 – The report was created successfully in online mode and returned in the response body.
     * 201 – The report was successfully placed in the queue to generate in offline mode. Go to Step 2.
     * 400 – The request parameters contain an error, or the request exceeded the limit on the number of requests or reports in the queue. In this case, review the error message, correct the request, and resend it.
     * 500 — A server error when creating the report. If this is the first time you have received an error for this report, try again. If the error persists, contact the support service.
  2. Wait the amount of time specified in the retryIn response header (or as long as you choose), then re-send the request with the same parameters.
The server response contains one of the following HTTP codes:
     * 200 — The report was created successfully and returned in the response body.
     * 202 — Report creation isn't finished yet. Repeat Step 2.
     * 500 — A server error when creating the report. If this is the first time a server error has occurred for this report, go back to Step 1 and try generating the report again. If the error persists, contact the support service.


###  [](https://yandex.com/dev/direct/doc/en/en/mode#learn-more)Learn more
[Response codes and error codes](https://yandex.com/dev/direct/doc/en/en/codes)
Copied
### Was the article helpful?
YesNo
Previous
[Report content](https://yandex.com/dev/direct/doc/en/en/report-format)
Next
[Data freshness](https://yandex.com/dev/direct/doc/en/en/actual)
