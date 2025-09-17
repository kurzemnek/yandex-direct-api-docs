---
title: Handle error 152 “Insufficient points” | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-file_get_contents-points
crawled_at: 2025-09-17T15:46:45.091818
---

Handle error 152 “Insufficient points”
# Handle error 152 “Insufficient points”
PHP version 5 using JSON with the file_get_contents function
In version 5 of the Yandex Direct API, points are awarded to advertisers every 60 minutes, but each advertiser receives points on its own schedule, not necessarily at the beginning of the astronomical hour. The example shows how requests are executed when the first request returns the 152 error code.
For demonstration purposes, it uses the `sleep` function, which allows you to set delays for running the script. The delays are set in seconds in the `set_DELAY` array, so that after the first attempt no more than 5 repeat requests are sent with increasing intervals that cover the next 60 minutes after receiving the first error.
You should preferably design your application to use more reliable approaches for resending requests. You can organize the query execution logic using a task scheduler (such as `cron`) or a queuing system (such as `Gearman`).
```
<?php
//--- Settings ---------------------------------------------------------//
$set_DEBUG = true; // Output of debugging information (html): false - do not output; true - output
$set_DELAY = array(0, 360, 540, 720, 900, 1080); // Array of delays between repeat requests (in seconds)
$err_NOT_ENOUGH_UNITS = 152; // "Insufficient points" error
ini_set('max_execution_time', 5400); // The maximum script execution time is 5400 seconds (90 minutes)
// Settings for buffer contents output used for screen output when using the sleep function
ob_implicit_flush();

//--- Request input data --------------------------------------------//
// Address of the Campaigns service for sending JSON requests (case-sensitive)
$url = 'https://api.direct.yandex.com/json/v5/campaigns';
// OAuth token of the Yandex Direct user who sends the requests
$token = 'TOKEN';
// The login of the advertising agency's client
// This is a required parameter when submitting requests on behalf of an advertising agency
$clientLogin = 'CLIENT_LOGIN';
      
//--- Preparing the request ------------------------------------------------//
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
      'ignore_errors' => true, // Get the response content even if the HTTP response code is not 200
      'header' => $headers,
      'content' => $body
   )
));

//--- Task execution -------------------------------------------------//
/*
Starting the request execution loop. If the first request completed successfully, i.e. it did not return error 152, the list of campaigns is output. 
If the first request fails with this error, repeat requests are made with the delays set in the set_DELAY array.
*/
foreach ($set_DELAY as $currentAttempt => $delay) {
   
      // Executing the request and getting the result
      $result = file_get_contents($url, 0, $streamOptions);
      
      //--- Processing the request result ---------------------//
      // Extracting HTTP headers from the response (if any)
      if (isset($http_response_header)) {
         foreach ($http_response_header as $header) {
            if (preg_match('#HTTP/[0-9\.]+\s+([0-9]+)#', $header, $arr)) {
               $httpStr = $header; // Explanation for the HTTP response code
               $httpCode = intval($arr[1]); // Numeric value of the HTTP response code
            }
            if (preg_match('/RequestId: (\d+)/', $header, $arr)) { 
               $requestId = $arr[1]; // Request ID
            }
            if (preg_match('/Units: (\d+)\/(\d+)\/(\d+)/', $header, $arr)) {
               $unitsSpent = $arr[1]; // Number of points spent
               $unitsAvailable = $arr[2]; // Number of points available
               $unitsLimit = $arr[3]; // Daily limit
            }
         }
      }
      else {
         // The absence of headers indicates a failed request. An error message is displayed.
         echo date("d.m.Y H:i:s > ").'Failed request to the API server';
      }
      
      // Processing the response based on the HTTP return code
      if (isset($httpCode)) {
         // If an HTTP status code of 200 is returned, process the response body
         if ($httpCode == 200) {            
            // Outputting information about points
            if (isset($unitsSpent)) {
               echo date("d.m.Y H:i:s > ")."Points spent on the request: $unitsSpent Currently available: $unitsAvailable Daily limit: $unitsLimit<br>";
            }
            
            // Converting a response from JSON
            $response = json_decode($result);
            
            // If the API server's response contains an error, output it
            if (isset($response->error)) {
               $apiErr = $response->error;
               echo date("d.m.Y H:i:s > ")."API error {$apiErr->error_code}: {$apiErr->error_string} - {$apiErr->error_detail} (RequestId: {$apiErr->request_id})<br>";         
            }
         }
         else { echo date("d.m.Y H:i:s > ").'Error sending the request to the API server: '.$httpStr; }
      }
      
      //--- Outputting debugging information ---------------------------------//
      if ($set_DEBUG) {
         echo "<hr>Request URL: $url<br>";
         echo "Request headers: <pre>".implode($headers, '<br>')."</pre>";
         echo "Request body (JSON): <pre>".json_encode($params, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES)."</pre>";
         if (isset($http_response_header)) { echo "Response headers: <pre>".implode($http_response_header, '<br>')."</pre>"; }
         if (isset($response)) { echo "Response body (JSON): <pre>".json_encode($response, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES)."</pre>"; }
         if (isset($httpCode) and $httpCode != 200) { echo "Response body: <pre>".htmlspecialchars($result)."</pre>"; }
         echo "<hr>";
      }

      //--- Processing the results ----------------------------------------//
      // Outputting the list of campaigns if there is a result
      if (isset($response->result)) {            
         foreach ($response->result->Campaigns as $campaign) {
            echo "{$campaign->Name} (№ {$campaign->Id})<br>";
         }
         
         if ($response->result->LimitedBy) {
            // If the response contains a LimitedBy parameter, it indicates that not all available objects were retrieved. 
            // In this case, send additional requests to retrieve all objects.
            // Details on paginated selections - https://tech.yandex.com/direct/doc/dg/best-practice/get-docpage/#page
            echo '<br>Not all objects received.';
         }
      }

      //--- Actions when error 152 "Insufficient points" occurs or doesn't occur ---//
      if (isset($apiErr->error_code) and $apiErr->error_code == $err_NOT_ENOUGH_UNITS) {
         // If the set_DELAY array has more values than the current iteration, set a delay before the next iteration of the loop
         if (isset($set_DELAY[$currentAttempt+1])) {
            unset ($apiErr); // Delete the variable with the error information
            echo date("d.m.Y H:i:s > ")."Repeat request in ".$set_DELAY[$currentAttempt+1]." seconds<br>";
            sleep ($set_DELAY[$currentAttempt+1]);
         }
      }
      // If error 152 "Insufficient points" didn't occur, consider the task completed and exit the script
      else { die(); }
}
?>

```

Copied
### Was the article helpful?
YesNo
Previous
[Create ads](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-ads)
Next
[PHP examples for JSON](https://yandex.com/dev/direct/doc/en/en/php5-json-curl)
