# 🤖 SaaS AI Chatbot

A modern AI-powered SaaS chatbot built using **FastAPI**, **HTML/CSS/JavaScript**, and **Google Gemini AI**. The application provides real-time conversational AI capabilities through a user-friendly web interface.

## 🚀 Features

* AI-powered chatbot using Gemini AI
* FastAPI backend
* Interactive frontend UI
* Real-time chat responses
* REST API integration
* Easy deployment
* Clean and responsive design

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* FastAPI
* Uvicorn
* Python

### AI Model

* Google Gemini API

## 📂 Project Structure

```bash
saas-chatbot/
│
├── backend/
│   ├── index.py
│   ├── config.py
│   ├── gemini_service.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── home.png
│   └── chat.png
│
└── README.md
```

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd saas-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file inside the backend folder:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

## ▶️ Run Backend

```bash
uvicorn index:app --reload
```

Backend URL:

```bash
http://127.0.0.1:8000
```

## ▶️ Run Frontend

Open `index.html` in your browser or use Live Server in VS Code.

## 📡 API Endpoint

### Chat Endpoint

```http
POST /api/chat
```

Request:

```json
{
  "message": "Hello AI"
}
```

Response:

```json
{
  "reply": "Hello! How can I help you today?"
}
```

## 📸 Screenshots

### Home Page

Add your screenshot here:

```markdown
![Home](screenshots/home.png)
```

### Chat Interface

```markdown
![Chat](screenshots/chat.png)
```

## 🌟 Future Enhancements

* Voice Assistant
* PDF Upload
* Image Upload
* Chat History
* User Authentication
* Multi-language Support
* Dark/Light Theme
* Database Integration

## 👨‍💻 Author

**Sayeed Ahmad**

* GitHub: https://github.com/your-github-username
* LinkedIn: https://linkedin.com/in/your-linkedin-profile

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you like this project, don't forget to star the repository.

