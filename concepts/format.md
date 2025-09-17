---
title: Interaction format | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/format
crawled_at: 2025-09-17T15:37:00.880401
---

Interaction format
# Interaction format
Requests to the Yandex Direct API are made over the HTTPS protocol using the POST method.
A request must contain the HTTP `Authorization` header with the OAuth token of the user that the API request is being made on behalf of. It may also contain other headers that are necessary for processing the request. The response contains the `RequestId` header — the unique ID of the request.
Input and output data structures are passed in the body of the request and response. The Yandex.Direct API supports two formats: [JSON](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json) and [SOAP/XML](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap). All data is UTF-8 encoded.
Copied
### Was the article helpful?
YesNo
Previous
[Roles and access of Yandex.Direct users](https://yandex.com/dev/direct/doc/en/concepts/en/objects/roles)
Next
[HTTP headers](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/headers)
