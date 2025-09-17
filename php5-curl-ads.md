---
title: Creating ads | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-curl-ads
crawled_at: 2025-09-17T15:46:54.732346
---

Creating ads
# Creating ads
PHP 5 using JSON with the cURL library
This example shows a request using the [{#T}](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.md).[{#T}](https://yandex.com/dev/direct/doc/ref-v5/ads/add.md) method, along with the result processing and output. To use this example, make sure that the input data specifies the OAuth token and the ID of the group where you want to create the new ad. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
<?php
//--- Input data ----------------------------------------------------//
// Address of the Ads service for sending JSON requests (case-sensitive)
$url = 'https://api.direct.yandex.com/json/v5/ads';
// OAuth token of the Yandex Direct user who sends the requests
$token = 'TOKEN';
// The login of the advertising agency's client
// This is a required parameter when submitting requests on behalf of an advertising agency
$clientLogin = 'CLIENT_LOGIN';
// ID of the group where you want to create a new ad.
$adGroupId = GROUP_ID;

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
   'method' => 'add',                                 // Used method
   'params' => array(
      'Ads' => array(
         array(
            'AdGroupId' => $adGroupId,
            'TextAd' => array(                        // Ad parameters
               'Title' => 'Ad title',
               'Text' => 'Ad text',
               'Mobile' => 'NO',
               'Href' => 'http://www.yandex.com'
            )
         )
      )
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

   if (curl_getinfo($curl, CURLINFO_HTTP_CODE) != 200) { echo "HTTP ошибка: ".curl_getinfo($curl, CURLINFO_HTTP_CODE); }
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
 
         // Result output
         // Processing all items in the AddResults array, where each item corresponds to a single ad
         foreach ($responseBody->result->AddResults as $item) {
            // Processing nested elements (these may be Errors or Id, or possibly Warnings)
            foreach ($item as $key => $value) {
               // If the Errors array is present, the ad wasn't created due to one or more errors
               if ($key == 'Errors') {
                  foreach ($value as $errItem) { echo "Error: {$errItem->Code} - {$errItem->Message} ({$errItem->Details})<br>"; }
               }
               else {
                  // If the Warnings array is present, the ad was created, but with a warning (there may be multiple warnings)
                  if ($key == 'Warnings') {
                     foreach ($value as $warItem) { echo "Warning: {$warItem->Code} - {$warItem->Message} ({$warItem->Details})<br>"; }
                  }
                  echo "Created ad #{$value}<br>";
               }
            }
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
[Get campaigns](https://yandex.com/dev/direct/doc/en/en/php5-curl-campaigns)
Next
[Get statistics for any dates](https://yandex.com/dev/direct/doc/en/en/php5-curl-stat1)
