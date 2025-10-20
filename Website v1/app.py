import streamlit as st

# Example tool: reverse text
def reverse_text(text):
    return text[::-1]

st.title("My First Public Python Tool 🚀")

user_input = st.text_input("Enter some text:")
if st.button("Run Tool"):
    result = reverse_text(user_input)
    st.success(f"Result: {result}")
