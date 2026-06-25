import streamlit as st
import pandas as pd

# --- SEITEN-SETUP ---
st.set_page_config(page_title="Geburtstags-Quiz", page_icon="🎁", layout="centered")

# --- SESSION STATE INITIALISIEREN ---
# Wir speichern, ob das Quiz gestartet wurde, bei welcher Frage wir sind und die Punkte
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.aktuelle_frage = 0
    st.session_state.scores = {"Pop-Punk": 0, "Electro": 0, "Comedy": 0}

# ==========================================
# 1. STARTSEITE (Vor dem Klick)
# ==========================================
if not st.session_state.quiz_started:
    st.title("🎁 Alles Gute zum Geburtstag!")
    
    st.markdown("""
    **Hey mein Schatz** 😊 Ich wünsche dir zum Geburtstag nur das Beste der Welt und dass all' deine Wünsche in Erfüllung gehen! 😊 Bei einigen dieser Wünsche spiele ich hoffentlich die Hauptrolle ❤️. 
    
    Ich will dir natürlich soviel bieten wie möglich! Allerdings haben wir uns ein Limit bei den Geschenken gesetzt. Daher kann ich dich nicht zu allen 3 Ideen einladen, woran ich so gedacht habe 😔. Das reduziert den Spaß nun auf ein Drittel, aber <span style="display:inline-block; text-align:center; vertical-align:middle; line-height:1;"><span style="display:block; border-bottom:1px solid currentColor; padding:0 2px;">∞</span><span style="display:block;">3</span></span> ist auch nicht gerade wenig! Ich möchte allerdings nicht, dass du nach Lust und Laune entscheidest und diese Entscheidung am Ende bereust! 
    
    Wie wäre es, wenn wir das machen, was am besten zu dir passt? Dir werden hier keine expliziten Erlebnisse vorgeschlagen. Stattdessen habe ich ein kleines Quiz für dich vorbereitet, das deinen Charakter prüft. 
    
    Nimm es mit einer Prise Humor und vielleicht kommst du ja anhand der Fragen schon darauf, was für Ideen ich im Hintergrund für dich geplant habe. Und nun: Klick den Button und viel Spaß bei deinem Quiz! 😊
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Der Start-Button
    if st.button("🚀 Quiz starten", use_container_width=True):
        st.session_state.quiz_started = True
        st.rerun()

# ==========================================
# 2. QUIZ-BEREICH (Nach dem Klick)
# ==========================================
else:
    st.title("🎟️ Wohin geht der nächste Ausflug?")
    
    # --- DIAGRAMM ZEICHNEN ---
    df = pd.DataFrame({
        "Kategorie": ["🎸 Pop-Punk", "⚡ Electro", "😂 Comedy"],
        "Punkte": [
            st.session_state.scores["Pop-Punk"], 
            st.session_state.scores["Electro"], 
            st.session_state.scores["Comedy"]
        ]
    }).set_index("Kategorie")

    st.bar_chart(df, color=["#ff4b4b"])
    st.divider()

    # --- FRAGENKATALOG ---
    fragen = [
        {
            "frage": "1. Wähle dein Starter-Team!",
            "typ": "bilder",
            "optionen": [
                {"bild": "pikachuKarnimani.png", "eigenschaft": "Electro", "label": "Pikachu & Karnimani"},
                {"bild": "entonGengar.png", "eigenschaft": "Comedy", "label": "Enton & Gengar"},
                {"bild": "pummeluffDitto.png", "eigenschaft": "Pop-Punk", "label": "Pummeluff & Ditto"}
            ]
        },
        {
            "frage": "2. Dein perfektes Outfit fürs Ausgehen besteht aus...",
            "typ": "text",
            "optionen": {
                "...Bandshirt, Jeans und Chucks (oder Doc Martens).": "Pop-Punk",
                "...Glitzer, bunten Farben und dem perfekten Festival-Look.": "Electro",
                "...etwas Bequemem, aber Schickem. Hauptsache man kann gut sitzen.": "Comedy"
            }
        },
        {
            "frage": "3. Was läuft auf dem Roadtrip dorthin im Radio?",
            "typ": "text",
            "optionen": {
                "Gitarren-Riffs und melancholische, aber laute Refrains.": "Pop-Punk",
                "Ein treibendes Set mit ordentlich BPM.": "Electro",
                "Ich höre lieber einen unterhaltsamen Podcast.": "Comedy"
            }
        },
        {
            "frage": "4. Welches Getränk hast du an einem perfekten Abend in der Hand?",
            "typ": "text",
            "optionen": {
                "Ein kühles Bierchen beim Pogen in der Menge.": "Pop-Punk",
                "Einen bunten Cocktail oder Energy-Drink für die Ausdauer.": "Electro",
                "Ein Glas Wein oder ein gezapftes Bier gemütlich am Tisch.": "Comedy"
            }
        },
        {
            "frage": "5. Was ist deine heimliche Superkraft?",
            "typ": "text",
            "optionen": {
                "Ich kenne alle Eras von Taylor Swift auswendig.": "Pop-Punk",
                "Ich kann 12 Stunden am Stück raven.": "Electro",
                "Ich habe für jede Situation den perfekten dummen Spruch.": "Comedy"
            }
        },
        {
            "frage": "6. Wie sieht die ideale Location für dich aus?",
            "typ": "text",
            "optionen": {
                "Ein schwitziger Club oder ein cooler Konzertsaal.": "Pop-Punk",
                "Open-Air mit Lasershow, Sand oder Wiese unter den Füßen.": "Electro",
                "Ein uriges Theater, ein Café oder eine kleine Bühne.": "Comedy"
            }
        },
        {
            "frage": "7. Was machst du, wenn jemand auf der Bühne einen Fehler macht?",
            "typ": "text",
            "optionen": {
                "Egal, das macht es erst authentisch!": "Pop-Punk",
                "Fällt beim nächsten Bass-Drop eh nicht auf.": "Electro",
                "Ich hoffe, da kommt direkt ein spontaner Witz drüber!": "Comedy"
            }
        },
        {
            "frage": "8. Wie beendest du einen legendären Abend?",
            "typ": "text",
            "optionen": {
                "Heiser vom vielen Schreien und Singen auf dem Heimweg.": "Pop-Punk",
                "Den Sonnenaufgang beobachten, weil die Party noch lief.": "Electro",
                "Mit Bauchmuskelkater vom Lachen ins Bett fallen.": "Comedy"
            }
        },
        {
            "frage": "9. Wofür gibst du vor Ort am ehesten Geld aus?",
            "typ": "text",
            "optionen": {
                "Merch! Ich brauche ein Shirt zur Erinnerung.": "Pop-Punk",
                "Für Foodtrucks und leuchtende Accessoires.": "Electro",
                "Für Snacks und Nachschub an guten Drinks am Platz.": "Comedy"
            }
        },
        {
            "frage": "10. Welches Emoji nutzt du am meisten?",
            "typ": "text",
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
        
        # 1. FALL: Es ist eine Bild-Frage
        if q["typ"] == "bilder":
            # Wir machen 3 Spalten nebeneinander
            col1, col2, col3 = st.columns(3)
            
            for index, (col, option) in enumerate(zip([col1, col2, col3], q["optionen"])):
                with col:
                    # Bild anzeigen
                    st.image(option["bild"], use_container_width=True)
                    # Button darunter
                    if st.button(option["label"], key=f"btn_{st.session_state.aktuelle_frage}_{index}", use_container_width=True):
                        st.session_state.scores[option["eigenschaft"]] += 1
                        st.session_state.aktuelle_frage += 1
                        st.rerun()
                        
        # 2. FALL: Es ist eine reine Text-Frage
        elif q["typ"] == "text":
            for antwort_text, eigenschaft in q["optionen"].items():
                if st.button(antwort_text, key=f"btn_{st.session_state.aktuelle_frage}_{antwort_text}", use_container_width=True):
                    st.session_state.scores[eigenschaft] += 1
                    st.session_state.aktuelle_frage += 1
                    st.rerun()

    # --- ERGEBNIS-ANZEIGE ---
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
            st.snow()
            
        else:
            st.markdown("### 😂 Dein Ticket: 3. Komische Nacht in Oldenburg!")
            st.success("Du liebst gute Unterhaltung und Humor! Dein Geschenk ist ein Ticket für die **3. Komische Nacht in Oldenburg** – ein genialer Comedy-Abend mit Lachkrampf-Garantie.")
            st.balloons()
        
        st.divider()
        if st.button("🔄 Quiz neu starten"):
            st.session_state.clear()
            st.rerun()
