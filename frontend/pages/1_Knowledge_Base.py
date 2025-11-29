import streamlit as st
import requests

import os

API_URL = os.getenv("API_URL", "http://localhost:8000/api/v1")

st.set_page_config(page_title="Knowledge Base", page_icon="📚")

st.header("📚 Knowledge Base Management")

st.markdown("Upload your project documentation and HTML files here to build the testing brain.")

uploaded_files = st.file_uploader(
    "Upload Documents", 
    accept_multiple_files=True,
    type=["md", "txt", "json", "html"]
)

if st.button("Build Knowledge Base"):
    if uploaded_files:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, file in enumerate(uploaded_files):
            status_text.text(f"Processing {file.name}...")
            files = {"file": (file.name, file, file.type)}
            try:
                response = requests.post(f"{API_URL}/ingest/upload", files=files)
                if response.status_code == 200:
                    st.success(f"✅ {file.name}: {response.json()['message']}")
                else:
                    st.error(f"❌ {file.name}: Failed to upload. {response.text}")
            except Exception as e:
                st.error(f"❌ {file.name}: Error connecting to backend. {e}")
            
            progress_bar.progress((i + 1) / len(uploaded_files))
        
        status_text.text("Knowledge Base Build Complete!")
    else:
        st.warning("Please upload at least one file.")

st.divider()

if st.button("⚠️ Reset Knowledge Base"):
    try:
        response = requests.post(f"{API_URL}/ingest/reset")
        if response.status_code == 200:
            st.success("Knowledge Base cleared successfully.")
        else:
            st.error("Failed to reset Knowledge Base.")
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
