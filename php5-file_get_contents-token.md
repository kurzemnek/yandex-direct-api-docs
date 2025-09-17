---
title: Getting a token | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/php5-file_get_contents-token
crawled_at: 2025-09-17T15:46:29.829840
---

Callback URL
# Getting a token
  * [Callback URL](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-token#callback-uri)
  * [Procedure](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-token#get-token)
  * [Script code](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-token#code)


PHP 5 using the file_get_contents function
This example shows getting an OAuth token in the web service. Recommendations for other types of applications (desktop or mobile) are given in the [Yandex OAuth documentation](https://tech.yandex.com/oauth/doc/dg/)[Yandex OAuth documentation](https://tech.yandex.com/oauth/doc/dg/).
##  [](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-token#callback-uri)Callback URL
When registering or editing application parameters on the Yandex.OAuth service, you must set the **Callback URL** to the URL of the script that is receiving the token. For example:
```
 https://site.ru/get_token.php

```

The code of the script is provided below.
##  [](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-token#get-token)Procedure
The token request requires specifying the application ID and password that were generated during registration on the Yandex.OAuth service.
  1. The application takes the user to the access request page using a link in the format
```
https://oauth.yandex.com/authorize?response_type=code&client_id=APPLICATION_ID

```

On the page that opens, the user clicks **Allow**.
  2. Yandex.OAuth performs a redirect to the address from **Callback URL**. In addition, the `code` parameter is appended to the address. For example:
```
http://site.ru/get_token.php?code=AUTHORIZATION_CODE

```

  3. The script sends a POST request to _https://oauth.yandex.com/token_ , passing the following parameters:
     * `grant_type = authorization_code`
     * `code` = AUTHORIZATION_CODE
     * `client_id` = APPLICATION_ID
     * `client_secret` = APPLICATION_PASSWORD
  4. Yandex.OAuth sends a response in JSON format. The `access_token` key contains the OAuth token. For example:
```
{"access_token": "0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f"}

```

The received token must be saved and used in requests to the Yandex Direct API.


##  [](https://yandex.com/dev/direct/doc/en/en/php5-file_get_contents-token#code)Script code
To use this example, specify the application ID and password.
```
<?php
// Application ID
$client_id = 'APPLICATION_ID'; 
// Application password
$client_secret = 'APPLICATION_PASSWORD';

// If the script is called with the "code" parameter specified in the URL,
// a request to get a token is executed
if (isset($_GET['code']))
  {
    // Forming parameters (the body) of a POST request specifying the authorization code
    $query = array(
      'grant_type' => 'authorization_code',
      'code' => $_GET['code'],
      'client_id' => $client_id,
      'client_secret' => $client_secret
    ).
    $query = http_build_query($query);

    // Forming headers for the POST request
    $header = "Content-type: application/x-www-form-urlencoded";

    // Executing the POST request and outputting the result
    $opts = array('http' =>
      array(
      'method'  => 'POST',
      'header'  => $header,
      'content' => $query
      ) 
    ).
    $context = stream_context_create($opts);
    $result = file_get_contents('https://oauth.yandex.com/token', false, $context);
    $result = json_decode($result);

    // The token must be saved and used in requests to the Yandex Direct API
    echo $result->access_token;
  }
// If the script is called without the "code" parameter,
// the user is shown a link to the access request page
  else 
    {
      echo '<a href="https://oauth.yandex.com/authorize?response_type=code&client_id='.$client_id.'">Страница запроса доступа</a>';
    }
?>

```

Copied
### Was the article helpful?
YesNo
Previous
[Examples in PHP 5](https://yandex.com/dev/direct/doc/en/en/php5)
Next
[PHP examples for JSON](https://yandex.com/dev/direct/doc/en/en/php5-json-file_get_contents)
