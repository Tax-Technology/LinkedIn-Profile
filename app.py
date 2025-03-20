import streamlit as st
import urllib.parse

# Streamlit UI
st.title("LinkedIn Google Search Generator")

# User Inputs
job_titles = st.text_area("Enter Job Titles (comma-separated)", 
                          "Marketing Manager, Digital Marketing Manager, Social Media Manager")
industry_keywords = st.text_area("Enter Industry Keywords (comma-separated)", 
                                 "e-invoice, einvoicing, SAF-T, FAIA, Tax Compliance, VAT Compliance")
location = st.text_input("Enter Location (optional)", "Luxembourg")

# Convert user input into Google search format
job_titles_list = [f'"{title.strip()}"' for title in job_titles.split(",") if title.strip()]
industry_keywords_list = [f'"{keyword.strip()}"' for keyword in industry_keywords.split(",") if keyword.strip()]
location_filter = f'"{location.strip()}"' if location.strip() else ""

# Construct Google Search Query
search_query = f'site:linkedin.com/in ({ " OR ".join(job_titles_list) }) ({ " OR ".join(industry_keywords_list) }) {location_filter}'

# URL Encode for Google
google_search_url = "https://www.google.com/search?q=" + urllib.parse.quote(search_query)

# Display Generated Search Query
st.subheader("Generated Google Search Query")
st.code(search_query, language="bash")

# Search Button
if st.button("Search on Google"):
    st.markdown(f'[Click here to search]({google_search_url})', unsafe_allow_html=True)