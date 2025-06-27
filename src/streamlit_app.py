import os
import streamlit as st
import requests

# === Streamlit UI Setup ===
st.set_page_config(page_title="Generative AI Q&A", page_icon="🤖")

st.markdown("""
## Generative AI Q&A
- 🔍 RAG System with LangChain
- ✨ Ask questions about AI, transformers, LLMs, DeepSeek and more
""")

# Input Form
st.markdown("#### Question")
question = st.text_area("Enter your question here...", key="question_input")

st.markdown("#### Answer")
answer_placeholder = st.empty()

# Endpoint of your FastAPI server (local or ngrok)
# Replace with ngrok URL if running from Colab
FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000/generative_ai")

# Ask Button
if st.button("Ask Question 🔍", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Thinking..."):
                payload = {"question": question}
                response = requests.post(FASTAPI_URL, json=payload)
                if response.status_code == 200:
                    answer = response.json()["answer"]
                    answer_placeholder.text_area(
                        "The answer will appear here...", value=answer, height=150)
                else:
                    st.error(
                        f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Could not reach the API: {e}")
