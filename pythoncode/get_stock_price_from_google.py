#! /usr/bin/python

from __future__ import print_function
import requests
from bs4 import BeautifulSoup

print ( "\r Enter Stock Symbol ", end="")
symbol = input("")

if (len(symbol)> 0 ):
    fullpage = requests.get("https://www.google.com/finance?q="+symbol)
    soup = BeautifulSoup(fullpage.text,"html.parser")
    sub = soup.find(id="price-panel")
    #now print the price
    if(sub != None):
        if (sub.div is not None):   #This is a stock, so the next sequence should get us there.
            print (sub.div.span.span.text,end="")
            #now print how much the price moved
            print (" " + soup.find(class_="ch bld").span.text )
        else:
            #Check if this is a mutual fund
            print(sub.span)
            print(sub.span.span)
    else:
        print("Symbol does not return data that I can parse for price")
else:
    print ("Invalid Symbol")
    exit(-1)
