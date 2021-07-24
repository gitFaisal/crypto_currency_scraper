 <h1 align="center">crypto_currency_scraper</h1>
                            
<p align="center">                           
Scrape Historical Data of any currency from coinmarketcap.com with this python script<br>

This is a script to scrape data of desired crypto currency, and saves 
the file as a csv to the directory script is being executed from. 
</p>
<p align="center">
 Super easy to use, simply run script and enter currency name and then enter a time interval.<br>
Example below.

</p>



Example of how to use: <br>
>>> *run terminal*<br>

- Make sure you in the right directory, in my case my script is on desktop. 

>>> cd desktop<br>
>>> python coinmarketcap.py<br>

- This will prompt you to enter name of currency you want.<br>

>>>Please enter currency name spelled correctly: <br>

- Enter name and hit enter

>>>"""Enter number to select time interval:<br>
                                              [1]: 7-Day Data<br>
                                              [2]: 30-Day Data<br>
                                              [3]: 3-Month Data<br>
                                              [4]: 12-Month Data<br>
                                              [5]: All Time Data -->"""<br>

- Then you will be presented with 5 options of time intervals for data. Type the number to select option and hit enter.


File will be saved as csv with time_interval of data + currency name in title.


