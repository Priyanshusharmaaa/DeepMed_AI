import streamlit as st
from chatbotBackend import ask_medical_bot

st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")
st.title("🩺 Medical Advisor Chatbot")
st.markdown("Feel free to ask any medical-related questions. ⚕️")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Describe your symptoms or ask a question...")

if user_input:
    response = ask_medical_bot(user_input)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))


for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)
