---
title: Get statistics for any dates | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3_requests_stat1
crawled_at: 2025-09-17T15:51:25.885621
---

Get statistics for any dates
# Get statistics for any dates
Python version 2 or 3 using JSON with the Requests library
This example shows a request to the [Reports](https://yandex.com/dev/direct/docreports/reports.md) service, along with the result processing and output. The mode for generating the report is selected automatically. If the report is added to the offline queue, the repeat requests are executed.
The report contains statistics on impressions, clicks, and expenditures for all the advertiser's campaigns for any specified period, with grouping by date, campaign name, and user location.
To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login. In the request message body, specify the start and end dates of the report period and a report name that is unique among the advertiser's reports.
```
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import ConnectionError
from time import sleep
import json

# Method for properly parsing the UTF-8 encoded strings both in Python 3 and Python 2
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
# Reports service address used to send JSON requests (case-sensitive)
ReportsURL = 'https://api.direct.yandex.com/json/v5/reports'

# OAuth token of the Yandex Direct user who sends the requests.
token = 'TOKEN'

# The login of the advertising agency's client
# This parameter is required when submitting requests on behalf of an advertising agency
clientLogin = 'CLIENT_LOGIN'

# --- Preparing the request ---
# Creating HTTP headers for the request
headers = {
           # OAuth token. The word “Bearer” is mandatory
           "Authorization": "Bearer " + token,
           # The login of the advertising agency's client
           "Client-Login": clientLogin,
           # Language of responses
           "Accept-Language": "ru",
           # Report generation mode
           "processingMode": "auto"
           # Format for monetary values in the report
           # "returnMoneyInMicros": "false",
           # Don't include the row with the report name and the date range in the report
           # "skipReportHeader": "true",
           # Don't include the row with the field names in the report
           # "skipColumnHeader": "true",
           # Don't include the row with the number of data rows in the report
           # "skipReportSummary": "true"
           }

# Creating the request body
body = {
    "params": {
        "SelectionCriteria": {
            "DateFrom": "START_DATE",
            "DateTo": "END_DATE"
        },
        "FieldNames": [
            "Date",
            "CampaignName",
            "LocationOfPresenceName",
            "Impressions",
            "Clicks",
            "Cost"
        ],
        "ReportName": u("REPORT_NAME"),
        "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
        "DateRangeType": "CUSTOM_DATE",
        "Format": "TSV",
        "IncludeVAT": "NO",
        "IncludeDiscount": "NO"
    }
}

# Encoding the request message body as JSON
body = json.dumps(body, indent=4)

# --- Starting the request execution loop ---
# If HTTP code 200 is returned, output the report contents
# If HTTP code 201 or 202 is returned, send repeat requests
while True:
    try:
        req = requests.post(ReportsURL, body, headers=headers)
        req.encoding = 'utf-8'  # Force the response to be interpreted as UTF-8
        if req.status_code == 400:
            print("Invalid request parameters, or the report queue has reached its limit")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("JSON code for the request: {}".format(u(body)))
            print("JSON code for the server response: \n{}".format(u(req.json())))
            break
        elif req.status_code == 200:
            Print("Report created")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("Report content: \n{}".format(u(req.text)))
            break
        elif req.status_code == 201:
            print("Report added to the offline queue")
            retryIn = int(req.headers.get("retryIn", 60))
            print("Request will be resent in {} seconds".format(retryIn))
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            sleep(retryIn)
        elif req.status_code == 202:
            print("Generating the report in offline mode")
            retryIn = int(req.headers.get("retryIn", 60))
            print("Request will be resent in {} seconds".format(retryIn))
            print("RequestId:  {}".format(req.headers.get("RequestId", False)))
            sleep(retryIn)
        elif req.status_code == 500:
            print("Error occurred when generating the report. Please repeat the request again later.")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("JSON code for the server response: \n{}".format(u(req.json())))
            break
        elif req.status_code == 502:
            print("Exceeded the server limit on report generation time.")
            print("Please try changing the request parameters: reduce the time period and the amount of data requested.")
            print("JSON code for the request: {}".format(body))
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("JSON code for the server response: \n{}".format(u(req.json())))
            break
        else:
            print("Unexpected error.")
            print("RequestId:  {}".format(req.headers.get("RequestId", False)))
            print("JSON code for the request: {}".format(body))
            print("JSON code for the server response: \n{}".format(u(req.json())))
            break

    # Handling errors when unable to connect to the Yandex Direct API server
    except ConnectionError:
        # In this case, we recommend repeating the request later
        print("Error connecting to the API server")
        # Forced exit from the loop
        break

    # If any other error occurred
    except:
        # In this case, we recommend analyzing the application's actions
        print("Unexpected error.")
        # Forced exit from the loop
        break

```

### Was the article helpful?
YesNo
Previous
[Handle error 152 Insufficient points](https://yandex.com/dev/direct/doc/en/en/python3-requests-points)
Next
[Get statistics for a selection of rows](https://yandex.com/dev/direct/doc/en/en/python3_requests_stat2)
