const chatBox = document.getElementById("chat");


// =====================
// LOAD CHAT HISTORY
// =====================
window.onload = async function () {
    try {
        const res = await fetch("/history");
        const data = await res.json();

        chatBox.innerHTML = "";

        data.forEach(msg => {
            const div = document.createElement("div");
            div.className = "msg " + msg.sender;
            div.innerText = msg.message;
            chatBox.appendChild(div);
        });

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (err) {
        console.log("History load error:", err);
    }
};


// =====================
// SEND MESSAGE
// =====================
async function sendMessage() {

    const input = document.getElementById("symptoms");
    const text = input.value.trim();

    if (!text) {
        alert("Please enter symptoms");
        return;
    }

    addMessage(text, "user");
    input.value = "";

    try {
        const res = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                symptoms: text,
                age_group: "Adult",
                duration: "1-3 days"
            })
        });

        const data = await res.json();

        if (data.error) {
            addMessage(data.error, "bot");
            return;
        }

        addMessage(data.reply, "bot");

    } catch (err) {
        addMessage("Server error", "bot");
    }
}


// =====================
// ADD MESSAGE TO CHAT
// =====================
function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = "msg " + type;
    div.innerText = text;

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// =====================
// VOICE INPUT (SPEAK BUTTON)
// =====================
function startVoice() {

    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Speech Recognition not supported in this browser");
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.interimResults = false;

    recognition.onresult = function (event) {
        const speech = event.results[0][0].transcript;
        document.getElementById("symptoms").value = speech;
    };

    recognition.onerror = function (event) {
        alert("Voice error: " + event.error);
    };

    recognition.start();
}


// =====================
// ENTER KEY SUPPORT
// =====================
document.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});