#import Python libraries regex, statistics, urllib.request and Beautiful Soup
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

# Find and store all contents in "srp-list-item-price" class in variable Scrapee_soup_price

Scrapee_soup_price = Scrapee_soup.findAll("span", {"class":"srp-list-item-price"})

# Create empty list for use below

prices = []

# Find all prices and text in Scrapee_soup_price variable and store in prices list, remove commas for below calculation

for x in range(len(Scrapee_soup_price)):
    m=re.search('([0-9]+\,[0-9]+)',str(Scrapee_soup_price[x].findAll(text=True)))
    if m:
       prices.append(int(m.group(0).replace(',', '')))

# Calculate average of all prices in prices list, format as float number with comma and print

def Average(prices):
    return "{:,}" .format(mean(prices))

print(Average(prices))

