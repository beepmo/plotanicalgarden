import re
from parse_data import df

all = 'All I mapped'
_4c = 'Carolinian Forest'
_1c = 'Contemporary Garden'
_1p = 'Winter Garden'
laa = 'Alpine Australasia'
laf = 'Alpine Africa'
las = 'Alpine Asia'  # include 'LAM'
lsa = 'Alpine South America'
lna = 'Alpine North America'
lcs = 'Alpine Cactus and Succulent'  # include 'LTC'
leu = 'Alpine Europe'


def regex_builder(array_of_gardens):
    regex = '^'

    if _4c in array_of_gardens:
        regex += '4C\d\d|'
    if _1c in array_of_gardens:
        regex += '1C0\d|'
    if _1p in array_of_gardens:
        regex += '1P0\d|'
    if laa in array_of_gardens:
        regex += 'LAA\d|'
    if laf in array_of_gardens:
        regex += 'LAF\d|'
    if las in array_of_gardens:
        regex += 'LAS\d|LAM|'
    if lsa in array_of_gardens:
        regex += 'LSA\d|'
    if lna in array_of_gardens:
        regex += 'LNA\d'
    if lcs in array_of_gardens:
        regex += 'LCS\d|LTC\d|'
    if leu in array_of_gardens:
        regex += 'LEU\d|'

    regex += '$'
    return regex

