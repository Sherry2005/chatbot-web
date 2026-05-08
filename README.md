# Multi-Persona AI Chatbot: Versatile Conversational Interface

[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.3-orange?style=for-the-badge)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, web-based conversational AI interface that leverages the **Groq Llama 3.3 70B** engine to deliver high-speed, personality-driven interactions. This project demonstrates full-stack integration of LLMs with a focus on **dynamic persona switching** and **persistent session state**.

## 🚀 Key Features

*   **Dynamic Personalities:** Instantly switch between three distinct AI personas:
    *   **Sarcastic:** Sharp, witty, and intellectually superior yet helpful.
    *   **Friendly:** Warm, supportive, and approachable.
    *   **Professional:** Formal, concise, and focused on clarity and efficiency.
*   **Sub-Second Responses:** Powered by **Groq's LPUs**, providing near-instantaneous token generation using the `llama-3.3-70b-versatile` model.
*   **Session Persistence:** Automatic chat history management via local JSON storage, ensuring continuity across page refreshes.
*   **Clean REST API:** Well-structured Flask backend with dedicated endpoints for chat, history retrieval, and persona management.
*   **Responsive UI:** A streamlined frontend designed for a seamless mobile and desktop chat experience.

## 🛠️ Tech Stack

*   **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
*   **LLM Engine:** [Groq API](https://groq.com/) (Llama 3.3 70B)
*   **Frontend:** HTML5, CSS3, JavaScript (Fetch API for async updates)
*   **Persistence:** JSON-based state management
*   **Environment:** Python 3.10+

## 🏗️ Architecture & Logic

1.  **Request Handling:** The Flask server manages incoming user messages via a `/chat` POST endpoint.
2.  **Persona Management:** A dedicated `/switch` endpoint updates the system prompt and resets/updates the context window based on the selected personality.
3.  **Context Window:** The application maintains a message history list, ensuring the LLM has full conversational context for multi-turn dialogues.
4.  **Inference:** User inputs and history are sent to the Groq API, which processes the request using the 70B Llama 3.3 model.
5.  **State Persistence:** Every interaction is serialized to `chat_history.json`, allowing the server to resume sessions even after a restart.

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- A [Groq API Key](https://console.groq.com/)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sherry2005/chatbot-web.git
   cd chatbot-web
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   For security, avoid hardcoding API keys. Create a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   Access the chatbot at `http://127.0.0.1:5000`.

## 🛡️ Security Best Practices

*   **API Protection:** This application is designed to use environment variables for credential management.
*   **Input Sanitization:** Uses Flask's built-in protections and structured JSON payloads to prevent injection attacks.
*   **System Prompt Hardening:** Personas are defined via immutable system prompts to ensure consistent behavior.

---
**Developed by [Sherry Mohareb](https://github.com/Sherry2005)**
*Engineering interactive AI experiences that bridge the gap between technology and personality.*
