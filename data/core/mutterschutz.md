## mutterschutz+difference+affirm_knowmore+deny_whatsappoffer
* get_started   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_general
  - utter_mutterschutz_mutterschutzfrist
  - utter_ask_knowmore
* affirm
  - utter_outofscope
  - utter_mutterschutz_reference
  - utter_whatsapp_offer
* deny
  - utter_im_here_4_u

## mutterschutz+difference+deny_knowmore+affirm_whatsapp
* get_started   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_general
  - utter_mutterschutz_mutterschutzfrist
  - utter_ask_knowmore
* deny
    - utter_hope_help
    - utter_whatsapp_offer
* affirm OR choose_request_whatsappcode
    - utter_whatsapp_code

## mutterschutz+period+affirm+whatsappoffer+deny
* ask_mutterschutz_period
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* affirm
  - utter_outofscope
  - utter_mutterschutz_reference
  - utter_whatsapp_offer
* deny
  - utter_im_here_4_u

## mutterschutz+period+deny+whatsappoffer+affirm/choose_request_whatsappcode
* ask_mutterschutz_period
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* deny
  - utter_hope_help
  - utter_whatsapp_offer
* affirm OR choose_request_whatsappcode
  - utter_whatsapp_code

## mutterschutz+mutterschutz_general
* choose_mutterschutz_general OR mutterschutz_topic
  - utter_mutterschutz_general
  - utter_ask_knowmore
