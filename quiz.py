import streamlit as st
import pandas as pd

# Seiten-Setup
st.set_page_config(page_title="Charakter-Quiz", page_icon="🎁", layout="centered")

# --- SESSION STATE INITIALISIEREN ---
# Wir speichern die aktuelle Frage und die Punkte dauerhaft für diese Sitzung
if 'aktuelle_frage' not in st.session_state:
    st.session_state.aktuelle_frage = 0
    st.session_state.scores = {"Entspannung": 0, "Action": 0, "Neugier": 0}

st.title("🎁 Welches Geschenk passt zu dir?")

# --- DIAGRAMM ZEICHNEN ---
# Das Diagramm wird immer aus dem aktuellen Session-State generiert
df = pd.DataFrame({
    "Kategorie": ["Entspannung", "Action", "Neugier"],
    "Punkte": [
        st.session_state.scores["Entspannung"], 
        st.session_state.scores["Action"], 
        st.session_state.scores["Neugier"]
    ]
}).set_index("Kategorie")

# Säulendiagramm anzeigen
st.bar_chart(df, color=["#1f77b4"])
st.divider()

# --- FRAGENKATALOG ---
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

# --- LOGIK FÜR FRAGEN & AUSWERTUNG ---

# Prüfen, ob noch Fragen übrig sind
if st.session_state.aktuelle_frage < len(fragen):
    # Aktuelle Frage holen
    q = fragen[st.session_state.aktuelle_frage]
    
    st.subheader(q["frage"])
    
    # Für jede Antwortmöglichkeit einen Button erstellen
    for antwort_text, eigenschaft in q["optionen"].items():
        # Wenn der Button geklickt wird:
        if st.button(antwort_text, use_container_width=True):
            # 1. Punkt zur jeweiligen Eigenschaft addieren
            st.session_state.scores[eigenschaft] += 1
            # 2. Zur nächsten Frage springen
            st.session_state.aktuelle_frage += 1
            # 3. Seite sofort neu laden, um Änderung anzuzeigen
            st.rerun()

else:
    # Alle Fragen wurden beantwortet -> Auswertung!
    st.success("🎉 Du hast alle Fragen beantwortet! Hier ist dein Ergebnis:")
    
    # Finde die Eigenschaft mit den meisten Punkten im Session State
    sieger = max(st.session_state.scores, key=st.session_state.scores.get)
    
    if sieger == "Entspannung":
        st.markdown("### 💆‍♀️ Dein Geschenk: Das Spa-Paket!")
        st.info("Du liebst die Ruhe! Du bekommst eine flauschige Decke, Premium-Badebomben, Duftkerzen und einen Gutschein für eine Massage.")
        st.balloons()
        
    elif sieger == "Action":
        st.markdown("### 🪂 Dein Geschenk: Das Adrenalin-Paket!")
        st.error("Du brauchst Nervenkitzel! Dein Geschenk ist ein Gutschein für einen Bungee-Sprung (oder Lasertag) und eine GoPro für deine nächsten Abenteuer.")
        st.snow()
        
    else:
        st.markdown("### 🕵️‍♂️ Dein Geschenk: Das Entdecker-Paket!")
        st.warning("Dein Kopf braucht Futter! Du bekommst ein geniales Escape-Room-Brettspiel, ein kniffliges 3D-Puzzle und ein Ticket für ein interaktives Museum.")
        st.balloons()
    
    st.divider()
    
    # Optional: Ein Button, um das Quiz neu zu starten
    if st.button("🔄 Quiz neu starten"):
        st.session_state.clear()
        st.rerun()
