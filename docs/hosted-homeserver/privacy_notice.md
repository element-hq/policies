# {{ hhs_entity_name }} ({{ hhs_name }}.{{ hhs_server_domain }}) Homeserver Privacy Notice

Please read this document carefully before accessing or using this service!

## 1. Introduction

### 1.1 English, Not Legalese

Most Terms of Use and Privacy Policy documents are unreadable. They are written by lawyers and for lawyers, and in our opinion are not very effective.

Data privacy is important, and we want you to understand the issues involved. For that reason we decided to use plain English instead as much as possible, to make our terms as clear as possible. Some sections still have room for improvement - we plan to tackle these over time.

Where you read 'the {{ hhs_name }}.{{ hhs_server_domain}} homeserver' or 'the Service' below, it refers to the services made available at **{{ hhs_name }}.{{ hhs_server_domain}}** which store your account and personal conversation history, provide integrations such as bots and bridges, and communicate via the open Matrix decentralised communication protocol with the public Matrix Network.

Where you read *New Vector*, *New Vector Ltd.* or *we *or* us* below, it refers to New Vector Ltd., and its French subsidiary: New Vector SARL and their agents. **This agreement does not apply to Matrix servers run by anyone else - Matrix is an open network like the Web and this agreement only applies to the server ({{ hhs_name }}.{{ hhs_server_domain}}) provided by New Vector Ltd.**

If this agreement is not acceptable, please use a Matrix server provided by someone else!

{{ hhs_entity_name }} is the Data Controller for the Service. They can be contacted as per the details below:
[{{ hhs_admin_email }}](mailto:{{ hhs_admin_email }})

New Vector Ltd. is the Data Processor for the Service. We can be contacted as per the details below:

Email: [support@modular.im](mailto:support@modular.im)

Postal address:
10 Queen Street Place,
London,
United Kingdom,
EC4R 1AG

Should you have other questions or concerns about this document, please send us an email at [support@modular.im](mailto:support@modular.im).

### 1.2 Scope of This Document

This document explains Data Privacy to the Users of the {{ hhs_name }}.{{ hhs_server_domain}} homeserver.

### 1.3 The Customer and The User

Put simply, you're a Customer if you're paying (or otherwise compensating) New Vector Ltd to provide a hosted messaging service. If you have an account registered on {{ hhs_name }}.{{ hhs_server_domain}} that you use to send and receive messages, you're a User.

It is possible to be both a Customer and a User, but we encourage you to consider these roles separately when thinking about Data Privacy.

### 1.4 Using The Service Means Accepting These Terms

By accessing or using the Service in any way, whether you have created a Matrix account on the {{ hhs_name }}.{{ hhs_server_domain}} homeserver, or whether you are accessing content federated from the {{ hhs_name }}.{{ hhs_server_domain}} homeserver to another Matrix homeserver, or are just browsing rooms as an unauthenticated guest, you agree to and are bound by the terms and conditions written in this document.

If you do not agree to all of the terms and conditions contained in this document, please use a Matrix server provided by someone else and refrain from accessing content federated from this server.

### 1.5 Changes to This Document

This is a living document. With your help, we want to make it the best in the industry.

If you read something that rubs you the wrong way, or if you think of something that should be added, please get in touch! We're all ears! Email [support@modular.im](mailto:support@modular.im) and we'll chat.

We don't amend this document for any specific Customers, Users or use case, but if your proposed changes apply more broadly, we'll be happy to update it for everyone. Scroll to the bottom to see the history so far.

If we make a material change to this document we will provide the Customer with reasonable notice prior to the change coming into effect. We will set forth the date upon which the changes will become effective, and any use of the Service by a User after said date will constitute the Customer's acceptance of these changes.

Your access and use of the Service is always subject to the most current version of this document.

## 2. Access to Your Data / Privacy Policy

### 2.1 What is the legal basis for processing my data and how does this affect my rights under GDPR (General Data Protection Regulation)?

#### 2.1.1 Legal Basis for Processing

New Vector processes your data under *[Legitimate Interest](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/legitimate-interests/when-can-we-rely-on-legitimate-interests/)*. This means that we process your data only as necessary to deliver the Service, and in a manner that you understand and expect.

The *Legitimate Interest* of our Service is the hosting and management of Matrix homeservers, providing decentralised, openly-federatable and (optionally) end-to-end encrypted communication services. The processing of user data we undertake is necessary to provide the Service. The nature of the Service and its implementation results in some  caveats concerning this processing, particularly in terms of GDPR Article 17 *Right to Erasure (Right to be Forgotten)*. We believe these caveats (discussed in the section below in detail) are in line with the broader societal interests served by providing the Service.

In situations where the interests of the individual appear to be in conflict with the broader societal interests, we will seek to reconcile those differences guided by our Exceptional Erasure Policy.

#### 2.1.2 Data Ownership

This Matrix.org hosted homeserver is a service paid for by the Customer. The Customer owns and controls all messages and files submitted to their homeserver by User accounts registered natively on their homeserver. This ownership does not extent to messages and files submitted over federation or bridging.

This means that, in addition to the usual data access controls defined by the Matrix protocol, all unencrypted messages and files can be accessed by the Customer, and that access will be retained even after no User account within the system retains access to the data.

#### 2.1.3 Right to Erasure

You can request that the Data Controller (see above) forget your copy of messages and files by instructing them to deactivate your account (using a matrix client such as [https://riot.im/app](https://riot.im/app)) and selecting the option instructing them to forget your messages. What happens next depends on who else had access to the messages and files you had shared.

Any messages or files that were only accessible by your account will remain accessible to the Customer for the duration of the homeserver. These messages and files will be inaccessible to all other Users.

Where you shared messages or files with another registered Matrix user, that user will still have access to their copy of those messages or files. Apart from state events (see below), these messages and files will *not* be shared with any unregistered or new users who view the room after we have processed your request to be forgotten.

State events are processed differently to non-state events. State events are used by the Service to record, amongst other things, your membership in a room, the configuration of room settings, your changing of another user's power level and your banning a user from a room. Were we to erase these state events from a room entirely, it would be very damaging to other users' experience of the room, causing banned users to become unbanned, revoking legitimate administrator privileges, etc. We therefore share state events sent by your account with all non-essential data removed ('redacted'), even after we have processed your request to be forgotten. This means that your username will continue to be publicly associated with rooms in which you have participated, even after we have processed your request to be forgotten. We are actively [working on a solution to ](https://matrix.org/blog/2018/05/08/gdpr-compliance-in-matrix/#mxid_erasure)[work around](https://matrix.org/blog/2018/05/08/gdpr-compliance-in-matrix/#mxid_erasure)[ this restriction](https://matrix.org/blog/2018/05/08/gdpr-compliance-in-matrix/#mxid_erasure) and allow you to be fully forgotten while maintaining a high quality experience for other users. If this is not acceptable to you, please do not use the Service.

#### 2.1.4 Data Portability

Under GDPR you have a right to request a copy of your data in a commonly-accepted format. If you would like a copy of your data, please send a request to the Data Controller (see above).

#### 2.1.5 Your Rights as Data Subject

You have rights in relation to the personal data we hold about you. Some of these only apply in certain circumstances. Some of these rights are explored in more detail elsewhere in this document. For completeness, your rights under GDPR are:

1. The right to be informed

2. The right of access

3. The right to rectification

4. The right to erasure

5. The right to restrict processing

6. The right to data portability

7. The right to object

8. Rights in relation to automated decision making and profiling.

For more details about these rights, please see [the guidance provided by the ICO](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/). If you have any questions or are unsure how to exercise your rights, please contact us at [support@modular.im](mailto:support@modular.im).

### 2.2 What Information Do You Collect About Me and Why?

#### **The information we collect is purely for the purpose of providing your communication service via Matrix. We do ****not**** profile users or their data on the Service.**

#### Be aware that while we do not profile users on the Service, Matrix clients may gather usage data - for instance Riot.im (the Matrix client provided by New Vector Ltd) optionally gathers anonymised opt-in usage data in order to improve the app.

#### 2.2.1 Information you provide to us:

We collect information about you when you input it into the Service or otherwise provide it directly to us, and process it in accordance with the Customer's instructions.

##### Account and Profile Information

We collect information about you when you register for an account. This information is kept to a minimum on purpose, and is restricted to:

* Username

* Password

* Display Name (if you choose to provide one)

* Your email address (if you choose to provide it)

* Your verified telephone number (if you choose to provide it)

Your username and password is used to authenticate your access to the Service and to uniquely identify you within the Service.

Your email address and/or telephone number, if you choose to provide them, are used so that other users can look up your Matrix ID from these identifiers. We will also use your email address to let you reset your password if you forget it, and to send you notifications about missed messages from users trying to contact you on Matrix if you enable the option. We may also send you infrequent urgent messages about platform updates.

##### Content you provide through using the Service

We store and distribute the messages and files you share using the Service (and across the wider Matrix ecosystem via federation) as described by the Matrix protocol, in accordance with the Customer's instructions, and according to the access rules configured within the system. **Storing and sharing this content is the reason the Service exists.**

This content includes any information about yourself that you choose to share.

#### 2.2.2 Information we collect automatically as you use the service:

##### Device and Connection Information

Each device you use to access the Service is allocated a (user-configurable) identifier. When you access the Service, we record the device identifier, the IP address it used to connect, user agent, and the time at which it last connected to the service.

This information is gathered to help you to manage your devices - you can view and manage the list of devices by connecting to the Service with a Matrix client such as [https://riot.im/app](https://riot.im/app).

Currently, we log the IP addresses of everyone who accesses the Service. This data is used in order to mitigate abuse, debug operational issues, and monitor traffic patterns. Our logs are kept for not longer than 180 days. Once Matrix is out of beta we will consider implementing log minimisation.

### 2.3 What Information is Shared With Third Parties and Why?

#### 2.3.1 Sharing Data with Connected Services

The {{ hhs_name }}.{{ hhs_server_domain}} homeserver is a *decentralised* and, if the Customer has enabled federation, *open* service. If federation is enabled, to support communication between users on different homeservers or different messaging platforms, your username, display name and messages and files are sometimes shared with other services that are connected with the {{ hhs_name }}.{{ hhs_server_domain}} homeserver.

##### Federation

If the Customer has enabled federation, then the {{ hhs_name }}.{{ hhs_server_domain}} homeserver will share user data with the wider ecosystem over federation:

* When you send messages or files in a room, a copy of the data is sent to all participants in the room. If these participants are on remote homeservers, your username, display name, messages and files may be replicated across each participating homeserver.

* We will forget your copy of your data upon your request. We will also forward your request to be forgotten onto federated homeservers. However - these homeservers are outside our span of control, so we cannot guarantee they will forget your data.

* Federated homeservers can be located anywhere in the world, and are subject to local laws and regulations.

Access control settings are shared between homeservers, as well as any requests to remove messages by "redactions", or remove personal data under GDPR Article 17 *Right to Erasure (Right to be Forgotten)*. Federated homeservers and Matrix clients which respect the Matrix protocol are asked to honour these controls and redaction/erasure requests, but other federated homeservers are outside of the span of control of New Vector Ltd., and we cannot guarantee how this data will be processed. Federated homeservers can also be located in any territory, and will be subject to the local regulations of that territory. We recommend the use of end-to-end encryption to protect your message and file data over federation, and in future [intend to enable end-to-end encryption by default](https://github.com/vector-im/riot-web/issues/6779). If the way in which data is shared is not acceptable to you, please use a different server or service.

##### Bridging

Some Matrix rooms are bridged to third-party services, such as IRC networks, twitter or email. When a room has been bridged, your username, display name, messages and file transfers may be duplicated on the bridged service where supported.

* It may not be technically possible to support your management of your data once it has been copied onto a bridged service.

* Bridged services can be located anywhere in the world, and are subject to local laws and regulations.

Access control settings, requests to remove messages by "redactions" or remove personal data under GDPR Article 17 *Right to Erasure (Right to be Forgotten)* are shared to bridging services, which are expected to honour them to the best of their ability. Be aware that not all bridged networks or bridges support the necessary technical capabilities to limit, remove or erase messages. If this is not acceptable to you, please do not use bridged rooms.

##### Integration Services (Bots and Widgets)

The {{ hhs_name }}.{{ hhs_server_domain}} homeserver provides a range of integrations in the form of Widgets (miniature web applications accessed as part of a Matrix Client) and Bots (automated participants in rooms). Bots and Widgets currently have access to all the messages and files in any room in which they participate, although we are adding a more sophisticated access control system.

### 2.4 Sharing Data in Compliance with Enforcement Requests and Applicable Laws; Enforcement of Our Rights

In exceptional circumstances, we may share information about you with a third party if we believe that sharing is reasonably necessary to 

(a) comply with any applicable law, regulation, legal process or governmental request, 

(b) protect the security or integrity of our products and services (e.g. for a security audit),

(c) protect New Vector Ltd. and our users from harm or illegal activities, or

(d) respond to an emergency which we believe in good faith requires us to disclose information to assist in preventing the serious bodily harm of any person.

### 2.5 How Do You Handle Passwords?

We never store password data in plain text; instead they are stored hashed (with at least 12 rounds of bcrypt, including both a salt and a server-side pepper secret). Passwords sent to the server are encrypted using SSL.

It is your sole responsibility to keep your user name, password and other sensitive information confidential. Actions taken using your credentials shall be deemed to be actions taken by you, with all consequences including service termination, civil and criminal penalties.

If you become aware of any unauthorized use of your account or any other breach of security, you must notify New Vector Ltd. immediately by sending an email to [security@matrix.org](mailto:security@matrix.org). Suspicious devices can be deleted using the User Settings management tools in a Matrix client such as [https://riot.im/app](https://riot.im/app), and users should manage good password hygiene (e.g. using a password manager) and change their password if they believe their account is compromised. 

If you forget your password (and you have registered an email address) you can use the password reset facility to reset it.

You can manage your account by using a Matrix client such as [https://riot.im/app](https://riot.im/app).

We will never change a password for you.

### 2.6 Our Commitment to Children's Privacy

We never knowingly collect or maintain information in the Service from those we know are under 16, and no part of the Service is structured to attract anyone under 16. If you are under 16, please do not use the Service.

### 2.7 How Can I Access or Correct My Information?

You can access all your personally identifiable information that we collect by using any compatible Matrix client (such as [https://riot.im/app](https://riot.im/app)) and managing your User Settings. You can download a copy of all your data as per section 2.1.3.

### 2.8 Who Can See My Messages and Files?

{{ hhs_name }}.{{ hhs_server_domain}} is a paid-for, hosted homeserver operating under the instructions of the Customer. All unencrypted messages and files submitted to the homeserver are visible to the Customer.

In unencrypted and encrypted rooms, users connecting to the {{ hhs_name }}.{{ hhs_server_domain}} homeserver (directly or over federation) will be able to see messages and files according to the access permissions configuration of the relevant room. This data is stored in the format it was received on our servers, and can be viewed by New Vector engineers (employees and contractors) under the conditions outlined below.

In encrypted rooms, the data is stored in our databases but the encryption keys are stored only on your devices or by yourself. In future we may allow users to optionally backup an encrypted copy of their keys on the Service to aid recovery if they lose all their keys and devices. This key backup would be encrypted by a recovery key that only the user has access to. This means that nobody, even New Vector engineers (employees and contractors) can see your message content in our database, and if you lose access to your encryption keys you lose access to your messages forever.

We use HTTPS to transfer all data. End-to-end encrypted messaging data is stored encrypted using AES-256, using message keys generated using the [Olm and Megolm cryptographic ratchets](https://matrix.org/blog/2016/11/21/matrixs-olm-end-to-end-encryption-security-assessment-released-and-implemented-cross-platform-on-riot-at-last/).

### 2.9 What Are the Guidelines New Vector Follows When Accessing My Data?

* We restrict who at New Vector Ltd. (employees and contractors) can access user data to roles which require access in order to maintain the health of the Service.

* We never share what we see with other users or the general public.

### 2.10 Who Else Has Access to My Data?

We host the majority of the Service on Amazon Web Services (AWS). Amazon employees have access to this data. Here's [Amazon's privacy policy](http://aws.amazon.com/privacy/). Amazon controls physical access to their locations.

We use Cloudflare to mitigate the risk of DDoS attacks. Here's [CloudFlare's privacy policy](https://www.cloudflare.com/privacypolicy/).

Physical access to our offices and locations use typical physical access restrictions.

We use secure private keys when accessing servers via SSH, and protect our AWS console passwords locally with a password management tool.

We log application data (username, user IP and user agent). We keep logs for no longer than 30 days.

### 2.11 What happens if New Vector is sold?

In the event that we sell or buy any business or assets, we may disclose your personal data to the prospective seller or buyer of such business or assets.

If we or substantially all of our assets are acquired by a third party, personal data held by us about our users will be one of the transferred assets.

### 2.12 How Is My Data Protected from Another User's Data?

All of the Users' data for the {{ hhs_name }}.{{ hhs_server_domain}} homeserver resides within the same dedicated cluster. We use software best practices to guarantee that only people designated by Customer or a User as viewers of a User's data can access it. In other words, we segment User data via software. We do our best and are very confident we're doing a good job at it, but, like every other service that hosts User data on the same database, we cannot guarantee that it is immune to a sophisticated attack.

### 2.13 What Should I Do If I Find a Security Vulnerability in the Service?

If you have discovered a security concern, please email us at [security@matrix.org](mailto:security@matrix.org). We'll work with you to make sure that we understand the scope of the issue, and that we fully address your concern. We consider correspondence sent to [security@matrix.org](mailto:security@matrix.org) our highest priority, and work to address any issues that arise as quickly as possible.

Please act in good faith towards our users' privacy and data during your disclosure. White hat security researchers are always appreciated.

## 3. Making a Complaint

We try to meet the highest standards when collecting and using personal information. For this reason, we take any complaints we receive about this very seriously. We encourage people to bring it to our attention at [support@modular.im](mailto:support@modular.im) if they think that our collection or use of information is unfair, misleading or inappropriate. We would also welcome any suggestions for improving our procedures.

If you want to make a complaint about the way we have processed your personal information to the supervisory authority, you can contact the ICO (the statutory body which oversees data protection law) at [https://www.ico.org.uk/concerns](https://www.ico.org.uk/concerns).

## 4. Document History

* 2018, March 28: Policy document for public homeserver exposed at https://matrix.org was created.
* 2018, August 2: This document was derived from the above.
