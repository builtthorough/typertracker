#!/usr/bin/env python3

#import Python libraries regex, statistics, urllib.request and Beautiful Soup
import locale
import re
from statistics import mean
from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup


# Declare my_url variable

my_url = "https://www.carfax.com/Used-Honda-Civic-Type-R_t10063"

# Load my_url contents into Scrapee variable

Scrapee = Req(my_url)

# Extract html to variable Scrapee_html

Scrapee_html = Scrapee.read()

# Close web page

Scrapee.close()

# Parse html into node tree and strip html tags, store as variable Scrapee_soup

Scrapee_soup = soup(Scrapee_html, "html.parser")


#Find matching class data and store into three variables

Scrapee_soup_model = Scrapee_soup.findAll("span", {"class":"srp-list-item-basic-info-model"})

Scrapee_soup_price = Scrapee_soup.findAll("span", {"class":"srp-list-item-price"})

Scrapee_soup_location = Scrapee_soup.findAll("div", {"class":"srp-list-item-dealership-location"})

#Strip html tags and store text into three variables and print

for x in range(len(Scrapee_soup_model)):
    model_text = Scrapee_soup_model[x].text
    price_text = Scrapee_soup_price[x].text
    location_text = Scrapee_soup_location[x].text
    print(model_text, price_text, location_text)

## Create empty list for use below

prices = []

# Find all prices and text in Scrapee_soup_price variable and store in prices list, remove commas for below calculation

for x in range(len(Scrapee_soup_price)):
    m=re.search('([0-9]+\,[0-9]+)',str(Scrapee_soup_price[x].findAll(text=True)))
    if m:
       prices.append(int(m.group(0).replace(',', '')))

# Calculate and return average price in prices list and format as US currency

locale.setlocale(locale.LC_ALL, '')

def Average(prices):
    return '${:,.2f}' .format(mean(prices))

#Print blank line

print()

#Print average price
print("The Average Price is: " + (Average(prices)))
