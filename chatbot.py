import streamlit as st
import pandas as pd
import requests

def chatbot_ui(df):
    st.subheader("🤖 Chat with your Excel Data")

    API_KEY = st.secrets["OPENROUTER_API_KEY"]  # Secure method using .streamlit/secrets.toml

    num_rows = st.slider("How many rows to include for analysis?", min_value=5, max_value=len(df), value=10)
    question = st.text_input("Ask your question about the data:")

    if question:
        with st.spinner("Generating answer..."):
            summary = f"""
Dataset Summary:
- Shape: {df.shape}
- Columns: {', '.join(df.columns)}
- Data types:\n{df.dtypes.to_string()}
- Missing values:\n{df.isnull().sum().to_string()}
- Sample data:\n{df.sample(num_rows).to_string(index=False)}
            """

            prompt = f"""
You are a data analyst. Use the dataset summary below to answer the user's question:

{summary}

User question: {question}
            """

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://your-app-url.streamlit.app",
                "X-Title": "ExcelAssistant"
            }

            payload = {
                "model": "meta-llama/llama-3.3-8b-instruct:free",
                "messages": [
                    {"role": "system", "content": "You are a helpful data analyst."},
                    {"role": "user", "content": prompt}
                ]
            }

            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
            result = response.json()

            if response.status_code == 200:
                st.success("Answer:")
                st.write(result["choices"][0]["message"]["content"])
            else:
                st.error(f"Error {response.status_code}: {result.get('error', {}).get('message', 'Unknown error')}")
