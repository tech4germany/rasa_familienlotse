## mutterschutz+difference+whatsapp
<!-- TODO: greet mutterschutz as Platzhalter until get started custom action implemented -->
* greet_mutterschutz   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_differencereply
  - utter_ask_knowmore
* ask_mutterschutz_period
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* deny
  - utter_hope_help
  - utter_whatsapp_offer


## mutterschutz+difference+nowhatsapp
<!-- TODO: greet mutterschutz as Platzhalter until get started custom action implemented -->
* greet_mutterschutz   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_differencereply
  - utter_ask_knowmore
* ask_mutterschutz_period
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* deny
  - utter_hope_help
  - utter_whatsapp_offer
* deny
  - utter_im_here_4_u

<!--
## mutterschutz+difference+whatsapp
* greet_mutterschutz   
  - utter_intro
  - utter_ask_mutterschutz_question
* choose_whatsapp
  - utter_whatsapp_offer
-->

## mutterschutz+mutterschutz_general
* choose_mutterschutz_general
  - utter_mutterschutz_reply_outofscope

## whatsapp+familydescription+elterngeldstart
* choose_whatsapp
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
* choose_whatsapp
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
* choose_whatsapp
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* deny
  - utter_hope_help
  - utter_im_here_4_u

## whatsapp+familydescription+stop
* choose_whatsapp
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
* choose_whatsapp
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
