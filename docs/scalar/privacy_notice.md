---
title: Element Manager and Connected Services Privacy Notice
slug: Privacy Notice
section: legal
version: 2.0.0
---

## 1. Introduction

### 1.1 English, Not Legalese

Privacy is important, and we want you to understand the issues involved. We have decided to use plain English as much as possible, to make our terms as clear as possible.

When you read 'the integration manager' below, it refers to the integration managers made available by Element (a trading name of New Vector Ltd.), which provide bots, bridges, widgets and sticker packs to Matrix users. Element hosts several integration manager instances - today these include:

* The primary instance, currently made available to compatible Matrix clients at https://scalar.vector.im

* The staging instance, currently made available to compatible Matrix clients at https://scalar-staging.vector.im

This agreement covers all of these instances, and any others that we may choose to provide on https://vector.im or any subdomain (https://\*.vector.im). We might change which instances we run, and how they are accessed, at any time.

Where you read *Element*, *we* or *us* below, it refers to the company created in July 2017 to hire the Matrix core team and support Matrix's development: New Vector Ltd., its French subsidiary: New Vector SARL, and their agents. Element is trading name of New Vector.

Should you have other questions or concerns about this document, please send us an email at [support@element.io](mailto:support@element.io).

### 1.2 Who Provides this Service?

This service is provided by Element. Element is the Data Controller for this service.

**This agreement does not apply to integration managers run by anybody else. Matrix is an open network like the Web and this agreement only applies to the integration manager provided by Element**

#### 1.2.1 Contact Details

##### Element

Email: [support@element.io](mailto:support@element.io

Postal address:

c/o New Vector Ltd
10 Queen Street Place  
London  
United Kingdom  
EC4R 1AG

### 1.3 What is the scope of this document?

New Vector uses an integration manager to give you access to additional connected services such as bots, bridges, widgets and sticker packs. This document details how your data is processed when you make use of these connected services.

### 1.4 This Is a Living Document

This is a living document. With your help, we want to make our policy documents the best in the industry.

If you read something that rubs you the wrong way, or if you think of something that should be added, please get in touch! We're all ears! Email [support@element.io](mailto:support@element.io) and we'll chat.

We don't amend this document for any specific users or use case, but if your proposed changes apply to all of our users, we'll be happy to update it for everyone. Scroll to the bottom to see the history so far.

We will likely improve this document over time. By continuing to use the Service, you will implicitly accept the changes we make.

Your access and use of the Service is always subject to the most current version of this document.

## 2. What is a Matrix Integration Manager?

A Matrix integration manager connects additional services into the Matrix ecosystem, such as bots, bridges widgets, and sticker packs. Integration managers can provide services for free, in exchange for payment, or a mixture of both.

A Matrix integration manager is usually closely coupled with a particular Matrix homeserver. Usually, bots and bridges are connected directly to this homeserver, and, if that homeserver is federated, exposed to the wider Matrix network over federation.

A Matrix client may use one or many integration managers, or no integration manager at all. This choice might be exposed to you as the user, or it might be made on your behalf by the client vendor or administrator.

Some integration managers support delegating some or all functionality to other integration managers.

The integration manager architecture is very flexible, so it is possible for an integration manager to provide services outside of the mechanisms described above. You should always consult your chosen integration manager's privacy policy for the specific details.

### 2.1 What's a bot?

A bot appears like Matrix user, but it is programmed to respond or take actions automatically. A bot might provide functionality directly, or through connecting to an external service.

### 2.2 What's a bridge?

A bridge connects Matrix to a third-party service. Different bridges have different capabilities (based on the features offered by the third-party service and the implementation of the bridge). Usually, a bridge will connect a Matrix room to a room or channel on a third party service, allowing users on both sides of the bridge to see the same messages and communicate with one another.

Some bridges support a feature called puppeting. Puppeting allows a bridge to use your real account on another service to send messages as if you were using that service directly. Some bridges (such as the New Vector-run IRC bridges) will do this automatically, where other bridges require further manual steps to link an account.

Bridges which do not support puppeting, or do not have it enabled will post your messages from a bot user on the remote server which may or may not use your displayname and avatar.

### 2.3 What's a widget?

A widget is a small web application that can be attached to a Matrix room and shared with the other users in that room.

### 2.4 What's a sticker pack?

A sticker pack is a set of images grouped together in a bundle. Ownership of a sticker pack means that you can choose a sticker from that bundle and send it as a message into a room using the sticker picker.

Some sticker packs are free, others can be purchased through the integration manager.

Stickers are selected to send using a sticker picker, which is itself a widget provided by the integrations manager.

## 3. Access to Your Data / Privacy Policy

### 3.1 What is the legal basis for processing my data and how does this affect my rights under GDPR (General Data Protection Regulation)?

#### 3.1.1 Legal Basis for Processing

Your data is processed under *[Legitimate Interest](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/legitimate-interests/when-can-we-rely-on-legitimate-interests/)*. This means that we process your data only as necessary to deliver the Service, and in a manner that you understand and expect.

The *Legitimate Interest* of the Service is the ability to make use of additional services connected into the Matrix ecosystem. The processing of user data we undertake is necessary to provide the Service. **This facility is an optional component of the services provided by Element** - Matrix works very well without an integration manager.

#### 3.1.2 Right to Erasure

We are working on bots' and bridges' exposing uniform support for erasure of configuration data. Until this is in place, data is erased manually. If you deactivate your account on the matrix.org homeserver we will within 30 days run a manual erasure process to delete your data from Element-provided bots and bridges. If you have an account on a different homeserver, or if you would like to erase your data on a subset of bots/bridges or without deactivating your account, please get in touch with [dpo@matrix.org](mailto:dpo@matrix.org).

#### 3.1.3 Data Portability

Under GDPR you have a right to request a copy of your data in a commonly-accepted format. If you would like a copy of your data from the integration manager, please send a request over Matrix to [dpo@matrix.org](mailto:dpo@matrix.org).

#### 3.1.4 Your Rights as Data Subject

You have rights in relation to the personal data we hold about you. Some of these only apply in certain circumstances. Some of these rights are explored in more detail elsewhere in this document. For completeness, your rights under GDPR are:

1. The right to be informed

2. The right of access

3. The right to rectification

4. The right to erasure

5. The right to restrict processing

6. The right to data portability

7. The right to object

8. Rights in relation to automated decision making and profiling.

For more details about these rights, please see [the guidance provided by the ICO](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/). If you have any questions or are unsure how to exercise your rights, please contact us at [dpo@matrix.org](mailto:dpo@matrix.org).

### 3.2 What Information Do You Collect About Me and Why?

**The information we collect is purely for the purpose of letting people use bots, bridges, widgets and sticker packs within the federated Matrix ecosystem. We do ****not**** profile users or their data on the Service.**

Data required to support the operation of bots, bridges, widgets and sticker packs via the New Vector integration manager may be collected across _four different service layers_. Use of the Element integration manager may cause your personal data to be persisted to:

* room data, stored on your homeserver and subject to the privacy policy of your chosen homeserver

* the Element integration manager, subject to this privacy policy

* configuration metadata within the New Vector-provided bots and bridges, subject to this privacy policy

* the connected (or bridged) third-party service, subject to the privacy policy associated with that service

The precise details will vary depending on the implementation and feature set of your chosen integration, but the following is designed to illustrate the persistence of personal data in some representative common cases:

| Integration | Matrix homeserver | Integration manager | Bridge/bot configuration metadata | Third party connected service |
|-------------|-------------|---------------------|-----------------------------------|-------------------|
| Bot | The bot's membership is persisted to the room state events and timeline | Setup metadata (who invited the bot, some at-setup configuration metadata) | Anything the bot might require to function - most likely third party service connection data such as OAuth access tokens or username/password | Bots have visibility on all events in any room in which they participate, so the bot may choose to share all events with a third party connected service. |
| Bridge | Membership and messages sent by users on third party connected services may be persisted to the room state events and timeline | n/a | Anything the bridge might require to function - most likely webhook URLs or third party service connection data such as OAuth access tokens or username/password | The visibility a bridge has is configured by the homeserver admin - a bridge will usually be configured by the bridge provider to have access to a restricted set of namespaced rooms and users. | The purposed of a bridge is to share traffic between Matrix and a third party connected service, usually bidirectionally, so you can assume that all events in all bridged rooms are persisted to the third party connected service.
| Widget | All widget configuration data is persisted to room state events. | Setup metadata (who configured the widget, some at-setup configuration metadata) | n/a | Anything shared with the widget, potentially including the user's display name, avatar, matrix ID and choice of theme within Element, as well as connection data such as IP address, may be persisted by the third party service providing the widget |
| Sticker pack | Stickers sent by the user are persisted to the room timeline | Which sticker packs are enabled/purchased is tracked within the integration manager | n/a | n/a | 

#### 3.2.1 Information you provide to us when configuring connected services:

We collect (within the integration manager and the configuration metadata for the New Vector-run bots and bridges) information about you when you configure bots, bridges, widgets or sticker packs using the New Vector integration manager.

##### Bots

* Matrix ID (including homeserver)

* Possibly, depending on the bot implementation and feature set:

    * Bot-specific configuration options

    * Third-party service access credentials (password, OAuth token or similar)

##### Bridges

* Matrix ID (including homeserver)

* Matrix room ID

* Possibly, depending on the bridge implementation and target network:

    * Bridged platform ID

    * Bridged platform access credentials (password, OAuth token or similar)

    * Bridged platform room analogue ID

    * Custom nicknames to be displayed over the bridge

    * Per-user configuration options

##### Widgets

* Matrix ID (including homeserver)

* Possibly, depending on the widget implementation and feature set:

    * Widget-specific configuration options

    * Display name

    * Avatar

    * Riot theme

    * Room id

##### Sticker packs

* Matrix ID (including homeserver)

* Activated sticker pack ID

#### 3.2.2 Information you provide to us when using connected services:

##### Bots

All unencrypted events in rooms in which a Element-managed bot is participating are theoretically visible to New Vector.

Bots log activity, including in some cases user-sent message text, as part of standard service operation. These logs are held for not longer than 14 days.

##### Bridges

All traffic sent via the bridges is visible to Element, and may be logged as part of standard service operation. These logs are held for not longer than 14 days.

##### Widgets

All data shared with widgets hosted by Element is visible to Element.

All data shared with widgets hosted by third party providers is visible to the third party provider and subject to their Privacy policy.

##### Sticker packs

* If you are using the Element sticker picker, Element can see which sticker packs you have enabled on your account.

#### 3.2.3 Information we collect automatically as you use the Integration Manager

In addition to the information you provide, the integration manager also logs your IP address and user agent. This data is used in order to mitigate abuse, debug operational issues, and monitor traffic patterns. These logs are held for not longer than 60 days.

IP addresses and user agent are logged by the integration manager when you configure a bot or bridge.


### 3.3 What Information is Shared With Third Parties and Why?

#### 3.3.1 Sharing Data with Connected Services

Many bots and bridges exist to share data with connected third party services. The nature of the data shared depends on the features, implementation and policies of the third party provider.

#### 3.3.2 Does the New Vector Integration Manager Delegate Functionality to Other Integration Managers?

No.

### 3.4 Sharing Data in Compliance with Enforcement Requests and Applicable Laws; Enforcement of Our Rights

In exceptional circumstances, we may share information about you with a third party if we believe that sharing is reasonably necessary to 

(a) comply with any applicable law, regulation, legal process or governmental request, 

(b) protect the security or integrity of our products and services (e.g. for a security audit),

(c) protect Element, The Matrix.org Foundation, and our users from harm or illegal activities, or

(d) respond to an emergency which we believe in good faith requires us to disclose information to assist in preventing the serious bodily harm of any person.

### 3.5 Our Commitment to Children's Privacy

We never knowingly collect or maintain information in the Service from those we know are under 16, and no part of the Service is structured to attract anyone under 16. If you are under 16, please do not use the Service.

### 3.6 How Can I Access or Correct My Information?

We are in the process of improving our tooling to access information supplied to the integration manager. For the time being, if you would like access to this data, please submit a request to [dpo@matrix.org](mailto:dpo@matrix.org) and we'll provide manual assistance.

### 3.7 Who can see my service configuration data?

Integration manager setup configuration metadata and bot/bridge configuration data are stored in Element databases. Element employees and agents can access this data, subject to the Element data access guidelines detailed below.

### 3.8 What Are the Guidelines New Vector Follows When Accessing My Data?

* We restrict who at Element (employees and contractors) can access user data to roles which require access in order to maintain the health of the Service.

* We never share what we see with other users or the general public.

### 3.9 Who Else Has Access to My Data?

We host the majority of the Service in [UpCloud](https://www.upcloud.com/) data centres. Here's [UpCloud's privacy policy](https://www.upcloud.com/blog/updated-terms-privacy-policy-gdpr/). UpCloud controls physical access to their locations.

We use Cloudflare to mitigate the risk of DDoS attacks. Here's [Cloudflare's privacy policy](https://www.cloudflare.com/privacypolicy/).

Physical access to our offices and locations use typical physical access restrictions.

We use secure private keys when accessing servers via SSH, and protect our AWS console passwords locally with a password management tool.

We log application data (caller IP and user agent). We keep logs for no longer than 60 days.

### 3.10 What happens if Element is sold?

In the event that we sell or buy any business or assets, we may disclose your personal data to the prospective seller or buyer of such business or assets.

If we or substantially all of our assets are acquired by a third party, personal data held by us about our users will be one of the transferred assets.

### 3.11 How Is My Data Protected from Another User's Data?

All of our users' data for the Service currently resides in the same database cluster which is due to the nature of our Service. We use software best practices to guarantee that only people who you designate as viewers of your data can access it. In other words, we segment our user data via software. We do our best and are very confident we're doing a good job at it, but, like every other service that hosts their user data on the same database, we cannot guarantee that it is immune to a sophisticated attack.

### 3.12 What Should I Do If I Find a Security Vulnerability in the Service?

If you have discovered a security concern, please follow the Matrix.org [Security Disclosure Policy](https://matrix.org/security-disclosure-policy/).

## 4. Making a Complaint

We try to meet the highest standards when collecting and using personal information. For this reason, we take any complaints we receive about this very seriously. We encourage people to bring it to our attention at [support@vector.im](mailto:support@vector.im) if they think that our collection or use of information is unfair, misleading or inappropriate. We would also welcome any suggestions for improving our procedures.

If you want to make a complaint about the way we have processed your personal information to the supervisory authority, you can contact the ICO (the statutory body which oversees data protection law) at [https://www.ico.org.uk/concerns](https://www.ico.org.uk/concerns).

## 5. Document History

* 2019, July 23: created (content derived from [Matrix.org Homeserver Privacy Policy](https://matrix.org/legal/privacy-notice)).
* 2020, July 14: brand name changes

**A note to other startups:** this document was heavily inspired by [Balsamiq's plain English ToS document](https://docs.balsamiq.com/mybalsamiq/tos/). We were impressed by their championing of plain English, and wanted to reproduce that as much as possible in our own legal documentation. Feel free to draw similar inspiration from this document, though be sure to get any documents you produce checked over by a lawyer. Good luck!

