---
title: Access and authorization | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/access
crawled_at: 2025-09-17T15:36:44.114203
---

Access and authorization
# Access and authorization
An application (program, script, or other type of app) sends an API request on behalf of a Yandex Direct user — a representative of an advertiser or advertising agency — and manages this user's data.
The app can access a user's data under the following conditions:
  1. The app developer completed the [application registration process](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register), and the request for access was approved.
  2. The user has a Yandex Direct account and represents a direct advertiser, an advertising agency, or a client of an advertising agency, who was granted access to the data by the agency.
Note
     * If the agency granted the client read-only access to the web interface, the client's representative can only get data when using the API, as well.
     * If the agency granted the client permission to edit campaigns, the client's representative can use either the web interface or the API for managing the client's campaigns.
  3. The user has accepted the user agreement on the [API page for the Yandex Direct service](https://direct.yandex.com/registered/main.pl?cmd=apiSettings&api_welcome=yes).
  4. The user has allowed the app to make requests.
The app must request permission from the user to access data, get an [access token](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/auth-token), and specify the token in requests.
To get a token, the application must redirect the user to the access request page. The user logs in to Yandex (using their login for Yandex Direct) and clicks the **Confirm** button. Next, the Yandex server generates a token and sends it to the app.


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/access#restrictions)Restricting access by IP address
API access may be restricted by IP address, for increased information security. The user can specify the allowed IP addresses on the **API settings** page under the [Settings](https://direct.yandex.com/registered/main.pl?cmd=apiSettings) tab.
### Was the article helpful?
YesNo
Previous
[SharedAccount](https://yandex.com/dev/direct/doc/en/concepts/en/objects/shared-account)
Next
[App registration](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/register)
