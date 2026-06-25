import streamlit as st

# Titel der Seite
st.title("Mein erstes Python-Quiz 🚀")

# Eine einfache Frage mit Radio-Buttons
st.header("Frage 1: Was ist die Hauptstadt von Frankreich?")
antwort = st.radio("Wähle eine Antwort:", ["Berlin", "London", "Paris", "Madrid"])

# Ein Button, um die Antwort zu bestätigen
if st.button("Antwort überprüfen"):
    if antwort == "Paris":
        st.success("Richtig! 🎉")
    else:
        st.error("Leider falsch. Die richtige Antwort ist Paris.")
