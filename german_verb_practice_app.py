import streamlit as st
import random
import base64
from PIL import Image
from io import BytesIO
import time
import openai

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

def evaluate_sentence_with_openai(sentence, verb):
    prompt = (
        f"Evaluate this German sentence: \"{sentence}\"\n"
        f"1. Is it grammatically correct?\n"
        f"2. Does it use the verb '{verb}' appropriately in context?\n"
        f"3. Suggest a better version if needed.\n\n"
        f"Respond in English."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=300
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ OpenAI API error: {e}"

# Sample dictionary
verbs = {
    "trinken": {
        "english": "to drink",
        "image": "coffee_cup",
        "sample_sentence": "Er trinkt einen Kaffee am Morgen.",
        "sample_translation": "He drinks coffee in the morning."
    }
}

def generate_image():
    img = Image.new('RGB', (300, 200), color=(255, 245, 230))
    img.paste((101, 67, 33), (120, 100, 180, 150))  # Cup
    img.paste((200, 150, 100), (125, 95, 175, 100))  # Top
    return img

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def main():
    st.set_page_config(page_title="German Verb Practice", page_icon="🇩🇪", layout="centered")
    st.title("🇩🇪 German Verb Practice with AI")

    if "correct_count" not in st.session_state:
        st.session_state.correct_count = 0
    if "wrong_count" not in st.session_state:
        st.session_state.wrong_count = 0

    verb = "trinken"
    data = verbs[verb]

    st.markdown(f"### What does **'{verb}'** mean in English?")
    user_translation = st.text_input("Enter the English translation:")

    img = generate_image()
    st.image(img, caption="Visual Reference", width=300)

    if user_translation:
        if user_translation.strip().lower() == data["english"]:
            st.success("✅ Correct! Now use it in a German sentence.")
            user_sentence = st.text_area(f"Write a German sentence using '{verb}':")
            if user_sentence:
                feedback = evaluate_sentence_with_openai(user_sentence, verb)
                st.markdown(f"**🧠 AI Feedback:**\n\n{feedback}")
                if st.button("Next (mock)"):
                    st.session_state.correct_count += 1
                    st.experimental_rerun()
        else:
            st.error(f"❌ Incorrect. The correct translation is: {data['english']}")
            st.session_state.wrong_count += 1

    st.markdown(f"---\n✅ Correct: **{st.session_state.correct_count}**  |  ❌ Wrong: **{st.session_state.wrong_count}**")

if __name__ == "__main__":
    main()
