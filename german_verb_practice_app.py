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

# (Optional) AI function placeholder
def evaluate_german_sentence(sentence, verb):
    if verb in sentence:
        return "✅ Sentence appears correct (mock check)."
    else:
        return f"⚠️ It looks like the verb '{verb}' is missing or misused."

# Setup session state
if "verb" not in st.session_state:
    st.session_state.verb = random.choice(list(verbs.keys()))
    st.session_state.correct_translation = verbs[st.session_state.verb]
if "reset" not in st.session_state:
    st.session_state.reset = False

# UI title
st.title("🇩🇪 German Verb Practice with Feedback")
st.markdown(f"### What does the German verb **'{st.session_state.verb}'** mean in English?")

# Show inputs only if not resetting
if not st.session_state.reset:
    user_translation = st.text_input("Enter the English translation:")
    
    if user_translation:
        if user_translation.lower() in st.session_state.correct_translation.lower():
            st.success("✅ Correct translation!")
        else:
            st.error(f"❌ Incorrect. The correct translation is: {st.session_state.correct_translation}")
        
        user_sentence = st.text_area(f"✍️ Now write a German sentence using **'{st.session_state.verb}'**:")

        if user_sentence:
            if st.session_state.verb in user_sentence:
                st.success("✅ The verb is in your sentence.")
            else:
                st.warning(f"⚠️ The verb '{st.session_state.verb}' was not found.")

            # Simulated grammar check
            feedback = evaluate_german_sentence(user_sentence, st.session_state.verb)
            st.markdown(f"🧠 **Grammar Feedback:**\n\n{feedback}")
else:
    # Reset and trigger safe rerun
    st.session_state.reset = False
    st.experimental_rerun()

# Button logic to load new verb
if st.button("Try another verb"):
    new_verb = random.choice(list(verbs.keys()))
    while new_verb == st.session_state.verb:
        new_verb = random.choice(list(verbs.keys()))
    st.session_state.verb = new_verb
    st.session_state.correct_translation = verbs[new_verb]
    st.session_state.reset = True
