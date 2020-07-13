---
title: EMS Server Users Terms of Service
version: 1.0.0
---

## 1. Introduction

The Matrix protocol is designed with your privacy and data sovereignty in mind. Because it is a decentralised, federated service with cryptographically-validated message integrity, there are a few important things to know before you use the Service.

This Service is hosted and run by New Vector Ltd (trading as Element) on behalf of the Homeserver Owner, Element's customer. The Service is configured by Element based on the Homeserver Owner's requirements.

## 2. Federation

If federation is enabled by the Homeserver Owner, this homeserver will share user data with the wider Matrix ecosystem over federation.

1. When you send messages or files in a room, a copy of the data is sent to all participants in the room. If these participants are registered on remote homeservers, your username, display name, messages and files may be replicated across each participating homeserver.
1. Your copy of your data will be forgotten upon your request. If federation is enabled, this request will also be forwarded onto federated homeservers. However - these homeservers are outside our span of control, so we cannot guarantee they will forget your data.
1. Federated homeservers can be located anywhere in the world, and are subject to local laws and regulations.

Federation on this homeserver is currently enabled. The Homeserver Owner may choose to change this at any time.

## 3. Bridging

Some Matrix rooms are bridged to third-party services, such as IRC networks, Slack, Twitter or email. When a room has been bridged, your messages and media may be copied onto the bridged service.

1. It may not be technically possible to support your management of your data once it has been copied onto a bridged service.
1. Bridged services can be located anywhere in the world, and are subject to local laws and regulations.

## 4. Integration Services (bots and widgets)

The homeserver can provide a range of integrations in the form of Widgets (web applications accessed as part of the Matrix Client webapp) and Bots (automated participants in rooms). Bots and Widgets have access to the messages and files in rooms in which they participate.

## 5. Forgetting your Data

You can request that your data be forgotten if you deactivate your account. Each user in a Matrix conversation receives their own copy of all messages and files in that conversation (similar to email), so we ensure data is forgotten by ensuring that your data is not shared further and is not visible to future users. After all users’ copies have been forgotten, the messages and files will remain accessible to the Homeserver Owner for the duration of the homeserver. For full details, please see the full [privacy notice](https://element.io/privacy).

If you remove (redact) a message, the message content will no longer be accessible to users. Redactions only remove message content, your display name and avatar - your username will still be visible. Federated homeservers and some Matrix clients may not honour the redaction request.

## 6. Legal Basis for Processing

Element processes your data under Legitimate Interest. This means that we process your data only as necessary to deliver the Service, and in a manner that you understand and expect.

This Legitimate Interest pertains to the hosting and management of Matrix homeservers, providing decentralised, openly-federatable and (by default but sometimes configurable) end-to-end encrypted communication services. The processing of user data we undertake is necessary to provide the Service. The nature of the Service and its implementation results in some caveats concerning this processing, particularly in terms of GDPR Article 17 Right to Erasure (Right to be Forgotten). We believe these caveats are in line with the broader societal interests served by providing the Service. These caveats are discussed in detail in the full privacy notice, but the most important restriction is that your username will still be publicly associated with rooms in which you have participated even if you deactivate your account and ask us to forget your data.

In situations where the interests of the individual appear to be in conflict with the broader societal interests, we will seek to reconcile those differences in accordance with our exceptional erasure policy.

---
If any of the above are unacceptable to you, please do not use the Service.

Please review the full [privacy notice](https://element.io/privacy) and code of conduct before using this Service.

Please review the terms and conditions before using this Service.

You must be at least 16 years old to use this Service.
