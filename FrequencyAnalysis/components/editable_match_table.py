from cProfile import label
from turtle import pos
import pandas as pd
import streamlit as st


def editable_table_to_dict(editable_table):
    return dict(zip(editable_table['Cypher String'], editable_table['English String']))


def show_editable_match_table(container, title: str = None, data=None):
    if title:
        container.subheader(title)
    match_using_this = container.checkbox(
        label="Match using this table", key={title})
    possible_replacements = data['English String']
    editable_table = container.data_editor(
        data,
        column_config={
            "English String": st.column_config.SelectboxColumn(
                "Replacement String",  # Column title
                options=possible_replacements,  # The possible options for replacement
                default=None,  # The default value
                help="Select the replacement string from the options",
            )
        },
        hide_index=True
    )
    if match_using_this:
        return editable_table_to_dict(editable_table)
    else:
        return {}
