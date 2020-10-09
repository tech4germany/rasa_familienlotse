<!-- Elterngeld -->
## intent:elterngeld_topic
- Hey, kannst Du mir beim Thema Elterngeld helfen?
- Thema Elterngeld
- Elterngeld
- Geld für Eltern
- Elterngeld Hilfe
- hilf mir bitte bei Elterngeld

## intent:choose_elterngeld_precise
- ich habe eine konkrete Frage
- konkret
- konkrete Frage
- spezielle Frage
- ich habe eine Frage

## intent:choose_elterngeld_general
- allgemeine Infos
- allgemeine Frage
- keine spezielle Frage
- Allgemeine Info
- Informationen

## intent:choose_elterngeld_requirements
- Voraussetzungen für Elterngeld
- Voraussetzungen
- Vorausetzung
- Vorraussetzung
- voraus setzung
- was sind die Voraussetzunge für Elterngeld?
- Elterngeld Voraussetzung

## intent:choose_elterngeld_application
- beantragung für Elterngeld in [BaWü](bundesland)
- benatragung
- Beantragungen
- beantragen in [Hamburg](bundesland)
- bearntragen
- ich will Elterngeld beantragen
- Elterngeld antrag
- Elterngeld beantragen in [RLP](bundesland)

## intent:choose_elterngeld_amount
- Höhe Elterngeld
- hoehe Elterngeld
- hoehe
- Höhe
- höhe
- wie viel Elterngeld bekomme ich?
- wie viel Elterngeld?
- Elterngeld viel?

## intent:choose_elterngeld_duration
- dauer elterngeld
- wie lange dauert elterngeld
- wie lange hält Elterngeld
- wie lange bekomme ich Elterngeld?
- Elterngeld wie viel Zeit

## intent:choose_elterngeld_residence
<!-- elterngeld_digital-->
- [Berlin](bundesland)
- [BER](bundesland)
- [Bremen](bundesland)
- [Hamburg](bundesland)
- [Rheinland-Pfalz](bundesland)
- [rlp](bundesland)
- [Sachsen](bundesland)
- [Thüringen](bundesland)
<!-- elterngeld__not_digital-->
- [Brandenburg](bundesland)
- [Mecklenburg-Vorpommern](bundesland)
- [meckpomm](bundesland)
- [Niedersachsen](bundesland)
- [Nordrhein-Westfalen](bundesland)
- [NRW](bundesland)
- [Sachsen-Anhalt](bundesland)
- [Schleswig-Holstein](bundesland)
- [SH](bundesland)
<!-- elterngeld_own_solution_digital-->
- [Baden-Württemberg](bundesland)
- [bawü](bundesland)
- [Bayern](bundesland)
- [bay](bundesland)
- [BY](bundesland)
- [Hessen](bundesland)
- [Saarland](bundesland)
- [sl](bundesland)
<!-- bundesland_fallback-->
- [ausland](bundesland)


<!-- Mutterschutz -->
## intent:mutterschutz_topic
- was ist Mutterschutz?
- mutterschutz
- was bekommt man bei Mutterschutz?
- wie funktioniert Mutterschutz?
- Schutz für Mütter

## intent:ask_mutterschutz_difference_mutterschutzfrist
- Was ist der Unterschied zwischen Mutterschutz und Mutterschutzfrist?
- Wie unterscheidet sich Mutterschutz und Mutterschutzfrist?
- Mutterschutz versus Mutterschutzfrist
- Was ist Mutterschutz im Vergleich zu Mutterschutzfrist
- Ich weiß nicht, was der Unterschied zwischen Mutterschutz und Mutterschutzfrist ist
- Mutterschutz Mutterschutzfrist

## intent:ask_mutterschutz_period
- Wie lange ist der Mutterschutzfrist-Zeitraum?
- Wie lange gilt die Mutterschutzfrist?
- Wann beginnt die Mutterschutzfrist?
- Wann endet die Mutterschutzfrist?

## intent:get_started
- start mutterschutz
- go mutterschutz
- Beginn mutterschutz
- beginn mutterschutz
- Start mutterschutz
- los gehts mutterschutz
- hallo mutterschutz

## intent:enter_whatsappcode
- t4g-sonne-start

## intent:choose_request_whatsappcode
- WhatsApp
- WA
- zu WhatsApp
- habt Ihr WhatsApp als Kanal?
- ist WhatsApp angeschlossen?
- WhatsApp möglich?

## intent:choose_mutterschutz_general
- mutterschutz
- schutz für mütter
- Mutterschutz
- schutz mutter
- schutz mama
- Mamaschutz

<!-- default -->

## intent:greet
- hey
- hallo
- hi
- Guten Morgen
- Guten Abend
- Guten Tag
- Hallo
- Servus

## intent:goodbye
- tschüss
- bis dann
- bis zum nächsten Mal
- ciao
- cu
- Bye
- Byebye
- machs gut

## intent:affirm
- ja
- joah
- jap
- yep
- jaaaa
- Ja
- ok
- ja bitte
- gerne
- gerne mehr
- erzähl mir mehr darüber

## intent:deny
- ne
- nein
- nö
- nicht
- nee
- Nein
- neeeee
- nein danke
- nein fürs erste nicht
- nicht fürs erste

## intent:out_of_scope
- Krankenschutz bei Elterngeld
- kann mein Partner auch Elterngeld beantragen
- ich arbeite im Ausland, lebe in Deutschland. kann ich Elterngeld beantragen?
- Wie bin ich versichert bei Elterngeld?
- kann ich Elterngeld auch beantragen, wenn Kind nicht bei mir wohnt?
- Wie hängt Kindergeld mit Elterngeld zusammen?

## intent:describe_family
<!-- TODO: extract entity from two inputs -->
- [ich]{"entity": "familydescription_parent", "value": "Mama"} bin im [3. Monat](familydescription_pregnancy_month) schwanger
- ich bin [Mutter](familydescription_parent).
- ich werde in [5 Monaten](familydescription_pregnancy_month) [Mutter](familydescription_parent)
- In [4 Monaten](familydescription_pregnancy_month) werde [ich]{"entity": "familydescription_parent", "value": "Mama"}
- in [8 Monaten](familydescription_pregnancy_month) bekomme [ich]{"entity": "familydescription_parent", "value": "Mama"} ein Baby
- [meine Freundin]{"entity": "familydescription_parent", "value": "Vater"} ist im [6. Monat](familydescription_pregnancy_month) schwanger.
- [meine Frau]{"entity": "familydescription_parent", "value": "Vater"} ist im [7. Monat](familydescription_pregnancy_month) schwanger.
- Ich werde in [1 Monat](familydescription_pregnancy_month) [Vater](familydescription_parent)
- Ich werde in [2 Monaten](familydescription_pregnancy_month) [Papa](familydescription_parent)
- wir bekommen in [6 Monaten](familydescription_pregnancy_month) unser Kind


## intent:familydescription_parent
- [Mutter](familydescription_parent)
- [Mudder](familydescription_parent)
- [Mama](familydescription_parent)
- [Mum](familydescription_parent)
- [Muddah](familydescription_parent)
- [muddi](familydescription_parent)
- [Vater](familydescription_parent)
- [Papa](familydescription_parent)
- [Dad](familydescription_parent)
- [Vaddi](familydescription_parent)
- [Daddy](familydescription_parent)
- [Paps](familydescription_parent)


<!-- Elternzeit -->
## intent:elternzeit_topic
- elternzeit
- zeit für Eltern
- Was ist Elternzeit?
- Thema Elternzeit?
- Kannst Du mir etwas über Elternezit sagen?

## intent:greet_elternzeit
- Start Elternzeit
- Hallo Elternzeit
- Los elternezit
- Los gehts elternzeit
- start elternzeit

## intent:elternzeit_timepartner
- kann ich auch Elternzeit nehmen?
- kann meine Frau auch Elternzeit nehmen?
- kann ich als Mutter auch Elternzeit beantragen
- kann ich Elternzeit anmelden?

## intent:choose_elternzeit_notification
- anmeldung
- anmelden
- Elternzeit anmelden
- Elternzeit nehmen
- elternzeit haben

<!-- NEED TO MERGE WITH ELTERNGELD USING SLOT
## intent:choose_elternzeit_requirements

## intent_choose_elternzeit_duration
-->