import streamlit as st

st.set_page_config(
    page_title="Autonomous QA Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous QA Agent")

st.markdown("""
### Welcome to the Autonomous QA Agent

This tool helps you build a "testing brain" from your project documentation and generate automated Selenium test scripts.

#### How to use:
1.  **Knowledge Base**: Upload your project documents (Specs, UI Guides) and HTML files.
2.  **Test Generation**: Describe a feature to generate comprehensive test cases.
3.  **Script Generation**: Select a test case to generate a ready-to-run Selenium script.

Navigate using the sidebar to get started!
""")

st.sidebar.success("Select a page above.")
