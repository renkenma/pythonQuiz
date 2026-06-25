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
    **Hey mein Schatz :)** Ich wünsche dir zum Geburtstag nur das beste der Welt und dass all' deine Wünsche in Erfüllung gehen! :) Bei einigen spiele ich hoffentlich die Hauptrolle <3. 
    
    Ich will dir natürlich soviel bieten wie möglich! Allerdings haben wir uns ein Limit bei den Geschenken gesetzt :(. Daher kann ich dich nicht zu allem einladen, woran ich so gedacht habe. Aber ich will ja nicht, dass du nach Lust und Laune entscheidest! 
    
    Wie wäre es, wenn wir das machen, was am besten zu dir passt? Dir werden hier keine expliziten Erlebnisse vorgeschlagen. Stattdessen habe ich ein kleines Quiz für dich organisiert, das deinen Charakter prüft. 
    
    Nimm es mit einer Prise Humor und vielleicht kommst du ja anhand der Fragen schon darauf, was für Ideen ich im Hintergrund für dich geplant habe.
    """)
    
    st.divider()
    
    # Der Start-Button
    if st.button("🚀 Klick hier und viel Spaß bei deinem Quiz!", use_container_width=True):
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

    # --- FRAGENKATALOG (Hier bauen wir dann die neuen Fragen & Bilder ein) ---
    fragen = [
        {
            "frage": "1. Test-Frage (wird später ersetzt)",
            "optionen": {
                "Antwort A": "Pop-Punk",
                "Antwort B": "Electro",
                "Antwort C": "Comedy"
            }
        },
        # Weitere Fragen folgen...
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
            st.balloons()
            
        elif sieger == "Electro":
            st.markdown("### 🏖️ Dein Ticket: Strandfieber Festival!")
            st.snow()
            
        else:
            st.markdown("### 😂 Dein Ticket: 3. Komische Nacht in Oldenburg!")
            st.balloons()
        
        st.divider()
        if st.button("🔄 Quiz neu starten"):
            st.session_state.clear()
            st.rerun()
