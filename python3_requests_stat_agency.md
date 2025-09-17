---
title: Get statistics for agency clients | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3_requests_stat_agency
crawled_at: 2025-09-17T15:53:30.621014
---

Get statistics for agency clients
# Get statistics for agency clients
Python version 2 or 3 using JSON with the Requests library
This example shows how to use the [AgencyClients](https://yandex.com/dev/direct/docref-v5/agencyclients/agencyclients.md).[get](https://yandex.com/dev/direct/docref-v5/agencyclients/get.md) method to get a list of agency clients and then execute requests to the [Reports](https://yandex.com/dev/direct/docreports/reports.md) service to get statistics for advertiser accounts for the past day. The mode for generating the report is selected automatically. If the report is added to the offline queue, the repeat requests are executed.
To use the example, specify the OAuth access token that you received for the agency representative in the input data.
```
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import ConnectionError
from time import sleep
import json
from datetime import date, timedelta
from time import time

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
        if isinstance(x, bytes):
            return x.decode('utf8')
        else:
            return x

# --- Input data ---
# Address of the AgencyClients service for sending JSON requests (case-sensitive)
AgencyClientsURL = 'https://api.direct.yandex.com/json/v5/agencyclients'

# Reports service address used to send JSON requests (case-sensitive)
ReportsURL = 'https://api.direct.yandex.com/json/v5/reports'

# OAuth token of the agency representative who is sending the requests.
token = 'TOKEN'

# --- Preparing the request to the AgencyClients service ---
# Creating HTTP headers for the request
headers = {
           # OAuth token. The word “Bearer” is mandatory
           "Authorization": "Bearer " + token,
           # Language of responses
           "Accept-Language": "ru"
           }

AgencyClientsBody = {
    "method": "get",
    "params": {
        "SelectionCriteria": {
            "Archived": "NO"   # Only get active clients
        },
        "FieldNames": ["Login"],
        "Page": {
            "Limit": 10000,  # Get no more than 10,000 clients in the server response
            "Offset": 0
        }
    }
}

# --- Executing requests to the AgencyClients service ---
# If the response doesn't contain a LimitedBy parameter, it indicates
# that all clients were retrieved
HasAllClientLoginsReceived = False
ClientList = []

while not HasAllClientLoginsReceived:
    ClientsResult = requests.post(AgencyClientsURL, json.dumps(AgencyClientsBody), headers=headers).json()
    for Client in ClientsResult['result']['Clients']:
        ClientList.append(Client["Login"])
    if ClientsResult['result'].get("LimitedBy", False):
        AgencyClientsBody['Page']['Offset'] = ClientsResult['result']["LimitedBy"]
    else:
        HasAllClientLoginsReceived = True

# --- Preparing the request to the Reports service ---
# Creating the request body
The report contains statistics on impressions, clicks, and expenses for all the client's campaigns
body = {
    "params": {
        "SelectionCriteria": {},
        "FieldNames": [
            "Impressions",
            "Clicks",
            "Cost"
        ],
        "ReportName": u("ACCOUNT_PERFORMANCE"),
        "ReportType": "ACCOUNT_PERFORMANCE_REPORT",
        "DateRangeType": "AUTO",
        "Format": "TSV",
        "IncludeVAT": "NO",
        "IncludeDiscount": "NO"
    }
}

# Generating output data
resultcsv = "Login;Impressions;Clicks;Costs\n"

# Additional HTTP headers for requesting reports
headers['skipReportHeader'] = "true"
headers['skipColumnHeader'] = "true"
headers['skipReportSummary'] = "true"
headers['returnMoneyInMicros'] = "false"

# --- Sending requests to the Reports service ---
for Client in ClientList:
    # Adding the "Client-Login" HTTP header
    headers['Client-Login'] = Client
    # Encoding the request message body as JSON
    requestBody = json.dumps(body, indent=4)
    # Starting the request execution loop
    # If an HTTP code of 200 is returned, the report contents is added to the output data
    # If HTTP code 201 or 202 is returned, send repeat requests
    while True:
        try:
            req = requests.post(ReportsURL, requestBody, headers=headers)
            req.encoding = 'utf-8'  # Force the response to be interpreted as UTF-8
            if req.status_code == 400:
                print("Invalid request parameters, or the report queue is full")
                print("RequestId: {}".format(req.headers.get("RequestId", False)))
                print("JSON code for the request: {}".format(u(body)))
                print("JSON code for the server response: \n{}".format(u(req.json())))
                break
            elif req.status_code == 200:
                print("Report for account {} created".format(str(Client)))
                print("RequestId: {}".format(req.headers.get("RequestId", False)))
                if req.text != "":
                    tempresult = req.text.split('\t')
                    resultcsv += "{};{};{};{}\n".format(Client, tempresult[0], tempresult[1], str(tempresult[2]).replace('.', ','))
                else:
                    resultcsv += "{};0;0;0\n".format(Client)
                break
            elif req.status_code == 201:
                print("Report for account {} added to the offline queue".format(str(Client)))
                retryIn = int(req.headers.get("retryIn", 60))
                print("Request will be resent in {} seconds".format(retryIn))
                print("RequestId: {}".format(req.headers.get("RequestId", False)))
                sleep(retryIn)
            elif req.status_code == 202:
                print("Generating the report in offline mode".format(str(Client)))
                retryIn = int(req.headers.get("retryIn", 60))
                print("Request will be resent in {} seconds".format(retryIn))
                print("RequestId: {}".format(req.headers.get("RequestId", False)))
                sleep(retryIn)
            elif req.status_code == 500:
                print("Error occurred when generating the report. Please repeat the request again later.")
                print("RequestId: {}".format(req.headers.get("RequestId", False)))
                print("JSON code for the server response: \n{}".format(u(req.json())))
                break
            elif req.status_code == 502:
                print("Exceeded the server limit on report generation time.")
                print(
                    "Please try changing the request parameters: reduce the time period and the amount of data requested.")
                print("JSON code for the request: {}".format(body))
                print("RequestId: {}".format(req.headers.get("RequestId", False)))
                print("JSON code for the server response: \n{}".format(u(req.json())))
                break
            else:
                print("Unexpected error.")
                print("RequestId: {}".format(req.headers.get("RequestId", False)))
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
            # In this case, we recommend analyzing the application's actions
            print("Unexpected error.")
            # Forced exit from the loop
            break

print("Reports for all accounts have been created")

# Creating and writing the file
filename = "AccountsPerfomanceReport_{}.csv".format(str(time()))
resultfile = open(filename, 'w+')
resultfile.write(resultcsv)
resultfile.close()

print("Results are saved to file {}".format(filename))

```

### Was the article helpful?
YesNo
Previous
[Get statistics for a selection of rows](https://yandex.com/dev/direct/doc/en/en/python3_requests_stat2)
Next
[Python examples for SOAP](https://yandex.com/dev/direct/doc/en/en/python3-soap)
