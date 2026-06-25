import streamlit as st
import pandas as pd

# Seiten-Setup
st.set_page_config(page_title="Geschenke-Quiz", page_icon="🎟️", layout="centered")

# --- SESSION STATE INITIALISIEREN ---
if 'aktuelle_frage' not in st.session_state:
    st.session_state.aktuelle_frage = 0
    st.session_state.scores = {"Pop-Punk": 0, "Electro": 0, "Comedy": 0}

st.title("🎟️ Wohin geht der nächste Ausflug?")
st.write("Finde heraus, welches Event am besten zu dir passt. Deine Antworten füllen die Säulen live auf!")

# --- DIAGRAMM ZEICHNEN ---
df = pd.DataFrame({
    "Kategorie": ["🎸 Pop-Punk & Vocals", "⚡ Beats & Bass", "😂 Humor & Lachen"],
    "Punkte": [
        st.session_state.scores["Pop-Punk"], 
        st.session_state.scores["Electro"], 
        st.session_state.scores["Comedy"]
    ]
}).set_index("Kategorie")

# Säulendiagramm anzeigen
st.bar_chart(df, color=["#ff4b4b"])
st.divider()

# --- FRAGENKATALOG ---
fragen = [
    {
        "frage": "1. Was ist dir auf einem Event am wichtigsten?",
        "optionen": {
            "Die Texte kennen und laut mitsingen können!": "Pop-Punk",
            "Ein fetter Bass und tanzen, bis die Füße wehtun.": "Electro",
            "Zurücklehnen, gut unterhalten werden und Tränen lachen.": "Comedy"
        }
    },
    {
        "frage": "2. Dein perfektes Outfit fürs Ausgehen besteht aus...",
        "optionen": {
            "...Bandshirt, Jeans und Chucks (oder Doc Martens).": "Pop-Punk",
            "...Glitzer, bunten Farben und dem perfekten Festival-Look.": "Electro",
            "...etwas Bequemem, aber Schickem. Hauptsache man kann gut sitzen.": "Comedy"
        }
    },
    {
        "frage": "3. Was läuft auf dem Roadtrip dorthin im Radio?",
        "optionen": {
            "Gitarren-Riffs und melancholische, aber laute Refrains.": "Pop-Punk",
            "Ein treibendes Set mit ordentlich BPM.": "Electro",
            "Ich höre lieber einen unterhaltsamen Podcast.": "Comedy"
        }
    },
    {
        "frage": "4. Welches Getränk hast du an einem perfekten Abend in der Hand?",
        "optionen": {
            "Ein kühles Bierchen beim Pogen in der Menge.": "Pop-Punk",
            "Einen bunten Cocktail oder Energy-Drink für die Ausdauer.": "Electro",
            "Ein Glas Wein oder ein gezapftes Bier gemütlich am Tisch.": "Comedy"
        }
    },
    {
        "frage": "5. Was ist deine heimliche Superkraft?",
        "optionen": {
            "Ich kenne alle Eras von Taylor Swift auswendig.": "Pop-Punk",
            "Ich kann 12 Stunden am Stück raven.": "Electro",
            "Ich habe für jede Situation den perfekten dummen Spruch.": "Comedy"
        }
    },
    {
        "frage": "6. Wie sieht die ideale Location für dich aus?",
        "optionen": {
            "Ein schwitziger Club oder ein cooler Konzertsaal.": "Pop-Punk",
            "Open-Air mit Lasershow, Sand oder Wiese unter den Füßen.": "Electro",
            "Ein uriges Theater, ein Café oder eine kleine Bühne.": "Comedy"
        }
    },
    {
        "frage": "7. Was machst du, wenn jemand auf der Bühne einen Fehler macht?",
        "optionen": {
            "Egal, das macht es erst authentisch!": "Pop-Punk",
            "Fällt beim nächsten Bass-Drop eh nicht auf.": "Electro",
            "Ich hoffe, da kommt direkt ein spontaner Witz drüber!": "Comedy"
        }
    },
    {
        "frage": "8. Wie beendest du einen legendären Abend?",
        "optionen": {
            "Heiser vom vielen Schreien und Singen auf dem Heimweg.": "Pop-Punk",
            "Den Sonnenaufgang beobachten, weil die Party noch lief.": "Electro",
            "Mit Bauchmuskelkater vom Lachen ins Bett fallen.": "Comedy"
        }
    },
    {
        "frage": "9. Wofür gibst du vor Ort am ehesten Geld aus?",
        "optionen": {
            "Merch! Ich brauche ein Shirt zur Erinnerung.": "Pop-Punk",
            "Für Foodtrucks und leuchtende Accessoires.": "Electro",
            "Für Snacks und Nachschub an guten Drinks am Platz.": "Comedy"
        }
    },
    {
        "frage": "10. Welches Emoji nutzt du am meisten?",
        "optionen": {
            "🎸 oder 💔": "Pop-Punk",
            "⚡ oder 🕺": "Electro",
            "😂 oder 🎤": "Comedy"
        }
    }
]

# --- LOGIK FÜR FRAGEN & AUSWERTUNG ---

if st.session_state.aktuelle_frage < len(fragen):
    q = fragen[st.session_state.aktuelle_frage]
    
    st.subheader(q["frage"])
    
    for antwort_text, eigenschaft in q["optionen"].items():
        if st.button(antwort_text, use_container_width=True):
            st.session_state.scores[eigenschaft] += 1
            st.session_state.aktuelle_frage += 1
            st.rerun()

else:
    st.success("🎉 Du hast alle Fragen beantwortet! Hier ist dein Ergebnis:")
    
    sieger = max(st.session_state.scores, key=st.session_state.scores.get)
    
    if sieger == "Pop-Punk":
        st.markdown("### 🎸 Dein Ticket: Call it Off!")
        st.info("Du brauchst Gitarren, Energie und große Gefühle! Dein Geschenk ist ein Ticket für **Call it Off** – mach dich bereit, Pop-Punk und Taylor Swift Covers lauthals mitzusingen!")
        st.balloons()
        
    elif sieger == "Electro":
        st.markdown("### 🏖️ Dein Ticket: Strandfieber Festival!")
        st.warning("Du willst treibende Beats und Festival-Vibes! Dein Geschenk ist ein Ticket für das **Strandfieber Festival** – pack die Tanzschuhe und die Sonnenbrille ein!")
        st.snow() # Lässt Konfetti/Schnee regnen, perfekt für Festivals
        
    else:
        st.markdown("### 😂 Dein Ticket: 3. Komische Nacht in Oldenburg!")
        st.success("Du liebst gute Unterhaltung und Humor! Dein Geschenk ist ein Ticket für die **3. Komische Nacht in Oldenburg** – ein genialer Comedy-Abend mit Lachkrampf-Garantie.")
        st.balloons()
    
    st.divider()
    
    if st.button("🔄 Quiz neu starten"):
        st.session_state.clear()
        st.rerun()
