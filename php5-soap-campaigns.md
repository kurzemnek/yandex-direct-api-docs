---
title: Get campaigns | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-soap-campaigns
crawled_at: 2025-09-17T15:46:59.291689
---

Get campaigns
# Get campaigns
PHP version 5 using SOAP with the SoapClient class
This example shows a request using the [{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html).[{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/get.html) method, along with the result processing and output. To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
<?php
ini_set("soap.wsdl_cache_enabled", "0");

//--- Input data -------------------------------------------------------------------------//
// Address of the WSDL description for the Campaigns service (case-sensitive)
$wsdlUrl = 'https://api.direct.yandex.com/v5/campaigns?wsdl';
// OAuth token of the Yandex Direct user who sends the requests
$token = 'TOKEN';
// The login of the advertising agency's client
// This is a required parameter when submitting requests on behalf of an advertising agency
$clientLogin = 'CLIENT_LOGIN';

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
   "SelectionCriteria" => (object) array(),     // Criteria for filtering campaigns. To get all campaigns, leave it empty
   "FieldNames" => array ('Id', 'Name')         // Names of the parameters that you want to retrieve
).

// Executing the request using the get method in the Campaigns service and receiving the response
$result = $client->get($params);

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
   
   // Output of the ad campaign list
   foreach ($result->Campaigns as $row) { echo "Ad campaign: {$row->Name} ({$row->Id})<br>"; }
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
[PHP examples for SOAP](https://yandex.com/dev/direct/doc/en/en/php5-soap)
Next
[Create ads](https://yandex.com/dev/direct/doc/en/en/php5-soap-ads)
