import pandas as pd

from request_csv import df

# list of bed
beds = []
# list of species list, same order as list of bed
species_in_bed = []

# populate the lists bed and species_in_bed
for index, row in df.iterrows():  # iterate over all rows of data
    bed = row['Bed']
    species = row['Taxon']

    try:
        # bed is in beds
        bed_location = beds.index(bed)

        in_this_bed = species_in_bed[bed_location]
        if not species in in_this_bed:
            in_this_bed.append(species)
    except ValueError:
        # bed is not in beds
        # add bed to beds
        beds.append(bed)
        # add species as list
        species_in_bed.append([species])

# species count by bed, in same order as beds
species_cnts = []
# genus count by bed, in same order as beds
genus_cnts = []

# get species and genus count from species list
for bed_group in species_in_bed:
    # count species incl. subspecies
    species_cnt = len(bed_group)
    species_cnts.append(species_cnt)

    # count genus (first word before space)
    unique = set()
    for i in range(len(bed_group)):
        genus = bed_group[i].partition(' ')[0]
        unique.add(genus)

    genus_cnt = len(unique)
    genus_cnts.append(genus_cnt)

# convert to pandas dataframe
dict_of_lists = {'Bed': beds,
                 'Species Count': species_cnts,
                 'Genus Count': genus_cnts
                 }
# replace raw data df
df = pd.DataFrame.from_dict(dict_of_lists)
