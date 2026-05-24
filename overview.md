# DGS Konzeptübersicht

## Aufgaben

- **Bestehendes Scraping/Code überarbeiten**
  - in einem ipynb + python Skripte
  - GitHub Konventionen einführen (requirements etc.)
- **Neues Scraping/Code einfügen**
  - Coauthors (gibt es dazu ORCIDs?)
- **Neue Datenquellen Scrapen?**
  - SCImago-Daten, Crossref / OpenAlex
- **Classifying the titles/abstracts for a content analysis**
- **Visualisierungen + git.io website aufsetzen**
- **händische Kodierung**
  - Person
    - Gender (M, F, D, NaN)
    - Level (PhD or less, PostDoc or equiv., Prof, NaN)
  - Employer
    - Name of Employer (Name, NaN)
    - Type of Employer (Uni, Hochschule, Forschungszentrum, Other, NaN)
    - Country of Employment (Name, NaN)
    - Region of Employment (Name, NaN)
    - City of Employment (Name, NaN)
  - Source
    - Link
    - Date of Input

---

Lukas
Paul

## Projektziel

Eine öffentlich zugängliche Website (github.io), die die Forschungsaktivität der DGS-Sektion kontinuierlich dokumentiert: die neuesten 10 Veröffentlichungen der Mitglieder, deskriptive Kennzahlen zur Zusammensetzung der Sektion sowie Netzwerk- und Impact-Analysen. Die Seite wird monatlich automatisch aktualisiert.

## Forschungsfragen

### F1) Demografie und Zusammensetzung

Wie ist die Sektion demografisch strukturiert?
Gibt es Muster in Alter, Geschlecht, Karrierestufe und institutioneller Anbindung?

### F2) Netzwerk und Kooperation

Welche Kooperationsmuster und Homophilietendenzen zeigen sich in der Koautorenschaft? Schreiben Frauen häufiger mit Frauen? Kooperieren Personen gleicher Karrierestufe bevorzugt miteinander? Wie verhält sich der Anteil sektionsinterner zu externen Ko-Autorschaften?

### F3) Wissenschaftliche Sichtbarkeit

In welchen Journals publizieren die Mitglieder, und wie stark werden ihre Arbeiten zitiert? Variieren diese Kennzahlen nach demografischen Merkmalen?

## Verfügbare Daten

| Datensatz         | Format     | Inhalt                                             | Status                                    |
| ----------------- | ---------- | -------------------------------------------------- | ----------------------------------------- |
| Mitgliederliste   | CSV        | Namen, ORCIDs                                      | Partiell (ORCIDs fehlen für einen Anteil) |
| Publikationsliste | CSV        | Alle ORCID-gelisteten Publikationen der Mitglieder | Abhängig von ORCID-Pflege                 |
| Scraping-Skript   | Python / R | Neuerscheinungen im Newsletter-Format              | Funktionsfähig                            |

## Offene Aufgaben

- **Demografische Daten (manuell)**
  - Geschlecht nachschlagen
  - Akademischen Titel / Karrierestufe erfassen
  - Arbeitgeber (universitär vs. außeruniversitär)
  - Alter (Proxy: Dissertationsjahr o. Ä., Abiturjahrgang)
- **Personenidentifikation und Netzwerkparameter**
  - Umgang mit Koautor:innen? Haben wir ORCIDs?
  - Umgang mit Personen ohne ORCID
  - Umgang mit Karteileichen (Veröffentlichungen in den letzten 5 Jahren?)
  - Umgang mit Namensgleichheit klären
  - Netzwerkparameter definieren
- **Impact-Daten**
  - Nach Journals?
    - ISSN-Matching mit SCImago-Daten (Journalkategorien Q1–Q4)
  - Nach Zitierung?
    - API-Anbindung OpenAlex oder Crossref für Zitationsdaten
- **Weiteres**
  - Codebuch: Alle Variablen, Ausprägungen und Kodierregeln dokumentieren
  - Weiteres Publikationsformat: Datenpaper in einem datenfokussierten Journal (Journal of Open Humanities Data, Data in Brief oder soziologisches Methodenheft)







# Paul

Das Kernproblem (5 Min)
Was ist die Forschungsfrage, in einem Satz?
Die Strukturelle Darstellung der DGS Sektion

Warum ist das relevant – wen interessiert das Ergebnis?
Die Ergebnisse könnten zum einen statisch innerhalb der DGS Sektion geteilt werden, wie auch kontinuierlich auf der website veröffentlicht werden


Machbarkeit (10 Min)
Was braucht man: Daten, Tools, Infrastruktur, Vorkenntnisse?
Eine noch aktuellere Liste der Mitglieder
Vielleicht kommt man an noch mehr Personenmerkmale

Was haben wir davon bereits, was fehlt noch?
Wir haben ein grobes Scraping bereits gemacht

Grobe Zeitschätzung: Wochen oder Monate bis zu ersten Ergebnissen?
1 Monat


Wissenschaftlicher Wert (5 Min)
Gibt es verwandte Arbeiten? (kurze Suche reicht)
Nein

Was wäre der konkrete Beitrag – neue Methode, neuer Datensatz, neue Erkenntnis?
Nicht groß, aber man könnte damit angeben
Datensatz + Connection zur DGS + vlt interessante Erkenntnisse

- Thematische Analyse über short_description (schwer)
    - Vielleicht passend zu ML Kurs
    - Dazu: Datensatznutzungen
- Die Struktur der eigenen Organisation
    - Netzwerkanalyse der Autoren
    - Geschlechter
    - Zeitanalyse
    - Jobverteilung (Roles)
- Publikationen, wo
Und ähnliche

2 aufgaben
1. Guter Code
2. Auswertung der Ergebnisse


Risiken (5 Min)
Was kann schiefgehen oder sich als unlösbar herausstellen?
- Es interessiert niemanden
- Die Ergebnisse sind zu personenbezogen
- Der Datensatz hat keine super interessanten Merkmale

Gibt es einen "Plan B" oder einen abgespeckten Scope?
- Die wäre das scraping
    - Das ist schon umgesetzt

Pitch selbst (5 Min)

3–5 Folien oder ein Whiteboard-Sketch vorbereiten
Kernaussage üben: "Wir untersuchen X, weil Y, mit Methode Z"















## 1. Wissenschaftssoziologie der eigenen Sektion (besonders reizvoll)

Die Daten erlauben es, **klassische bibliometrische Ungleichheitsmuster** in der Sektion selbst zu prüfen:

- **Matthäus-Effekt / Produktivitätsverteilung**: Gini-Koeffizient der Publikationen pro Person, Lorenz-Kurve. Wie viele Mitglieder publizieren wie viel? Folgt es einer Pareto-/Lotka-Verteilung?
- **Geschlechterungleichheit in Autorenschaft** (Vornamen → Geschlecht inferieren mit `gender_guesser` oder Wikidata):
  - First-Author / Last-Author / Middle-Author-Anteile nach Geschlecht
  - Solo- vs. Ko-Autorenschaft nach Geschlecht
  - Veränderung über Zeit
- **Institutionelle Konzentration** (über das `employments`-Feld): Welche Universitäten/Institute dominieren? Wie viele Mitglieder kommen aus außeruniversitären Einrichtungen (DIW, WZB, IAB, GESIS)?
- **Karrierestufen-Proxy**: Role-Titles aus Employment (`Professor`, `Postdoc`, `Doktorand`) → wer publiziert wo in welcher Stufe?

## 2. Thematische Analyse (inhaltlich am ergiebigsten)

- **Topic Modeling** über Titel + `short_description` (LDA klassisch oder BERTopic mit deutsch-englischem Sentence-Transformer): Welche Forschungslinien existieren in der Sektion?
- **Begriffshäufigkeiten über Zeit**: Wann taucht „Intersektionalität", „Pandemie", „Klimaungleichheit", „KI", „Migration" auf, wann verschwinden Begriffe?
- **Ungleichheitsdimensionen-Mapping**: Heuristisches Codieren (Wörterbuch oder LLM-Klassifikation) nach Klasse / Bildung / Gender / Migration / Gesundheit / Region — Welche Dimensionen sind über/unterrepräsentiert?
- **Methoden-Klassifikation** aus Abstract: quantitativ / qualitativ / Mixed / theoretisch — und wie verteilt sich das auf Personen und Zeit?
- **Survey-/Datenquellen-Erwähnung**: Welche Datensätze werden zitiert (SOEP, ALLBUS, NEPS, MZ, PIAAC …)? Das wäre ein interessanter „Datenlandschafts"-Befund.

## 3. Ko-Autorenschafts-Netzwerk (Bild schon da, aber tiefer)

Du hast bereits `koautorinnen_netzwerk_gefiltert.png` — da geht noch viel mehr:

- **Community-Detection** (Louvain / Leiden): Gibt es identifizierbare Forschungs-Cluster innerhalb der Sektion?
- **Brücken-Personen**: Wer verbindet sonst getrennte Cluster (Betweenness-Zentralität)?
- **Intern vs. Extern**: Wie hoch ist der Anteil sektionsinterner Ko-Autorenschaft an allen Ko-Autorenschaften? Ist die Sektion ein „Netzwerk" oder eher ein loses Label?
- **Homophilie**: Publizieren Personen eher mit gleichgeschlechtlichen / gleich-institutionellen Ko-Autor:innen?
- **Dynamik**: Netzwerk pro Jahr → wachsen Cluster, verschmelzen sie?

## 4. Internationalisierung & Open Access

- **Sprache** (`language_code`): Anglisierungs-Trend über Jahre — ein lang diskutiertes Thema in der deutschen Soziologie.
- **Internationale Ko-Autorenschaft**: Wie oft sind Ko-Autor:innen erkennbar nicht an deutschen Institutionen (über CrossRef-Affiliationen anreichern)?
- **OA-Anteil**: Per DOI gegen die **Unpaywall-API** → Welcher Anteil ist frei zugänglich? Gold/Green/Closed-Verteilung über Zeit.
- **Preprint-Anteil**: Steigt die Bedeutung von SocArXiv & Co.?

## 5. Zeitschriften-Landschaft

- **Konzentrations-Index** der Zeitschriften (HHI): Publiziert die Sektion stark in wenigen Hauszeitschriften (KZfSS, ZfS, ZfSoz, Soziale Welt) oder breit gestreut?
- **Disziplinär vs. interdisziplinär**: Soziologie-Journals vs. ökonomische / pädagogische / Public-Health-Journals → Wie disziplinär ist die Sektion?
- **Deutsch- vs. englischsprachige Zeitschriften** im Zeitverlauf.

## 6. Impact & Reichweite (braucht Anreicherung)

- **Zitationen** über die **OpenAlex-API** (kostenlos, gut, statt CrossRef): Verteilung Zitationen pro Paper → wieder mit Lorenz/Gini.
- **Altmetric / Bluesky / Mastodon**: Schwieriger, aber interessant.

## 7. Praktisch für die Sektionsarbeit

- **Newsletter-Frequenz-Diagnostik**: Wie viele Publikationen kommen pro Monat? Lohnt monatlich, alle zwei Monate, quartalsweise?
- **„Aktivitäts-Heatmap"**: Mitglieder × Jahre → wo sind „stille" Mitglieder, die man im Newsletter nie sieht?
- **Daten-Lückenkarte**: Wer hat keine ORCID, wer hat eine, pflegt aber nicht? → Outreach-Liste für den Vorstand.

---

**Wenn du mich fragst**, wo der **größte Mehrwert** für eine **Sektion zu sozialer Ungleichheit** liegt: die Kombination aus **Topic-Modeling** (was wird beforscht?) + **Ungleichheits-Strukturanalyse der Sektion selbst** (Geschlecht, Institutionen, Produktivitäts-Gini). Das ist nicht nur deskriptiv hübsch, sondern hat einen reflexiven Twist, der sich rhetorisch gut auf der Tagung präsentieren lässt: „Die Soziologie der sozialen Ungleichheit — und ihre eigene Ungleichheitsstruktur."

Soll ich eine dieser Analysen konkret ausarbeiten? Wenn ja, welche?