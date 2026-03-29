import os

from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("Student Study Helper Chatbot")

if gemini_api_key:
    client = OpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    provider_name = "Gemini"
elif openai_api_key and openai_api_key.startswith("AIza"):
    # Gemini keys typically start with AIza; use Gemini endpoint automatically.
    client = OpenAI(
        api_key=openai_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    provider_name = "Gemini"
elif openai_api_key:
    client = OpenAI(api_key=openai_api_key)
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    provider_name = "OpenAI"
else:
    st.error("Set either GEMINI_API_KEY or OPENAI_API_KEY in your .env file, then restart the app.")
    st.stop()

st.caption(f"Provider: {provider_name} | Model: {model_name}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a study question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            stream = client.chat.completions.create(
                model=model_name,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    full_response += delta
                    message_placeholder.markdown(full_response + "|")
        except Exception as exc:
            error_text = str(exc)
            if "Error code: 429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                full_response = (
                    "Quota reached for this Gemini model. Try setting GEMINI_MODEL=gemini-2.5-flash "
                    "in your .env, or check quota/billing in Google AI Studio."
                )
            else:
                full_response = f"Sorry, I hit an error while generating a response: {exc}"

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
