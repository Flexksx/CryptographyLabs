import altair as alt
import streamlit as st
import pandas as pd
from lf import *
from english_language import english_frequency_analysis
from utils import show_expander_for_language, show_mappings_in_expander
default_cypher_text = open("./input.txt", "r").read()
st.set_page_config(page_title='Frequency Analysis', layout='wide')
st.title('Decryption using Frequency Analysis')
show_expander_for_language(english_frequency_analysis, 'English')

input_text_form = st.form("Cyphertext to analyse")
cypher_text = input_text_form.text_area(
    'Enter the cypher text here', value=default_cypher_text, height=500)
submitted = input_text_form.form_submit_button("Analyse")


def display_mapping(mapping, expander):
    df = pd.DataFrame(list(mapping.items()), columns=[
        "Cipher", "Decrypted"])
    expander.write(df)


if submitted:
    foreign_frequency_analysis = analyse_frequencies(cypher_text)
    show_expander_for_language(foreign_frequency_analysis, 'Foreign')
    matches = match_analysed_frequencies(
        foreign_frequency_analysis, english_frequency_analysis)
    show_mappings_in_expander(matches)
    translation = translate_text(
        cypher_text, english_frequency_analysis, foreign_frequency_analysis)
    st.write(translation)
