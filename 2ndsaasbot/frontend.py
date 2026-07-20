import streamlit as st
import requests

st.set_page_config(
    page_title="Gemini Ultra AI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🤖 Gemini Ultra")
    st.button("➕ New Chat")

    st.markdown("---")

    st.subheader("💬 Recent Chats")
    st.write("Python Roadmap")
    st.write("Machine Learning")
    st.write("Data Science")

    st.markdown("---")

    st.subheader("🛠 AI Tools")
    st.write("📄 PDF Chat")
    st.write("🖼️ Image Analysis")
    st.write("🎤 Voice Assistant")

# Main Header
st.title("✨ Gemini Ultra AI")
st.caption("Your Intelligent AI Assistant")

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = requests.post(
            "http://localhost:8502/api/chat",
            json={"message": prompt}
        )

        answer = response.json().get(
            "reply",
            "No response received"
        )

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        st.error(str(e)) 