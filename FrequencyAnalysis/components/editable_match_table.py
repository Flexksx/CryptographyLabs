import pandas as pd
import streamlit as st


# def editable_table_to_dict(editable_table):
#     return dict(zip(editable_table['Cypher String'], editable_table['English String']))

def filter_selected_replacements_with_none(selected_replacements):
    return {k: v for k, v in selected_replacements.items() if v is not None}


def show_frequency_match_table(container, title: str = None, data=None):
    if title:
        container.subheader(title)
    data = pd.DataFrame(data)
    container.data_editor(
        data,
        hide_index=True,
    )


def show_letter_cypher_selector(container, title: str = None, data=None):
    if title:
        container.subheader(title)

    data_df = pd.DataFrame(data)
    # data_df['Selected Replacement'] = None
    possible_replacements = [None] + list(data_df['English String'].unique())
    foreign_letters = data_df['Cypher String'].unique()
    rows = 2
    columns = container.columns(round(len(foreign_letters)/rows))
    selected_replacements = {}
    for foregin_letter in foreign_letters:
        selected_replacements[foregin_letter] = None
    for i, letter in enumerate(foreign_letters):
        column = columns[i // rows]
        letter_to_replace = foreign_letters[i]
        selected_replacement = column.selectbox(
            label=letter_to_replace,
            options=possible_replacements,
            key=f'{letter}_replacement',
            index=0
        )
        selected_replacements[letter_to_replace] = selected_replacement
    selected_replacements = filter_selected_replacements_with_none(
        selected_replacements)
    return selected_replacements
