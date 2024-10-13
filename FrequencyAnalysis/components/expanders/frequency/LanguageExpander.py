import streamlit as st
from components.charts.FrequencyBarChart import FrequencyBarChart
from utils import get_frequencies_dict


class LanguageExpander:
    def __init__(self, container, language_frequencies: dict, language_name: str):
        self.__container = container
        self.__language_frequencies = language_frequencies
        self.__language_name = language_name
        expander = st.expander(
            f'Expand here to see the frequency analysis of the {language_name} Language')
        col1, col2 = expander.columns(2)
        analysis_frequencies = get_frequencies_dict(language_frequencies)
        for i, analysis in enumerate(analysis_frequencies):
            if i % 2 == 0:
                FrequencyBarChart(col1, analysis['data'],
                                  analysis['title'], 'Frequency')
            else:
                FrequencyBarChart(col2, analysis['data'],
                                  analysis['title'], 'Frequency')
