
# Web scraper for all-time historical data from coinmarketcap of choosen currency.
# Saves file as  csv, file name will be printed at end.

from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Empty lists to store values that will be scraped.
datelist = []
highlist = []
lowlist = []
marketCaplist = []

# Raw_input will prompt user to enter currency name in lower-case spelled correctly

currency = raw_input("Please enter currency name in all lower-cases...spelled correctly: ")

url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20130428&end=20190615'.format(currency)
response = get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Using soup.find_all to store all rows into variable rows.
# Which we will loop through and apppend items we want to our lists.
rows = soup.find_all('tr', class_='text-right')

for row in rows:
    datelist.append(row.find_all('td')[0].text)
    highlist.append(row.find_all('td')[2].text)
    lowlist.append(row.find_all('td')[3].text)
    marketCaplist.append(row.find_all('td')[6].text.replace(',',''))

# Create Pandas DataFrame
currency_df = pd.DataFrame({'Date':datelist,
                             'Low':lowlist,
                             'High':highlist,
                             'MarketCap(Millions)':marketCaplist
                             })
# Converting MarketCap to int64, and then dividing it to get value in millions.
# Will be easier to read in our excel/csv file.
currency_df['MarketCap(Millions)'] = currency_df['MarketCap(Millions)'].astype('int64')


def convert_millions(amount):
    converted = amount / 1000000
    return converted
# Running function on marketcap column, and then rounding all the numbers in dataframe by 3.
currency_df['MarketCap(Millions)'] = convert_millions(currency_df['MarketCap(Millions)'])
currency_df = currency_df.round(3)


# Save dataframe as csv file + Print message with filename.

filename = 'AllTimeData_'+ currency + '.csv'

currency_df.to_csv(filename, index=False)

print ("Your file has been saved as %s")%(filename)
