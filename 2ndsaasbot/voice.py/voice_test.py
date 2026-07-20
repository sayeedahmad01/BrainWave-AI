import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak now...")
    
    r.adjust_for_ambient_noise(source, duration=1)

    audio = r.listen(
        source,
        timeout=5,
        phrase_time_limit=5
    )

print("⏳ Processing...")

try:
    text = r.recognize_google(audio)
    print("✅ You said:", text)

except Exception as e:
    print("❌ Error:", e) 