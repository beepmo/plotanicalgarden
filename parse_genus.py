import pandas as pd

from request_csv import df

# list of bed
beds = []
item_cnts = []


def parse_genus(genus):
    for index, row in df.iterrows():  # iterate over all rows of data
        bed = row['Bed']
        cur_genus = row['Taxon'].partition(' ')[0]

        try:
            # bed is in beds
            bed_location = beds.index(bed)

            if genus == cur_genus:
                item_cnts[bed_location] += 1

        except ValueError:
            # bed is not in beds
            # add bed to beds
            beds.append(bed)

            if genus == cur_genus:
                item_cnts.append(1)
            else:
                item_cnts.append(0)

    dict_of_lists = {'Bed': beds,
                     genus + ' Count': item_cnts
                     }

    genus_df = pd.DataFrame.from_dict(dict_of_lists)