import streamlit as st

st.set_page_config(page_title = "Chat with Website", page_icon = "🤖")

st.title("Chat with Website")

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")