---
title: Handle error 152 “Insufficient points” | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3-requests-points
crawled_at: 2025-09-17T15:51:21.067420
---

Handle error 152 “Insufficient points”
# Handle error 152 “Insufficient points”
Python version 2 or 3 using JSON with the Requests library
In version 5 of the Yandex Direct API, points are awarded to advertisers every 60 minutes, but each advertiser receives points on its own schedule, not necessarily at the beginning of the astronomical hour. The example shows how requests are executed when the first request returns the 152 error code.
For demonstration purposes, it uses the `sleep` function, which allows you to set delays for running the script. The delays are set in seconds in the `delays` array, so that after the first attempt no more than 5 repeat requests are sent with increasing intervals that cover the next 60 minutes after receiving the first error.
```
# -*- coding: utf-8 -*-
import sys
from time import sleep

import json
import requests

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

# --- Settings ---
# Outputting debugging information
debug = True

# Delay interval array
delays = [360, 540, 720, 900, 1080]

# "Insufficient points" error
notEnoughUnitsError = "152"

# --- Request input data ---
# Address of the Campaigns service for sending JSON requests (case-sensitive)
CampaignsURL = 'https://api.direct.yandex.com/json/v5/campaigns'

# OAuth token of the Yandex Direct user who sends the requests.
token = 'TOKEN'

# The login of the advertising agency's client
# This parameter is required when submitting requests on behalf of an advertising agency
clientLogin = 'CLIENT_LOGIN'

# --- Preparing the request ---
# Creating HTTP headers for the request
headers = {
    "Authorization": "Bearer " + token,     # Oauth token. The word “Bearer” is mandatory
    "Client-Login": clientLogin,            # Login of the advertising agency's client
    "Accept-Language": "ru",                # Language of response messages
}

# Creating the request body
body = {
    "method": "get",                        # Used method
    "params": {
        "SelectionCriteria": {},            # Criteria for filtering campaigns. To get all campaigns, leave it empty
        "FieldNames": ["Id", "Name"]        # Names of the parameters that you want to retrieve
    }
}

# Converting input parameters to JSON
jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')

# --- Task execution ---
# Starting the request execution loop. If the first request is successful, which means it doesn't result in error 152,
# a list of campaigns is returned.
# If the first request fails with this error, repeat requests are made with the delays
# set in the delays array.
for delay in delays:
    try:
        # Executing the request and getting the result
        result = requests.post(CampaignsURL, jsonBody, headers=headers)

        # Debugging information
        if debug:
            print("Request headers: {}".format(result.request.headers))
            print("Request: {}".format(u(result.request.body)))
            Print("Response headers: {}".format(result.headers))
            print("Response: {}".format(u(result.text)))
            print("\n")

        # Processing the request
        if result.status_code == 200:
            If an HTTP code of 200 is returned, output the report contents

            # Output the RequestId and information about points
            print("RequestId: {}".format(result.headers.get("RequestId", False)))
            print("Information about points: {}".format(result.headers.get("Units", False)))

            # If the output data doesn't contain the primary error key, the request was successful
            if not result.json().get("error", False):
                # Outputting the list of campaigns
                for campaign in result.json()["result"]["Campaigns"]:
                    Print("Ad campaign: {} No. {}".format(u(campaign['Name']), campaign['Id']))

                # If the response contains a LimitedBy parameter, it indicates that not all available objects were retrieved.
                if result.json()['result'].get('LimitedBy', False):
                    # In this case, send additional requests to get all objects.
                    # Details on paginated selections - https://tech.yandex.com/direct/doc/dg/best-practice/get-docpage/#page
                    print("Not all objects retrieved.")

                # Forced exit from the loop
                break

            Processing errors for requests sent to the Yandex Direct API server
            elif result.json().get("error", False):
                print("Error sending a request to the Yandex Direct API server.")
                print("Error code: {}".format(result.json()["error"]["error_code"]))
                print("Error description: {}".format(u(result.json()["error"]["error_detail"])))
                if result.json()['error'].get('error_code', 0) == notEnoughUnitsError:
                    # Insufficient points to execute the request
                    print("Resending in {} seconds".format(delay))
                    # Delay before the next request
                    sleep(delay)

        # Handling other errors
        else:
            print("Error sending a request to the Yandex Direct API server.")
            print("HTTP error code: {}".format(u(result.status_code)))
            # Here you can describe the steps to take when an HTTP request returns an error

    # Handling errors when unable to connect to the Yandex Direct API server
    except ConnectionError:
        # In this case, we recommend repeating the request later
        print("Error connecting to the API server.")
        # Forced exit from the loop
        break


    # If any other error occurred
    except:
        # In this case, we recommend analyzing the application's actions
        print("Unexpected error.")
        # Forced exit from the loop
        break

```

Copied
### Was the article helpful?
YesNo
Previous
[Create ads](https://yandex.com/dev/direct/doc/en/en/python3-requests-ads)
Next
[Get statistics for any dates](https://yandex.com/dev/direct/doc/en/en/python3_requests_stat1)
