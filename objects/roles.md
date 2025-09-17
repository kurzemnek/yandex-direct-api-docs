---
title: Roles and access of Yandex.Direct users | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/objects/roles
crawled_at: 2025-09-17T15:40:11.751257
---

Direct advertiser
# Roles and access of Yandex.Direct users
  * [Direct advertiser](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#standalone)
  * [Agency](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#agency)
  * [Working with the API](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#agency-api)
  * [Agency client advertiser](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#subclient)
  * [Learn more](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#learn-more)


An advertiser's campaigns are managed by Yandex.Direct users. The actions available to a user depend on the user's role.
The table below shows the user roles and access for each type of client.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#standalone)Direct advertiser
A direct advertiser can have representatives with the following roles:
**Role** |  **Manage campaigns** |  **Managing the advertiser's representatives**  
---|---|---  
Chief representative |  Full access to manage the advertiser's campaigns. |  Full access to manage the advertiser's representatives: add, delete, restore, edit settings, and change the chief representative. Managing representatives is only available in the web interface (see [Registering representatives](https://yandex.com/support/direct/campaigns/representatives.html) in Yandex.Direct Help). You can't change the access level for representatives who are registered in Yandex Balance.  
Representative (full access) |  Full access to manage the advertiser's campaigns, just like the chief representative. |  Access to edit own settings.  
Representative (read only) |  They have access only to viewing campaign settings and statistics. |  Access to edit own settings.  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#agency)Agency
An agency can have representatives with the following roles:
**Role** |  **Managing agency clients and their campaigns** |  **Using agency representatives to manage accounts**  
---|---|---  
Chief representative |  Full access to manage all the agency's clients and their campaigns. |  Full access to manage the agency's representatives: add, delete, restore, edit settings, assign representatives to work with clients, and change the chief representative. Managing representatives is only available in the web interface (see [Registering agency representatives](https://yandex.com/support/direct/campaigns/agency-representatives.html) in Yandex.Direct Help). You can't change the access level for representatives who are registered in Yandex Balance.  
Representative |  Full access to manage all the agency's clients and their campaigns, just like the chief representative. |  Access to edit settings for all the agency's representatives (except the chief representative).  
Сlient representative |  Full access to manage only personal clients and their campaigns:
  * Register new agency clients.
  * Manage clients that were registered personally or that were assigned by the chief representative.

|  Access to edit own settings.  
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#agency-api)Working with the API
An agency can only work with the data of a single client in each request. Each request must pass the client username (preferably the chief representative) in the HTTP `Client-Login` header.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#subclient)Agency client advertiser
An agency can allow a client advertiser to access data:
  * If the agency granted the advertiser read-only access to the web interface, the advertiser's representatives can only receive data via the API, as well.
  * If the agency granted the advertiser permission to edit campaigns, the advertiser's representatives can use either the web interface or the API for managing their campaigns.


An agency client can have representatives with the following roles:
**Role** |  **Manage campaigns** |  **Managing the advertiser's representatives**  
---|---|---  
Chief representative |  Access to manage the advertiser's campaigns, within the permissions granted to the advertiser by the agency. |  Full access to manage the advertiser's representatives: add, delete, restore, edit settings, and change the chief representative (only if the agency gave the advertiser access to the web interface). You can't change the access level for representatives who are registered in Yandex Balance.  
Representative (full access) |  Access to manage the advertiser's campaigns, within the permissions granted to the advertiser by the agency (just like the chief representative). |  Access to edit own settings (only if the agency gave the advertiser access to the web interface).  
Representative (read only) |  They have access only to viewing campaign settings and statistics. |  Access to edit own settings.  
Thus, an agency client's campaigns can be managed either by agency representatives, or by representatives of the advertiser itself, if the agency provided appropriate access.
##  [](https://yandex.com/dev/direct/doc/en/objects/en/objects/roles#learn-more)Learn more
  * [Client](https://yandex.com/dev/direct/doc/en/objects/en/objects/client)
  * [Recommendations for registering representatives](https://yandex.com/dev/direct/doc/en/objects/en/objects/representatives-recommendations)


Copied
### Was the article helpful?
YesNo
Previous
[Access tokens](https://yandex.com/dev/direct/doc/en/objects/en/concepts/auth-token)
Next
[Interaction format](https://yandex.com/dev/direct/doc/en/objects/en/concepts/format)
