## elterngeld+precise+out_of_scope
* elterngeld_topic
  - utter_welcomeback
  - utter_elterngeld_precise_general
* choose_elterngeld_precise
  - utter_ask_elterngeld_precisequestion
* out_of_scope
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

## elterngeld+general
* elterngeld_topic
  - utter_welcomeback
  - utter_elterngeld_precise_general
* choose_elterngeld_general
  - utter_elterngeld_inform
  - utter_ask_elterngeld_subtopic
> elterngeld_subtopics

<!-- Subtopics: prerequisites, application, amount, timeframe -->
## elterngeld+prerequisites
> elterngeld_subtopics
* choose_elterngeld_requirements
  - utter_ask_elterngeld_situation
* affirm
  - elterngeldrequirements_form
  - form{"name": "elterngeldrequirements_form"}
  - form{"name": null}
  - utter_elterngeld_slots
  - utter_ask_elterngeld_furthertopic

## elterngeld+prerequisites+denied+nofurtherquestion
> elterngeld_subtopics
* choose_elterngeld_requirements
  - utter_ask_elterngeld_situation
* deny
  - utter_ask_elterngeld_furthertopic
* deny
  - utter_goodbye

## elterngeld+prerequisites+denied+furtherquestion
> elterngeld_subtopics
* choose_elterngeld_requirements
  - utter_ask_elterngeld_situation
* deny
  - utter_ask_elterngeld_furthertopic

## elterngeld+prerequisites+stop
> elterngeld_subtopics
* choose_elterngeld_requirements
  - utter_ask_elterngeld_situation
* affirm
  - elterngeldrequirements_form
  - form{"name": "elterngeldrequirements_form"}
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name":null}
  - utter_goodbye

## elterngeld+prerequisites+continue
> elterngeld_subtopics
* choose_elterngeld_requirements
  - utter_ask_elterngeld_situation
* affirm
  - elterngeldrequirements_form
  - form{"name": "elterngeldrequirements_form"}
* out_of_scope
  - utter_ask_continue
* affirm
  - elterngeldrequirements_form
  - form{"name":null}

<!-- further topic: application, amount, duration -->

## elterngeld application
> elterngeld_subtopics
* choose_elterngeld_application
  - utter_outofscope
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

## elterngeld amount
> elterngeld_subtopics
* choose_elterngeld_amount
  - utter_outofscope
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

## elterngeld duration
> elterngeld_subtopics
* choose_elterngeld_duration
  - utter_outofscope
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

<!--
## elterngeld+prerequisites+application+elterngelddigital
* choose_elterngeld_application{"elterngeld_residence": "Berlin"} OR choose_elterngeld_application{"elterngeld_residence": "Bremen"}
  - utter_elterngeld_application_elterngelddigital

## elterngeld+prerequisites+application+bawü
* choose_elterngeld_application{"elterngeld_residence": "Baden-Württemberg"}
  - utter_elterngeld_application_bawue
-->