# -- Imports -- #
import requests
from bs4 import BeautifulSoup as sorter
import csv

# -- Request website -- #
URL = 'https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm'
page = requests.get(URL)
sorted = sorter(page.content, 'html.parser')

# -- List comprehention for getting dates, could be done statically, but will be updated in the future
years_li = [date.next for date in sorted.find_all('td', class_ = 'B4')]
years_li = [str(year).replace('\xa0', '') for year in years_li]

# -- Creating the Dates column -- #
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
final = []
for year in years_li:
    for month in months:
        final.append(month + ' ' + year)

# -- Getting the prices -- #
prices_li = [date.next for date in sorted.find_all('td', class_ = 'B3')]

# -- Writing to csv -- #
with open('montly prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Price'])
    for i in range(len(prices_li)):
        writer.writerow([final[i], prices_li[i]])