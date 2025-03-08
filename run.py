import streamlit as st
import time
import importlib
import botTest

# Reload botTest to prevent caching issues
importlib.reload(botTest)
from botTest import run

st.title("Kolkata ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Hello, How can I help you?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get chatbot response
    assistant_response = run(prompt)

    # Debugging: Print response
    print(f"User Input: {prompt}, Chatbot Response: {assistant_response}")

    # Handle empty responses
    if not assistant_response:
        assistant_response = "Sorry, I couldn't understand that."

    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Typing effect simulation (optional)
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.03)
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})