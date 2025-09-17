---
title: How to generate a report | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/how-to
crawled_at: 2025-09-17T15:36:02.724968
---

How to generate a report
# How to generate a report
  1. Prepare a request and send it to the `Reports` service.
In the `Authorization` header, specify the OAuth token that you received for the user that has rights to the campaigns that the report is for. For the full list of headers, see the section [HTTP headers](https://yandex.com/dev/direct/doc/en/en/headers).
In the request body, specify values for the main parameters, depending on which data you want to get:
     * What [time period](https://yandex.com/dev/direct/doc/en/en/period) to create the report for, and what periods to aggregate data for.
     * What [type of report](https://yandex.com/dev/direct/doc/en/en/type) fits your needs.
     * Which [fields](https://yandex.com/dev/direct/doc/en/en/fields) (columns) to show in the report.
     * How to display [monetary values](https://yandex.com/dev/direct/doc/en/en/money).
     * Which [filters](https://yandex.com/dev/direct/doc/en/en/filters) to use for filtering rows.
For a complete list of input parameters, see the section [Request: report specification](https://yandex.com/dev/direct/doc/en/en/spec).
  2. Reports that contain a relatively small amount of data are generated in online mode. In this case, you immediately get a response with an HTTP code of 200 and the report in the HTTP message body data.
Reports that contain a large volume of data and certain types of reports are generated in offline mode. In this case, you get an HTTP code of 201 in response.
For more information on the flow for requests and responses, see [Online and offline reports](https://yandex.com/dev/direct/doc/en/en/mode).
  3. To get a report that is generated in offline mode, wait some time and then repeat the request with the same parameters.
If the report isn't ready yet, you receive the response code 202.
If the report is ready, you receive the response code 200 with the report in the response body.


For a sample request and sample report, see [Example: clicks and cost](https://yandex.com/dev/direct/doc/en/en/example).
Copied
### Was the article helpful?
YesNo
Previous
[Campaign settings (Option parameter)](https://yandex.com/dev/direct/doc/en/en/annex/campaign-options)
Next
[Report period](https://yandex.com/dev/direct/doc/en/en/period)
