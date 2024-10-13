import pandas as pd
import altair as alt
import streamlit as st


def get_frequencies_dict(language_frequencies):
    analysis_subjects = ['letters', 'bigrams', 'trigrams', 'quadgrams']
    analysis_frequencies = []
    for subject in analysis_subjects:
        title = f'{subject.capitalize()}'
        df = pd.DataFrame(
            language_frequencies[subject].items(), columns=[title, 'Frequency']
        ).sort_values(by='Frequency', ascending=False).reset_index(drop=True)
        analysis_frequencies.append({'title': title, 'data': df})
    return analysis_frequencies


def show_mappings_in_expander(matches_dict):
    titles = ['letters', 'bigrams', 'trigrams', 'quadgrams']
    for title in titles:
        matches = matches_dict[title]
        expander = st.expander(f'{title.capitalize()} Mapping')
        df = pd.DataFrame(list(matches.items()), columns=[
            "Cipher", "Decrypted"]).T
        expander.table(df)
    return expander
