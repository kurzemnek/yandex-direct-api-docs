---
title: Get campaigns | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-curl-campaigns
crawled_at: 2025-09-17T15:46:49.929932
---

Get campaigns
# Get campaigns
PHP 5 using JSON with the cURL library
This example shows a request using the [{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html).[{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/get.html) method, along with the result processing and output. To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
<?php
//--- Input data -------------------------------------------------------------------------//
// Address of the Campaigns service for sending JSON requests (case-sensitive)
$url = 'https://api.direct.yandex.com/json/v5/campaigns';
// OAuth token of the Yandex Direct user who sends the requests
$token = 'TOKEN';
// The login of the advertising agency's client
// This is a required parameter when submitting requests on behalf of an advertising agency
$clientLogin = 'CLIENT_LOGIN';

//--- Request preparation and execution -----------------------------------//
// Setting HTTP headers for the request
$headers = array(
    "Authorization: Bearer $token",                   // Oauth token. The word “Bearer” is mandatory
    "Client-Login: $clientLogin",                     // Login of the advertising agency's client
    "Accept-Language: ru",                            // Language of response messages
    "Content-Type: application/json; charset=utf-8"   // Data type and request encoding
).

// Parameters for the request to the Yandex Direct API server
$params = array(
    'method' => 'get',                                // Method of the Campaigns service
    'params' => array(
        'SelectionCriteria' => (object) array(),      // Criteria for filtering campaigns. To get all campaigns, leave it empty
        'FieldNames' => array('Id', 'Name')           // Names of the parameters you want to get
    )
).
// Converting input parameters to JSON
$body = json_encode($params, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

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
//curl_setopt($curl, CURLOPT_CAINFO, getcwd().'\CA.pem');

curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_HEADER, true);
curl_setopt($curl, CURLINFO_HEADER_OUT, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

// Executing the request and getting the result
$result = curl_exec($curl);

//--- Processing the request result ---------------------------//
if(!$result) { echo ('Ошибка cURL: '.curl_errno($curl).' - '.curl_error($curl)); }
else {
   // Separating HTTP headers from the response body
   $responseHeadersSize = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
   $responseHeaders = substr($result, 0, $responseHeadersSize);
   $responseBody = substr($result, $responseHeadersSize);
    
   if (curl_getinfo($curl, CURLINFO_HTTP_CODE) != 200) { echo "HTTP error: ".curl_getinfo($curl, CURLINFO_HTTP_CODE); }
   else {
      // Converting a response from JSON
      $responseBody = json_decode($responseBody);

      if (isset($responseBody->error)) {
         $apiErr = $responseBody->error;
         echo "API error {$apiErr->error_code}: {$apiErr->error_string} - {$apiErr->error_detail} (RequestId: {$apiErr->request_id})";
      }
      else {
         // Extracting HTTP response headers: RequestId (the request's ID) and Units (information about points)
         $responseHeadersArr = explode("\r\n", $responseHeaders);
         foreach ($responseHeadersArr as $header) {
            if (preg_match('/(RequestId|Units):/', $header)) { echo "$header <br>"; }
         }

         // Output of the ad campaign list
         foreach ($responseBody->result->Campaigns as $campaign) {
            echo "Advertising campaign: {$campaign->Name} ({$campaign->Id})<br>";
         }
      }
   }
}

//--- Debugging information ---------------------------------------------//
//echo "<hr>Request headers: <pre>".curl_getinfo($curl, CURLINFO_HEADER_OUT)."</pre>";
//echo "Request: <pre>".json_encode($params, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES)."</pre>";
//echo "Response headers: <pre>".$responseHeaders."</pre>";
//echo "Response: <pre>".json_encode($responseBody, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES)."</pre>";

curl_close($curl);
?>

```

### Was the article helpful?
YesNo
Previous
[PHP examples for JSON](https://yandex.com/dev/direct/doc/en/en/php5-json-curl)
Next
[Create ads](https://yandex.com/dev/direct/doc/en/en/php5-curl-ads)
