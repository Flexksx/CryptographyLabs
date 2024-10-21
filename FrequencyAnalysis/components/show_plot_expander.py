from .create_frequency_bar_chart import create_frequency_bar_chart
import streamlit as st


def show_plot_expander(first_letters_frequencies, letter_frequencies, bigrams_frequencies, trigrams_frequencies, quadgrams_frequencies, container=None):
    frequency_data_map = {
        "First Letters": first_letters_frequencies,
        "Letters": letter_frequencies,
        "Bigrams": bigrams_frequencies,
        "Trigrams": trigrams_frequencies,
        "Quadgrams": quadgrams_frequencies
    }
    if container is None:
        container = st
    selected_category = container.selectbox(
        "Select frequency category", list(frequency_data_map.keys()))

    selected_data = frequency_data_map[selected_category]

    chart = create_frequency_bar_chart(selected_data)
    container.altair_chart(chart, use_container_width=True)
