#---------import libraries----------------
import streamlit as st

st.sidebar.title("THE MULTIVERSE OF CHATBOTS")
st.title("THE MULTIVERSE OF CHATBOTS")
st.subheader("Hey,  Whats on your mind?...")
personality=st.sidebar.selectbox("Who do you want to talk to?. ",
    ["Normal",
    "Mr. cool dhoni",
    "The torchberer Rajamouli",
    "The masterpeice Hans zimmer",
    "The goat Vijay Thalapathi",]
)
#-----------adding intensity---------
intensity=st.sidebar.slider("Intensity",min_value=1, max_value=10, value=5)

# ------import libraries------
import os
from google import genai
from dotenv import load_dotenv

#-------adding API key ---------
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#---------chat history------------
if "chat_history" not in st.session_state :
    st.session_state.chat_history = []


#---------user message--------------------
user_message =st.chat_input("Say Something........")
if user_message :
    ai_instruction=f"You are acting as {personality} with the intensity of {intensity}. respond to the message sent by the user staying complete in that character: {user_message}"
    with st.spinner("sit tight!, we are working on it..."):
        response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=ai_instruction
            )
        
# ---------save conversation in session state------------
        st.session_state.chat_history.append(("user",user_message))
        st.session_state.chat_history.append(("ai",response.text))

#-----------displaying history---------------------
for role, msg in st.session_state.chat_history:
    if role =="user":
        st.chat_message("user").write(msg)
    elif role=="ai":
        st.chat_message("ai").write(msg)






