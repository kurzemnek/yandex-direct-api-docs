---
title: Get statistics for a selection of rows | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-curl-stat2
crawled_at: 2025-09-17T15:47:12.758941
---

Get statistics for a selection of rows
# Get statistics for a selection of rows
PHP 5 using JSON with the cURL library
This example shows a request to the [Reports](https://yandex.com/dev/direct/docreports/reports.md) service, along with the result processing and output. The mode for generating the report is selected automatically. If the report is added to the offline queue, the repeat requests are executed.
The report contains statistics on impressions, clicks, and expenditures for all the advertiser's campaigns for the past month, with grouping by date, campaign name, and ad ID. The report filters the rows with the most expensive clicks, where the number of clicks is lower than the set value and the CPC is higher than the set value.
To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login. In the body of the request message, specify the floor for the number of clicks and the CPC, as well as a report name that is unique among the advertiser's reports.
```
<?php

// Settings for buffer contents output used for screen output
// when using the sleep function
ob_implicit_flush();

//--- Input data ---------------------------------------------------//
// Reports service address used to send JSON requests (case-sensitive)
$url = 'https://api.direct.yandex.com/json/v5/reports';
// OAuth token of the Yandex Direct user who sends the requests
$token = 'TOKEN';
// The login of the advertising agency's client
// This is a required parameter when submitting requests on behalf of an advertising agency
$clientLogin = 'CLIENT_LOGIN';

//--- Preparing the request -----------------------------------------------//
// Creating the request body
$params = [
    "params" => [
        "SelectionCriteria" => [
            "Filter" => [
                [
                    "Field" => "Clicks",
                    "Operator" => "LESS_THAN",
                    "Values" => ["CLICK_FLOOR"]
                ],
                [
                    "Field" => "Cost",
                    "Operator" => "GREATER_THAN",
                    "Values" => ["CPC_FLOOR"]
                ]
            ]],
        "FieldNames" => ["Date", "CampaignName", "AdId", "Impressions", "Clicks", "Cost"],
        "ReportName" => "REPORT_NAME",
        "ReportType" => "AD_PERFORMANCE_REPORT",
        "DateRangeType" => "LAST_MONTH",
        "Format" => "TSV",
        "IncludeVAT" => "NO",
        "IncludeDiscount" => "NO"
    ]
];

// Converting input parameters to JSON
$body = json_encode($params);

// Creating HTTP headers for the request
$headers = array(
    // OAuth token. The word “Bearer” is mandatory
    "Authorization: Bearer $token",
    // The login of the advertising agency's client
    "Client-Login: $clientLogin",
    // Language of responses
    "Accept-Language: ru", 
    // Report generation mode
    "processingMode: auto",
    // Format for monetary values in the report
    // "returnMoneyInMicros: false",
    // Don't include the row with the report name and the date range in the report
    // "skipReportHeader: true",
    // Don't include the row with field names in the report
    // "skipColumnHeader: true",
    Don't include the row with the number of data rows in the report
    // "skipReportSummary: true" 

).

// Initializing cURL
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_POSTFIELDS, $body);

/*
To ensure full-scale HTTPS utilization, enable SSL certificate verification for the Yandex Direct API server
To enable verification, set the CURLOPT_SSL_VERIFYPEER to true. Uncomment the line that contains CURLOPT_CAINFO and specify the path to the local copy of the root SSL certificate.
*/
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
// curl_setopt($curl, CURLOPT_CAINFO, getcwd().'\CA.pem');

curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_HEADER, true);
curl_setopt($curl, CURLINFO_HEADER_OUT, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

// --- Starting the request execution loop ---
// If HTTP code 200 is returned, output the report contents
// If HTTP code 201 or 202 is returned, send repeat requests
while (true) {

    $result = curl_exec($curl);

    if (!$result) {

        echo ('cURL error: '.curl_errno($curl).' - '.curl_error($curl));

        break;

    } else {

        // Separating HTTP headers from the response body
        $responseHeadersSize = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
        $responseHeaders = substr($result, 0, $responseHeadersSize);
        $responseBody = substr($result, $responseHeadersSize);

        // Getting the HTTP status code
        $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        // Extracting HTTP response headers
        // Request ID
        $requestId = preg_match('/RequestId: (\d+)/', $responseHeaders, $arr) ? $arr[1] : false;
        // The recommended interval in seconds for checking the report status.
        $retryIn = preg_match('/retryIn: (\d+)/', $responseHeaders, $arr) ? $arr[1] : 60;

        if ($httpCode == 400) {

            echo "Invalid request parameters, or the report queue has reached its limit<br>";
            echo "RequestId: {$requestId}<br>";
            echo "JSON code for the request:<br>{$body}<br>";
            echo "JSON code for the server response:<br>{$responseBody}<br>";

            break;

        } elseif ($httpCode == 200) {

            echo "Report created<br>";
            echo "RequestId: {$requestId}<br>";
            echo $responseBody;

            break;

        } elseif ($httpCode == 201) {

            echo "Report added to the offline queue<br>";
            echo "Request will be resent in {$retryIn} seconds<br>";
            echo "RequestId: {$requestId}<br>";

            sleep($retryIn);

        } elseif ($httpCode == 202) {

            echo "The report is generated in offline mode.<br>";
            echo "Request will be resent in {$retryIn} seconds<br>";
            echo "RequestId: {$requestId}<br>";

            sleep($retryIn);

        } elseif ($httpCode == 500) {

            echo "Error occurred when creating the report. Please repeat the request again later.<br>";
            echo "RequestId: {$requestId}<br>";
            echo "JSON code for the server response:<br>{$responseBody}<br>";

            break;

        } elseif ($httpCode == 502) {

            echo "Exceeded the server limit on report creation time.<br>";
            echo "Please try changing the request parameters: reduce the time period and the amount of data requested.<br>";
            echo "RequestId: {$requestId}<br>";

            break;

        } else {

            echo "Unexpected error.<br>";
            echo "RequestId: {$requestId}<br>";
            echo "JSON code for the request:<br>{$body}<br>";
            echo "JSON code for the server response:<br>{$responseBody}<br>";

            break;

        }
    }
}

curl_close($curl);
?>


```

### Was the article helpful?
YesNo
Previous
[Get statistics for any dates](https://yandex.com/dev/direct/doc/en/en/php5-curl-stat1)
Next
[PHP examples for SOAP](https://yandex.com/dev/direct/doc/en/en/php5-soap)
