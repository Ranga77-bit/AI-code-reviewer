import streamlit as st
import google.generativeai as genai

# actual GoogleAI API key
genai.configure(api_key="AIzaSyD2pFAv4wpZCgFrPZm4LGKz_G8sexQUM0U")

# Define the system instruction (sys_prompt)
sys_prompt = "You are a helpful assistant that reviews Python code and provides feedback on potential bugs along with suggested fixes."

# Create the model instance
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", system_instruction=sys_prompt)

# Initialize chatbot
chatbot = model.start_chat(history=[])

st.title("AI Code Reviewer")

# Initial AI message
if "history" not in st.session_state:
    st.session_state.history = []
    st.chat_message("ai").write("Hi there! I am a helpful AI Assistant. How can I help you today?")

# Function to review code
def review_code(code):
    try:
        # Generate feedback
        feedback_response = chatbot.send_message(
            f"Review the following Python code and provide feedback on potential bugs and suggest fixes:\n\n{code}\n\nFeedback:"
        )
        feedback = feedback_response.text.strip()

        # Generate fixed code based on feedback
        fixed_code_response = chatbot.send_message(
            f"Here is the Python code with suggested fixes based on the feedback:\n\n{feedback}\n\nFixed Code:"
        )
        fixed_code = fixed_code_response.text.strip()

        return feedback, fixed_code

    except Exception as e:
        return f"An error occurred: {e}", ""

# Handle user input and AI responses
user_prompt = st.chat_input("Enter your Python code here...")

if user_prompt:
    st.session_state.history.append(("Human", user_prompt))
    st.chat_message("Human").write(user_prompt)

    feedback, fixed_code = review_code(user_prompt)
    st.session_state.history.append(("AI", feedback))
    st.session_state.history.append(("AI", fixed_code))

# Display chat history
for sender, message in st.session_state.history:
    st.chat_message(sender).write(message)

# Additional interactive elements
st.write("Submit your Python code for review and get feedback on potential bugs along with suggestions for fixes.")
st.write("Make sure your code is well-formatted before submission for the best results.")
