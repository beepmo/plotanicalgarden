import pandas as pd

from request_csv import df

print('max rows: ', pd.options.display.max_rows)


# return dataframe color with columns bed, species cnt, genera cnt
def by_bed():
    color = pd.DataFrame(columns=['Bed', 'Species', 'Genera'])
    # df.set_index('bed', inplace=True)

    # helper dict
    dict = {}

    for index, row in df.iterrows():  # iterate over all rows of data

        bed = row['Bed']
        taxon = row['Taxon']

        if not bed in color['Bed'].values:
            color['Bed'].append(bed)
            dict.update({bed: [taxon]})
        if bed in color['Bed'].values:
            taxons_in_bed = dict.get(bed)
            if not taxon in taxons_in_bed:
                taxons_in_bed.append(taxon)
                dict.update({bed: taxons_in_bed})

    for index, row in color.iterrows():  # fill in cnts for each bed

        bed = index
        taxons = dict.get(bed)

        species = len(taxons)

        for i in range(len(taxons)):
            taxons[i] = taxons[i].split()[0]  # split by space; get first part

        unique = set(taxons)
        genera = len(unique)

        result = color.loc(bed)
        print(result)


# return bed/garden
def taxons_in_bed():
    pass


def main():
    by_bed()


if __name__ == '__main__':
    main()
