---
title: Get campaigns | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-file_get_contents-campaings
crawled_at: 2025-09-17T15:46:34.844837
---

Get campaigns
# Get campaigns
PHP version 5 using JSON with the file_get_contents function
This example shows a request using the [Campaigns](https://yandex.com/dev/direct/docref-v5/campaigns/campaigns.md).[get](https://yandex.com/dev/direct/docref-v5/campaigns/get.md) method, along with the result processing and output. To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
<?php
//--- Input data ----------------------------------------------------//
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
   "Authorization: Bearer $token",                    // Oauth token. The word “Bearer” is mandatory
   "Client-Login: $clientLogin",                      // Login of the advertising agency's client
   "Accept-Language: ru",                             // Language for response messages
   "Content-Type: application/json; charset=utf-8"    // Data type and request encoding
).

// Parameters for the request to the Yandex Direct API server
$params = array(
   'method' => 'get',                                 // Method of the Campaigns service
   'params' => array(
      'SelectionCriteria' => (object) array(),      // Criteria for filtering campaigns. To get all campaigns, leave it empty
      'FieldNames' => array('Id', 'Name')             // Names of the parameters that you want to retrieve
   )
).
// Converting input parameters to JSON
$body = json_encode($params, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

// Creating the stream context: Setting HTTP headers and the body of the request message
$streamOptions = stream_context_create(array(
   'http' => array(
      'method' => 'POST',
      'header' => $headers,
      'content' => $body
   ),
   /*
   // To ensure full-scale HTTPS utilization, enable SSL certificate verification for the Yandex Direct API server
   'ssl' => array(
      'verify_peer' => true,
      'cafile' => getcwd().DIRECTORY_SEPARATOR.'CA.pem' // Path to the local copy of the root SSL certificate
   )
   */ 
));

// Executing the request and getting the result
$result = file_get_contents($url, 0, $streamOptions);

//--- Processing the request result ---------------------------//
if ($result === false) { echo "Request execution error!"; }
else {
   // Converting a response from JSON
   $result = json_decode($result);

   if (isset($result->error)) {
      $apiErr = $result->error;
      echo "API error {$apiErr->error_code}: {$apiErr->error_string} - {$apiErr->error_detail} (RequestId: {$apiErr->request_id})";
   }
   else {
      // Extracting HTTP response headers: RequestId (the request's ID) and Units (information about points)
      foreach ($http_response_header as $header) {
         if (preg_match('/(RequestId|Units):/', $header)) { echo "$header <br>"; }
      }

      // Output of the ad campaign list
      foreach ($result->result->Campaigns as $campaign) {
         echo "Advertising campaign: {$campaign->Name} ({$campaign->Id})<br>";
      }
   }   
}

//--- Debugging information ---------------------------------------------//
//echo "<hr>Request headers: <pre>".implode($headers, '<br>')."</pre>";
//echo "Request: <pre>".json_encode($params, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES)."</pre>";
//echo "Response headers: <pre>".implode($http_response_header, '<br>')."</pre>";
//echo "Response: <pre>".json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES)."</pre>";
?>

```

### Was the article helpful?
YesNo
Previous
[PHP examples for JSON](https://yandex.com/dev/direct/doc/en/en/php5-json-file_get_contents)
Next
[Create ads](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-ads)
