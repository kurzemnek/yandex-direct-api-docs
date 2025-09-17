---
title: Get statistics for any dates | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3_pyxb_stat1
crawled_at: 2025-09-17T15:51:45.054548
---

Get statistics for any dates
# Get statistics for any dates
Python 2 or 3 using XML with the Requests and PyXB libraries
After [installing](https://yandex.com/dev/direct/doc/en/en/python3#python-modules) the PyXB library, the utility for generating pyxbgen classes will be available. Run the command
```
pyxbgen -u https://api.direct.yandex.com/v5/reports.xsd -m directapi5reports

```

As a result, two files will be formed: _general.py and directapi5reports.py. Import the directapi5reports.py file to the script to generate valid XML request codes. For more information, see 
This example shows a request to the [Reports](https://yandex.com/dev/direct/docreports/reports.md) service, along with the result processing and output. The mode for generating the report is selected automatically. If the report is added to the offline queue, the repeat requests are executed.
The report contains statistics on impressions, clicks, and expenditures for all the advertiser's campaigns for any specified period, with grouping by date, campaign name, and user location.
To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login. In the request message body, specify the start and end dates of the report period and a report name that is unique among the advertiser's reports.
```
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import ConnectionError
from time import sleep
import directapi5reports
import pyxb

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
# Reports service address used to send XML requests (case-sensitive)
ReportsURL = 'https://api.direct.yandex.com/v5/reports'

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
requestData = directapi5reports.ReportDefinition()
# Data selection criteria
requestData.SelectionCriteria = pyxb.BIND()
requestData.SelectionCriteria.DateFrom = pyxb.BIND("START_DATE")
requestData.SelectionCriteria.DateTo = pyxb.BIND("END_DATE")

# Fields that must be included in the report
requestData.FieldNames = ["Date","CampaignName","LocationOfPresenceName","Impressions","Clicks","Cost"]
# Sort by date in ascending order
requestData.OrderBy = [pyxb.BIND("Date","ASCENDING")]
# Report name
requestData.ReportName = u("REPORT_NAME")
# Report type: Campaign statistics
requestData.ReportType = "CAMPAIGN_PERFORMANCE_REPORT"
# Report period: Dates specified in the DateFrom and DateTo parameters
requestData.DateRangeType = "CUSTOM_DATE"
# Report format
requestData.Format = "TSV"
# Return CPC without VAT
requestData.IncludeVAT ="NO"
# Return CPC without the client's discount
requestData.IncludeDiscount = "NO"

# Converting data to XML for the request
requestData = requestData.toxml()

# --- Starting the request execution loop ---
# If HTTP code 200 is returned, output the report contents
# If HTTP code 201 or 202 is returned, send repeat requests
while True:
    try:
        req = requests.post(ReportsURL,requestData,headers=headers)
        req.encoding = 'utf-8'  # Force the response to be interpreted as UTF-8
        if req.status_code == 400:
            print("Invalid request parameters, or the report queue has reached its limit")
            print("RequestId: {}".format(req.headers.get("RequestId",False)))
            print("XML code of the request: {}".format(u(requestData)))
            print("XML code of the server response: \n{}".format(u(req.text)))
            break
        elif req.status_code == 200:
            Print("Report created")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            Print("Resulting report file: \n{}".format(u(req.text)))
            break
        elif req.status_code == 201:
            print("Report added to the offline queue")
            retryIn = int(req.headers.get("retryIn",60))
            print("Request will be resent in {} seconds".format(retryIn))
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            sleep(retryIn)
        elif req.status_code == 202:
            print("Generating the report in offline mode")
            retryIn = int(req.headers.get("retryIn", 60))
            print("Request will be resent in {} seconds".format(retryIn))
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            sleep(retryIn)
        elif req.status_code == 500:
            print("Error occurred when generating the report. Please repeat the request again later.")
            print("RequestId: {}".format(req.headers.get("RequestId",False)))
            print("XML code of the server response: \n{}".format(u(req.text)))
            break
        elif req.status_code == 502:
            print("Exceeded the server limit on report generation time.")
            print("Please try changing the request parameters: reduce the time period and the amount of data requested.")
            print("XML code of the request: {}".format(requestData))
            print("RequestId: {}".format(req.headers.get("RequestId",False)))
            print("XML code of the server response: \n{}".format(u(req.text)))
            break
        else:
            print("Unexpected error.")
            print("RequestId: {}".format(req.headers.get("RequestId", False)))
            print("XML code of the request: {}".format(requestData))
            print("XML code of the server response: \n{}".format(u(req.text)))
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
[Python examples for XML](https://yandex.com/dev/direct/doc/en/en/python3-xml)
Next
[Get statistics for a selection of rows](https://yandex.com/dev/direct/doc/en/en/python3_pyxb_stat2)
