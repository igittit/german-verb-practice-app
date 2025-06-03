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

# Optional AI feedback stub
def evaluate_german_sentence(sentence, verb):
    if verb in sentence:
        return "✅ Sentence appears correct (mock check)."
    else:
        return f"⚠️ It looks like the verb '{verb}' is missing or misused."

# INITIALIZE SESSION STATE
if "verb" not in st.session_state:
    st.session_state.verb = random.choice(list(verbs.keys()))
    st.session_state.correct_translation = verbs[st.session_state.verb]
    st.session_state.step = 0  # 0: ask, 1: new verb

# MAIN INTERFACE
st.title("🇩🇪 German Verb Practice with Feedback")

# Show current verb
st.markdown(f"### What does the German verb **'{st.session_state.verb}'** mean in English?")

# Only proceed if not in reset mode
user_translation = st.text_input("Enter the English translation:")
if user_translation:
    if user_translation.lower() in st.session_state.correct_translation.lower():
        st.success("✅ Correct translation!")
    else:
        st.error(f"❌ Incorrect. The correct translation is: {st.session_state.correct_translation}")

    user_sentence = st.text_area(f"✍️ Now write a German sentence using the verb **'{st.session_state.verb}'**:")
    if user_sentence:
        if st.session_state.verb in user_sentence:
            st.success("✅ The verb is in your sentence.")
        else:
            st.warning(f"⚠️ The verb '{st.session_state.verb}' was not found.")

        feedback = evaluate_german_sentence(user_sentence, st.session_state.verb)
        st.markdown(f"🧠 **Grammar Feedback:**\n\n{feedback}")

# Safely switch to a new verb without rerun
if st.button("Try another verb"):
    current = st.session_state.verb
    options = [v for v in verbs if v != current]
    new_verb = random.choice(options)
    st.session_state.verb = new_verb
    st.session_state.correct_translation = verbs[new_verb]
    st.session_state.step = 0
    st.experimental_set_query_params()  # soft-refresh helper (optional)
    st.info(f"🎲 New verb: **{new_verb}** — scroll up to start!")
