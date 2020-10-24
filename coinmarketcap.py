
# Web scraper for all-time historical data from coinmarketcap.com of choosen currency.
# Saves file as  csv, file name will be printed at end.
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

def convert_millions(amount):
    converted = amount / 1000000
    return converted

while True:

    # Prompt user to enter currency name in lower-case spelled correctly
    # Prompt user to enter time_interval for data
    currency = input("Please enter currency name in all lower-cases...spelled correctly: ").lower()
    time_interval = input("""Enter number to select time interval:
                                [1]: 7-Day Data
                                [2]: 30-Day Data
                                [3]: 3-Month Data
                                [4]: 12-Month Data
                                [5]: All Time Data -->""")
    if time_interval == '1':
        url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20190619&end=20190625'.format(currency)
    elif time_interval == '2':
        url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20190526&end=20190625'.format(currency)
    elif time_interval == '3':
        url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20190325&end=20190625'.format(currency)
    elif time_interval == '4':
        url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20180625&end=20190625'.format(currency)
    elif time_interval == '5':
        url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start=20130428&end=20190615'.format(currency)
    else:
        print("Option out of range. Please enter a number 1 - 5")
        break

    response = get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # Using soup.find_all to store all rows into variable rows.
    # Which we will loop through and apppend items we want to our lists.
    rows = soup.find_all('tr', class_='cmc-table-row')

    # Empty lists to store values that will be scraped.
    datelist = []
    highlist = []
    lowlist = []
    marketCaplist = []


    for row in rows:
        if row.find_all('td')[6].text != '-':
            datelist.append(row.find_all('td')[0].text)
            highlist.append(row.find_all('td')[2].text)
            lowlist.append(row.find_all('td')[3].text)
            marketCaplist.append(row.find_all('td')[6].text.replace(',',''))

    # Create Pandas DataFrame
    currency_df = pd.DataFrame({
        'Date':datelist,
        'Low':lowlist,
        'High':highlist,
        'MarketCap(Millions)':marketCaplist
    })
    # Converting MarketCap to int64, and then dividing it to get value in millions.
    # Will be easier to read in our excel/csv file.
    currency_df['MarketCap(Millions)'] = currency_df['MarketCap(Millions)'].astype('int64')

    # Running function on marketcap column, and then rounding all the numbers in dataframe by 3.
    currency_df['MarketCap(Millions)'] = convert_millions(currency_df['MarketCap(Millions)'])
    currency_df = currency_df.round(3)


    # Save dataframe as csv file + Print message with filename if status_code is 200.
    # No file saved if response code is not 200.

    if response.status_code == 200:
        if time_interval == '1':
            filename = '7_DayData_'+ currency.upper() + '.csv'
        elif time_interval =='2':
            filename = '30_DayData_'+ currency.upper() + '.csv'
        elif time_interval =='3':
            filename = '3_MonthData_'+ currency.upper() + '.csv'
        elif time_interval == '4':
            filename = '12_MonthData_'+ currency.upper() + '.csv'
        elif time_interval == '5':
            filename = 'AllTimeData_'+ currency.upper() + '.csv'
        currency_df.to_csv(filename, index=False)
        print ("Your file has been saved as {}").format(filename)
        break
    else:
        print("Please try again with a valid currency name.")
