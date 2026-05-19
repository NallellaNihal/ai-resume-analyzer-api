import json

import matplotlib.pyplot as plt
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write(
    "Upload your resume PDF and paste a job description "
    "to get an ATS-style analysis."
)

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=220,
    placeholder="Paste the job description here..."
)

if st.button("Analyze Resume"):
    if resume_file is None:
        st.error("Please upload a resume PDF.")

    elif not job_description.strip():
        st.error("Please paste a job description.")

    else:
        with st.spinner("Analyzing resume..."):
            files = {
                "resume": (
                    resume_file.name,
                    resume_file.getvalue(),
                    "application/pdf"
                )
            }

            data = {
                "job_description": job_description
            }

            try:
                response = requests.post(
                    API_URL,
                    files=files,
                    data=data
                )

                if response.status_code == 200:
                    result = response.json()

                    st.success("Analysis completed!")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "ATS Score",
                            f"{result['ats_score']}%"
                        )

                    with col2:
                        st.metric(
                            "Text Match",
                            f"{result['match_percentage']}%"
                        )

                    st.progress(int(result["ats_score"]))

                    if result["ats_score"] >= 80:
                        st.success("Strong Resume Match ✅")
                    elif result["ats_score"] >= 60:
                        st.warning("Moderate Resume Match ⚠️")
                    else:
                        st.error("Weak Resume Match ❌")

                    st.divider()

                    col3, col4 = st.columns(2)

                    with col3:
                        st.subheader("Matched Skills")
                        if result["matched_skills"]:
                            st.success(
                                ", ".join(result["matched_skills"])
                            )
                        else:
                            st.info("No matched skills found.")

                    with col4:
                        st.subheader("Missing Skills")
                        if result["missing_skills"]:
                            st.warning(
                                ", ".join(result["missing_skills"])
                            )
                        else:
                            st.success("No missing skills found.")

                    st.subheader("Missing Keywords")
                    if result["missing_keywords"]:
                        st.warning(
                            ", ".join(result["missing_keywords"])
                        )
                    else:
                        st.success("No missing keywords found.")

                    matched = len(result["matched_skills"])
                    missing = len(result["missing_skills"])

                    if matched > 0 or missing > 0:
                        st.subheader("Skill Match Distribution")

                        fig, ax = plt.subplots(figsize=(3, 3))
                        ax.pie(
                            [matched, missing],
                            labels=["Matched", "Missing"],
                            autopct="%1.1f%%"
                        )
                        st.pyplot(fig, use_container_width=False)

                    st.subheader("Recommendation")
                    st.info(result["recommendation"])

                    st.download_button(
                        label="Download Analysis Report",
                        data=json.dumps(result, indent=4),
                        file_name="resume_analysis.json",
                        mime="application/json"
                    )

                    with st.expander("Full JSON Response"):
                        st.json(result)

                else:
                    st.error("API Error")
                    st.json(response.json())

            except requests.exceptions.ConnectionError:
                st.error(
                    "FastAPI server is not running. Start it first using: "
                    "python -m uvicorn app.main:app --reload"
                )
