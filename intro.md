---
title: Lesson 1. What is Yandex Direct API | Yandex Direct API
url: https://yandex.com/dev/direct/doc/en/intro
crawled_at: 2025-09-17T15:58:36.733893
---

Lesson 1. What is Yandex Direct API
# Lesson 1. What is Yandex Direct API
  * [What is an API?](https://yandex.com/dev/direct/doc/en/en/intro#intro_whats_api)
  * [Why do I need Yandex Direct API](https://yandex.com/dev/direct/doc/en/en/intro#intro_forwhat_api)
  * [Where to start](https://yandex.com/dev/direct/doc/en/en/intro#intro_begining)
  * [Objects in the web interface and API](https://yandex.com/dev/direct/doc/en/en/intro#intro_objects)
  * [Task](https://yandex.com/dev/direct/doc/en/en/intro#task)
  * [What an API request looks like](https://yandex.com/dev/direct/doc/en/en/intro#intro_request)
  * [Useful links](https://yandex.com/dev/direct/doc/en/en/intro#intro_usfull_links)


In this lesson, we will explain why Yandex Direct needs an API, and introduce you to the basics of its operation.
_Yandex Direct_ is a unified platform for placing contextual ads and banner ads. Yandex Direct serves your ads to the target audience of your business, interested in your products or services.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_start.png)
To work with Yandex Direct, all you need to do is to open a web interface, create an account, and place your ads. After that, you can manage your ads in Yandex Direct not only onamd the web, but also via the API.
Tip
If you're new to Yandex Direct, we recommend that you first take the 
##  [](https://yandex.com/dev/direct/doc/en/en/intro#intro_whats_api)What is an API?
_API_ stands for an application programming interface. The API of a service provides a set of pre-built procedures, functions, and structures that developers can use to create their programs, applications, and scripts (hereinafter referred to as apps) to interact with the service.
In other words, the API is a constructor that has a set of building blocks (functions and methods) and rules how to use them. You can build your own application based on such building blocks.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_lego_scheme.png)
When interacting with the service via the API, the application sends a request to the service and gets a response containing the data requested. The API lets you automate the workflow of operations that you perform in the web interface.
##  [](https://yandex.com/dev/direct/doc/en/en/intro#intro_forwhat_api)Why do I need Yandex Direct API
Using Direct.API, you can manage the same ads as through the web interface. The API allows you to automate routine operations, accelerate their execution, and hence boost your account management efficiency. The API is a right choice if you wish to handle large amounts of data, stay independent of the browser interface, and prefer fine-tuning your ads.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_for_what.png)
You can create an app for your tasks as an independent developer, advertiser, or advertising agency. For example, you can write a script to update bids based on your custom algorithm via the API automatically. You can integrate your corporate information system with Yandex Direct: upload a large number of ads from your database to Yandex Direct, automatically update ad texts as your product price changes, and stop and resume ad serving depending on product availability in stock. You can upload daily statistics on advertising campaigns to your analytical or finance system.
You can connect to and use the Yandex Direct API for free.
##  [](https://yandex.com/dev/direct/doc/en/en/intro#intro_begining)Where to start
To complete the course, you need to create an account in Yandex Direct. If you do not have an account yet, then create it:
  1. Log in to Yandex with the username you are going to use as an app developer. If you don't have a Yandex username, get one.
  2. In Yandex Direct web interface (**Get started** button.
  3. Enter an email address you currently use, select your country and currency. Click **Start using the service**.
  4. Create your first advertising campaign: we recommend you to select "Text & Image Ads" campaign type. Specify the campaign parameters and create your first ad. For now, it is sufficient to create one draft ad with a single keyword. You don't need to submit ads for review or deposit money for the campaign.


Note
For instructions on how to create an account in Yandex Direct, see 
Now you have an account in Yandex Direct. Let's see what your ads look like in the web interface and in the API.
##  [](https://yandex.com/dev/direct/doc/en/en/intro#intro_objects)Objects in the web interface and API
A Yandex Direct ad campaign contains ad groups, each of which contains ads and keywords. Ads can include additional elements, such as images, site links, and others.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_adv_screenshot.png)
Links between objects in the API is shown in the diagram:
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_objects_scheme.png)
  * `Campaign` — advertising campaign, `AdGroup` — ad group, `Ad` — ad.
  * Ad extensions: `AdImage` — an image, `VCard` — a virtual business card, `SitelinksSet` — a set of sitelinks, `AdExtension` — a callout.
  * Ad group targeting criteria: `Keyword` — keyword (and others, depending on the campaign type). You can set a bid for a targeting criteria — `KeywordBid`.


![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_objects_screenshot.png)
##  [](https://yandex.com/dev/direct/doc/en/en/intro#task)Task
Go through the settings of your advertising campaign in Yandex Direct. Create new ads with different parameters. If you do not want to launch a real campaign, do not submit your ad groups for moderation to keep your ads in the "Draft" status.
##  [](https://yandex.com/dev/direct/doc/en/en/intro#intro_request)What an API request looks like
You can retrieve the ads you see in the web interface, using API requests. You can also make changes using API requests, and see the result immediately reflected in the web interface. The API works with each object individually: different API methods allow you to create an ad, update a vCard, get statistics, and more.
Here is the API request allowing you to retrieve the list of the user's ad campaigns. The request is sent using the HTTPS protocol's POST method.
![](https://yandex.com/dev/direct/doc/en/docs-assets/dev-direct/rev/f4a886bf8b0e7d4eb651fadce7b571ee835bbe0a/en/_assets/intro_request.png)
In the next lessons, you will step through all the initial steps of working with the API:
  * You will learn how to get access to the API: register your application with Yandex OAuth service, apply for access, and get an OAuth token.
  * Also, you will learn to set up Sandbox: a testing debug environment for your app.
  * You will learn to write API requests: you will get familiar with services and methods provided by the API and learn request structure details.
  * Finally, you will get some advice on how to proceed from Sandbox practice to handling real-life ads of real users.


We strongly recommend that you go through the lessons in their native order. Previous lesson information (and results of actions you performed there) are prerequisite for each next lesson.
Best of luck!
##  [](https://yandex.com/dev/direct/doc/en/en/intro#intro_usfull_links)Useful links
Copied
### Was the article helpful?
YesNo
Previous
[About](https://yandex.com/dev/direct/doc/en/en/start)
Next
[Lesson 2. API access: how to register an app in Yandex OAuth](https://yandex.com/dev/direct/doc/en/en/register)
