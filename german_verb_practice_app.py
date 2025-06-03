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

# Feedback stub (replace with OpenAI later if needed)
def evaluate_german_sentence(sentence, verb):
    if verb in sentence:
        return "✅ Sentence appears correct (mock check)."
    else:
        return f"⚠️ It looks like the verb '{verb}' is missing or misused."

# Initialize session state
if "verb" not in st.session_state or "reset" in st.session_state:
    st.session_state.verb = random.choice(list(verbs.keys()))
    st.session_state.correct_translation = verbs[st.session_state.verb]
    if "reset" in st.session_state:
        del st.session_state["reset"]

if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "wrong_count" not in st.session_state:
    st.session_state.wrong_count = 0

# App title
st.title("🇩🇪 German Verb Practice with Feedback")

# Score display
st.markdown(f"✅ **Correct answers:** {st.session_state.correct_count}")
st.markdown(f"❌ **Incorrect answers:** {st.session_state.wrong_count}")

# Show current verb
st.markdown(f"### What does the German verb **'{st.session_state.verb}'** mean in English?")

# Step 1: English translation
user_translation = st.text_input("Enter the English translation:")

if user_translation:
    if user_translation.lower().strip() == st.session_state.correct_translation:
        st.success("✅ Correct! Now use it in a sentence:")
        st.session_state.correct_count += 1

        # Step 2: Ask for sentence usage
        user_sentence = st.text_area(f"✍️ Write a German sentence using **'{st.session_state.verb}'**:")

        if user_sentence:
            if st.session_state.verb in user_sentence:
                st.success("✅ The verb appears in your sentence.")
            else:
                st.warning(f"⚠️ The verb '{st.session_state.verb}' was not found.")

            feedback = evaluate_german_sentence(user_sentence, st.session_state.verb)
            st.markdown(f"🧠 **Grammar Feedback:**\n\n{feedback}")

            if "correct" in feedback.lower():
                st.session_state["reset"] = True
                st.experimental_rerun()

    else:
        st.error(f"❌ Incorrect. The correct translation is: '{st.session_state.correct_translation}'")
        st.session_state.wrong_count += 1

# Safe verb change without crashing
if st.button("Try another verb"):
    st.session_state["reset"] = True
