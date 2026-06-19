# 📚 Local Notes RAG Chatbot

A beginner-friendly AI chatbot that answers questions using your own local notes.

This project uses:

* **Python**
* **Streamlit**
* **Gemini API**
* **Local text files**
* **VS Code**

---

## 🚀 Project Goal

The goal of this project is to build a simple RAG-based chatbot.

RAG means:

> Retrieval Augmented Generation

In simple words:

* We provide our own local notes
* User asks a question
* AI reads the notes
* AI gives an answer based on the notes

---

## 🧠 What This Project Does

This chatbot can:

* Read local `.txt` notes
* Take user questions
* Send notes + question to Gemini AI
* Generate answers from local notes
* Say `"I don't know from the provided notes"` if answer is not available

---

## 🛠️ Tech Stack

| Tool          | Purpose                   |
| ------------- | ------------------------- |
| Python        | Main programming language |
| Streamlit     | Web app / chatbot UI      |
| Gemini API    | AI answer generation      |
| python-dotenv | Load API key securely     |
| VS Code       | Code editor               |

---

## 📁 Folder Structure

```text
local-notes-rag-chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
└── data/
    └── notes.txt
```

---

## 📌 Step 1: Create Project Folder

```bash
mkdir local-notes-rag-chatbot
cd local-notes-rag-chatbot
```

---

## 📌 Step 2: Open Project in VS Code

```bash
code .
```

---

## 📌 Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## 📌 Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

After activation, terminal will show:

```text
(venv)
```

---

## 📌 Step 5: Create `requirements.txt`

Add this code:

```txt
streamlit
google-genai
python-dotenv
```

---

## 📌 Step 6: Install Requirements

```bash
pip install -r requirements.txt
```

---

## 📌 Step 7: Create `.env` File

Create `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 📌 Step 8: Create `data/notes.txt`

Inside `data/notes.txt`, add sample notes:

```txt
RAG means Retrieval Augmented Generation.
It helps AI answer questions using our own local documents.
A RAG system has documents, chunks, retriever, and LLM.
```

---

## 📌 Step 9: Create `app.py`

```python
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="Local Notes RAG Chatbot", page_icon="📚")

st.title("📚 Local Notes RAG Chatbot")
st.write("Ask questions from your local notes.")

def load_notes():
    notes_text = ""
    folder_path = "data"

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                notes_text += file.read() + "\n\n"

    return notes_text

def ask_gemini(question, context):
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using only the local notes below.

Local Notes:
{context}

User Question:
{question}

If the answer is not available in the notes, say:
"I don't know from the provided notes."
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

notes = load_notes()

question = st.text_input("Ask something from your local notes:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = ask_gemini(question, notes)
        st.subheader("Answer")
        st.write(answer)
```

---

## 📌 Step 10: Run the Project

```bash
streamlit run app.py
```

The app will open in browser.

Usually:

```text
http://localhost:8501
```

---

## 🧪 Test Questions

Try asking:

```text
What is RAG?
```

```text
Why is RAG used?
```

```text
What are the components of RAG?
```

---

## ✅ Expected Output

If the answer is available in notes:

```text
RAG means Retrieval Augmented Generation.
```

If the answer is not available:

```text
I don't know from the provided notes.
```

---

## 🧩 How This Project Works

Simple flow:

```text
User Question
     ↓
Local Notes
     ↓
Gemini API
     ↓
AI Answer
```

---

## 📚 Beginner Explanation

### What is Streamlit?

Streamlit helps us create a web app using Python.

### What is Gemini API?

Gemini API is used to generate AI answers.

### What is `.env`?

`.env` stores secret API keys safely.

### What is `data/notes.txt`?

This file contains our local knowledge.

---

## 🔐 Important Security Note

Never upload your `.env` file to GitHub.

Create `.gitignore` file and add:

```txt
.env
venv/
__pycache__/
```

---

## 🚀 Future Improvements

Next versions can include:

* PDF support
* ChromaDB vector database
* embeddings
* chat history
* multiple file upload
* source references
* better UI
* deployment

---

## 🧑‍💻 Author

**Mohan Veera Manikanta**

AI Engineering Learner | Full Stack Developer | RAG Beginner

---

## 📌 Project Status

✅ Beginner version completed
🔜 Next version: PDF RAG Chatbot with ChromaDB

---

## ⭐ Summary

This is a simple beginner-level RAG chatbot project.

You learned:

* How to build a chatbot UI
* How to use Gemini API
* How to load local notes
* How to ask questions from local data
* How RAG works at a basic level
