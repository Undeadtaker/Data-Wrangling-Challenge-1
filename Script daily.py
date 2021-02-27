# -- Imports -- #
import requests
import csv
import re
from bs4 import BeautifulSoup as sorter
from datetime import date, timedelta


# -- Request website -- #
URL = 'https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'
page = requests.get(URL)
sorted = sorter(page.content, 'html.parser')

# -- Short word months -- #
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# -- Getting the first date in the given dataset -- #
start = str(sorted.find_all('td', class_ = 'B6')[0].contents[0])
start = start.replace('\xa0', '')
start_li = re.findall(r'\w+', start)

month = start_li[1]
if month in months:
    month = (months.index(month) + 1)

# -- Creating the format for the date module (year, month, date) start -- #
year_start = int(start_li[0])
month_start = month
day_start = int(start_li[2])

# -- Getting the last date in the given dataset -- #
end = str(sorted.find_all('td', class_ = 'B6')[-1].contents[0])
end = end.replace('\xa0', '')
end_li = re.findall(r'\w+', end)

# -- Checking if the month is a valid -- #
month = end_li[1]
if month in months:
    month = (months.index(month) + 1)

# -- Creating the format for the date module (year, month, date) end -- #
year_end = int(end_li[0])
month_end = month
day_end = int(end_li[-1])

# -- Combining everything together -- #
sdate = date(year_start, month_start, day_start)
edate = date(year_end, month_end, day_end)
delta = edate - sdate

# -- Scraping the website for all the prices -- #
li = sorted.find_all('td', class_ = 'B3')
li2 = []

# -- Creating date and excluding the weekends, so from Mon-Fri -- #
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)

    # -- If it's weekend pass -- #
    if day.weekday() == 5 or day.weekday() == 6:
        pass
    else:
        li2.append(day)

# -- In the dataset the dates 2005-09-26 to 2005-09-30 are not present, probably forgotten to be inputted, -- #
# -- so I excluded them, I got the index of them with li2.index(date(2005-09-26)) and removed that week -- #
del li2[2275:2280]

# -- Create file and write rows first Date then its price -- #
with open('daily prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Price'])
    for i in range(len(li)):
        writer.writerow([li2[i], li[i].next])
