#! /usr/bin/python

from __future__ import print_function
import requests
from bs4 import BeautifulSoup

print ( "\r Enter Stock Symbol ", end="")
symbol = raw_input("")

if (len(symbol)> 0 ):
    fullpage = requests.get("https://www.google.com/finance?q="+symbol)
    soup = BeautifulSoup(fullpage.text)
    sub = soup.find(id="price-panel")
    #now print the price
    print (sub.div.span.span.text,end="")
    #sub = soup.find(id="id-price-change nwp goog-inline-block")
    print (" " + soup.find(class_="ch bld").span.text )
else:
    print ("Invalid Symbol")
    exit(-1)
