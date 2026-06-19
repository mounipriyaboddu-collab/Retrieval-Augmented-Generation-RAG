# ▶️ Run Commands

## 📌 Step 1: Open Terminal

In VS Code:

```text
Terminal → New Terminal
```

Shortcut:

```text
Ctrl + `
```

---

# 📌 Step 2: Go to Project Folder

```bash
cd local-notes-rag-chatbot
```

---

# 📌 Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

# 📌 Step 4: Activate Virtual Environment

## Windows

```bash
venv\Scripts\activate
```

## Mac / Linux

```bash
source venv/bin/activate
```

After activation:

```text
(venv)
```

will appear in terminal.

---

# 📌 Step 5: Install Requirements

```bash
pip install -r requirements.txt
```

---

# 📌 Step 6: Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📌 Step 7: Open Browser

Streamlit automatically opens browser.

If not, open manually:

```text
http://localhost:8501
```

---

# 📌 Step 8: Ask Questions

Example:

```text
What is RAG?
```

---

# 📌 Step 9: Stop the Server

Press:

```text
Ctrl + C
```

inside terminal.

---

# 🔄 Full Beginner Workflow

```bash
mkdir local-notes-rag-chatbot

cd local-notes-rag-chatbot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

# 📦 Install Libraries One-by-One (Optional)

```bash
pip install streamlit

pip install google-genai

pip install python-dotenv
```

---

# 📌 Check Installed Libraries

```bash
pip list
```

---

# 📌 Freeze Installed Requirements

```bash
pip freeze > requirements.txt
```

This saves all installed packages inside `requirements.txt`.

---

# 📌 Deactivate Virtual Environment

```bash
deactivate
```

---

# 🚨 Common Beginner Errors

## Error:

```text
streamlit is not recognized
```

### Solution:

Activate virtual environment first.

---

## Error:

```text
No module named streamlit
```

### Solution:

Install requirements again:

```bash
pip install -r requirements.txt
```

---

## Error:

```text
API key not found
```

### Solution:

Check `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ✅ Successful Output

You should see:

```text
📚 Local Notes RAG Chatbot
```

inside browser.
