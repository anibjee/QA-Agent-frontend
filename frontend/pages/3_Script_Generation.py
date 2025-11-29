import streamlit as st
import requests

import os

API_URL = os.getenv("API_URL", "http://localhost:8000/api/v1")

st.set_page_config(page_title="Script Generation", page_icon="📜")

st.header("📜 Selenium Script Generation Agent")

st.markdown("Select a generated test case to convert into an executable Selenium script.")

# Retrieve test cases from session state
if "generated_test_cases" not in st.session_state:
    st.info("No test cases found. Please go to the 'Test Generation' page first.")
else:
    test_cases = st.session_state["generated_test_cases"]
    
    # Create a selection box
    options = {f"{tc['test_id']}: {tc['test_scenario']}": tc for tc in test_cases}
    selected_option = st.selectbox("Select Test Case", list(options.keys()))
    
    if selected_option:
        selected_tc = options[selected_option]
        
        st.write("### Selected Test Case Details")
        st.json(selected_tc)
        
        if st.button("Generate Selenium Script"):
            with st.spinner("Reading HTML and Generating Script..."):
                try:
                    response = requests.post(
                        f"{API_URL}/generate/script", 
                        json={"test_case": selected_tc}
                    )
                    
                    if response.status_code == 200:
                        script_code = response.json().get("script_code", "")
                        st.success("Script Generated Successfully!")
                        st.code(script_code, language="python")
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Error connecting to backend: {e}")
