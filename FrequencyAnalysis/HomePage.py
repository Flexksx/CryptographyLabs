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
default_cypertext = open("./input.txt", "r").read()
st.session_state['cypher_text'] = default_cypertext

nr_of_letters_in_english = get_nr_of_key_in_english('letters')
nr_of_bigrams_in_english = get_nr_of_key_in_english('bigrams')
nr_of_trigrams_in_english = get_nr_of_key_in_english('trigrams')
nr_of_quadgrams_in_english = get_nr_of_key_in_english('quadgrams')

input_text_form = st.form("Cyphertext to analyse")
cypher_text = input_text_form.text_area(
    'Enter the cypher text here', value=default_cypertext, height=500)
submitted = input_text_form.form_submit_button("Analyse")

if submitted:
    st.session_state['cypher_text'] = cypher_text

text_to_decode = st.session_state['cypher_text']

first_letters_frequencies = lf.get_first_letters_frequencies(text_to_decode)
letter_frequencies = lf.get_word_parts_frequencies(
    text=text_to_decode, nr_of_letters=1, max_parts=nr_of_letters_in_english)
bigrams_frequencies = lf.get_word_parts_frequencies(
    text=text_to_decode, nr_of_letters=2, max_parts=nr_of_bigrams_in_english)
trigrams_frequencies = lf.get_word_parts_frequencies(
    text=text_to_decode, nr_of_letters=3, max_parts=nr_of_trigrams_in_english)
quadgrams_frequencies = lf.get_word_parts_frequencies(
    text=text_to_decode, nr_of_letters=4, max_parts=nr_of_quadgrams_in_english)

show_plot_expander_toggle = st.toggle("Show plot", False)
if show_plot_expander_toggle:
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

letters_match_table = get_match_table(letters_match)
bigrams_match_table = get_match_table(bigrams_match)
trigrams_match_table = get_match_table(trigrams_match)
quadgrams_match_table = get_match_table(quadgrams_match)

match_tables = [letters_match_table, bigrams_match_table,
                trigrams_match_table, quadgrams_match_table]
match_tables_titles = ["Letters", "Bigrams", "Trigrams", "Quadgrams"]


matches_columns = st.columns(len(match_tables))
for i in range(len(match_tables)):
    index = len(match_tables)-1-i
    show_frequency_match_table(
        matches_columns[i],
        title=match_tables_titles[index],
        data=match_tables[index])


letter_replacements = show_letter_cypher_selector(
    st,
    title="Select replacements for the foreign letters",
    data=letters_match_table)

if len(letter_replacements) == 0:
    st.write(cypher_text)
else:
    print(letter_replacements)
    translated_text = lf.translate(cypher_text, letter_replacements)
    st.markdown(translated_text, unsafe_allow_html=True)
