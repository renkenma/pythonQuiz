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
    # NEU: merkt sich für jede beantwortete Frage, welcher Text gewählt wurde
    # und welcher Kategorie das zugeordnet war -> Liste von Dicts:
    # {"frage": "...", "antwort": "...", "eigenschaft": "..."}
    st.session_state.beantwortete_fragen = []
    # NEU: Tie-Break Status
    st.session_state.tie_break_active = False
    st.session_state.tie_break_runde = 0

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
    st.title("Schauen wir, was bei diesem kleinen Persönlichkeitstest rauskommt!")

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
            "frage": "1. Stell dir vor, du dürftest ab heute nur noch eine einzige Art von Serie gucken. Wofür entscheidest du dich?",
            "typ": "text",
            "optionen": {
                "Sitcoms wie 'Friends' oder 'The Office'": "Pop-Punk",
                "Action-Game-Shows wie die 'Beast Games' oder 'Crash Games'": "Electro",
                "Trash-TV wie 'Temptation Island' & 'Are you the one?'": "Comedy"
            }
        },
        {
            "frage": "2. Du stehst auf dem Volleyballfeld. Was beschreibt dich am besten?",
            "typ": "text",
            "optionen": {
                "Am wichtigsten ist der Teamgeist und der Spaß mit der Mannschaft": "Pop-Punk",
                "Ich verhaue einen Ball, über den am Ende mit allen gelacht wird": "Comedy",
                "Ich bin motiviert, gebe auf dem Feld alles und will das Spiel unbedingt gewinnen": "Electro"
                
            }
        },
        {
            "frage": "3. Stell dir vor, wir irren bei 35 Grad durch eine fremde Stadt, suchen ewig nach etwas Bestimmten und nichts läuft nach Plan. Was passiert?",
            "typ": "text",
            "optionen": {
                "Augen zu und durch! Die Hitze wird ignoriert, die Energie oben gehalten und es wird zielstrebig weitergelaufen, bis wir da sind.": "Electro",
                "Einer von uns atmet tief durch, nimmt den anderen bei der Hand und es wird versucht, uns gegenseitig zu beruhigen und das Beste daraus zu machen.": "Pop-Punk",
                "Ich bin erst super gestresst, aber spätestens am Abend im Hotel lachen wir uns über dieses komplette Chaos einfach nur kaputt.": "Comedy"
            }
        },
        {
            "frage": "4. Wir gehen heute Abend aus und du machst dich fertig. Wie sieht dieses Szenario typischerweise aus?",
            "typ": "text",
            "optionen": {
                "Die Musik wird aufgedreht, um richtig in Stimmung zu kommen und es wird hier bereits getanzt.": "Electro",
                "Ich ziehe fünf Sachen an, werfe alles aufs Bett und nehme am Ende doch das erste Outfit.": "Comedy",
                "Meine Lieblings-Playlist läuft, ich singe vor dem Spiegel laut mit und probiere in Ruhe meine Outfits an.": "Pop-Punk"
            }
        },
        {
            "frage": "5. Ein komplett freier Tag nur für dich. Wie verbringst du ihn am liebsten?",
            "typ": "text",
            "optionen": {
                "Ich genieße die Zeit mit Freunden oder der Familie": "Pop-Punk",
                "Am liebsten an den See und am noch liebsten davor noch eine Runde wandern": "Electro",
                "Abwechselnd einen spannenden Krimi lesen und Nintendogs spielen": "Comedy"
            }
        },
        {
            "frage": "6. Wenn wir uns in ein Krimi-Ermittler-Duo verwandeln könnten – welches wären wir?",
            "typ": "text",
            "optionen": {
                "Erica Falck & Patrik Hedström (Läckberg)": "Pop-Punk",
                "Ann Kathrin Klaasen & Frank Weller (Wolf)": "Comedy",
                "Pia Sander & Oliver von Bodenstein (Neuhaus)": "Electro"
            }
        },
        {
            "frage": "7. Wähle dein Starter-Team!",
            "typ": "bilder",
            "optionen": [
                {"bild": "pikachuKarnimani.png", "eigenschaft": "Electro", "label": "Pikachu & Karnimani"},
                {"bild": "entonGengar.png", "eigenschaft": "Comedy", "label": "Enton & Gengar"},
                {"bild": "pummeluffDitto.png", "eigenschaft": "Pop-Punk", "label": "Pummeluff & Ditto"}
            ]
        },
        {
            "frage": "8. Was bedeutet dir deine Heimat in Dorum mit einem - damalig noch in Betrieb laufenden - Bauernhof mit der Nähe zur Küste für dich?",
            "typ": "text",
            "optionen": {
                "Meine Familie ist das, was es zu meiner Heimat macht. Die Nähe zur Nordsee und der Bauernhof sind das i-Tüpfelchen oben drauf": "Pop-Punk",
                "Die frische Luft tut mir gut. Neben einem guten Buch auf der Terasse bin ich auch gerne hier an der frischen Luft und am Meer": "Electro",
                "Es ist mein Ort für Ruhe und Entspannung. Ich mag es, wenn man die Dinge einfach mal langsamer angeht und sich nicht von der Hektik treiben lässt": "Comedy"
            }
        },
        {
            "frage": "9. Ganz ehrlich: Was schätzt du an mir am meisten?",
            "typ": "text",
            "optionen": {
                "Dass ich mich so schnell und leidenschaftlich für neue Dinge begeistern kann": "Pop-Punk",
                "Mein Nerd-Wissen über Pokémon und Yu-Gi-Oh!": "Electro",
                "Dass wir in fast jeder Situation gemeinsam Spaß haben können": "Comedy"
            }
        },
        {
            "frage": "10. Wir verkaufen was bei Kleinanzeigen. Jemand nervt total – wie reagierst du?",
            "typ": "text",
            "optionen": {
                "Ich antworte selbst in einem lustig-frechen Ton und mache mir einen Spaß daraus": "Comedy",
                "Ich bin etwas angefresse und überlege, ob ich gar nicht antworte oder dieser Person die Leviten lese": "Electro",
                "Ich versuche das Gute in dieser Person zu sehen und versuche freundlich ein vernünftiges Gespräch zu führen": "Pop-Punk"
                
                
            }
        },
    ]

    # --- LOGIK FÜR FRAGEN & AUSWERTUNG ---
    if not st.session_state.tie_break_active and st.session_state.aktuelle_frage < len(fragen):
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
                        st.session_state.beantwortete_fragen.append({
                            "frage": q["frage"],
                            "antwort": option["label"],
                            "eigenschaft": option["eigenschaft"]
                        })
                        st.session_state.aktuelle_frage += 1
                        st.rerun()

        # 2. FALL: Es ist eine reine Text-Frage
        elif q["typ"] == "text":
            for antwort_text, eigenschaft in q["optionen"].items():
                if st.button(antwort_text, key=f"btn_{st.session_state.aktuelle_frage}_{antwort_text}", use_container_width=True):
                    st.session_state.scores[eigenschaft] += 1
                    st.session_state.beantwortete_fragen.append({
                        "frage": q["frage"],
                        "antwort": antwort_text,
                        "eigenschaft": eigenschaft
                    })
                    st.session_state.aktuelle_frage += 1
                    st.rerun()

    else:
        # Alle 10 Fragen sind durch (oder wir kommen aus einem Tie-Break) ->
        # jetzt prüfen, ob ein Gleichstand vorliegt.
        sorted_scores = sorted(st.session_state.scores.values(), reverse=True)
        ist_gleichstand = sorted_scores[0] == sorted_scores[1]

        if ist_gleichstand:
            # Welche Kategorien stecken im Gleichstand?
            top_wert = sorted_scores[0]
            tie_kategorien = [k for k, v in st.session_state.scores.items() if v == top_wert]

            # WICHTIG: tie_break_runde nur erhöhen, wenn wir NEU in den
            # Tie-Break-Modus wechseln (nicht bei jedem Rerun während wir
            # schon drin sind) - sonst ändern sich die Button-Keys zwischen
            # Klick und Auswertung und der Klick geht "verloren".
            if not st.session_state.tie_break_active:
                st.session_state.tie_break_runde += 1
            st.session_state.tie_break_active = True

            st.warning(f"🤔 Kopf-an-Kopf-Rennen!")
            st.subheader("Welche dieser Fragen war für dich am wichtigsten?")

            for i, eintrag in enumerate(st.session_state.beantwortete_fragen):
                label = f"**{eintrag['frage']}**\n"
                if st.button(
                    label,
                    key=f"tiebreak_{st.session_state.tie_break_runde}_{i}",
                    use_container_width=True
                ):
                    # Die Eigenschaft dieser Frage bekommt einen weiteren Punkt
                    st.session_state.scores[eintrag["eigenschaft"]] += 1
                    st.session_state.tie_break_active = False
                    st.rerun()

        else:
            # --- ERGEBNIS-ANZEIGE (klarer Sieger) ---
            st.success("🎉 Du hast alle Fragen beantwortet!")

            sieger = max(st.session_state.scores, key=st.session_state.scores.get)
            st.success(f"Dein Ergebnis ist: {sieger}")

            if sieger == "Pop-Punk":
                st.markdown("### 🎸 Dein Ticket: Call it Off!")
                st.info("Du brauchst Gitarren, Energie und große Gefühle! Dein Geschenk ist ein Ticket für **Call it Off** – mach dich bereit, Pop-Punk und Taylor Swift Covers lauthals mitzusingen!")
                st.info("Solltest du Interesse daran haben zu erfahren, was sich hinter den anderen Geschenken verbirgt, halte ich dich nicht davon ab dieses Quiz erneut zu spielen 😊! Vielleicht ist dein Charakter ja doch anders als in diesem Durchlauf 🤫.")
                st.balloons()

            elif sieger == "Electro":
                st.markdown("### 🏖️ Dein Ticket: Strandfieber Festival!")
                st.warning("Du willst treibende Beats und Festival-Vibes! Dein Geschenk ist ein Ticket für das **Strandfieber Festival** – pack die Tanzschuhe und die Sonnenbrille ein!")
                st.warning("Solltest du Interesse daran haben zu erfahren, was sich hinter den anderen Geschenken verbirgt, halte ich dich nicht davon ab dieses Quiz erneut zu spielen 😊! Vielleicht ist dein Charakter ja doch anders als in diesem Durchlauf 🤫.")
                st.balloons()

            else:
                st.markdown("### 😂 Dein Ticket: 3. Komische Nacht in Oldenburg!")
                st.success("Du liebst gute Unterhaltung und Humor! Dein Geschenk ist ein Ticket für die **3. Komische Nacht in Oldenburg** – ein genialer Comedy-Abend mit Lachkrampf-Garantie.")
                st.success("Solltest du Interesse daran haben zu erfahren, was sich hinter den anderen Geschenken verbirgt, halte ich dich nicht davon ab dieses Quiz erneut zu spielen 😊! Vielleicht ist dein Charakter ja doch anders als in diesem Durchlauf 🤫.")
                st.balloons()

            st.divider()
            if st.button("🔄 Quiz neu starten"):
                st.session_state.clear()
                st.rerun()
