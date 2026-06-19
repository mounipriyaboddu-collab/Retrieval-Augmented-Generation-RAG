import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="Local Notes RAG Chatbot", page_icon="🤖")
st.title("📚 Local Notes RAG Chatbot")

def load_notes():
    notes_txt = ""
    folder_path = "data"

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                notes_txt += file.read() + "\n\n"

    return notes_txt

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