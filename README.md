#  AI Personal Assistant & Email Summarizer

An AI-powered web application that combines a **Personal AI Assistant** with an **Email Summarizer** in a simple Flask-based interface.

The application uses an LLM through the **Groq API** to answer user questions and generate concise summaries of long emails.

---

## ✨ Features

*  **AI Personal Assistant**

  * Ask questions and get AI-generated responses.
  * Designed to behave as a helpful personal assistant.

*  **Email Summarizer**

  * Paste a long email into the application.
  * Generates a concise **2–3 sentence summary**.
  * Useful for quickly understanding lengthy emails.

* ⚡ **Fast AI Responses**

  * Uses Groq's API for LLM inference.

*  **Web-Based Interface**

  * Built using Flask.
  * Simple and easy-to-use frontend.

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* OpenAI Python SDK
* python-dotenv

### AI / API

* Groq API
* `openai/gpt-oss-20b` model

### Frontend

* HTML
* CSS
* JavaScript

---

##  Project Structure

```text
AI ASSISTANT/
│
├── static/
│   └── CSS / JavaScript / Static Files
│
├── templates/
│   └── index.html
│
├── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

##  How It Works

### Personal Assistant

```text
User Question
      ↓
Flask Backend
      ↓
Groq API
      ↓
LLM
      ↓
AI Response
      ↓
Web Interface
```

### Email Summarizer

```text
Email Text
    ↓
Flask Backend
    ↓
Summarization Prompt
    ↓
Groq LLM
    ↓
Concise Summary
    ↓
Web Interface
```

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jadhavaakash41074-dev/AI-Personal-Assistant-and-Email-Summarizer.git
```

### 2. Navigate to the Project

```bash
cd AI-Personal-Assistant-and-Email-Summarizer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file in the project root:

```env
GROCK_API_KEY=your_groq_api_key
```

> **Important:** Never upload your `.env` file or API key to GitHub.

### 6. Run the Application

```bash
python main.py
```

The application will start locally. Open the URL shown in the terminal in your browser.

---

##  Environment Variables

| Variable        | Description                         |
| --------------- | ----------------------------------- |
| `GROCK_API_KEY` | API key used to access the Groq API |

---

##  API Endpoints

| Endpoint     | Method | Purpose                    |
| ------------ | ------ | -------------------------- |
| `/`          | GET    | Loads the main application |
| `/ask`       | POST   | Processes user questions   |
| `/summarize` | POST   | Summarizes email content   |

---

##  Use Cases

* Quickly understanding lengthy emails
* Getting answers to general questions
* Building an AI-powered productivity assistant
* Learning how to integrate LLM APIs with Flask
* Understanding frontend-to-backend AI workflows

---

##  Future Improvements

* 📩 Direct Gmail integration
* 📬 Automatic email fetching
* 🗂️ Email categorization
* 🔍 Search through emails
* 💬 Conversation history
* 🔐 User authentication
* 📊 AI-powered email priority detection
* 🌍 Support for multiple languages

---

##  Project

If you find this project useful, consider giving it a ⭐ on GitHub.
