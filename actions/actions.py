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
                self.from_entity(entity="elterngeld_residence", intent=["choose_elterngeld_residence"]),
            ],

        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        residence2link = {
            "Berlin": "https://www.elterngeld-digital.de/ams/Elterngeld/wizardng/FFE7CD?v=1601979713870",
            "Bremen": "https://www.elterngeld-digital.de/ams/Elterngeld/wizardng/FFE7CD?v=1601979713870",
            "Hamburg": "https://www.elterngeld-digital.de/ams/Elterngeld/wizardng/FFE7CD?v=1601979713870",
            "Rheinland-Pfalz": "https://www.elterngeld-digital.de/ams/Elterngeld/wizardng/FFE7CD?v=1601979713870",
            "Thüringen": "https://www.elterngeld-digital.de/ams/Elterngeld/wizardng/FFE7CD?v=1601979713870",
            "Sachsen": "https://www.elterngeld-digital.de/ams/Elterngeld/wizardng/FFE7CD?v=1601979713870",
            "Bayern": "https://www.zbfs.bayern.de/familie/elterngeld/antraege/index.php",
            "Baden-Württemberg": "https://www.l-bank.de/produkte/familienfoerderung/elterngeld.html",
            "Brandenburg": "https://www.arbeitswelt-elternzeit.de/werdende-eltern/elterngeldantraege/",
            "Hessen": "http://www.familienatlas.de/geld/finanzielle-hilfen/elterngeld",
            "Mecklenburg-Vorpommern": "https://www.lagus.mv-regierung.de/Soziales/Elterngeld_ElterngeldPlus/",
            "Niedersachsen": "https://www.ms.niedersachsen.de/startseite/jugend_amp_familie/familien_kinder_und_jugendliche/familien/elterngeld_elterngeld_plus/das-elterngeld-13791.html",
            "Nordrhein-Westfalen": "https://www.mkffi.nrw/antragstellung-elterngeld",
            "Saarland": "https://service.buergerdienste-saar.de/Elterngeld-Onlineantrag/",
            "Sachsen-Anhalt": "https://ms.sachsen-anhalt.de/themen/familie/familienratgeber/familien-mit-kleinkindern/arbeit-und-finanzen/direkte-hilfen/",
            "Schleswig-Holstein": "https://www.schleswig-holstein.de/DE/Landesregierung/LASD/Aufgaben/KinderUndEltern/Download/BereichElterngeld_ab_2015-07.html" 
        }

        if tracker.get_slot("elterngeld_care") is False or tracker.get_slot("elterngeld_samehousehold") is False or tracker.get_slot("elterngeld_workparttime") is False or tracker.get_slot("elterngeld_residence") == "ausland":
            dispatcher.utter_message(template="utter_elterngeld_inform_prerequisites")
            return []
        residence = tracker.get_slot('elterngeld_residence')
        if residence is not None:
            if residence[0].islower():
                residence_adapted = residence[0].upper()+residence[1:]
            else:
                residence_adapted = residence
            return [SlotSet("elterngeld_residence", residence_adapted), SlotSet("elterngeld_residence_link", residence2link[residence_adapted])]
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
                self.from_intent(intent="deny", value=False),
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
