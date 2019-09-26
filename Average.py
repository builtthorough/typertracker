#import Python libraries regex, statistics, urllib.request and Beautiful Soup
import re
from statistics import mean
from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup

# Declaring my_url variable as the desired url and then using urllib.request ("Req") to
# download the desired url's web page and store it in the Scrapee variable

my_url = "https://www.carfax.com/Used-Honda-Civic-Type-R_t10063"

# Downloading web page to variable

Scrapee = Req(my_url)

# "" html to variable

Scrapee_html = Scrapee.read()

# Closing web page

Scrapee.close()

#Running Scrapee_html through bs4

Scrapee_soup = soup(Scrapee_html, "html.parser")

#Strip out HTML tags

#Finding all containers with Type R Listings inside

Scrapee_soup_price = Scrapee_soup.findAll("span", {"class":"srp-list-item-price"})

prices = []

for x in range(len(Scrapee_soup_price)):
    m=re.search('([0-9]+\,[0-9]+)',str(Scrapee_soup_price[x].findAll(text=True)))
    if m:
       prices.append(int(m.group(0).replace(',', '')))

def Average(prices):
    return "{:,}" .format(mean(prices))

print(Average(prices))

