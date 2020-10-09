## mutterschutz+difference
<!-- TODO: greet mutterschutz as Platzhalter until get started custom action implemented -->
* get_started   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_differencereply
  - utter_ask_knowmore

## mutterschutz+difference
<!-- TODO: greet mutterschutz as Platzhalter until get started custom action implemented -->
* get_started   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_differencereply
  - utter_ask_knowmore

## mutterschutz+period+affirm [utter_ask_knowmore -> affirm]
* ask_mutterschutz_period
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* affirm
  - utter_mutterschutz_reply_outofscope
  - utter_whatsapp_offer
* deny
  - utter_im_here_4_u

## mutterschutz+period+deny [utter_ask_knowmore -> deny] [2check]
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* deny
  - utter_hope_help
  - utter_whatsapp_offer
* affirm OR choose_request_whatsappcode
  - utter_whatsapp_code

## mutterschutz+mutterschutz_general
* choose_mutterschutz_general OR mutterschutz_topic
  - utter_mutterschutz_reply_outofscope

<!-- Übergabe an WhatsApp -->
## whatsapp+familydescription+elterngeldstart [2check]
* enter_whatsappcode
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - utter_ask_familydescription
* describe_family
  - familydescription_form
  - form{"name": "familydescription_form"}
  - form{"name": null}
  - utter_recommend_elterngeld
  - utter_ask_elterngeld_priorknowledge
* deny
  - utter_elterngeld_inform
  - utter_ask_elterngeld_subtopic

## whatsapp+familydescription+elterngeldrelated
* enter_whatsappcode
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - utter_ask_familydescription
* describe_family
  - familydescription_form
  - form{"name": "familydescription_form"}
  - form{"name": null}
  - utter_recommend_elterngeld
  - utter_ask_elterngeld_priorknowledge
* affirm
  - utter_im_here_4_u
* out_of_scope
  - utter_outofscope
  - utter_elterngeld_reply_outofscope

## whatsapp+familydescription+permissiondenied
* enter_whatsappcode
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* deny
  - utter_hope_help
  - utter_im_here_4_u

## whatsapp+familydescription+stop
* enter_whatsappcode
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - utter_ask_familydescription
* describe_family
  - familydescription_form
  - form{"name": "familydescription_form"}
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_im_here_4_u

## whatsapp+familydescription+continue
* enter_whatsappcode
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - utter_ask_familydescription
* describe_family
  - familydescription_form
  - form{"name": "familydescription_form"}
* out_of_scope
  - utter_ask_continue
* affirm
  - familydescription_form
  - form{"name": null}
