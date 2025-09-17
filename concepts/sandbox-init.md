---
title: Managing the Sandbox | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/concepts/sandbox-init
crawled_at: 2025-09-17T15:42:45.346456
---

Managing the Sandbox
# Managing the Sandbox
To use the Sandbox, enable it in the Yandex Direct interface as described below.
  1. On the **API settings** page, go to the [Sandbox](https://direct.yandex.com/registered/main.pl?cmd=apiSandboxSettings) tab.
  2. Click the **Launch sandbox** link.  
A window for creating a sandbox opens.
  3. Set parameters.
     * The **Role** that the application will play in the Sandbox:
       * Client: A regular Yandex Direct client.
       * Agency — An advertising agency (additional functionality is available for managing agency clients).
     * **Currency** of the client or agency.
     * **Create test campaigns**. If the option is selected, test data is created. For the “Client” role this creates three campaigns, and for the “Agency” role it creates three clients with three campaigns each. Client usernames are generated automatically. A certain amount of money is credited to one of the campaigns for each client.
If you unchecked this option when creating the sandbox, you can create test data later in the Yandex Direct interface (see below) or programmatically.
     * **Shared account**. If this option is selected, a client is created with a shared account enabled. This option is not available for agencies.
  4. Click **Continue**.


The Sandbox will be initialized, and the following elements will be displayed on the tab.
  * The **role** selected in the Sandbox.
  * **Currency**.
  * **Shared account** : enabled or disabled.
Note
    * If you change the role, currency, or the shared account setting, data is deleted from the Sandbox.
    * In order to change the currency or enable/disable the shared account, you must create the sandbox again. Click **Stop using "Sandbox** , then **Launch sandbox**.
  * **Master token**. Used for accessing the finance methods in the Sandbox (see in the documentation for version 4 of the API).
  * **Create test campaigns**. Deletes Sandbox data, then creates three campaigns for the “Client” role, or three clients with three campaigns each for the “Agency” role. A certain amount of money is credited to one of the campaigns for each client.
  * **Clear "Sandbox"**. Deletes Sandbox data.
  * **Reset transaction counter**. Starts the numbering over for financial operations (see in the documentation for version 4 of the API).
  * **Stop using "Sandbox"**. Deletes Sandbox data and disables the Sandbox.


### Was the article helpful?
YesNo
Previous
[Sandbox](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/sandbox)
Next
[List of terms](https://yandex.com/dev/direct/doc/en/concepts/en/concepts/glossary)
