#!/usr/bin/env python3

#import Python libraries regex, statistics, urllib.request and Beautiful Soup
import locale
import re
from statistics import mean
from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup


# Declaring my_url variable as the desired url and then using urllib.request ("Req") to
# download the desired url's web page and store it in the Scrapee variable

my_url = "https://www.carfax.com/Used-Honda-Civic-Type-R_t10063"

Scrapee = Req(my_url)

# With the Python object referenced as Scrapee, deploy .read() Python object method to download entire web page contents
# and store in Scrapee_html variable

Scrapee_html = Scrapee.read()

# Close the Scrapee file

Scrapee.close()

#Transforming the Python object referenced as Scrapee_html into a Python object parsed by Beautiful Soup
#functions to a new, better-organized Python object referenced as Scrapee_soup

Scrapee_soup = soup(Scrapee_html, "html.parser")


#Create three new Python objects, referenced as below, as subsets of the Python object referenced as Scrapee_soup
#that contain the specific data to be viewed using the Beautiful Soup object method .findAll

Scrapee_soup_model = Scrapee_soup.findAll("span", {"class":"srp-list-item-basic-info-model"})

Scrapee_soup_price = Scrapee_soup.findAll("span", {"class":"srp-list-item-price"})

Scrapee_soup_location = Scrapee_soup.findAll("div", {"class":"srp-list-item-dealership-location"})

#Use Beautiful Soup object method .text on above-refenced objects to strip out desired text and create list of strings
# and store them in three variables

for x in range(len(Scrapee_soup_model)):
    model_text = Scrapee_soup_model[x].text
    price_text = Scrapee_soup_price[x].text
    location_text = Scrapee_soup_location[x].text
    print(model_text, price_text, location_text)

#Use regex to search for each price in Scrapee_soup_price object then strip out the commas and convert them to
# integers and store in Python list object prices

prices = []

for x in range(len(Scrapee_soup_price)):
    m=re.search('([0-9]+\,[0-9]+)',str(Scrapee_soup_price[x].findAll(text=True)))
    if m:
       prices.append(int(m.group(0).replace(',', '')))

# Use locale and statistics Python library functions to return an average price in prices list and format as
# US currency

locale.setlocale(locale.LC_ALL, '')

def Average(prices):
    return '${:,.2f}' .format(mean(prices))

print()

print("The Average Price is: " + (Average(prices)))
