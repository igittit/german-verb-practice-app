import streamlit as st
import random

# Sample German verb dictionary
verbs = {
    "gehen": "to go",
    "sehen": "to see",
    "machen": "to do/make",
    "haben": "to have",
    "sein": "to be",
    "sprechen": "to speak",
    "nehmen": "to take",
    "kommen": "to come",
    "essen": "to eat",
    "trinken": "to drink"
}

st.title("🇩🇪 German Verb Practice")

if "verb" not in st.session_state:
    st.session_state.verb = random.choice(list(verbs.keys()))
    st.session_state.correct_translation = verbs[st.session_state.verb]

st.markdown(f"### What does the German verb **'{st.session_state.verb}'** mean in English?")

user_translation = st.text_input("Enter the English translation:")

if user_translation:
    if user_translation.lower() in st.session_state.correct_translation.lower():
        st.success("✅ Correct translation!")
    else:
        st.error(f"❌ Incorrect. The correct translation is: {st.session_state.correct_translation}")

    user_sentence = st.text_area(f"Now write a German sentence using the verb **'{st.session_state.verb}'**:")

    if user_sentence:
        if st.session_state.verb in user_sentence:
            st.success("✅ You used the verb in your sentence.")
        else:
            st.error(f"❌ The verb '{st.session_state.verb}' was not found in your sentence.")

    if st.button("Try another verb"):
        st.session_state.verb = random.choice(list(verbs.keys()))
        st.session_state.correct_translation = verbs[st.session_state.verb]
        st.experimental_rerun()
