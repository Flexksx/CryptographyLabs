import pandas as pd
import streamlit as st


class LanguageDataFrameExpander:
    def __init__(self, container, language_frequency_analysis) -> None:
        container.write(language_frequency_analysis)
        first_letters = language_frequency_analysis['first_letters']
        monograms = language_frequency_analysis['letters']
        bigrams = language_frequency_analysis['bigrams']
        trigrams = language_frequency_analysis['trigrams']
        quadgrams = language_frequency_analysis['quadgrams']
        df = pd.DataFrame({
            "First Letters": first_letters,
            "Monograms": monograms,
            "Bigrams": bigrams,
            "Trigrams": trigrams,
            "Quadgrams": quadgrams
        })
        container.write(df)
