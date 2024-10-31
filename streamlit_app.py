import streamlit as st
import toml
import os

tabs = st.tabs(["Hello world", "Debug"])

with tabs[0]:
    st.header("Hello World App")
    st.write("Hello, world! Toto je tvoje první aplikace ve Streamlit.")

    name = st.text_input("Zadej své jméno:")

    if st.button("Pozdrav"):
        st.write(f"Ahoj, {name}!")

with tabs[1]:
    st.header("Debug")

    config_file_path = os.path.join(os.path.dirname(__file__), os.path.pardir, '.streamlit', 'config.toml')

    try:
        config = toml.load(config_file_path)

        st.title('Current path')
        st.write(os.path.dirname(__file__))

        st.title('Current working directory')
        st.write(os.getcwd())

        st.title('Obsah config.toml')
        st.write(config)

    except FileNotFoundError:
        st.error(f'Soubor {config_file_path} nebyl nalezen.')
    except toml.TomlDecodeError:
        st.error(f'Soubor {config_file_path} má neplatný formát.')

