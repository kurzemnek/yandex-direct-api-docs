---
title: Get campaigns | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3-suds-campaigns
crawled_at: 2025-09-17T15:51:35.371172
---

Get campaigns
# Get campaigns
Python version 2 or 3 using SOAP with the Suds library
This example shows a request using the [{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/campaigns.html).[{#T}](https://yandex.com/dev/direct/doc/ref-v5/campaigns/get.html) method, along with the result processing and output. To use the example, specify the OAuth access token in the input data. If you're submitting a request on behalf of an agency, be sure to include the client's login.
```
# -*- coding: utf-8 -*-
from suds.client import Client, WebFault
from suds.transport.http import HttpTransport

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


# Debugging information
# import logging
#
# logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)
# logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
# logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)

# Additional class for proper handling of HTTP response headers for a SOAP request
class MyTransport(HttpTransport):
    def __init__(self, *args, **kwargs):
        HttpTransport.__init__(self, *args, **kwargs)
        self.last_headers = None

    def send(self, request):
        result = HttpTransport.send(self, request)
        self.last_headers = result.headers
        return result


# --- Input data ---
# Address of the WSDL description for the Campaigns service (case-sensitive)
CampaignsURL = 'https://api.direct.yandex.com/v5/campaigns?wsdl'

# OAuth token of the Yandex Direct user who sends the requests.
token = 'TOKEN'

# The login of the advertising agency's client
# This parameter is required when submitting requests on behalf of an advertising agency
clientLogin = 'CLIENT_LOGIN'

# --- Request preparation, execution, and processing ---
# Creating HTTP headers for the request
headers = {
    "Authorization": "Bearer " + token,         # OAuth-token. The word “Bearer” is mandatory
    "Client-Login": clientLogin,                # Login of the advertising agency's client
    "Accept-Language": "ru",                    # Language of response messages
}

# SOAP client constructor
client = Client(CampaignsURL, location='https://api.direct.yandex.com/v5/campaigns')
client.set_options(transport=MyTransport())     # Setting an auxiliary class for sending requests
client.set_options(headers=headers)             # Setting HTTP request headers


# Creating the request body
params = {
    "SelectionCriteria": {},                    # Criteria for filtering campaigns. To get all campaigns, leave it empty
    "FieldNames": ["Id", "Name"]                # Names of the parameters that you want to retrieve
}

# Executing the request
try:
    result = client.service.get(**params)
    print("RequestId: {}".format(client.options.transport.last_headers.get("requestid",False)))
    Print("Information about points: {}".format(client.options.transport.last_headers.get("units", False)))
    for campaign in result["Campaigns"]:
        Print("Ad campaign: {} No. {}".format(u(campaign['Name']), campaign['Id']))

except WebFault as err:
    print("Error sending a request to the Yandex Direct API server.")
    print("Error code: {}".format(err.fault['detail']['FaultResponse']['errorCode']))
    print("Error details: {}".format(u(err.fault['detail']['FaultResponse']['errorDetail'])))
    print("RequestId: {}".format(err.fault['detail']['FaultResponse']['requestId']))

except:
    err = sys.exc_info()
    print('Error accessing the Yandex Direct API server: ' + str(err[1]))

```

### Was the article helpful?
YesNo
Previous
[Python examples for SOAP](https://yandex.com/dev/direct/doc/en/en/python3-soap)
Next
[Create ads](https://yandex.com/dev/direct/doc/en/en/python3-suds-ads)
