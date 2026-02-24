# 📧 AI Email Generator (API Based)

An AI-powered Email Generator built using **FastAPI** and **OpenAI API**.  
This backend application generates structured, professional emails based on user input such as recipient, tone, purpose, and key points.

---

## 🚀 Project Overview

This project:

- Accepts structured email details via API
- Builds a smart AI prompt dynamically
- Sends the prompt to an AI model
- Returns a clean, professional email response

It follows proper email structure:

- Subject  
- Salutation  
- Body  
- Closing  
- Signature  

---

## 🧠 Architecture

```
Client (Swagger / Frontend)
        ↓
FastAPI Backend
        ↓
Prompt Builder
        ↓
OpenAI API
        ↓
Generated Email Response
```

---

## 📂 Project Structure

```
Email Generator (API Based)
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── email_service.py     # AI API integration logic
│   ├── prompt_builder.py    # Prompt engineering logic
│
├── .env                     # Environment variables (API key)
├── requirements.txt         # Project dependencies
├── venv/                    # Virtual environment
```

---

## ⚙️ Tech Stack

- Python 3.12  
- FastAPI  
- Uvicorn  
- OpenAI API  
- Python-dotenv  

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_actual_api_key_here
```

⚠ Important:
- Do NOT push `.env` to GitHub.
- Add `.env` to `.gitignore`.

---

## 📦 Installation Guide

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

If you have `requirements.txt`:

```bash
pip install -r requirements.txt
```

If not:

```bash
pip install fastapi uvicorn openai python-dotenv
```

---

## ▶️ Run the Server

```bash
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📥 API Endpoint

### POST `/generate-email`

### Example Request

```json
{
  "recipient": "Principal",
  "sender_role": "Student",
  "purpose": "Leave Request",
  "tone": "Formal",
  "key_points": "Fever for 3 days, leave from 21 Feb to 23 Feb",
  "length": "Medium"
}
```

---

## 📤 Example Response

```
Subject: Leave Application for Medical Reasons

Respected Principal,

I hope this message finds you well. I am writing to inform you that I have been suffering from a fever for the past three days. Due to my condition, I kindly request leave from 21 February to 23 February.

I will ensure that I complete all missed assignments once I recover. I request your kind consideration and approval.

Thank you for your understanding.

Sincerely,
[Student Name]
```

---

## 🔥 Achievements

- Built AI-powered backend using FastAPI  
- Integrated OpenAI API  
- Implemented structured prompt engineering  
- Handled authentication and environment security  
- Implemented clean project architecture  
- Debugged API errors (401, 404, 429)  
- Created production-ready backend structure  

---

## ⚠️ Current Limitations

- Requires OpenAI API credits  
- No frontend interface yet  
- No database integration yet  

---

## 🚀 Future Improvements

- Add frontend (React / Next.js / Tailwind)  
- Add user authentication  
- Store generated emails in database  
- Add email history feature  
- Deploy to cloud (Render / AWS / Railway)  
- Add tone slider and length control UI  
- Add multi-language support  

---

## 🎯 Resume Value

This project demonstrates:

- Backend API development  
- AI API integration  
- Prompt engineering  
- Secure environment configuration  
- Error handling and debugging  
- Production-ready architecture  

---

## 👨‍💻 Author

**Sagnik Basu**  
AI Backend Development Project  
