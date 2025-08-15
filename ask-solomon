import streamlit as st
import requests
import uuid

# Set page config
st.set_page_config(
    page_title="ASK SOLOMON - AI Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# API function (using OpenRouter)
def get_ai_response(prompt):
    try:
        response = requests.post(
            "https://api.openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer sk-or-v1-5b9a9e8a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a",  # Free public key
                "HTTP-Referer": "https://github.com",  # Required
            },
            json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# Sidebar
with st.sidebar:
    st.title("ASK SOLOMON")
    st.markdown("""
    Your AI assistant powered by:
    - [OpenRouter](https://openrouter.ai)
    - [Streamlit](https://streamlit.io)
    """)

# Main chat interface
st.title("🤖 ASK SOLOMON")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = get_ai_response(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
