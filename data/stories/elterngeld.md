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
* choose_elterngeld_prerequisites
  - utter_ask_elterngeld_situation
* affirm
  - elterngeldprerequisites_form
  - form{"name": "elterngeldprerequisites_form"}
  - form{"name": null}

## elterngeld+prerequisites+denied+nofurtherquestion
> elterngeld_subtopics
* choose_elterngeld_prerequisites
  - utter_ask_elterngeld_situation
* deny
  - utter_ask_elterngeld_furthertopic
* deny
  - utter_goodbye

## elterngeld+prerequisites+denied+furtherquestion
> elterngeld_subtopics
* choose_elterngeld_prerequisites
  - utter_ask_elterngeld_situation
* deny
  - utter_ask_elterngeld_furthertopic

## elterngeld+prerequisites+stop
> elterngeld_subtopics
* choose_elterngeld_prerequisites
  - utter_ask_elterngeld_situation
* affirm
  - elterngeldprerequisites_form
  - form{"name": "elterngeldprerequisites_form"}
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name":null}
  - utter_goodbye

## elterngeld+prerequisites+stop
> elterngeld_subtopics
* choose_elterngeld_prerequisites
  - utter_ask_elterngeld_situation
* affirm
  - elterngeldprerequisites_form
  - form{"name": "elterngeldprerequisites_form"}
* out_of_scope
  - utter_ask_continue
* affirm
  - elterngeldprerequisites_form
  - form{"name":null}
<!-- further topic: application, amount, duration -->

## elterngeld application
> elterngeld_subtopics
* choose_elterngeld_application
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

## elterngeld amount
> elterngeld_subtopics
* choose_elterngeld_amount
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

## elterngeld duration
> elterngeld_subtopics
* choose_elterngeld_duration
  - utter_elterngeld_reply_outofscope
  - utter_goodbye 
  
<!-- chitchat & co -->

## say hello
* greet
  - utter_welcomeback

## say goodbye
* goodbye
  - utter_goodbye
