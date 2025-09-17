---
title: Creating ads | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/python3-suds-ads
crawled_at: 2025-09-17T15:51:40.099135
---

Creating ads
# Creating ads
Python version 2 or 3 using SOAP with the Suds library
This example shows a request using the [{#T}](https://yandex.com/dev/direct/doc/ref-v5/ads/ads.md).[{#T}](https://yandex.com/dev/direct/doc/ref-v5/ads/add.md) method, along with the result processing and output. To use this example, make sure that the input data specifies the OAuth token and the ID of the group where you want to create the new ad. If you're submitting a request on behalf of an agency, be sure to include the client's login.
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
AdsURL = 'https://api.direct.yandex.com/v5/ads?wsdl'

# OAuth token of the user who sends the requests
token = 'TOKEN'

# The login of the advertising agency's client
# This parameter is required when submitting requests on behalf of an advertising agency
clientLogin = 'CLIENT_LOGIN'

# ID of the ad group where you want to create a new ad
adGroupId = GROUP_ID

# --- Request preparation, execution, and processing ---
# Creating HTTP headers for the request
headers = {
    "Authorization": "Bearer " + token,         # Oauth token. The word “Bearer” is mandatory
    "Client-Login": clientLogin,                # Login of the advertising agency's client
    "Accept-Language": "ru",                    # Language of response messages
}

# SOAP client constructor
client = Client(AdsURL, location='https://api.direct.yandex.com/v5/ads')
client.set_options(transport=MyTransport())     # Setting an auxiliary class for sending requests
client.set_options(headers=headers)             # Setting HTTP request headers

# Creating the request body
params = {
    "Ads": [{
        "AdGroupId": adGroupId,
        "TextAd": {                             # Ad parameters
            "Title": u"Ad title",
            "Text": u"Ad text",
            "Mobile": "NO",
            "Href": "http://www.yandex.com"
        }}
    ]
}

# Executing the request
try:
    result = client.service.add(**params)
    # Result output
    print("RequestId: {}".format(client.options.transport.last_headers.get("requestid", False)))
    Print("Information about points: {}".format(client.options.transport.last_headers.get("units", False)))
    # Processing all items in the AddResults array, where each item corresponds to a single ad
    for add in result:
        add = dict(add)
        # Processing nested elements (these may be Errors or Id, or possibly Warnings)
        if add.get("Errors", False):
            # If the Errors array is present, the ad wasn't created due to one or more errors
            for error in add["Errors"]:
                print("Error: {} - {} ({})".format(error["Code"], u(error["Message"]),
                                                 u(error["Details"])))
        else:
            # If the Id parameter is present, it indicates that the ad was created
            print("Created ad #{}".format(add["Id"]))
            # If the Warnings array is present, the ad was created, but with a warning (one or more)
            if add.get("Warnings", False):
                for warning in add["Warnings"]:
                    print("Предупреждение: {} - {} ({})".format(warning["Code"], u(warning["Message"]),
                                                         u(warning["Details"])))

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
[Get campaigns](https://yandex.com/dev/direct/doc/en/en/python3-suds-campaigns)
Next
[Python examples for XML](https://yandex.com/dev/direct/doc/en/en/python3-xml)
