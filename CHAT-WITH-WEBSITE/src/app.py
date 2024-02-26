
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_query):
    return "I don't know!"

#app config
st.set_page_config(page_title = "Chat with Website", page_icon = "🤖")
st.title("Chat with Website")

#schemas - building bots of langchain models.
chat_history = [
    AIMessage(content="Hello! I am a chatbot. How can I help you?"),
]

#sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

#user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    response = get_response(user_query)
    chat_history.append(HumanMessage(content=user_query))
    chat_history.append(AIMessage(content=response))

#chat history

with st.sidebar:
    st.write(chat_history)