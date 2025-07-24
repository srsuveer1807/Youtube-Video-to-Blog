import streamlit as st
from crewai import Crew, Process
from agents import create_blog_researcher, create_blog_writer
from tasks import create_tasks
from tools import get_yt_tool
import html  # For escaping unsafe characters

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# UI Config
st.set_page_config(
    page_title="Universal AI Blog Generator",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
local_css("style.css")  # You need this file in the same folder

# Title
st.markdown("""
    <div class="title-container">
        <h1 class="main-title">📝 AI Blog Generator from YouTube</h1>
        <p class="subtitle">Turn YouTube content into professional blog posts</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <h2>⚙️ Configuration</h2>
        </div>
    """, unsafe_allow_html=True)

    with st.form("input_form"):
        topic = st.text_input(
            "Blog Topic:",
            value="Introduction to AI",
            help="Enter the blog topic"
        )

        input_type = st.radio(
            "Choose YouTube Source:",
            ["Channel", "Video Link"],
            index=0
        )
        if input_type == "Channel":
            youtube_input = st.text_input("YouTube Channel Handle:", placeholder="e.g. @krishnai06")
        else:
            youtube_input = st.text_input("YouTube Video URL:", placeholder="e.g. https://youtube.com/watch?v=abc123")
        


        submitted = st.form_submit_button("Generate Blog Post")
        if submitted:
            st.session_state.submitted = True

# State initialization
if 'result' not in st.session_state:
    st.session_state.result = None
if 'running' not in st.session_state:
    st.session_state.running = False

# Crew Execution
def generate_blog(topic, input_type, youtube_input):
    st.session_state.running = True
    st.session_state.result = None

    yt_tool = get_yt_tool(input_type, youtube_input)
    researcher = create_blog_researcher()
    writer = create_blog_writer()
    research_task, write_task = create_tasks(researcher, writer, yt_tool, topic)

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True,
    )

    result = crew.kickoff(inputs={'topic': topic})
    st.session_state.result = result
    st.session_state.running = False
    return result

# Main content area
col1, col2 = st.columns([3, 1])
with col1:
    if st.session_state.get('submitted', False):
        with st.spinner("🔍 Researching and writing blog post..."):
            result = generate_blog(topic, input_type, youtube_input)
            st.session_state.result = result
            st.session_state.submitted = False

with col2:
    if st.session_state.running:
        st.markdown("""
            <div class="status-box">
                <p class="status-text">⏳ Blog generation in progress...</p>
                <p class="status-note">Please wait, this may take a few moments.</p>
            </div>
        """, unsafe_allow_html=True)

# Display blog content
if st.session_state.result:
    st.markdown("""
        <div class="result-header">
            <h2>📝 Generated Blog Post</h2>
        </div>
    """, unsafe_allow_html=True)

    try:
        content = st.session_state.result.output
    except AttributeError:
        content = str(st.session_state.result)

    escaped_content = html.escape(content)

    st.markdown(f"""
        <div class="blog-container" style="
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            color: #333;
            font-family: 'Segoe UI', sans-serif;
            line-height: 1.6;
        ">
            <pre style="white-space: pre-wrap; font-size: 1rem;">{escaped_content}</pre>
        </div>
    """, unsafe_allow_html=True)

    st.download_button(
        label="📥 Download Blog Post",
        data=content,
        file_name=f"{topic.replace(' ', '_')}_blog_post.txt",
        mime="text/plain",
        help="Download the blog post as a .txt file"
    )

# Info section
st.markdown("""
    <div class="info-section">
        <h3>✨ How It Works</h3>
        <div class="steps-container">
            <div class="step">
                <h4>1. Choose Source</h4>
                <p>Select YouTube channel or video URL</p>
            </div>
            <div class="step">
                <h4>2. AI Research</h4>
                <p>We extract and analyze relevant video content</p>
            </div>
            <div class="step">
                <h4>3. Blog Generation</h4>
                <p>An AI writer converts insights into a blog post</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
