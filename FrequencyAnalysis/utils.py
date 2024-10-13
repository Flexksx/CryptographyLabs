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


def bar_chart_freq(df, label_column, frequency_column, container):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(f'{label_column}:O', sort='-y', title=label_column),
        y=alt.Y(f'{frequency_column}:Q', title=frequency_column),
        tooltip=[f'{label_column}:O', f'{frequency_column}:Q']
    )
    container.altair_chart(chart)
    return container


def show_expander_for_language(language_frequencies, language_name):
    expander = st.expander(
        f'Expand here to see the frequency analysis of the {language_name} Language')
    col1, col2 = expander.columns(2)
    analysis_frequencies = get_frequencies_dict(language_frequencies)
    for i, analysis in enumerate(analysis_frequencies):
        if i % 2 == 0:
            bar_chart_freq(analysis['data'],
                           analysis['title'], 'Frequency', col1)
        else:
            bar_chart_freq(analysis['data'],
                           analysis['title'], 'Frequency', col2)
    return expander


def show_mappings_in_expander(matches_dict):
    titles = ['letters', 'bigrams', 'trigrams', 'quadgrams']
    for title in titles:
        matches = matches_dict[title]
        expander = st.expander(f'{title.capitalize()} Mapping')
        df = pd.DataFrame(list(matches.items()), columns=[
            "Cipher", "Decrypted"]).T
        expander.table(df)
    return expander
