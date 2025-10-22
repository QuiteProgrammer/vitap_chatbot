import streamlit as st
from responses import get_response

# Streamlit app for VITAP Chatbot
st.title("VITAP Chatbot")
st.write("Ask me anything about VITAP, courses, registration, hostels, venues, classes, faculty, events, or backlog guidance!")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You: ", key="input")

if st.button("Send"):
    if user_input:
        response = get_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.write(f"**{speaker}:** {message}")
    else:
        st.write(f"**{speaker}:** {message}")
