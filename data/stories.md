## elterngeld info
* elterngeld_topic
  - utter_welcomeback
  - utter_elterngeld_precise_general
> elterngeld_precise_general

## elterngeld precise 
> elterngeld_precise_general
* choose_elterngeld_precise
  - utter_elterngeld_ask_precisequestion
* out_of_scope
  - utter_elterngeld_reply_outofscope
  - utter_goodbye

## elterngeld general
> elterngeld_precise_general
* choose_elterngeld_general
  - utter_elterngeld_inform
  - utter_elterngeld_ask_subtopic
> elterngeld_subtopics

<!-- Subtopics: prerequisites, application, amount, timeframe -->
## elterngeld prerequisites intro
> elterngeld_subtopics
* choose_elterngeld_prerequisites
  - utter_elterngeld_ask_situation
> elterngeld_situation

## elterngeld prerequisites check
> elterngeld_situation
* affirm
  - utter_elterngeld_ask_care
> elterngeld_ask_care

## elterngeld care yes
> elterngeld_ask_care
* affirm
  - utter_elterngeld_ask_samehousehold
> elterngeld_ask_samehousehold

## elterngeld care no
> elterngeld_ask_care
* deny
  - utter_elterngeld_inform_prerequisites

## elterngeld same household yes
> elterngeld_ask_samehousehold 
* affirm
  - utter_elterngeld_ask_workparttime
> elterngeld_ask_workparttime

## elterngeld same household no
> elterngeld_ask_samehousehold
* deny
  - utter_elterngeld_inform_prerequisites

## elterngeld workparttime yes
> elterngeld_ask_workparttime
* affirm
  - utter_elterngeld_ask_livegermany
> elterngeld_ask_livegermany

## elterngeld workparttime no
> elterngeld_ask_workparttime
* deny
  - utter_elterngeld_inform_prerequisites

## elterngeld livegermany yes
> elterngeld_ask_livegermany
* affirm
  - utter_elterngeld_affirm_prerequisites
  - utter_elterngeld_ask_furthertopic
<!-- further topic: application, amount, time frame-->
* deny
  - utter_goodbye

## elterngeld livegermany no
> elterngeld_ask_livegermany
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
  - utter_goodbye



## say hello
* greet
  - utter_welcomeback

## say goodbye
* goodbye
  - utter_goodbye

