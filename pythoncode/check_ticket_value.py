#!/home/abhinav/my_project/venv3/bin/python
import requests
from bs4 import BeautifulSoup
import smtplib
import time

def sendtxt(phonenumbers,count=0):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("kabhinav","This is where your password should go. This is application password from google. Not real password")
    for number in phonenumbers:
        server.sendmail("kabhinav@gmail.com",number+"@txt.att.net","Tickets remaining"+str(count))
    server.quit()

def get_tickets():
    r = requests.get('http://rangamancha.brownpapertickets.com/')
    soup = BeautifulSoup(r.content)
    sub = soup.findAll("td",{"class":"bpt_widget_price_border"})[30]
    return(int(sub.text))


phonenumbers = []
phonenumbers.append("512XXXXX")
count = 100

while count != 0:
    count = get_tickets()
    if count == 0:
        sendtxt(phonenumbers,count)
    else:
        time.sleep(60)

if(int(sub.text) == 0):
    print("Tickets remaining", sub.text)

