import streamlit as st
import google.generativeai as genai


# Set up the OpenAI API key
genai.configure(api_key="AIzaSyD2pFAv4wpZCgFrPZm4LGKz_G8sexQUM0U")

model = genai.GenerativeModel (model_name = "models/gemini-1.5-flash",system_instruction = sys_prompt)

chatbot = model.start_chat(history=[])
st.title("AI Code Reviewer")

st.chat_message("ai").write("Hi there! I am a helpful AI Assistant. How can I help you today?")

user_prompt = st.chat_input("Enter your Prompt here...")
if user_prompt:
    messager = st.chat_message("Human").write(user_prompt)
    response = chatbot.send_message(user_prompt)
    st.chat_message("ai").write( response.text)

