import altair as alt
import streamlit as st
import pandas as pd
from .show_plot_expander import show_plot_expander
from .create_frequency_bar_chart import create_frequency_bar_chart
from .editable_match_table import show_editable_match_table


def display_frequencies(frequency_data, title="Frequencies", container=None):
    """Displays word parts and their frequencies in a Streamlit app."""
    if container is None:
        container = st
    df = pd.DataFrame.from_dict(frequency_data, orient='index')
    container.subheader(title)
    df_sorted = df.sort_values(by='count', ascending=False)
    container.table(df_sorted)
