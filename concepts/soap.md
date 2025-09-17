---
title: SOAP protocol | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/soap
crawled_at: 2025-09-17T15:39:52.331106
---

WSDL
# SOAP protocol
  * [WSDL](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap#wsdl)
  * [API requests in SOAP format](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap#api-requests-in-soap-format)
  * [Learn more](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap#learn-more)


Many programming languages have libraries for working with SOAP. The recommended libraries for popular languages are listed below.
  * **Perl:**
  * **PHP:**
  * **Python:**
  * **Java:**


##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap#wsdl)WSDL
A WSDL (Web Services Description Language) description has been developed for each of the Yandex Direct API services. The description includes the methods, input and output data structures, data types, address for requests to the service, and other information.
The WSDL address is given in the documentation for each service.
The most functional SOAP libraries use WSDL to query services and verify transmissions. These libraries download the WSDL description, analyze it, and form the necessary data structures for making method calls. The application only needs to add data to the structures and send the query. Similarly, the response message is output as a structure inherent to the programming language. This frees the application from having to process XML.
Note
The application can form SOAP queries in XML format by itself, but this is a tedious task that isn't worth the effort, when there are fully-functional SOAP libraries available.
##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap#api-requests-in-soap-format)API requests in SOAP format
The method for sending requests depends on the SOAP library. If the library supports WSDL, it is sufficient to specify the URL of its WSDL description. The library will get the service URL from the description and perform the operations necessary to send the request. If the library doesn't support WSDL, you need to explicitly specify the service URL.
The WSDL address and address for requests are given in the documentation for each service.
# Request example
Calling the `Ads.add` method to create ads for the advertiser `agrom`. Performed in the name of an advertising agency.
```
POST /v5/ads/ HTTP/1.1
Host: api.direct.yandex.com
Authorization: Bearer 0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f
Accept-Language: en
Client-Login: agrom
Content-Type: text/xml; charset=utf-8
SOAPAction: "https://api.direct.yandex.com/v5/ads/add"

`<?xml version="1.0" encoding="UTF-8"?>`
<SOAP-ENV:Envelope>
    xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ns1="http://api.direct.yandex.com/v5/ads"
  <SOAP-ENV:Body>
    <ns1:AddRequest>
      <Ads>
        <AdGroupId>1234567</AdGroupId>
        <TextAd>
          <Text>All breeds of elephants. Certified breeder.</Text>
          <Title>Buy an elephant!</Title>
          <Href>http://exotic-farm.com/elephants</Href>
          <Mobile>NO</Mobile>
        </TextAd>
      </Ads>
      <Ads>
        <AdGroupId>1234567</AdGroupId>
        <TextAd>
          <Text>Rhino delivery. Spring sale.</Text>
          <Title>Buy a rhino!</Title>
          <Mobile>NO</Mobile>
        </TextAd>
      </Ads>
    </ns1:AddRequest>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

```

# Response example
```
HTTP/1.1 200 OK
Connection:close
Content-Type:text/xml; charset=utf-8
Date:Fri, 28 Nov 2014 17:07:02 GMT
RequestId:1010101010101010101
Units:10/20828/64000
Units-Used-Login:agrom
Server:nginx
Transfer-Encoding:chunked

`<?xml version="1.0" encoding="UTF-8"?>`<SOAP-ENV:Envelope>
    xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  <SOAP-ENV:Body>
    <ns3:AddResponse xmlns:ns3="http://api.direct.yandex.com/v5/ads">
      <AddResults>
        <Id>7654321</Id>
      </AddResults<!-- Ad created and its ID returned --
      <AddResults>
        <Errors>
          <Code>6000</Code>
          <Message>Inconsistent object state</Message>
          <Details>The ad must specify the vCard or the main link</Details>
        </Errors>
      </AddResults><!-- Error creating ad --
    </ns3:AddResponse>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

```

# Error example
If the request could not be processed, an error message is returned.
```
HTTP/1.1 200 OK
Connection:close
Content-Type:text/xml; charset=utf-8
Date:Fri, 28 Nov 2014 17:07:02 GMT
RequestId:1010101010101010101
Units:10/20828/64000
Units-Used-Login:agrom
Server:nginx
Transfer-Encoding:chunked

`<?xml version="1.0" encoding="UTF-8"?>`<SOAP-ENV:Envelope>
    xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  <SOAP-ENV:Body>
    <SOAP-ENV:Fault>
      <faultcode>SOAP-ENV:Client</faultcode>
      <faultstring>Invalid request</faultstring>
      <detail>
        <ns3:FaultResponse xmlns:ns3="http://direct.yandex.com/api/v5/general">
          <requestId>1010101010101010101</requestId>
          <errorCode>8000</errorCode>
          <errorDetail>TextAd is missing the required Text field</errorDetail>
        </ns3:FaultResponse>
      </detail>
    </SOAP-ENV:Fault>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

```

##  [](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/soap#learn-more)Learn more
Copied
### Was the article helpful?
YesNo
Previous
[JSON format](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/json)
Next
[Error handling](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/errors)
