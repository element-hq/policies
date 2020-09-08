## 1. Introduction

The Matrix protocol is designed with your privacy and data sovereignty in mind. Because it is a decentralised, federated service with cryptographically-validated message integrity, there are a few important things to know before you use the Service.

This Service is hosted and run by New Vector Ltd (trading as Element) on behalf of the Homeserver Owner, %%HHS_ENTITY_NAME%%. The Service is configured by Element based on the %%HHS_ENTITY_NAME%% requirements.

## 2. Federation

If federation is enabled by the Homeserver Owner, this homeserver will share user data with the wider Matrix ecosystem over federation.

1.  When you send messages or files in a room, a copy of the data is sent to all participants in the room. If these participants are registered on remote homeservers, your username, display name, messages and files may be replicated across each participating homeserver.
2.  Your copy of your data will be forgotten upon your request. If federation is enabled, this request will also be forwarded onto federated homeservers. However - these homeservers are outside our span of control, so we cannot guarantee they will forget your data.
3.  Federated homeservers can be located anywhere in the world, and are subject to local laws and regulations.

Federation on this homeserver is currently **%%FEDERATION_ENABLED%%**. The Homeserver Owner may choose to change this at any time.

## 3. Bridging

Some Matrix rooms are bridged to third-party services, such as IRC networks, Slack, Twitter or email. When a room has been bridged, your messages and media may be copied onto the bridged service.

1.  It may not be technically possible to support your management of your data once it has been copied onto a bridged service.
2.  Bridged services can be located anywhere in the world, and are subject to local laws and regulations.

## 4. Integration Services (bots and widgets)

The homeserver can provide a range of integrations in the form of Widgets (web applications accessed as part of the Matrix Client webapp) and Bots (automated participants in rooms). Bots and Widgets have access to the messages and files in rooms in which they participate.

## 5. Forgetting your Data

You can request that your data be forgotten if you deactivate your account. Each user in a Matrix conversation receives their own copy of all messages and files in that conversation (similar to email), so we ensure data is forgotten by ensuring that your data is not shared further and is not visible to future users. After all users’ copies have been forgotten, the messages and files will remain accessible to the Homeserver Owner for the duration of the homeserver. For full details, please see the full [full privacy notice](https://%%THEIR_CLIENT_FQDN%%/privacy_policy/en/privacy_notice.html).

If you remove (redact) a message, the message content will no longer be accessible to users. Redactions only remove message content, your display name and avatar - your username will still be visible. Federated homeservers and some Matrix clients may not honour the redaction request.

## 6. Legal Basis for Processing

Element processes your data under Legitimate Interest. This means that we process your data only as necessary to deliver the Service, and in a manner that you understand and expect.

This Legitimate Interest pertains to the hosting and management of Matrix homeservers, providing decentralised, openly-federatable and (by default but sometimes configurable) end-to-end encrypted communication services. The processing of user data we undertake is necessary to provide the Service. The nature of the Service and its implementation results in some caveats concerning this processing, particularly in terms of GDPR Article 17 Right to Erasure (Right to be Forgotten). We believe these caveats are in line with the broader societal interests served by providing the Service. These caveats are discussed in detail in the full privacy notice, but the most important restriction is that your username will still be publicly associated with rooms in which you have participated even if you deactivate your account and ask us to forget your data.

In situations where the interests of the individual appear to be in conflict with the broader societal interests, we will seek to reconcile those differences in accordance with our [exceptional erasure policy](https://%%THEIR_CLIENT_FQDN%%/privacy_policy/en/exceptional_erasure_policy.html).

If any of the above are unacceptable to you, **please do not use the Service.**

Please review the full [privacy notice](https://%%THEIR_CLIENT_FQDN%%/privacy_policy/en/privacy_notice.html) and [code of conduct](https://%%THEIR_CLIENT_FQDN%%/privacy_policy/en/code_of_conduct.html) before using this Service.

{% if not public_version %}

{% if has_consented %}  {% else %}  {% endif %}  I have read and understood the full privacy notice and code of conduct 

{% endif %}

Please review the [terms and conditions](https://%%THEIR_CLIENT_FQDN%%/privacy_policy/en/terms_and_conditions.html) before using this Service.

{% if not public_version %}

{% if has_consented %}  {% else %}  {% endif %}  I have read and understood the terms and conditions 

{% endif %}

You must be at least 16 years old to use this Service (%%THEIR_CLIENT_FQDN%%)

{% if not public_version %}

{% if has_consented %}  {% else %}  {% endif %}  I am at least 16 years old. 

{% endif %} {% if not public_version %}

   

{% if has_consented %}

You have already agreed to these terms and conditions, thank you.

If you would like us to stop processing your data (subject to the conditions outlined above and in the Privacy Policy), please deactivate your account and select the option asking us to forget your data.

{% else %} var checkbox_understand = document.getElementById('checkbox_understand'); var checkbox_at_least_sixteen = document.getElementById('checkbox_at_least_sixteen'); var checkbox_tcs_and_cs = document.getElementById('checkbox_tcs_and_cs'); var submit_button = document.getElementById('submit_button'); function validateInput() { submit_button.disabled = !checkbox_understand.checked || !checkbox_tcs_and_cs.checked || !checkbox_at_least_sixteen.checked; } {% endif %} {% endif %}