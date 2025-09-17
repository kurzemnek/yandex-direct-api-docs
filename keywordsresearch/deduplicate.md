---
title: deduplicate | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/keywordsresearch/deduplicate
crawled_at: 2025-09-17T15:56:28.382309
---

deduplicate
# deduplicate
  * [Request](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/deduplicate#input)
  * [Response](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/deduplicate#output)
  * [Example](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/deduplicate#samples)


Performs preprocessing on an array of keywords.
This method performs the following actions with keywords:
**Merge duplicates**  
  
Joins together multiple keywords that differ only in the negative keywords, word form, or presence of stop words. The unified keyword contains the negative keywords from all the original keywords. For example, the keywords _custom windows -cheap_ and _custom window -blinds_ would be replaced with the single keyword phrase _custom window -cheap -blinds_. In addition, duplicate keywords are deleted when joining keywords.
**Eliminate overlap**  
  
Adds a negative keyword if the keyword is contained in another keyword phrase that differs by just one word. An example is the keywords _coat_ and _fur coat_. A negative keyword will be added to the first keyword, resulting in _coat -fur_. This means that a search query for _fur coats_ will match only one of the keywords, not both.
The method accepts an input array that can contain:
  * New keywords without an ID.
  * Existing keywords that have an ID in Yandex Direct or an external database.


As the result of unifying duplicates and differentiating overlapping keywords, the method returns instructions about which keywords to add, change, or delete. The response format is as close as possible to the request format for the [add](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/add), [update](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/update) and [delete](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/delete) methods in the [Keywords](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/keywords) service.
##  [](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/deduplicate#input)Request
Request structure in JSON format:
```
{
  "method": "deduplicate",
  "params": { /* params */
    "Keywords": [ {  /* DeduplicateRequestItem */
      "Id": (long),
      "Keyword": (string), /* required */
      "Weight": (long)
    }, ... ], /* required */
    "Operation": [( MERGE_DUPLICATES | ELIMINATE_OVERLAPPING ), ... ]
  }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**Params structure (for JSON) / DeduplicateRequest structure (for SOAP)** |  |  |   
`Keywords` |  array of DeduplicateRequestItem |  Keywords to pre-preprocess. Maximum 400,000 items per array. |  Yes  
`Operation` |  array of DeduplicateOperationEnum |  Operations to perform on an array of keywords:
  * MERGE_DUPLICATES — Unifying duplicate keywords.
  * ELIMINATE_OVERLAPPING — Differentiating overlapping keywords.

If this parameter is omitted, both operations are performed. |  No  
**DeduplicateRequestItem structure** |  |  |   
`Id` |  long |  The keyword ID in Yandex Direct or in an external database. |  No  
`Keyword` |  string |  Keywords. Can contain negative keywords and operators. The maximum length of a keyword is 4096 characters. The “!” operator before a negative keyword is not counted in the keyword length (the sequence “-!” is considered one character). Maximum of 7 words per keyword, not counting stop words and negative keywords. Each word can have up to 35 characters, not counting the minus sign before a negative keyword. |  Yes  
`Weight` |  long |  Weight of the keyword. Positive integer. If multiple keywords are joined together, the keyword with the highest weight is kept or is modified, and the others are deleted. |  No  
##  [](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/deduplicate#output)Response
Response structure in JSON format:
```
{
  "result": { /* result */
    "Add": [{ /* DeduplicateResponseAddItem */
      "Keyword": (string) /* required */
    }, ... ],
    "Update": [{ /* DeduplicateResponseUpdateItem */
      "Id": (long), /* required */
      "Keyword": (string) /* required */
    }, ... ],
    "Delete": { /* IdsCriteria */
      "Ids": [(long), ... ] /* required */
    },
    "Failure": [{ /* DeduplicateErrorItem */
      "Position": (long), /* required */
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
      }, ... ]
    }, ... ]
  }
}

```

Parameters are described below.
**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / DeduplicateResponse structure (for SOAP)** |  |   
`Add` |  array of DeduplicateResponseAddItem |  Keywords that can be input to the [Keywords](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/keywords).[add](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/add) method.  
`Update` |  array of DeduplicateResponseUpdateItem |  Keywords that can be input to the [Keywords](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/keywords).[update](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/update) method.  
`Delete` |  IdsCriteria |  Keywords that can be input to the [Keywords](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/keywords).[delete](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywords/delete) method.  
`Failure` |  array of DeduplicateErrorItem |  Keywords that weren't processed due to an error.  
**DeduplicateResponseAddItem structure** |  |   
`Keyword` |  string |  A keyword to add.  
**DeduplicateResponseUpdateItem structure** |  |   
`Id` |  long |  Keyword ID from the request.  
`Keyword` |  string |  Changed keyword.  
**IdsCriteria structure** |  |   
`Ids` |  array of long |  IDs of keywords to delete.  
**DeduplicateErrorItem structure** |  |   
`Position` |  long |  The sequential number of the keyword in the input array (starting from 1).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that were issued when processing the keyword.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred when processing the keyword.  
##  [](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/deduplicate#samples)Example
**Request**
```
    {
      "method": "deduplicate",
      "params": {
        "Keywords": [{
          "Keyword": "A B -C"
        },
        {
          "Id": 1000,
          "Keyword": "A B -D"
        },
        {
          "Id": 1001,
          "Keyword": "A B"
        },
        {
          "Keyword": "E F"
        }]
      }
    }

```

**Response**
The keywords _A B -C_ , _A B -D_ and _A B_ are joined together into the combined keyword _A B -C -D_ :
```
- Фраза _A B -C_ новая. Ее не требуется добавлять, поскольку ее аналог уже есть в базе данных. В ответе она пропущена.
- Фраза _A B -D_ есть в базе данных, ее нужно изменить на объединенную фразу. Идентификатор фразы и новое значение возвращены в структуре `Update`.
- Фраза _A B_ есть в базе данных, ее нужно удалить. Идентификатор фразы возвращен в структуре `Delete`.

Фраза _E F_ новая, ее нужно добавить. Она возвращена в структуре `Add`.

```javascript
{
  "result": {
    "Add": [{
      "Keyword": "E F"
    }],
    "Update": [{
      "Id": 1000,
      "Keyword": "A B -C -D"
    }],
    "Delete": {
      "Ids": [ 1001 ]
    }
  }
}
```

```

Copied
### Was the article helpful?
YesNo
Previous
[KeywordsResearch: preprocessing of keywords](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/keywordsresearch)
Next
[hasSearchVolume](https://yandex.com/dev/direct/doc/en/keywordsresearch/en/keywordsresearch/hasSearchVolume)
