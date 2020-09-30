## elterngeld info
* elterngeld_topic
  - utter_welcomeback
  - utter_elterngeld_precise_general
> elterngeld_precise_general

## elterngeld precise 
> elterngeld_precise_general
* choose_elterngeld_precise
  - utter_ask_elterngeld_precisequestion
* out_of_scope
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

## elterngeld general
> elterngeld_precise_general
* choose_elterngeld_general
  - utter_elterngeld_inform
  - utter_ask_elterngeld_subtopic
> elterngeld_subtopics

<!-- Subtopics: prerequisites, application, amount, timeframe -->
## elterngeld prerequisites intro
> elterngeld_subtopics
* choose_elterngeld_prerequisites
  <!-- - utter_ask_elterngeld_situation -->
  - elterngeldprerequisites_form
  - form{"name": "elterngeldprerequisites_form"}
  - form{"name": null}
  - utter_slots_values
<!-- > elterngeld_situation

## elterngeld prerequisites check
> elterngeld_situation
* affirm
  - utter_ask_elterngeld_care
> elterngeld_care

## elterngeld care yes
> elterngeld_care
* affirm
  - utter_ask_elterngeld_samehousehold
> elterngeld_samehousehold

## elterngeld care no
> elterngeld_care
* deny
  - utter_elterngeld_inform_prerequisites

## elterngeld same household yes
> elterngeld_samehousehold 
* affirm
  - utter_ask_elterngeld_workparttime
> elterngeld_workparttime

## elterngeld same household no
> elterngeld_samehousehold
* deny
  - utter_elterngeld_inform_prerequisites

## elterngeld workparttime yes
> elterngeld_workparttime
* affirm
  - utter_ask_elterngeld_livegermany
> elterngeld_livegermany

## elterngeld workparttime no
> elterngeld_workparttime
* deny
  - utter_elterngeld_inform_prerequisites

## elterngeld livegermany yes
> elterngeld_livegermany
* affirm
  - utter_elterngeld_affirm_prerequisites
  - utter_ask_elterngeld_furthertopic 
  * deny
  - utter_goodbye
  -->

<!-- further topic: application, amount, time frame-->


<!-- 

## elterngeld livegermany no
> elterngeld_livegermany
* deny
  - utter_elterngeld_inform_prerequisites

## elterngeld prerequisites info
> elterngeld_situation
* deny
  - utter_elterngeld_inform_prerequisites


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
  - utter_goodbye -->



## say hello
* greet
  - utter_welcomeback

## say goodbye
* goodbye
  - utter_goodbye

