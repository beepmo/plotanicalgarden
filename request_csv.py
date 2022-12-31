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

# Downloading the csv file from your GitHub

url = 'https://raw.githubusercontent.com/beepmo/gardens/main/dashboard_food.csv?token=GHSAT0AAAAAAB4Y6LCO7PDEY5NL4O76IHFEY5OJJKQ'
# Make sure the url is the raw version of the file on GitHub
download = github_session.get(url).content

# Reading the downloaded content and making it a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe to make sure everything is good
if __name__ == '__main__':
    print(df.head())