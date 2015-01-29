#! /usr/bin/python


import requests
from bs4 import BeautifulSoup

print "Enter Stock Symbol"
symbol = raw_input("")


if (len(symbol)> 0 ):
    fullpage = requests.get("https://www.google.com/finance?q="+symbol)
    soup = BeautifulSoup(fullpage.text)
    sub = soup.find(id="price-panel")
    #now print the price
    print sub.div.span.span.text
else:
    print "Invalid Symbol"
    exit(-1)
