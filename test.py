import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyD2pFAv4wpZCgFrPZm4LGKz_G8sexQUM0U")

sys_prompt = """Your a helpful AI Tutor for Data Science.
Students will ask you doubts related to varius topics in data science.
You expected to reply in as much detail as possible.
Make sure to take examples while explaining a concept
In case if a student ask any questions outside the data science scope.
politely decline and tell them to ask the questions from data science domin only. """

model = ai.GenerativeModel (model_name = "models/gemini-1.5-flash",system_instruction = sys_prompt)

st.title("Data Science Tutor Application")
st.subheader("By: :blue[Ranga] :sunglasses:")
user_prompt = st.text_input("Enter your query:",placeholder="Type your query here...")
On_click = st.button("Generate Answer")
if On_click == True:
    # do somethin 
    # generate response: we need gemini  or gpt model, configure (set the api key),call the model to generate the response.
    response = model.generate_content(user_prompt)
    st.write(response.text)
