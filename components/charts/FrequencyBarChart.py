import altair as alt
import streamlit as st
import pandas as pd


class FrequencyBarChart:
    def __init__(self, container, df: pd.DataFrame, label_column, frequency_column):
        self.__chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(f'{label_column}:O', sort='-y', title=label_column),
            y=alt.Y(f'{frequency_column}:Q', title=frequency_column),
            tooltip=[f'{label_column}:O', f'{frequency_column}:Q']
        )
        container.altair_chart(self.__chart)
    