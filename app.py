import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="My Campaign Tool", layout="centered")
st.title("MediaGrowth — SMB Campaign Tool")

# Read API key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use a fast/cheap model
model = genai.GenerativeModel("gemini-1.5-flash")

# --- UI ---
business = st.text_input("Business / Brand name")
goal = st.selectbox("Goal", ["Leads", "Sales", "App installs", "Brand awareness"])
budget = st.text_input("Monthly budget (₹)")
audience = st.text_area("Target audience (who?)")
geo = st.text_input("Location (city/state/country)")
notes = st.text_area("Any extra notes / constraints")

prompt = f"""
You are a performance marketing strategist.
Create a campaign plan for:
- Business: {business}
- Goal: {goal}
- Budget: {budget}
- Audience: {audience}
- Location: {geo}
- Notes: {notes}

Output in structured bullets with:
1) Channel mix (Google/Meta/etc.)
2) Recommended creatives (3 ideas)
3) Targeting suggestions
4) Weekly plan
5) KPIs to track
6) Risks + quick fixes
Keep it concise and practical.
"""

if st.button("Generate plan"):
    if not business or not audience:
        st.warning("Please fill at least Business name and Target audience.")
    else:
        with st.spinner("Generating..."):
            resp = model.generate_content(prompt)
        st.subheader("Campaign plan")
        st.write(resp.text)
