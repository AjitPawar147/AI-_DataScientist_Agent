import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title("AI Data Scientist Agent")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Basic Statistics")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    numeric_columns = df.select_dtypes(include=['int64','float64']).columns

    if len(numeric_columns) > 0:
        column = st.selectbox("Select column for chart", numeric_columns)

        fig, ax = plt.subplots()
        df[column].hist(ax=ax)
        st.pyplot(fig)

    if st.button("AI Analyze Dataset"):

        files = {
    "file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
}

        response = requests.post(
            "http://localhost:5678/webhook-test/data-analysis-agent",
            files=files
        )

        st.subheader("AI Insights")
        try:
            result = response.json()
            st.write(result)
        except:
            st.error("Response is not JSON")
        st.write(response.text)