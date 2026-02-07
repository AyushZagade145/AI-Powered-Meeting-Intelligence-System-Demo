import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AI Meeting Intelligence Demo",
    layout="wide"
)

# Read HTML file
html_file = Path("index.html")
html_content = html_file.read_text(encoding="utf-8")

# Display HTML
st.components.v1.html(
    html_content,
    height=1200,
    scrolling=True
)
