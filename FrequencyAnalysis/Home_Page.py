import altair as alt
import streamlit as st
import pandas as pd
from lf import *
from english_language import ENGLISH_FREQUENCY_ANALYSIS
from workers.FrequencyAnalyser import FrequencyAnalyser
from workers.translation.Translator import Translator
from components.expanders.frequency.LanguageExpander import LanguageExpander
from components.expanders.mappings.LanguageMappingExpander import LanguageMappingExpander
from utils import show_mappings_in_expander
default_cypher_text = open("./input.txt", "r").read()

st.set_page_config(page_title='Frequency Analysis', layout='wide')
st.title('Decryption using Frequency Analysis')

LanguageExpander(st, ENGLISH_FREQUENCY_ANALYSIS, 'English')

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
    LanguageExpander(st, foreign_frequency_analysis, 'Foreign')
    matches = match_analysed_frequencies(
        foreign_frequency_analysis, ENGLISH_FREQUENCY_ANALYSIS)
    print(matches)
    LanguageMappingExpander(matches)
    translator = Translator(matches, cypher_text)
    translation = translator.translate()
    st.write(translation)
    # translation = translate_text(
    #     cypher_text, ENGLISH_FREQUENCY_ANALYSIS, foreign_frequency_analysis)
    # st.write(translation)
