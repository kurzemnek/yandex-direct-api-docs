---
title: update | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/retargetinglists/update
crawled_at: 2025-09-17T15:55:02.062121
---

Restrictions
# update
  * [Restrictions](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/update#restrictions)
  * [Request](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/update#input)
  * [Response](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/update#output)


Changes the parameters of retargeting lists.## Learn more
  * [How the "update" method works](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html)
  * [How to handle errors](https://yandex.com/dev/direct/doc/dg/concepts/errors.html)


##  [](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/update#restrictions)Restrictions
Maximum of 1000 retargeting lists per method call.
##  [](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/update#input)Request
Request structure in JSON format:
```
{
  "method": "update",
  "params": { /* params */
    "RetargetingLists": [{  /* RetargetingListUpdateItem */
      "Id": (long), /* required */
      "Name": (string),
      "Description": (string),
      "Rules": [{  /* RetargetingListRuleItem */
        "Arguments": [{  /* RetargetingListRuleArgumentItem */
          "MembershipLifeSpan": (int),
          "ExternalId": (long) /* required */
        }, ... ], /* required */
        "Operator": ( "ALL" | "ANY" | "NONE" ) /* required */
      }, ... ]
    }, ... ] /* required */
 }
}

```

**Parameter** |  **Type** |  **Description** |  **Required**  
---|---|---|---  
**params structure (for JSON) / UpdateRequest structure (for SOAP)** |  |  |   
`RetargetingLists` |  array of [RetargetingListUpdateItem](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/update#RetargetingListUpdateItem) |  Retargeting lists to modify. |  Yes  
**RetargetingListUpdateItem structure** |  |  |   
`Id` |  long |  ID of the retargeting list. |  Yes  
`Name` |  string |  Name of the retargeting list (maximum of 250 characters). |  No  
`Description` |  string |  Text note for the retargeting list (maximum of 4096 characters). |  No  
`Rules` |  array of RetargetingListRuleItem |  Rules for selecting site users. In order for the retargeting list to apply, the user must meet all the rules at once.  
For restrictions on user selection rules and examples of the structure, see the section [Rules for user selection](https://yandex.com/dev/direct/doc/dg/objects/retargeting-list.html). |  No  
**RetargetingListRuleItem structure** |  |  |   
`Arguments` |  array of RetargetingListRuleArgumentItem |  Goals and segments. See the section [Goals and segments](https://yandex.com/dev/direct/doc/dg/objects/retargeting-list.html). |  Yes  
`Operator` |  RetargetingListRuleOperatorEnum |  Logical operator for the retargeting list:
  * ALL — the rule is met if the user completed all the goals and is included in all the segments.
  * ANY — The rule is met if the user completed at least one of the goals or the user's session is included in at least one of the segments.
  * NONE — The rule is met if the user didn't complete any of the goals and the user's session isn't included in any of the segments.

|  Yes  
**RetargetingListRuleArgumentItem structure** |  |  |   
`MembershipLifeSpan` |  int |  The number of days (from 1 to 540) for checking for a goal conversion. For Yandex Metrica and Yandex Audience segments, this parameter is not used and the passed value is ignored. |  For Yandex Metrica goals  
`ExternalId` |  long |  ID of the goal or segment. For segments by [user interests](https://yandex.com/support/direct/products-cpm-campaign/display-ads-settings.dita#display-ads-settings/user-interests), use identifier prefixes to specify interest types:
  * 10 — A short-term interest.
  * 20 — A long-term interest.
  * 30 — Any interest.

For example, the segment ID `2499001105` with a long-term interest will become `ExternalId``202499001105`. |  Yes  
##  [](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/update#output)Response
Response structure in JSON format:
```
{
  "result": {  /* result */
    "UpdateResults": [{  /* ActionResult */
      "Id": (long),
      "Warnings": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ],
      "Errors": [{  /* ExceptionNotification */
        "Code": (int), /* required */
        "Message": (string), /* required */
        "Details": (string)
       }, ...
      ]
    }, ... ] /* required */
  }
}

```

**Parameter** |  **Type** |  **Description**  
---|---|---  
**result structure (for JSON) / UpdateResponse structure (for SOAP)** |  |   
`UpdateResults` |  array of ActionResult |  Results of changing parameters for retargeting lists.  
**ActionResult structure** |  |   
`Id` |  long |  ID of the retargeting list. Returned if there aren't any errors. See the section [Operations on object arrays](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html).  
`Warnings` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Warnings that occurred during the operation.  
`Errors` |  array of [ExceptionNotification](https://yandex.com/dev/direct/doc/dg/best-practice/modify.html) |  Errors that occurred during the operation.  
Copied
### Was the article helpful?
YesNo
Previous
[get](https://yandex.com/dev/direct/doc/en/retargetinglists/en/retargetinglists/get)
Next
[Sitelinks: operations with sitelinks](https://yandex.com/dev/direct/doc/en/retargetinglists/en/sitelinks/sitelinks)
