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

if not st.session_state.get("reset"):
    user_translation = st.text_input("Enter the English translation:")
    
    if user_translation:
        if user_translation.lower() in st.session_state.correct_translation.lower():
            st.success("✅ Correct translation!")
        else:
            st.error(f"❌ Incorrect. The correct translation is: {st.session_state.correct_translation}")
        
        user_sentence = st.text_area(f"✍️ Now write a German sentence using the verb **'{st.session_state.verb}'**:")
        
        if user_sentence:
            if st.session_state.verb in user_sentence:
                st.success("✅ You used the verb in your sentence.")
            else:
                st.warning(f"⚠️ The verb '{st.session_state.verb}' is not in the sentence.")

            st.markdown("🔍 **Evaluating your sentence...**")
            feedback = evaluate_german_sentence(user_sentence, st.session_state.verb)
            st.markdown(f"🧠 **Grammar Feedback:**\n\n{feedback}")
else:
    # Clear the reset flag and rerun once
    st.session_state["reset"] = False
    st.experimental_rerun()

# This button triggers the session flag instead of a hard rerun
if st.button("Try another verb"):
    new_verb = random.choice(list(verbs.keys()))
    while new_verb == st.session_state.verb:
        new_verb = random.choice(list(verbs.keys()))
    st.session_state.verb = new_verb
    st.session_state.correct_translation = verbs[new_verb]
    st.session_state["reset"] = True
