import streamlit as st
import requests
import speech_recognition as sr
import pyttsx3
from PIL import Image
from pypdf import PdfReader

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Gemini Ultra AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0F172A;
    color: white;
}

h1 {
    text-align:center;
    color:#60A5FA;
}

[data-testid="stSidebar"] {
    background-color:#111827;
}

.chat-box {
    background:#1E293B;
    padding:15px;
    border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Voice Functions ----------------
def speech_to_text():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            st.info("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        return text

    except Exception as e:
        st.error(f"Voice Error: {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🤖 Gemini Ultra AI")

    st.button("➕ New Chat")

    st.markdown("---")

    st.subheader("📄 Upload PDF")
    pdf_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    st.markdown("---")

    st.subheader("🖼️ Upload Image")
    image_file = st.file_uploader(
        "Choose Image",
        type=["png", "jpg", "jpeg"]
    )

    st.markdown("---")

    voice_btn = st.button("🎤 Speak")

# ---------------- Header ----------------
st.title("✨ Gemini Ultra AI Assistant")
st.caption("Voice • PDF • Image • Gemini")

# ---------------- PDF Preview ----------------
if pdf_file:
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.success("PDF Uploaded")
    st.text_area(
        "PDF Content Preview",
        text[:2000],
        height=200
    )

# ---------------- Image Preview ----------------
if image_file:
    img = Image.open(image_file)
    st.image(img, caption="Uploaded Image")

# ---------------- Chat History ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- Voice Input ----------------
voice_prompt = ""

if voice_btn:
    voice_prompt = speech_to_text()

# ---------------- Chat Input ----------------
prompt = st.chat_input("Ask me anything...")

if voice_prompt:
    prompt = voice_prompt

# ---------------- Send to Gemini ----------------
if prompt:

    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.spinner("🤖 Thinking..."):

            response = requests.post(
                "http://localhost:8502/api/chat",
                json={"message": prompt}
            )

            answer = response.json().get(
                "reply",
                "No response received"
            )

        st.session_state.messages.append({
            "role":"assistant",
            "content":answer
        })

        with st.chat_message("assistant"):
            st.markdown(answer)

        # AI Voice Output
        speak(answer)

    except Exception as e:
        st.error(f"Error: {e}") 