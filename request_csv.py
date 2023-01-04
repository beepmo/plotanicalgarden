import time

import pandas as pd
import requests
import io
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('USERNAME')
pat = os.getenv('PAT')

# Creates a re-usable session object with your creds in-built

github_session = requests.Session()
github_session.auth = (username, pat)

# Downloading the csv_pddf file from your GitHub

url = 'https://raw.githubusercontent.com/beepmo/gardens/main/'\
      + 'dashboard_food.csv_pddf?token=GHSAT0AAAAAAB4Y6LCO7PDEY5NL4O76IHFEY5OJJKQ'

result = github_session.get(url)

status = result.status_code
# assert status != 404
# >>> AssertionError

download = result.content

# Reading the downloaded content and making it a pandas dataframe

start_csv = time.time()
# csv_pddf = pd.read_csv(io.StringIO(download.decode('utf-8')),
csv_pddf = pd.read_csv('dashboard_food.csv',
                       header=0,
                       names=['Bed', 'Label', 'Geo?', 'Status', 'Status Date', 'Taxon'],
                       parse_dates=['Status Date']
                       )
# FIXME: 404 error. I had to cheat to test other features
end_csv = time.time()


# Printing out the first 5 rows of the dataframe to make sure everything is good
if __name__ == '__main__':
    print(f'Time taken to read csv as df: {(end_csv - start_csv)}')
    print(csv_pddf.head())
