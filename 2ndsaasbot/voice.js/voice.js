const recognition = new webkitSpeechRecognition();

recognition.lang = "en-US";
recognition.continuous = false;

document.getElementById("voiceBtn").onclick = () => {
    recognition.start();
};

recognition.onresult = function (event) {
    const text = event.results[0][0].transcript;
    document.getElementById("userInput").value = text;
};