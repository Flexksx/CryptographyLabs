from english_language import english_frequency_analysis
from lf import *
input_text = open("./input.txt", "r").read()

frequencies = analyse_frequencies(input_text)
print(match_analysed_frequencies(frequencies, english_frequency_analysis))
print(translate_text(input_text, english_frequency_analysis, frequencies))
print(input_text)
