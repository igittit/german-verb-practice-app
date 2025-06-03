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

# Audio playback function
def play_audio(word):
    if word == "trinken":
        st.audio("trinken.mp3", format="audio/mp3")
    else:
        st.info(f"🔊 No audio file found for '{word}' (demo).")

def repeat_audio(word):
    st.info(f"🔁 Repeating audio for: {word} (mock)")

# Function to check sentence validity
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

# Layout
st.title("🇩🇪 German Word Trainer")
col1, col2 = st.columns(2)
col1.markdown(f"**:green[correct answers:]** {st.session_state.correct_count}")
col2.markdown(f"**:red[wrong answers:]** {st.session_state.wrong_count}")
st.markdown("**Total:**")

# Word prompt
st.markdown(f"#### What does **'{st.session_state.verb}'** mean in English?")
st.session_state.user_translation = st.text_input("Enter answer here:", value=st.session_state.user_translation)

# Sentence usage
st.markdown("### Use the word in a sentence")
st.session_state.user_sentence = st.text_area("", value=st.session_state.user_sentence, height=120)

# Audio buttons
audio_col1, audio_col2 = st.columns([9, 1])
with audio_col2:
    if st.button("🔊", key="play"):
        play_audio(st.session_state.verb)
    if st.button("🔁", key="repeat"):
        repeat_audio(st.session_state.verb)

def reset_and_continue():
    current = st.session_state.verb
    available = [v for v in verbs if v != current]
    st.session_state.verb = random.choice(available)
    st.session_state.correct_translation = verbs[st.session_state.verb]
    st.session_state.user_translation = ""
    st.session_state.user_sentence = ""
    st.session_state.reset = True
    st.experimental_rerun()

# Evaluate answer
if st.session_state.user_translation:
    if st.session_state.user_translation.strip().lower() == st.session_state.correct_translation:
        st.success("✅ Correct translation!")
        if st.session_state.user_sentence:
            feedback = evaluate_german_sentence(st.session_state.user_sentence, st.session_state.verb)
            st.markdown(f"**Feedback:** {feedback}")
            if "correct" in feedback.lower():
                if st.button("Next Word"):
                    st.session_state.correct_count += 1
                    reset_and_continue()
    else:
        st.error(f"❌ Incorrect. The correct translation is '{st.session_state.correct_translation}'.")
        if st.button("Try Another Word"):
            st.session_state.wrong_count += 1
            reset_and_continue()
