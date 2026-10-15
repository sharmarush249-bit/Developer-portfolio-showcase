import streamlit as st
import json
import os

# --- Page Configuration & Realistic Web Layout ---
st.set_page_config(
    page_title="Project Showcase Portal",
    page_icon="🌐",
    layout="wide"
)

DB_FILE = "projects_database.json"

# --- Backend Database Controller (JSON File Automation) ---
def initialize_database():
    if not os.path.exists(DB_FILE):
        default_records = [
            {
                "title": "E-Commerce Sentiment Analyzer",
                "developer": "Aarushi Sharma",
                "college": "Arya College",
                "problem": "Unstructured customer reviews make it hard for businesses to improve products.",
                "description": "An AI-driven dashboard that categorizes thousands of reviews into positive, negative, and neutral sentiments automatically.",
                "tools": "Python, Streamlit, Pandas, NLTK",
                "outcome": "Reduced review analysis time by 70% for sample local retail businesses."
            },
            {
                "title": "Smart Attendance Tracker",
                "developer": "Rahul Verma",
                "college": "Arya College",
                "problem": "Manual attendance marking in lectures wastes 10-15 minutes of class time.",
                "description": "A lightweight application that tracks student attendance securely using local system data inputs.",
                "tools": "Python, OpenCV, Tkinter",
                "outcome": "Successfully tested with a small batch of 30 students to automate logging."
            }
        ]
        with open(DB_FILE, "w") as file:
            json.dump(default_records, file, indent=4)
        return default_records
    
    with open(DB_FILE, "r") as file:
        return json.load(file)

def commit_to_database(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Load global application data state
project_records = initialize_database()

# --- Session State Routing Engine ---
if "current_route" not in st.session_state:
    st.session_state.current_route = "Home"

# --- Main Application Header & Branding ---
st.markdown("<h1 style='text-align: center; color: #111111; margin-bottom: 5px;'>PROJECT SHOWCASE PLATFORM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666666;'>Track: Software Development (Python Framework)</p>", unsafe_allow_html=True)

# --- Top Navigation Bar Configuration (Simulating Real Website Header) ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([2, 1, 1, 2])

with nav_col2:
    if st.button("🌐 Explore Directory", use_container_width=True):
        st.session_state.current_route = "Home"

with nav_col3:
    if st.button("➕ Submit Project", use_container_width=True):
        st.session_state.current_route = "AddProject"

st.markdown("<hr style='margin-top: 5px; margin-bottom: 25px;'>", unsafe_allow_html=True)

# ==================== VIEW VIEWPORT: EXPLORE SUB-PAGE ====================
if st.session_state.current_route == "Home":
    st.markdown("### 💻 Project Directory")
    st.markdown("Browse, filter, and discover engineering prototypes developed within the community.")
    
    # Live Search Engine Blocks
    search_col1, search_col2 = st.columns(2)
    with search_col1:
        query_search = st.text_input("🔍 Search Matrix (Title / Keywords)", placeholder="Type to search projects...")
    with search_col2:
        query_filter = st.text_input("🛠️ Filter Stack (e.g., Python, OpenCV)", placeholder="Type technology tags...")
        
    # Search Optimization Filter Queries
    filtered_results = project_records
    if query_search:
        filtered_results = [item for item in filtered_results if query_search.lower() in item["title"].lower() or query_search.lower() in item["description"].lower()]
    if query_filter:
        filtered_results = [item for item in filtered_results if query_filter.lower() in item["tools"].lower()]
        
    st.markdown(f"**Available Inventory:** {len(filtered_results)} verified records found.")
    
    # Dynamic Render Engine for Project Web Cards
    for record in filtered_results:
        st.markdown(
            f"""
            <div style="border: 1px solid #E0E0E0; border-radius: 8px; padding: 24px; margin-bottom: 20px; background-color: #FFFFFF; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <h3 style="margin-top: 0; color: #1A1A1A; font-size: 22px;">{record['title']}</h3>
                <p style="color: #666666; font-size: 14px; margin-top: -10px;">
                    <b>Lead Developer:</b> {record['developer']} &nbsp;|&nbsp; <b>Institution:</b> {record['college']}
                </p>
                <div style="height: 1px; background-color: #EAEAEA; margin: 15px 0;"></div>
                <p style="font-size: 15px; color: #333333;"><b>⚠️ Identified Problem:</b> {record['problem']}</p>
                <p style="font-size: 15px; color: #333333;"><b>📝 Technical Architecture:</b> {record['description']}</p>
                <p style="font-size: 15px; color: #333333;">
                    <b>⚙️ Technologies Leveraged:</b> 
                    <span style="background-color: #F0F0F0; padding: 4px 10px; border-radius: 4px; font-family: Courier, monospace; font-size: 13px;">{record['tools']}</span>
                </p>
                <p style="font-size: 15px; color: #008080; margin-bottom: 0;"><b>🚀 Project Outcome:</b> {record['outcome']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==================== VIEW VIEWPORT: ADD PROJECT SUB-PAGE ====================
elif st.session_state.current_route == "AddProject":
    st.markdown("### ➕ Project Onboarding Console")
    st.markdown("Deploy metadata structure to append new development work onto the distributed registry.")
    
    # Concrete Layout Form Structure
    with st.form("web_submission_form", clear_on_submit=True):
        st.markdown("#### 👤 Primary Author Profile")
        input_author = st.text_input("Full Name Identifier", value="Aarushi Sharma")
        input_college = st.text_input("Academic Institution", value="Arya College")
        
        st.markdown("<br>#### 📦 Project Core Metadata", unsafe_allow_html=True)
        input_title = st.text_input("Project Headline *", placeholder="Enter official system name")
        input_problem = st.text_area("Target Problem Definition *", placeholder="Describe the operational gap addressed")
        input_desc = st.text_area("Functional System Summary *", placeholder="Detail the execution and logic flows")
        input_tools = st.text_input("Technology Matrix *", placeholder="Comma-separated values (e.g., Python, Streamlit, JSON)")
        input_outcome = st.text_area("Quantifiable Project Impact *", placeholder="State verified system outcomes or goals")
        
        form_submit = st.form_submit_button("🚀 Commit Architecture to Production")
        
        if form_submit:
            # Field integrity evaluation check
            if not input_title or not input_problem or not input_desc or not input_tools or not input_outcome:
                st.error("Operation failed: All mandatory metadata blocks (*) must be populated.")
            else:
                structured_payload = {
                    "title": input_title,
                    "developer": input_author,
                    "college": input_college,
                    "problem": input_problem,
                    "description": input_desc,
                    "tools": input_tools,
                    "outcome": input_outcome
                }
                
                # Append payload memory state and execute disk write operation
                project_records.append(structured_payload)
                commit_to_database(project_records)
                
                st.success(f"Transaction Success: '{input_title}' registered globally.")
                st.balloons()

# --- Permanent Platform Footer ---
st.markdown("<br><br><br><br><p style='text-align: center; color: #999999; font-size: 12px;'>Dev Registry Framework v2.1 • Managed Local Session Environment</p>", unsafe_allow_html=True)
