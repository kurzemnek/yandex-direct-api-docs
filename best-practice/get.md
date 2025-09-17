---
title: Getting data: the "get" method | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/best-practice/get
crawled_at: 2025-09-17T15:40:28.245806
---

Getting only requested data
# Getting data: the "get" method
  * [Getting only requested data](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#field-names)
  * [Example](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example)
  * [Selection criteria](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#criteria)
  * [Example](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example1)
  * [Paginated selection](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#page)
  * [Example 1](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example-1)
    * [How to determine whether all objects have been received](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#page1)
  * [Example 2](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example-2)
  * [Example 3](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example-3)


##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#field-names)Getting only requested data
When calling the _get_ method, you must explicitly list the parameters you want to get in the `FieldNames` array.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example)Example
If the request specifies
```
"FieldNames": ["Id","Name","Status"]

```

you will get IDs, names, and statuses of objects.
If you need to get a parameter that does not have a value set, the _get_ method returns "null" in this parameter. See the section [The null (nil) value](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/nillable).
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#criteria)Selection criteria
Use the `SelectionCriteria` input structure for filtering objects in the _get_ method. The set of criteria differs for different services. It is given in the description of the _get_ method for each service.
Each criterion works like the IN operator in SQL. If you set multiple criteria, they are combined with AND: you will get objects that match all the criteria. If no objects matching the criteria are found, an empty structure is returned.
Note
The _get_ method ignores the IDs of objects that are non-existing, deleted, or don't belong to an advertiser. It doesn't return any warnings or errors for such IDs.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example1)Example
If the request sets the criteria
```
"SelectionCriteria": {
   "CampaignIds": [1234567,1234589,1234777],
   "Statuses": ["PREACCEPTED","ACCEPTED"]
}

```

you will get objects with the status `PREACCEPTED` or `ACCEPTED` that belong to the campaigns 1234567, 1234589 or 1234777. Similar to the SQL statement `SELECT ... WHERE CampaignId IN (1234567,1234589,1234777) AND Status IN ("PREACCEPTED","ACCEPTED")`.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#page)Paginated selection
The _get_ method returns a maximum of 10,000 objects per request. To get paginated data, use the structure
```
"Page": { /* LimitOffset */
   "Limit": (long),
   "Offset": (long)
}

```

**Parameter** |  **Type** |  **Description** |  **Mandatory**  
---|---|---|---  
**LimitOffset structure** |   
`Limit` |  long |  Number of returned objects (page size). From 0 to 10,000. If omitted, the limit is 10,000. |  No  
`Offset` |  long |  The number of objects that should be skipped when getting the selection. If omitted, 0 is assumed. |  No  
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example-1)Example 1
If the request sets this:
```
"Page": { /* LimitOffset */
   "Limit": 200,
   "Offset": 600
}

```

objects numbered 601 to 800 will be returned.
###  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#page)How to determine whether all objects have been received
If the page returned is not the last one (there are more objects remaining in the selection), the `get` method returns the `LimitedBy` field — the number of the last object returned. To get the next page, specify the `LimitedBy` value as `Offset` for the next call of the `get` method, with the same `SelectionCriteria`.
##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example-2)Example 2
If the response to the `get` method in Example 1 does not contain the `LimitedBy` parameter, this is the last page in the selection.
If the response contains the `LimitedBy` parameter with the value 800, the next request must specify
```
"Page": { /* LimitOffset */
   "Limit": 200,
   "Offset": 800
}

```

##  [](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/get#example-3)Example 3
If the request did not have the `Page` structure, but the response contains the `LimitedBy` parameter set to 10,000, this means that the selection contains more than 10,000 objects and only the first page was returned. To get the next page, the next request must specify
```
"Page": { /* LimitOffset */
   "Offset": 10000
}

```

The `Limit` parameter is not required. By default, the limit is 10,000.
Copied
### Was the article helpful?
YesNo
Previous
[General method properties in the API version 5](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/principles)
Next
[Operations on object arrays](https://yandex.com/dev/direct/doc/en/best-practice/en/best-practice/modify)
