import streamlit as st
import requests
import pandas as pd

import os

API_URL = os.getenv("API_URL", "http://localhost:8000/api/v1")

st.set_page_config(page_title="Test Generation", page_icon="🧪")

st.header("🧪 Test Case Generation Agent")

st.markdown("Describe a feature to generate comprehensive test cases grounded in your documentation.")

feature_request = st.text_area("Feature Description", placeholder="e.g., Generate all positive and negative test cases for the discount code feature.")

if st.button("Generate Test Cases"):
    if feature_request:
        with st.spinner("Analyzing Knowledge Base and Generating Test Cases..."):
            try:
                response = requests.post(
                    f"{API_URL}/generate/test-cases", 
                    json={"feature": feature_request}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    test_cases = data.get("test_cases", [])
                    
                    if test_cases:
                        st.success(f"Generated {len(test_cases)} test cases!")
                        
                        # Store in session state for next step
                        st.session_state["generated_test_cases"] = test_cases
                        
                        # Display as table
                        df = pd.DataFrame(test_cases)
                        st.dataframe(df, width="stretch")
                        
                        # Display detailed view
                        for tc in test_cases:
                            with st.expander(f"{tc['test_id']}: {tc['test_scenario']}"):
                                st.write(f"**Feature:** {tc['feature']}")
                                st.write(f"**Expected Result:** {tc['expected_result']}")
                                st.write(f"**Grounded In:** {tc['grounded_in']}")
                    else:
                        st.warning("No test cases generated. Try a different query.")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Error connecting to backend: {e}")
    else:
        st.warning("Please enter a feature description.")
