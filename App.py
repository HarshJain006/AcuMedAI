import streamlit as st
import requests
import json

# Set up Streamlit page
st.set_page_config(page_title="Local ChatGPT Clone", page_icon="🤖", layout="wide")
st.title("🤖 Local ChatGPT Clone")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What's on your mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user prompt to vLLM server and get the response
    response = requests.post(
        "http://localhost:8000/v1/completions",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "model": "meta-llama/Llama-3.2-3B",
            "prompt": prompt,
            "max_tokens": 512,
            "temperature": 0.5
        })
    )

    # Get the response text
    if response.status_code == 200:
        response_text = response.json().get("choices")[0].get("text")
        st.session_state.messages.append({"role": "assistant", "content": response_text})

        with st.chat_message("assistant"):
            st.markdown(response_text)
    else:
        st.error("Failed to get a response from the model. Please check the server.")

# Add a sidebar with information
st.sidebar.title("About")
st.sidebar.info("This is a local ChatGPT clone using Llama-3.2 model and Streamlit.")
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by Harsh Jain")
