<!-- Übergabe an WhatsApp -->
## whatsapp+familydescription+affirm+form_complete+affirm
* enter_whatsappcode OR start
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - familydescription_form
  - form{"name": "familydescription_form"}
  - form{"name": null}
  - utter_recommend_elterngeld
  - utter_ask_elterngeld_priorknowledge
* affirm
  - utter_im_here_4_u

## whatsapp+familydescription+affirm+form_complete+deny
* enter_whatsappcode OR start
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - familydescription_form
  - form{"name": "familydescription_form"}
  - form{"name": null}
  - utter_recommend_elterngeld
  - utter_ask_elterngeld_priorknowledge
* deny
  - utter_elterngeld_inform
  - utter_ask_elterngeld_subtopic

## whatsapp+familydescription+affirm+form_continue
* enter_whatsappcode OR start
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - familydescription_form
  - form{"name": "familydescription_form"}
* out_of_scope
  - utter_ask_continue
* affirm
  - familydescription_form
  - form{"name": null}
  

## whatsapp+familydescription+affirm
* enter_whatsappcode OR start
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* affirm
  - familydescription_form
  - form{"name": "familydescription_form"}
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_im_here_4_u

## whatsapp+familydescription+deny
* enter_whatsappcode OR start
  - utter_welcomeback
  - utter_more_info
  - utter_ask_permission_familydescription
* deny
  - utter_hope_helped
  - utter_im_here_4_u
