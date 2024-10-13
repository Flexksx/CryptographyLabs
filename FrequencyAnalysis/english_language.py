english_letters_frequencies: dict = {
    "A": 8.17,
    "B": 1.49,
    "C": 2.78,
    "D": 4.25,
    "E": 12.70,
    "F": 2.23,
    "G": 2.01,
    "H": 6.09,
    "I": 6.97,
    "J": 0.15,
    "K": 0.77,
    "L": 4.03,
    "M": 2.41,
    "N": 6.75,
    "O": 7.51,
    "P": 1.93,
    "Q": 0.09,
    "R": 5.99,
    "S": 6.33,
    "T": 9.06,
    "U": 2.76,
    "V": 0.98,
    "W": 2.36,
    "X": 0.15,
    "Y": 1.97,
    "Z": 0.07
}


english_digraphs_frequencies: dict = {
    'TH': 3.882543,
    'HE': 3.681391,
    'IN': 2.283899,
    'ER': 2.178042,
    'AN': 2.140460,
    'RE': 1.749394,
    'ND': 1.571977,
    'ON': 1.418244,
    'EN': 1.383239,
    'AT': 1.335523,
    'OU': 1.285484,
    'ED': 1.275779,
    'HA': 1.274742,
    'TO': 1.169655,
    'OR': 1.151094,
    'IT': 1.134891,
    'IS': 1.109877,
    'HI': 1.092302,
    'ES': 1.092301,
    'NG': 1.053385
}


english_trigraphs_frequencies: dict = {
    'THE': 3.508232,
    'AND': 1.593878,
    'ING': 1.147042,
    'HER': 0.822444,
    'HAT': 0.650715,
    'HIS': 0.596748,
    'THA': 0.593593,
    'ERE': 0.560594,
    'FOR': 0.555372,
    'ENT': 0.530771,
    'ION': 0.506454,
    'TER': 0.461099,
    'WAS': 0.460487,
    'YOU': 0.437213,
    'ITH': 0.431250,
    'VER': 0.430732,
    'ALL': 0.422758,
    'WIT': 0.397290,
    'THI': 0.394796,
    'TIO': 0.378058
}


english_quadrigraphs_frequencies: dict = {
    'THAT': 0.761242,
    'THER': 0.604501,
    'WITH': 0.573866,
    'TION': 0.551919,
    'HERE': 0.374549,
    'OULD': 0.369920,
    'IGHT': 0.309440,
    'HAVE': 0.290544,
    'HICH': 0.284292,
    'WHIC': 0.283826,
    'THIS': 0.276333,
    'THIN': 0.270413,
    'THEY': 0.262421,
    'ATIO': 0.262386,
    'EVER': 0.260695,
    'FROM': 0.258580,
    'OUGH': 0.253447,
    'WERE': 0.231089,
    'HING': 0.229944,
    'MENT': 0.223347
}

ENGLISH_FREQUENCY_ANALYSIS = {
    "letters": english_letters_frequencies,
    "bigrams": english_digraphs_frequencies,
    "trigrams": english_trigraphs_frequencies,
    "quadgrams": english_quadrigraphs_frequencies
}
