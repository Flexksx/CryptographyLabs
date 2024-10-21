import pandas as pd
import altair as alt


def create_frequency_bar_chart(frequency_data):
    # Convert the frequency data to a DataFrame
    df = pd.DataFrame.from_dict(frequency_data, orient='index')

    # Reset index to make STRING_VALUE a column
    df.reset_index(inplace=True)
    df.columns = ['Label', 'Count', 'Frequency']  # Rename columns

    # Create the bar chart
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Label:O', sort='-y', title='Label'),
        y=alt.Y('Frequency:Q', title='Frequency'),
        # Include Count in the tooltip
        tooltip=['Label:O', 'Count:Q', 'Frequency:Q']
    )

    return chart
