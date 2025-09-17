---
title: Creating ads | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-soap-ads
crawled_at: 2025-09-17T15:47:03.904876
---

Creating ads
# Creating ads
PHP version 5 using SOAP with the SoapClient class
This example shows a request using the [{#T}](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.md).[{#T}](https://yandex.com/dev/direct/doc/ref-v5/ads/add.md) method, along with the result processing and output. To use this example, make sure that the input data specifies the OAuth token and the ID of the group where you want to create the new ad. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
<?php
ini_set("soap.wsdl_cache_enabled", "0");

//--- Input data ----------------------------------------------------//
// Address of the WSDL description for the Ads service (case-sensitive)
$wsdlUrl = 'https://api.direct.yandex.com/v5/ads?wsdl';
// OAuth token of the Yandex Direct user who sends the requests
$token = 'TOKEN';
// The login of the advertising agency's client
// This is a required parameter when submitting requests on behalf of an advertising agency
$clientLogin = 'CLIENT_LOGIN';
// ID of the group where you want to create a new ad.
$adGroupId = GROUP_ID;

//--- Request preparation and execution -----------------------------------//
// Creating the stream context: Setting HTTP headers
$streamOptions = stream_context_create(array(
   'http' => array(
      'header' => "Authorization: Bearer $token"."\r\n".    // OAuth token. The word “Bearer” is mandatory
                  "Client-Login: $clientLogin"."\r\n".      // Login of the advertising agency's client
                  "Accept-Language: ru"                     // Language of response messages
   ),
   /*
   // To ensure full-scale HTTPS utilization, enable SSL certificate verification for the Yandex Direct API server
   'ssl' => array(
      'verify_peer' => true,
      'cafile' => getcwd().DIRECTORY_SEPARATOR.'CA.pem' // Path to the local copy of the root SSL certificate
   )
   */
));

// Initializing the SOAP client
$client = new SoapClient($wsdlUrl,
   array(
      'trace'             => true,
      'exceptions'        => false,
      'features'          => SOAP_SINGLE_ELEMENT_ARRAYS,
      'cache_wsdl'        => WSDL_CACHE_NONE,
      'encoding'          => 'UTF-8',
      'stream_context'    => $streamOptions
    )
).

// Parameters for the request to the Yandex Direct API server
$params = array(
   'Ads' => array(
      array(
         'AdGroupId' => $adGroupId,
         // Ad parameters
         'TextAd' => array(
            'Title' => 'Ad title',
            'Text' => 'Ad text',
            'Mobile' => 'NO',
            'Href' => 'http://www.yandex.com'
         )
      )
   )
).

// Executing the request using the add method in the Ads service and receiving the response
$result = $client->add($params);

//--- Processing the request result ---------------------------//
if (is_soap_fault($result)) {
   $error = "SOAP Fault: faultcode: {$result->faultcode}, faultstring: {$result->faultstring}";
   if (isset($result->detail->FaultResponse)) { 
      $apiErr = $result->detail->FaultResponse;
      $error .= " detail: {$apiErr->errorCode} - {$apiErr->errorDetail} (RequestId: {$apiErr->requestId})";
   }
   echo $error;
}
else {
   // Extracting HTTP response headers: RequestId (the request's ID) and Units (information about points)
   $headers = explode("\r\n", $client->__getLastResponseHeaders());
   foreach ($headers as $header) {
      if (preg_match('/(RequestId|Units):/', $header)) { echo "$header<br>"; }
   }

   // Result output
   // Processing all items in the AddResults array, where each item corresponds to a single ad
   foreach ($result->AddResults as $item) {
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

//--- Debugging information ---------------------------------------------//
//echo "<hr>Request headers:<pre>".$client->__getLastRequestHeaders()."</pre>";
//echo "Request:<pre>".htmlspecialchars($client->__getLastRequest())."</pre>";
//echo "Response headers:<pre>".$client->__getLastResponseHeaders()."</pre>";
//echo "Response:<pre>".htmlspecialchars($client->__getLastResponse())."</pre>";
?>

```

### Was the article helpful?
YesNo
Previous
[Get campaigns](https://yandex.com/dev/direct/doc/en/en/php5-soap-campaigns)
Next
[Examples for Python 2 or 3](https://yandex.com/dev/direct/doc/en/en/python3)
