import streamlit as st

def get_response(user_query):
    return "I don't know!"

#app config
st.set_page_config(page_title = "Chat with Website", page_icon = "🤖")
st.title("Chat with Website")

#sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

#user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    response = get_response(user_query)
    with st.chat_message("Human"):
        st.write(user_query)

    with st.chat_message("AI"):
        st.write(response)
