import streamlit as st
import requests

# Configure page
st.set_page_config(
    page_title="ASK SOLOMON",
    page_icon="🤖",
    layout="wide"
)

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# API function (using OpenRouter)
def get_ai_response(prompt):
    try:
        response = requests.post(
            "https://api.openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer sk-or-v1-5b9a9e8a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a4f3a",  # Public test key
                "HTTP-Referer": "https://huggingface.co",
            },
            json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# Sidebar
with st.sidebar:
    st.title("Settings")
    model = st.selectbox(
        "AI Model",
        ["mistralai/mistral-7b-instruct", "gryphe/mythomax-l2-13b"]
    )

# Main interface
st.title("🤖 ASK SOLOMON")
st.caption("Powered by OpenRouter API")

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get response
    with st.spinner("Thinking..."):
        response = get_ai_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Refresh to show new messages
    st.rerun()
