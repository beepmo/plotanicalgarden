import re
import time

from parse_data import df

all = 'All that beep mapped'
_4c = 'Carolinian Forest'
# _1c = 'Contemporary Garden'
_1p = 'Winter Garden'
laa = 'Alpine Australasia'
laf = 'Alpine Africa'
las = 'Alpine Asia'  # include 'LAM'
lsa = 'Alpine South America'
lna = 'Alpine North America'
lcs = 'Alpine Cactus and Succulent'  # include 'LTC'
leu = 'Alpine Europe'

gardens = [all, _4c, laa, laf, las, lsa, lna, lcs, leu]


def build_pattern(array_of_gardens):
    regex = '^'

    if _4c in array_of_gardens:
        regex += '4C\d\d|'
    # if _1c in array_of_gardens:
    #     regex += '1C0\d|'
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


def filter_bed(array_of_gardens):
    if all in array_of_gardens:
        return df

    filter_bed_start = time.time()

    bed_pattern = build_pattern(array_of_gardens)
    filtered = df[df.Bed.str.match(bed_pattern)]

    filter_bed_stop = time.time()

    print(
        f'Time taken to apply filter is {(filter_bed_stop - filter_bed_start)}. \n Gardens selected: {array_of_gardens}')

    return filtered
