import streamlit as st

if "messages" not in st.session_state:
  st.session_state.messages = []
# redraw every bubble
for m in st.session_state.messages:
  with st.chat_message(m["role"]):
   st.write(m["content"])
if prompt := st.chat_input("Type here…"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
   st.write(prompt)
  reply = f"You said: {prompt}"
  with st.chat_message("assistant"):
   st.write(reply)
  st.session_state.messages.append({"role": "assistant", "content":
 reply})