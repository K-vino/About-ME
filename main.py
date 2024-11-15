import streamlit as st
from PIL import Image
import webbrowser
import random
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

# Set up page configuration
st.set_page_config(page_title="Vino K's Portfolio", page_icon="💼", layout="wide")

# Custom CSS for styling and animations
st.markdown("""
    <style>
        /* Background and text styling */
        body {
            background-color: #F5F5F5;
            font-family: Arial, sans-serif;
        }
        .header, .section-header {
            color: #2C3E50;
            font-weight: bold;
            padding: 10px;
            margin-bottom: 5px;
            border-bottom: 2px solid #ddd;
        }
        .header {
            font-size: 2.5em;
            animation: fadeIn 2s ease-in-out;
        }
        .section-header {
            font-size: 1.75em;
            color: #3E92CC;
        }

        /* Button and form styling */
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 10px;
            margin: 5px;
            border: 1px solid #ddd;
        }
        .contact-form button {
            background-color: #3E92CC;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            margin-top: 10px;
            transition: background-color 0.3s;
        }
        .contact-form button:hover {
            background-color: #2C3E50;
            transform: scale(1.05);
            transition: transform 0.2s;
        }

        /* Skill bar animation */
        .skill-bar {
            background-color: #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
            overflow: hidden;
        }
        .skill-bar-fill {
            height: 100%;
            background-color: #3E92CC;
            width: 0%;
            animation: fillBar 2s forwards;
        }

        /* Keyframe animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes fillBar {
            from { width: 0%; }
            to { width: var(--bar-width); }
        }

        /* Expander section animation */
        .st-expander {
            transition: transform 0.3s ease-in-out;
        }
        .st-expander:hover {
            transform: scale(1.02);
        }

        /* Footer Styling */
        .footer {
            background-color: #3E92CC;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 1.2em;
            margin-top: 50px;
        }

        .footer a {
            color: white;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# Display the Logo and Header Section with profile picture
st.markdown("<div class='header'>Welcome to My Portfolio</div>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    profile_photo = Image.open("vino.png")  # Ensure vino.png is in the same directory
    st.image(profile_photo, width=150)

with col2:
    st.title("Vino K")
    st.write("""
    **Data Engineer | Big Data Enthusiast | Content Creator**  
    I'm currently pursuing a B.Tech in Information Technology with a passion for data-driven technologies, 
    content creation, and data analytics.
    """)

# About Me section
st.markdown("<div class='section-header'>About Me</div>", unsafe_allow_html=True)
st.write("""
    I am a dedicated Data Engineer with a solid foundation in data modeling, data pipelines, and database management.
    Pursuing a B.Tech in Information Technology from Knowledge Institute of Technology, Salem, Tamil Nadu, India, 
    I have consistently achieved academic excellence and am eager to bring data-driven solutions to real-world problems.
    With hands-on experience in big data technologies, cloud platforms, and data visualization tools, I strive to create 
    meaningful insights from data.
""")

# Education Section
st.markdown("<div class='section-header'>Education</div>", unsafe_allow_html=True)
st.write("""
- **B.Tech in Information Technology**  
  *Knowledge Institute of Technology (KIoT), Salem, Tamil Nadu*  
  *2022-2026*  
  *Current CGPA: 8.5*

- **12th Standard - Higher Secondary**  
  *ABC School, Salem, Tamil Nadu*  
  *2019-2022*  
  *Marks: 66%*

- **10th Standard**  
  *XYZ School, Salem, Tamil Nadu*  
  *2017-2019*  
  *Marks: 58% (Corona Batch)*  
""")

# Interactive Skill Sliders with CSS-animated bars
st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)
skills = {
    "Data Engineering & Big Data Technologies": "85%",
    "ETL, Data Pipelines, Database Management": "80%",
    "Business Intelligence & Data Visualization": "75%",
    "Cloud Platforms": "65%",
    "Python & Programming Languages": "90%",
    "Machine Learning & AI": "70%",
    "Data Analysis & Visualization": "80%",
}

for skill, proficiency in skills.items():
    st.write(f"**{skill}**")
    st.markdown(f"""
    <div class="skill-bar">
        <div class="skill-bar-fill" style="--bar-width: {proficiency};">{proficiency}</div>
    </div>
    """, unsafe_allow_html=True)

# Projects section with hover animations
st.markdown("<div class='section-header'>Projects</div>", unsafe_allow_html=True)
with st.expander("Data-Driven Demand Forecasting Model"):
    st.write("""
    Developed a demand forecasting model for seasonal products, using historical sales, weather data, and special events
    to optimize inventory. This model improved forecasting accuracy and streamlined inventory management.
    """)
with st.expander("AI Application Deployment"):
    st.write("""
    Built and deployed an AI-powered application on Render, integrating GitHub for version control and Streamlit for 
    front-end interaction. This app demonstrated my skills in model deployment and cloud-hosted applications.
    """)
with st.expander("Big Data Analytics on Azure"):
    st.write("""
    Worked with large datasets using Azure Data Lake and HDInsight for processing and analysis. Utilized PySpark for 
    distributed data processing, significantly improving the speed and scalability of data analytics tasks.
    """)

# Experience Section
st.markdown("<div class='section-header'>Experience</div>", unsafe_allow_html=True)
st.write("""
- **Intern, Data Engineering**  
  *XYZ Tech Solutions* | *June 2023 - August 2023*  
  Worked on building ETL pipelines using Apache Spark and Azure Data Lake, focusing on automating data ingestion 
  and transformation tasks.

- **Intern, Cloud Computing**  
  *Cloud Innovations* | *December 2023 - February 2024*  
  Assisted in the migration of legacy data systems to the cloud using AWS and Azure, improving data accessibility 
  and security.
""")

# Content Creation section with YouTube video
st.markdown("<div class='section-header'>Content Creation</div>", unsafe_allow_html=True)
st.write("""
I am also a content creator and run a **YouTube channel** called **Info Tech VMD** where I publish technology guides 
in Tamil, using animations and visuals to simplify complex topics. Below is a recent video I created on the role of technology in everyday life:
""")
st.video("https://youtu.be/r-yYqj2-nOw?si=aGLJUuDuemIGVwKr")

# Online presence section with LinkedIn and AI app link
st.markdown("<div class='section-header'>Find Me Online</div>", unsafe_allow_html=True)
linkedin_url = "https://www.linkedin.com/in/vino-k-5b2a11262/"
render_url = "https://vmd-ai-app-uyz7.onrender.com/"

col1, col2 = st.columns(2)
if st.button("View LinkedIn Profile", key="linkedin"):
    webbrowser.open(linkedin_url)
if st.button("View AI App on Render", key="render"):
    webbrowser.open(render_url)

# Footer Section with contact details
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.write("""
For any inquiries, collaboration opportunities, or feedback, feel free to reach out via LinkedIn or the contact form below. 
<br><br> 
© 2024 Vino K. All rights reserved.  
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
