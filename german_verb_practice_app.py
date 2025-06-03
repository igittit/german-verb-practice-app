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

# Function to check sentence validity
def evaluate_german_sentence(sentence, verb):
    # Improved checking for verb forms
    verb_forms = [
        verb,  # infinitive
        verb[:-2] + "e",  # ich form for regular verbs
        verb[:-2] + "st", # du form
        verb[:-2] + "t",  # er/sie/es form
        verb[:-1]         # wir/sie/Sie form
    ]
    
    # Check if any form of the verb appears
    if any(form in sentence.lower() for form in verb_forms):
        return "✅ Great! Verb used correctly in sentence."
    return f"⚠️ The verb '{verb}' appears to be missing or misused."

# Initialize session state
if "verb" not in st.session_state:
    st.session_state.verb = random.choice(list(verbs.keys()))
    st.session_state.correct_translation = verbs[st.session_state.verb]
    st.session_state.user_translation = ""
    st.session_state.user_sentence = ""
    st.session_state.correct_count = 0
    st.session_state.wrong_count = 0
    st.session_state.stage = "translation"  # Track progress stage

st.title("🇩🇪 German Verb Practice")
st.markdown(f"✅ **Correct:** {st.session_state.correct_count}  |  ❌ **Incorrect:** {st.session_state.wrong_count}")
st.markdown(f"### What does the German verb **'{st.session_state.verb}'** mean in English?")

# Step 1: Translation
user_translation = st.text_input(
    "Enter the English translation:", 
    value=st.session_state.user_translation,
    key="translation_input"
)

# Handle translation submission
if st.session_state.stage == "translation" and user_translation:
    st.session_state.user_translation = user_translation
    
    if user_translation.strip().lower() == st.session_state.correct_translation:
        st.success("✅ Correct translation!")
        st.session_state.stage = "sentence"
    else:
        st.error(f"❌ Incorrect. The correct translation is '{st.session_state.correct_translation}'.")
        st.session_state.wrong_count += 1

# Step 2: Sentence (only show if translation was correct)
if st.session_state.stage == "sentence":
    user_sentence = st.text_area(
        f"✍️ Write a sentence using '{st.session_state.verb}':", 
        value=st.session_state.user_sentence,
        key="sentence_input"
    )
    
    if user_sentence:
        st.session_state.user_sentence = user_sentence
        
        # Basic verb presence check
        if st.session_state.verb.lower() in user_sentence.lower():
            st.success("✅ Verb found in your sentence.")
        else:
            st.warning(f"⚠️ The verb '{st.session_state.verb}' appears to be missing.")
        
        # Get detailed feedback
        feedback = evaluate_german_sentence(user_sentence, st.session_state.verb)
        st.markdown(f"**Feedback:** {feedback}")
        
        # Move to next verb
        if st.button("Next Verb"):
            # Reset state for new verb
            st.session_state.verb = random.choice(list(verbs.keys()))
            st.session_state.correct_translation = verbs[st.session_state.verb]
            st.session_state.user_translation = ""
            st.session_state.user_sentence = ""
            st.session_state.stage = "translation"
            st.session_state.correct_count += 1
            st.experimental_rerun()
