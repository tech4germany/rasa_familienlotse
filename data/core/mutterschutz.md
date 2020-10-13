## mutterschutz+difference+affirm_knowmore+deny_telegramoffer
* get_started   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_inform
  - utter_mutterschutz_mutterschutzfrist
  - utter_ask_knowmore
* affirm
  - utter_sorry
  - utter_mutterschutz_reference
  - utter_telegram_offer
* deny
  - utter_im_here_4_u

## mutterschutz+difference+deny_knowmore+affirm_telegram
* get_started   
  - utter_intro
  - utter_ask_mutterschutz_question
* ask_mutterschutz_difference_mutterschutzfrist
  - utter_mutterschutz_inform
  - utter_mutterschutz_mutterschutzfrist
  - utter_ask_knowmore
* deny
  - utter_hope_helped
  - utter_telegram_offer
* affirm OR choose_request_telegramcode
    - utter_telegram_code

## mutterschutz+period+affirm+telegramoffer+deny
* ask_mutterschutz_period
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* affirm
  - utter_sorry
  - utter_mutterschutz_reference
  - utter_telegram_offer
* deny
  - utter_im_here_4_u

## mutterschutz+period+deny+telegramoffer+affirm/choose_request_telegramcode
* ask_mutterschutz_period
  - utter_mutterschutz_periodreply
  - utter_ask_knowmore
* deny
  - utter_hope_helped
  - utter_telegram_offer
* affirm OR choose_request_telegramcode
  - utter_telegram_code

## mutterschutz+mutterschutz_general
* choose_mutterschutz_general OR mutterschutz_topic
  - utter_mutterschutz_inform
