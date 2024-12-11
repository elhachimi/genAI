import requests
import streamlit as st

st.title("Generate text")

# Checks if the session state has a messages
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    # st.chat_essage is used to display the message in the chat box
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# here we assign the result of st.chat_input to prompt and check if its true
if prompt := st.chat_input("Write your prompt in this input field "):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.text(prompt)

    with st.chat_message("assistant"):
        st.status("Generating response...")
        response = requests.get(
            f"http://localhost:8000/generate/text?prompt={prompt}"
        ).text
        st.text(response)
