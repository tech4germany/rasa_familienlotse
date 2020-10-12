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
from rasa_sdk.events import SlotSet

class ElterngeldRequirementsForm(FormAction):

    def name(self):
        return "elterngeldrequirements_form"

    @staticmethod
    def required_slots(tracker):
        if tracker.get_slot("elterngeld_care") is False: 
            return []
        elif tracker.get_slot("elterngeld_samehousehold") is False:
            return []
        elif tracker.get_slot("elterngeld_workparttime") is False:
            return []
        elif tracker.get_slot("elterngeld_workparttime") == "ausland":
            return []  
        else:
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
        if tracker.get_slot("elterngeld_care") is False or tracker.get_slot("elterngeld_samehousehold") is False or tracker.get_slot("elterngeld_workparttime") is False or tracker.get_slot("elterngeld_residence") == "ausland":
            dispatcher.utter_message(template="utter_elterngeld_inform_prerequisites")
            return []
        residence = tracker.get_slot('elterngeld_residence')
        if residence is not None:
            if residence[0].islower():
                residence_adapted = residence[0].upper()+residence[1:]
            else:
                residence_adapted = residence
            return [SlotSet("elterngeld_residence", residence_adapted)]
        else:
            return []
                    

class FamilyDescriptionForm(FormAction):

    def name(self):
        return "familydescription_form"

    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot("familydescription_parent") != "Mutter":
            return ["familydescription_parent"]
        else:
            return ["familydescription_parent", "familydescription_pregnancy_month"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        
        return {
            "familydescription_parent": [
                self.from_entity(entity="familydescription_parent", intent=["familydescription_parent"]), 
            ],
            "familydescription_pregnancy_month": [
                self.from_entity(entity="familydescription_pregnancy_month", intent=["familydescription_pregnancy_month"]),
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

