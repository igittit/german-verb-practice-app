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

# Function to check sentence validity (stub for AI integration)
def evaluate_german_sentence(sentence, verb):
    if verb in sentence:
        return "✅ Sentence appears correct (mock check)."
    return f"⚠️ It looks like the verb '{verb}' is missing or misused."

# Initialize session state
if "verb" not in st.session_state or st.session_state.get("reset", False):
    st.session_state.verb = random.choice(list(verbs.keys()))
    st.session_state.correct_translation = verbs[st.session_state.verb]
    st.session_state.user_translation = ""
    st.session_state.user_sentence = ""
    st.session_state.reset = False

if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "wrong_count" not in st.session_state:
    st.session_state.wrong_count = 0

st.title("🇩🇪 German Verb Practice")
st.markdown(f"✅ **Correct:** {st.session_state.correct_count}  |  ❌ **Incorrect:** {st.session_state.wrong_count}")
st.markdown(f"### What does the German verb **'{st.session_state.verb}'** mean in English?")

# Step 1: Translation
st.session_state.user_translation = st.text_input("Enter the English translation:", value=st.session_state.user_translation)

# Step 2: Sentence
if st.session_state.user_translation:
    if st.session_state.user_translation.strip().lower() == st.session_state.correct_translation:
        st.success("✅ Correct translation!")
        st.session_state.user_sentence = st.text_area(f"✍️ Write a sentence using '{st.session_state.verb}':", value=st.session_state.user_sentence)

        if st.session_state.user_sentence:
            if st.session_state.verb in st.session_state.user_sentence:
                st.success("✅ Verb found in your sentence.")
            else:
                st.warning(f"⚠️ The verb '{st.session_state.verb}' is missing.")

            feedback = evaluate_german_sentence(st.session_state.user_sentence, st.session_state.verb)
            st.markdown(f"**Feedback:** {feedback}")

            if "correct" in feedback.lower():
                st.session_state.correct_count += 1
                if st.button("Next Verb"):
                    st.session_state.reset = True
                    st.experimental_rerun()
    else:
        st.error(f"❌ Incorrect. The correct translation is '{st.session_state.correct_translation}'.")
        st.session_state.wrong_count += 1
        if st.button("Try Another Verb"):
            st.session_state.reset = True
            st.experimental_rerun()
