---
title: Getting a token | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3-requests-token
crawled_at: 2025-09-17T15:51:05.696142
---

Installing additional libraries
# Getting a token
  * [Installing additional libraries](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#python-modules)
  * [Callback URL](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#callback-uri)
  * [Procedure](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#get-token)
  * [Run the script](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#webserver)
  * [Script code](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#code)


Python 2 or 3 with the Flask and Requests libraries
This example shows getting an OAuth token in the web service. Recommendations for other types of applications (desktop or mobile) are given in the [Yandex OAuth documentation](https://tech.yandex.com/oauth/doc/dg/)[Yandex OAuth documentation](https://tech.yandex.com/oauth/doc/dg/).
##  [](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#python-modules)Installing additional libraries
You can use the pip utility for installing libraries (Flask, Requests, Suds, PyXB, and others):
```
pip install %package_name%

```

The pip utility is included in Python 2 beginning with version 2.7.9, and in Python 3 beginning with version 3.4. If you are using an earlier version of Python, you need to install pip. For example, you can use the script 
For more information, see 
##  [](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#callback-uri)Callback URL
When registering or editing application parameters on the Yandex.OAuth service, you must set the **Callback URL** to the URL of the script that is receiving the token. For example:
```
 https://site.ru/get_token

```

##  [](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#get-token)Procedure
The token request requires specifying the application ID and password that were generated during registration on the Yandex.OAuth service.
  1. The application takes the user to the access request page using a link in the format
```
https://oauth.yandex.com/authorize?response_type=code&client_id=APPLICATION_ID

```

On the page that opens, the user clicks **Allow**.
  2. Yandex.OAuth performs a redirect to the address from **Callback URL**. In addition, the `code` parameter is appended to the address. For example:
```
http://site.ru/get_token?code=AUTHORIZATION_CODE

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


##  [](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#webserver)Run the script
Flask allows you to specify just the IP address and port to run the script on. There are several options for running the script:
  * Run the application on a public IP address (one that other devices on the internet can see). This IP address must be specified for your domain in DNS, and the application must be running on the relevant port (443 for HTTPS).
  * Use a web server for proxying requests. For example, you can use Nginx with the following configuration:
```
server {
listen 443;

# Specify the domain from the Callback URL field
server_name site.ru;

access_log  /var/log/nginx/access.log;
error_log  /var/log/nginx/error.log;

location /get_token {
proxy_pass         http://127.0.0.1:8000/;
proxy_redirect     off;

proxy_set_header   Host                 $host;
proxy_set_header   X-Real-IP            $remote_addr;
proxy_set_header   X-Forwarded-For     $proxy_add_x_forwarded_for;
proxy_set_header   X-Forwarded-Proto    $scheme;
}
}

```

The script code shown below specifies the launch parameters for this configuration.


For more information, see 
##  [](https://yandex.com/dev/direct/doc/en/en/python3-requests-token#code)Script code
To use this example, specify the application ID and password.
```
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, redirect
from requests import post

# The URL encoding method used in both Python 3 and Python 2
import sys

if sys.version_info < (3, 0):  # Python2.x
    from urllib import urlencode
else:  # Python3.x
    from urllib.parse import urlencode

# Application ID
client_id = 'APPLICATION_ID'
# Application password
client_secret = 'APPLICATION_PASSWORD'
# Yandex OAuth server address
baseurl = 'https://oauth.yandex.com/'

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('code', False):
        # If the script is called with the "code" parameter specified in the URL,
        # a request to get a token is executed
        print(request.args)
        print(request.data)
        data = {
            'grant_type': 'authorization_code',
            'code': request.args.get('code'),
            'client_id': client_id,
            'client_secret': client_secret
        }
        data = urlencode(data)
        # The token must be saved and used in requests to the Yandex Direct API
        return jsonify(post(baseurl + "token", data).json())
    else:
        If the script is called without the "code" parameter,
        # the user is redirected to the access request page
        return redirect(baseurl + "authorize?response_type=code&client_id={}".format(client_id))


if __name__ == '__main__':
    # Debugging information
    # app.debug = True
    Start the web server accessible on port 8000
    app.run(host='127.0.0.1', port=8000)

```

Copied
### Was the article helpful?
YesNo
Previous
[Examples for Python 2 or 3](https://yandex.com/dev/direct/doc/en/en/python3)
Next
[Python examples for JSON](https://yandex.com/dev/direct/doc/en/en/python3-json)
