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

class ElterngeldPrerequisitesForm(FormAction):

    def name(self):
        return "elterngeldprerequisites_form"

    @staticmethod
    def required_slots(tracker):
        return ["elterngeld_situation", "elterngeld_care", "elterngeld_samehousehold", "elterngeld_workparttime", "elterngeld_livegermany"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        
        return {
            "elterngeld_situation": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
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
            "elterngeld_livegermany": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],

        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []