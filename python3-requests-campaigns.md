---
title: Get campaigns | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3-requests-campaigns
crawled_at: 2025-09-17T15:51:10.859270
---

Get campaigns
# Get campaigns
Python version 2 or 3 using JSON with the Requests library
This example shows a request using the [{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html).[{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/get.html) method, along with the result processing and output. To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
# -*- coding: utf-8 -*-
import requests, json
from requests.exceptions import ConnectionError
from time import sleep

# Method for properly parsing UTF-8 encoded strings for both Python 3 and Python 2
import sys

if sys.version_info < (3,):
    def u(x):
        try:
            return x.encode("utf8")
        except UnicodeDecodeError:
            return x
else:
    def u(x):
        if type(x) == type(b''):
            return x.decode('utf8')
        else:
            return x

# --- Input data ---
// Address of the Campaigns service for sending JSON requests (case-sensitive)
CampaignsURL = 'https://api.direct.yandex.com/json/v5/campaigns'

# OAuth token of the Yandex Direct user who sends the requests.
token = 'TOKEN'

# The login of the advertising agency's client
# This parameter is required when submitting requests on behalf of an advertising agency
clientLogin = 'CLIENT_LOGIN'

# --- Request preparation, execution, and processing ---
// Creating HTTP headers for the request
headers = {"Authorization": "Bearer " + token,  # OAuth token. The word “Bearer” is mandatory
           "Client-Login": clientLogin,  # Login of the advertising agency's client
           "Accept-Language": "ru",  # Language of response messages
           }

# Creating the request body
body = {"method": "get",  # Used method.
        "params": {"SelectionCriteria": {},  # Criteria for filtering campaigns. To get all campaigns, leave it empty
                   "FieldNames": ["Id", "Name"]  # Names of the parameters that you want to retrieve.
                   }}

# Encoding the request message body as JSON
jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')

# Executing the request
try:
    result = requests.post(CampaignsURL, jsonBody, headers=headers)

    # Debugging information
    # print("Request headers: {}".format(result.request.headers))
    # print("Request: {}".format(u(result.request.body)))
    # print("Response headers: {}".format(result.headers))
    # print("Response: {}".format(u(result.text)))
    # print("\n")

    # Processing the request
    if result.status_code != 200 or result.json().get("error", False):
        print("Error sending a request to the Yandex Direct API server.")
        print("Error code: {}".format(result.json()["error"]["error_code"]))
        print("Error description: {}".format(u(result.json()["error"]["error_detail"])))
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
    else:
        print("RequestId: {}".format(result.headers.get("RequestId", False)))
        print("Information about points: {}".format(result.headers.get("Units", False)))
        # Outputting the list of campaigns
        for campaign in result.json()["result"]["Campaigns"]:
            Print("Ad campaign: {} No. {}".format(u(campaign['Name']), campaign['Id']))

        if result.json()['result'].get('LimitedBy', False):
            # If the response contains a LimitedBy parameter, it indicates that not all available objects were retrieved.
            # In this case, send additional requests to get all objects.
            # Details on paginated selections - https://tech.yandex.com/direct/doc/dg/best-practice/get-docpage/#page
            print("Not all objects retrieved.")


# Handling errors when unable to connect to the Yandex Direct API server
except ConnectionError:
    # In this case, we recommend repeating the request later
    print("Error connecting to the API server.")

# If any other error occurred
except:
    # In this case, we recommend analyzing the application's actions
    print("Unexpected error.")

```

### Was the article helpful?
YesNo
Previous
[Python examples for JSON](https://yandex.com/dev/direct/doc/en/en/python3-json)
Next
[Create ads](https://yandex.com/dev/direct/doc/en/en/python3-requests-ads)
