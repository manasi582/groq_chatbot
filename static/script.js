// static/script.js
const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("sendBtn");
const toggleTheme = document.getElementById("toggleTheme");

// Helper: format time
function timeNow(){
  const d = new Date();
  return d.toLocaleTimeString([], {hour: "2-digit", minute: "2-digit"});
}

// Add a message element
function addMessage(text, who, opts = {}) {
  const div = document.createElement("div");
  div.className = "message " + (who === "user" ? "user" : "bot");

  const meta = document.createElement("div");
  meta.className = "meta";
  const whoSpan = document.createElement("span");
  whoSpan.className = "who";
  whoSpan.textContent = who === "user" ? "You" : "Bot";
  const ts = document.createElement("span");
  ts.className = "ts";
  ts.textContent = timeNow();

  const copyBtn = document.createElement("button");
  copyBtn.className = "copyBtn";
  copyBtn.innerText = "📋";
  copyBtn.onclick = () => {
    navigator.clipboard.writeText(text).then(()=> {
      copyBtn.innerText = "✅";
      setTimeout(()=> copyBtn.innerText = "📋", 900);
    });
  };

  meta.appendChild(whoSpan);
  meta.appendChild(ts);
  meta.appendChild(copyBtn);

  const content = document.createElement("div");
  content.className = "content";
  content.innerText = text;

  div.appendChild(meta);
  div.appendChild(content);

  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

// Show typing indicator
function showTyping(){
  const el = document.createElement("div");
  el.id = "typing";
  el.className = "message bot typing";
  el.innerHTML = `<div class="typingDots"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>`;
  chat.appendChild(el);
  chat.scrollTop = chat.scrollHeight;
}

// Remove typing
function removeTyping(){
  const t = document.getElementById("typing");
  if(t) t.remove();
}

// Send message to server
async function sendMessage(){
  const text = input.value.trim();
  if(!text) return;
  addMessage(text, "user");
  input.value = "";

  showTyping();

  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({message: text})
    });

    const data = await res.json();
    removeTyping();

    if(res.ok && data.reply){
      addMessage(data.reply, "bot");
    } else {
      addMessage("⚠️ Error: " + (data.error || "Unknown"), "bot");
    }
  } catch (err) {
    removeTyping();
    addMessage("⚠️ Network error", "bot");
    console.error(err);
  }
}

// Send button event
sendBtn.addEventListener("click", sendMessage);

// Enter to send, Shift+Enter for newline
input.addEventListener("keydown", (e) => {
  if(e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
  // Command/Ctrl+Enter to send
  if((e.metaKey || e.ctrlKey) && e.key === "Enter"){
    e.preventDefault();
    sendMessage();
  }
});

// Toggle theme placeholder (keeps dark theme by default)
toggleTheme && toggleTheme.addEventListener("click", () => {
  document.body.classList.toggle("light");
  toggleTheme.innerText = document.body.classList.contains("light") ? "🌞" : "🌙";
});
const themeToggle = document.getElementById("themeToggle");
const body = document.body;

// 1️⃣ Load saved theme
if (localStorage.getItem("theme") === "dark") {
    body.classList.replace("light", "dark");
    themeToggle.textContent = "☀️ Light";
}

// 2️⃣ Toggle theme on button click
themeToggle.addEventListener("click", () => {
    if (body.classList.contains("light")) {
        body.classList.replace("light", "dark");
        themeToggle.textContent = "☀️ Light";
        localStorage.setItem("theme", "dark");
    } else {
        body.classList.replace("dark", "light");
        themeToggle.textContent = "🌙 Dark";
        localStorage.setItem("theme", "light");
    }
});
