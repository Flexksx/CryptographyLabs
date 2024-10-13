import streamlit as st
import pandas as pd


class LanguageMappingExpander:
    def __init__(self, matches_dict: dict) -> None:
        titles = ['letters', 'bigrams', 'trigrams', 'quadgrams']
        for title in titles:
            matches = matches_dict[title]
            expander = st.expander(f'{title.capitalize()} Mapping')
            df = pd.DataFrame(list(matches.items()), columns=[
                "Cipher", "Decrypted"]).T
            expander.table(df)
