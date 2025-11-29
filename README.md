# QA Agent Frontend

This is the frontend user interface for the Autonomous QA Agent, built with Streamlit.

## Deployment on Streamlit Community Cloud

1.  Create a new **App** on Streamlit Cloud.
2.  Connect this repository.
3.  **Settings**:
    *   **Main file path**: `frontend/app.py`
4.  **Secrets** (Advanced Settings):
    *   Add your Backend URL:
        ```toml
        API_URL = "https://<your-backend-url>.onrender.com/api/v1"
        ```
