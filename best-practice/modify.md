---
title: Operations on object arrays | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/modify
crawled_at: 2025-09-17T15:41:49.221780
---

Operations on object arrays
# Operations on object arrays
  * [How to process errors](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#errors-processing)
  * [Error example](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#error-example)
  * [How to process warnings](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#warnings-processing)
  * [Warning example](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#warning-example)
  * [Duplicate IDs](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#duplicate-id)


The input for all methods that change data specifies an array of objects to perform the operation on.
The elements in the input array match the elements in the output array, in the same order. Each element in the input array contains:
  * The ID of the created, modified, or deleted object if the operation was successful.
  * The object ID and the `Warnings` array, if the operation completed with some issues.
  * The `Errors` array (and possibly the `Warnings` array), if the operation was not completed due to an error. The object ID is not returned.


An error when performing an operation with one of the objects does not affect the success of the operation with the rest of the objects. **Exception:** If a required parameter is missing for any object, the request is considered invalid. This causes an error for the entire request, not just for the specific operation.
The `Errors` and `Warnings` arrays contain one or more `ExceptionNotification` structures:
**Parameter** |  **Type** |  **Description**  
---|---|---  
**ExceptionNotification structure**  
`Code` |  int |  Numeric code of the error or warning.  
`Message` |  string |  Textual message about the error or warning.  
`Details` |  string |  Detailed description of the error or warning.  
Codes and descriptions for errors and warnings are listed in the section .
  * [How to process errors](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#errors-processing)
  * [How to process warnings](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#warnings-processing)
  * [Duplicate IDs](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#duplicate-id)


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#errors-processing)How to process errors
  * The presence of the `Errors` array in the response means that the operation was not completed.
  * The application should not try to repeat an operation that returned an error.
  * The application should log the error. We also recommend sending errors to email or a monitoring system.
  * Errors must be analyzed in order to make changes in the application to prevent future errors.


Note that an operation that finished with an error costs more points than a successful operation does.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#error-example)Error example
The input array has two ads that need to be added. The first add operation is successful, and the ad ID is returned. The second operation returns an error.
**Request** :
```
    {
      "method": "add",
      "params": {
        "Ads": [{
          "AdGroupId": 1234567,
          "TextAd": {
            "Text": "All breeds of elephants. Certified breeder",
            "Title": "Buy an elephant!",
            "Href": "http://exotic-farm.com/elefants",
            "Mobile": "NO"
          }
        },
        {
          "AdGroupId": 1234567,
          "TextAd": {
            "Text": "Rhino delivery. Spring sale.",
            "Title": "Buy a rhinoceros!",
            "Mobile": "NO"
          }
        }]
      }
    }

```

**Response** :
```
    {
      "result": {
        "AddResults": [{
          "Id": 7654321
        },
        {
          "Errors": [{
            "Code": 6000,
            "Message": "Inconsistent object state",
            "Details": "The ad must specify the vCard or the main link"
          }]
        }]
      }
    }

```

##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#warnings-processing)How to process warnings
  * The presence of the `Warnings` array and the object ID in the response indicates that the operation finished successfully. The application can continue running.
  * The application should log the warnings. We also recommend sending the warnings to email or a monitoring system.
  * The warnings must be analyzed in order to make changes in the application to prevent repeated warnings.


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#warning-example)Warning example
The input array has two ads that need to be paused. A warning is returned for the first suspend operation because the ad was already paused.
**Request** :
```
    {
      "method": "suspend",
      "params": {
        "SelectionCriteria": {
          "Ids": [7654300, 7654321]
        }
      }
    }

```

**Response** :
```
    {
      "result": {
        "SuspendResults": [{
          "Id": 7654300,
          "Warnings": [{
            "Code": 10200,
            "Message": "Ad already stopped"
          }]
        },
        {
          "Id": 7654321
        }]
      }
    }

```

##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify#duplicate-id)Duplicate IDs
If a single call of the _update_ , _set_ , or _delete_ method contains multiple objects with the same ID, the operation is not performed for any of these objects, and an error is returned. Any other objects in the request are processed normally.
If a single call of the _suspend_ , _resume_ , _moderate_ , _archive_ , or _unarchive_ method contains multiple objects with the same ID, the operation is performed, but a warning is returned for the duplicate IDs.
Copied
### Was the article helpful?
YesNo
Previous
[Getting data: the "get" method](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get)
Next
[Editing separate parameters](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/part-update)
