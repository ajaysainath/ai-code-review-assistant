import streamlit as st
import requests
import pandas as pd
from reports.generate_report import generate_pdf_report

API_CODE_URL = "http://127.0.0.1:8001/review"
API_FILE_URL = "http://127.0.0.1:8001/review-file"
API_PROJECT_URL = "http://127.0.0.1:8001/review-project"

st.title("AI Code Review Assistant")

# -------- CODE INPUT --------

st.subheader("Paste Python Code")

code = st.text_area("Enter Python code")

if st.button("Analyze Code"):

    if code.strip() == "":
        st.warning("Please enter some code")

    else:
        response = requests.post(
            API_CODE_URL,
            json={"code": code}
        )

        result = response.json()

        st.subheader("Quality Score")
        st.write(result["quality_score"])

        st.subheader("Issues Found")
        st.write(result["issues_found"])

        st.subheader("Suggestions")

        for issue in result["rule_based_suggestions"]:
            st.write(issue["issue"])
            st.write(issue["suggestion"])

        st.subheader("AI Improved Code")
        st.code(result["ai_analysis"]["improved_code"], language="python")

        improved_code = result["ai_analysis"]["improved_code"]

        st.download_button(
            label="Download Improved Code (.py)",
            data=improved_code,
            file_name="improved_code.py",
            mime="text/plain"
        )

# -------- FILE UPLOAD --------

st.subheader("Upload Python File")

uploaded_file = st.file_uploader("Upload .py file", type=["py"])

if uploaded_file is not None:

    files = {"file": uploaded_file.getvalue()}

    response = requests.post(API_FILE_URL, files={"file": uploaded_file})

    result = response.json()

    st.subheader("File Name")
    st.write(result["filename"])

    st.subheader("Quality Score")
    st.write(result["quality_score"])

    st.subheader("Issues Found")
    st.write(result["issues_found"])

    st.subheader("Suggestions")

    for issue in result["rule_based_suggestions"]:
        st.write(issue["issue"])
        st.write(issue["suggestion"])

    st.subheader("AI Improved Code")
    st.code(result["ai_analysis"]["improved_code"], language="python")

st.subheader("Analyze Project Folder")

folder_path = st.text_input("Enter project folder path")

if st.button("Analyze Project"):

    response = requests.post(
        API_PROJECT_URL,
        params={"folder_path": folder_path}
    )

    result = response.json()

    st.write("Files analyzed:", result["files_analyzed"])
    st.write("Average quality score:", result["average_quality_score"])
    st.write("Total issues:", result["total_issues"])

    st.subheader("Project Health Dashboard")

    file_reports = result["file_reports"]

    df = pd.DataFrame(file_reports)

    st.write("Issues per File")
    st.bar_chart(df.set_index("file")["issues_found"])

    st.write("Quality Score per File")
    st.bar_chart(df.set_index("file")["quality_score"])

    # Generate PDF report
    report_file = generate_pdf_report(result)

    with open(report_file, "rb") as f:
        st.download_button(
            label="Download Code Review Report (PDF)",
            data=f,
            file_name="code_review_report.pdf",
            mime="application/pdf"
        )

    st.subheader("File Reports")

    for file in result["file_reports"]:
        st.write(file)