import streamlit as st
import requests

st.set_page_config(page_title="Career360 Bot", layout="centered")
st.title("Career360 Bot")

query = st.text_input("Ask a career question:")

if st.button("Submit") and query.strip():
    try:
        r = requests.post("http://127.0.0.1:8000/chat", json={"question": query}, timeout=30)
        data = r.json()
        st.success(data.get("answer", ""))
    except Exception as e:
        st.error(f"Backend error: {e}")
