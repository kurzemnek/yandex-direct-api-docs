---
title: Sandbox | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/sandbox
crawled_at: 2025-09-17T15:46:08.136378
---

Sandbox
# Sandbox
  * [Restrictions](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox#restrictions)
  * [Sandbox address](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox#url)


Sandbox is a testing environment for debugging apps that interact with the Yandex Direct API.
Sandbox provides a simulated environment of the Yandex Direct API, completely isolated from live data. It is a playground where you can invoke API methods, get responses, and observe changes to test campaigns and ads. Those operations that are available in the API only when there are sufficient funds are always available in the Sandbox, without having to actually credit funds to an account.
Requests sent to the sandbox do not modify data in Yandex Direct. Ads that are created are not actually displayed anywhere, and funds that are deducted and credited do not affect real campaigns. However, the entire set of possible campaign states is simulated, from under review to stopping displays due to insufficient funds. Although statistical reports contain simulated data, their structure is the same as a real report. This makes the Sandbox a fully-functional environment for debugging applications.
The sandbox doesn't have a web interface, so test campaigns can't be viewed in the interface. You can only access the sandbox by calling API methods.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox#restrictions)Restrictions
The same restrictions apply in the sandbox as in the API.
In the [Reports](https://yandex.com/dev/direct/doc/reports/reports.html) service you can request data for one campaign per report.
Sandbox data is stored for a month from the last time it was accessed, and then it is deleted.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox#url)Sandbox address
####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox#url)WSDL description address
```
https://api-sandbox.direct.yandex.com/v5/{service}?wsdl 

```

####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox#url)Address for SOAP requests
```
https://api-sandbox.direct.yandex.com/v5/{service}

```

####  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox#url)Address for JSON requests
```
https://api-sandbox.direct.yandex.com/json/v5/{service}

```

### Was the article helpful?
YesNo
Previous
[For agencies](https://yandex.com/dev/direct/doc/en/concepts/en/best-practice/agency)
Next
[Managing the Sandbox](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox-init)
