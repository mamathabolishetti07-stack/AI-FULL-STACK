import streamlit as st
import time 

st.set_page_config(page_title="Chat Bot UI Demo")
st.title("Chat Bot UI Demo")

with st.chat_message("user"):
    st.write("Hello from user side!")

with st.chat_message("assistant"):
    st.write("Hello I'm your assistant.Type something...")

user_message=st.chat_input("Type something...")
if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(2.5)
        st.write(f"Hey you wrote:{user_message}, but I'm still in development.I can't reply.")


