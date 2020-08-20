---
title: {{ hhs_entity_name }} ({{ hhs_name }}.{{ hhs_server_domain }}) Policy for Exceptional Exercising of Right To Erasure on State Events
version: 1.0.0
---

# {{ hhs_entity_name }} ({{ their_server_name }}) Policy for Exceptional Exercising of Right To Erasure on State Events

# 1. Introduction

Where you read *Element*,or *we* or *us* below, it refers to New Vector Ltd., and its French subsidiary: New Vector SARL and their agents. Element is a trading name of New Vector. **This policy does not apply to Matrix servers run by anyone else - Matrix is an open network like the Web and this policy only applies to the server ({{ our_server_fqdn }}) provided by Element.**

The legal basis for our processing Personal Data, the reasons for there being restrictions upon users' ability to exercise their *Right to Erasure (Right to be Forgotten)* upon state events, and the description of those restrictions, are detailed in the [full {{ their_server_name }} Privacy Notice](https://{{ their_client_fqdn }}/privacy_policy/en/privacy_notice.html).

This document serves to detail how we decide what to do in the event of the interests of an individual user appearing to be in conflict with the broader societal interests.

# 2. How we decide

As described in the [full {{ their_server_name }} Privacy Notice](https://{{ their_client_fqdn }}/privacy_policy/en/privacy_notice.html), erasing state events is very damaging to the integrity of a Matrix conversation.

Erasing a state event may result in our needing to erase the entire conversation at the same time. Deciding whether to take this drastic step will require a balancing exercise to be carried out at the time of the request, and will depend on:

*   the nature of the Personal Data that the user is requesting to be erased;
    
*   how many other users would have their fundamental rights and freedoms put at risk if the Right to Erasure were to be exercised
    
*   to what degree these other users would have their fundamental rights and freedoms put at risk if the Right to Erasure were to be exercised
    

If the homeserver is a commercial service paid for by a Customer, any exceptional erasure will be conducted in conjunction with the Customer.

The Personal Data contained in a state event is usually limited to the username, the timestamp and the conversation in which the state event was issued. State events only represent that a user participated in a given conversation at a given time. It is rare that this data is sensitive enough to warrant its erasure given the drastic impact this will have on other users.

Each case will be decided based on the factors listed above. In most situations we will not erase state events. In extreme situations, where not erasing state events will place people at material risk of harm, we may choose to erase state events or remove the entire conversation.

# 3. Contacting Us

If you would like us to consider erasing state events containing your Personal Data, please get in touch at [dpo@element.io](mailto:dpo@element.io).