import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize Hugging Face model and tokenizer
model_name = "your-huggingface-username/ollama-3.2-model"  # Use your model's Hugging Face path
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

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

    # Generate AI response using Hugging Face model
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        inputs = tokenizer(prompt, return_tensors="pt")

        # Generate response using the Hugging Face model
        with torch.no_grad():
            outputs = model.generate(inputs['input_ids'], max_length=200, num_return_sequences=1)
            full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Add a sidebar with information
st.sidebar.title("About")
st.sidebar.info("This is a local ChatGPT clone using Hugging Face's Ollama 3.2 model and Streamlit.")
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by Harsh Jain")
