# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ElterngeldRequirementsForm(FormAction):

    def name(self):
        return "elterngeldrequirements_form"

    @staticmethod
    def required_slots(tracker):
        # TODO: wenn ein slot mit nein, dann zu Ende
        return ["elterngeld_care", "elterngeld_samehousehold", "elterngeld_workparttime", "elterngeld_residence"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        
        return {
            "elterngeld_care": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
            "elterngeld_samehousehold": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
            "elterngeld_workparttime": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
            "elterngeld_residence": [
                self.from_entity(entity="bundesland", intent=["choose_elterngeld_residence"]),
            ],

        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # dispatcher.utter_message("Thanks, great job!")
        return []
