 import streamlit as st
import requests

st.title("Gemini Chatbot")

message = st.text_input("Enter your message")

if st.button("Send"):
    try:
        response = requests.post(
            "http://localhost:8502/api/chat",
            json={"message": message}
        )

        st.write(response.json())

    except Exception as e:
        st.error(f"Error: {e}")