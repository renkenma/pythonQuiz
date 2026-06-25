import streamlit as st
import pandas as pd

# Seiten-Setup
st.set_page_config(page_title="Charakter-Quiz", page_icon="🎁", layout="centered")

st.title("🎁 Welches Geschenk passt zu dir?")
st.write("Finde heraus, welcher Typ du bist. Je nachdem, wie du antwortest, wachsen die Säulen live mit!")

# Platzhalter für das Diagramm erstellen (damit es ganz oben steht, aber erst später gefüllt wird)
chart_placeholder = st.empty()

# --- FRAGENKATALOG ---
# Jede Antwort ist fest einer der drei Kategorien zugeordnet.
fragen = [
    {
        "frage": "1. Wie verbringst du dein perfektes Wochenende?",
        "optionen": {
            "Auf der Couch mit einer gemütlichen Serie": "Entspannung",
            "Mit Mountainbiken oder Bouldern": "Action",
            "Ich besuche ein Museum oder lerne ein neues Hobby": "Neugier"
        }
    },
    {
        "frage": "2. Du gewinnst eine Reise! Wohin geht's?",
        "optionen": {
            "All-Inclusive Strandurlaub auf den Malediven": "Entspannung",
            "Wildwasser-Rafting und Dschungeltour in Costa Rica": "Action",
            "Eine Expedition zu den alten Ruinen von Machu Picchu": "Neugier"
        }
    },
    {
        "frage": "3. Du entdeckst eine geheimnisvolle, alte Tür im Wald. Was tust du?",
        "optionen": {
            "Ich gehe weiter, ist mir zu anstrengend heute.": "Entspannung",
            "Ich trete sie ein und schaue, was mich erwartet!": "Action",
            "Ich untersuche das Schloss und suche nach Hinweisen.": "Neugier"
        }
    },
    {
        "frage": "4. Welches Film-Genre wählst du für den Kinoabend?",
        "optionen": {
            "Eine schöne Feel-Good-Komödie": "Entspannung",
            "Einen lauten, schnellen Blockbuster": "Action",
            "Einen kniffligen Sci-Fi- oder Mystery-Thriller": "Neugier"
        }
    },
    {
        "frage": "5. Ein freier Nachmittag, aber es regnet in Strömen:",
        "optionen": {
            "Perfekt! Zeit für Tee, Decke und Musik.": "Entspannung",
            "Ich fahre in die Indoor-Kletterhalle oder ins Spaßbad.": "Action",
            "Ich verliere mich in einem Wikipedia-Rabbit-Hole.": "Neugier"
        }
    },
    {
        "frage": "6. Auf einer großen Party findet man dich am ehesten...",
        "optionen": {
            "...gemütlich auf dem Sofa in der Ecke.": "Entspannung",
            "...mitten auf der Tanzfläche!": "Action",
            "...in der Küche bei tiefgründigen Diskussionen.": "Neugier"
        }
    },
    {
        "frage": "7. Du bekommst 500 Euro, musst sie aber sofort ausgeben für:",
        "optionen": {
            "Ein luxuriöses Wellness-Wochenende.": "Entspannung",
            "Einen Tandem-Fallschirmsprung.": "Action",
            "Ein hochwertiges Teleskop oder Mikroskop.": "Neugier"
        }
    },
    {
        "frage": "8. Welches dieser Tiere ist dein 'Spirit Animal'?",
        "optionen": {
            "Das Faultier (Meister des Chillens)": "Entspannung",
            "Der Gepard (Schnell und energiegeladen)": "Action",
            "Die Eule (Weise und beobachtend)": "Neugier"
        }
    },
    {
        "frage": "9. Welches Fortbewegungsmittel wählst du?",
        "optionen": {
            "Einen bequemen Zug mit Schlafwagen": "Entspannung",
            "Ein schnelles Motorrad oder einen Jetski": "Action",
            "Ein Forschungs-U-Boot": "Neugier"
        }
    },
    {
        "frage": "10. Was ist dein Lebensmotto?",
        "optionen": {
            "In der Ruhe liegt die Kraft.": "Entspannung",
            "No risk, no fun!": "Action",
            "Man lernt niemals aus.": "Neugier"
        }
    }
]

# --- PUNKTE ZÄHLEN ---
scores = {"Entspannung": 0, "Action": 0, "Neugier": 0}
beantwortet = 0

st.divider()

# Schleife, die alle Fragen anzeigt
for i, q in enumerate(fragen):
    # index=None bewirkt, dass am Anfang kein Punkt ausgewählt ist
    auswahl = st.radio(q["frage"], list(q["optionen"].keys()), index=None, key=f"frage_{i}")
    
    if auswahl:
        # Eigenschaft zur ausgewählten Antwort herausfinden
        eigenschaft = q["optionen"][auswahl]
        scores[eigenschaft] += 1
        beantwortet += 1

st.divider()

# --- DIAGRAMM ZEICHNEN ---
# Hier übergeben wir die gezählten Punkte an das Diagramm oben auf der Seite
df = pd.DataFrame({
    "Kategorie": ["Entspannung", "Action", "Neugier"],
    "Punkte": [scores["Entspannung"], scores["Action"], scores["Neugier"]]
}).set_index("Kategorie")

# st.bar_chart zeichnet die Säulen
chart_placeholder.bar_chart(df, color=["#1f77b4"]) 


# --- AUSWERTUNG & GESCHENK ---
if beantwortet == len(fragen):
    st.success("🎉 Du hast alle Fragen beantwortet! Hier ist dein Ergebnis:")
    
    # Finde die Eigenschaft mit den meisten Punkten
    sieger = max(scores, key=scores.get)
    
    if sieger == "Entspannung":
        st.markdown("### 💆‍♀️ Dein Geschenk: Das Spa-Paket!")
        st.info("Du liebst die Ruhe! Du bekommst eine flauschige Decke, Premium-Badebomben, Duftkerzen und einen Gutschein für eine Massage.")
        st.balloons() # Lässt Ballons über den Bildschirm fliegen
        
    elif sieger == "Action":
        st.markdown("### 🪂 Dein Geschenk: Das Adrenalin-Paket!")
        st.error("Du brauchst Nervenkitzel! Dein Geschenk ist ein Gutschein für einen Bungee-Sprung (oder Lasertag) und eine GoPro für deine nächsten Abenteuer.")
        st.snow() # Lässt passend zu Action Schnee/Konfetti regnen
        
    else:
        st.markdown("### 🕵️‍♂️ Dein Geschenk: Das Entdecker-Paket!")
        st.warning("Dein Kopf braucht Futter! Du bekommst ein geniales Escape-Room-Brettspiel, ein kniffliges 3D-Puzzle und ein Ticket für ein interaktives Museum.")
        st.balloons()

else:
    st.info(f"Es fehlen noch {len(fragen) - beantwortet} Fragen bis zu deinem Geschenk.")
