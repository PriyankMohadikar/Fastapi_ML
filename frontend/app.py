import streamlit as st
from rich import prompt

st.title("My first app")
st.write("If this is working My app got started !!")

# name = st.text_input("Enter your name")

# st.chat_message("My chatbot")
with st.chat_message("user"):
    st.write("Which suppliment is use for muscle gain?")

# with st.chat_message("assistant"):
#     st.write("Creatine is used for Muscle Gain")
#     st.write("Protien is also main")
# st.write("Protien is also main Check THis ")
#

box = st.chat_message("assistant")
box.write("Creatine is used for Muscle Gain")

if prompt:=st.chat_input("ask me"):
    with st.chat_message("P"):
        st.write(prompt)




#
# if "count" not in st.session_state:
#     st.session_state["count"] = 0
# if st.button("+1"):
#     st.session_state["count"] += 1
# st.write("count:", st.session_state["count"])
#
#
# if st.button("Ask"):
#     st.write(f"Hello {name} predicting output for you!")
#
