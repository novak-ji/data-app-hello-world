import streamlit as st

st.title("Hello World App")

st.write("Hello, world! Toto je tvoje první aplikace ve Streamlit.")

name = st.text_input("Zadej své jméno:")

if st.button("Pozdrav"):
    st.write(f"Ahoj, {name}!")