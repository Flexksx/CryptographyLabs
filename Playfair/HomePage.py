import streamlit as st

st.title("Playfair Cipher")
st.write("The Playfair Cipher is a digraph substitution cipher that encrypts pairs of letters (digraphs) instead of single letters.")
input_column, matrix_column = st.columns(2)

with input_column:
    text = st.text_area("Enter text to encrypt or decrypt", "Hello, World!")
    key = st.text_input("Enter key", "KEYWORD")

with matrix_column:
    matrix = st.text_area("Matrix", "ABCDEFGHIKLMNOPQRSTUVWXYZ")
