from fnmatch import translate
import pandas as pd
import string
from collections import Counter
import streamlit as st
import workers.language_frequencies as lf
from components.components import *
from utils import *
from ENGLISH import ENGLISH_FREQUENCY_ANALYSIS

st.set_page_config(page_title='Frequency Analysis', layout='wide')
st.title('Decryption using Frequency Analysis')

nr_of_letters_in_english = get_nr_of_key_in_english('letters')
nr_of_bigrams_in_english = get_nr_of_key_in_english('bigrams')
nr_of_trigrams_in_english = get_nr_of_key_in_english('trigrams')
nr_of_quadgrams_in_english = get_nr_of_key_in_english('quadgrams')

default_cypertext = open("./input.txt", "r").read()
input_text_form = st.form("Cyphertext to analyse")
cypher_text = input_text_form.text_area(
    'Enter the cypher text here', value=default_cypertext, height=500)
submitted = input_text_form.form_submit_button("Analyse")

first_letters_frequencies = lf.get_first_letters_frequencies(cypher_text)
letter_frequencies = lf.get_word_parts_frequencies(
    text=cypher_text, nr_of_letters=1, max_parts=nr_of_letters_in_english)
bigrams_frequencies = lf.get_word_parts_frequencies(
    text=cypher_text, nr_of_letters=2, max_parts=nr_of_bigrams_in_english)
trigrams_frequencies = lf.get_word_parts_frequencies(
    text=cypher_text, nr_of_letters=3, max_parts=nr_of_trigrams_in_english)
quadgrams_frequencies = lf.get_word_parts_frequencies(
    text=cypher_text, nr_of_letters=4, max_parts=nr_of_quadgrams_in_english)

show_plot_expander(first_letters_frequencies, letter_frequencies,
                   bigrams_frequencies, trigrams_frequencies, quadgrams_frequencies)

letters_match = lf.map_strings_by_frequency(
    ENGLISH_FREQUENCY_ANALYSIS['letters'], letter_frequencies)
bigrams_match = lf.map_strings_by_frequency(
    ENGLISH_FREQUENCY_ANALYSIS['bigrams'], bigrams_frequencies)
trigrams_match = lf.map_strings_by_frequency(
    ENGLISH_FREQUENCY_ANALYSIS['trigrams'], trigrams_frequencies)
quadgrams_match = lf.map_strings_by_frequency(
    ENGLISH_FREQUENCY_ANALYSIS['quadgrams'], quadgrams_frequencies)

combined_matches = {**letters_match, **bigrams_match,
                    **trigrams_match, **quadgrams_match}


translated_text = lf.translate(cypher_text, combined_matches)
st.write("Translated text:")
st.write(translated_text)
