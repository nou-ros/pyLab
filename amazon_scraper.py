import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Wacom-Drawing-Software-Included-CTL4100/dp/B079HL9YSF/ref=sr_1_5?keywords=wacom+intuos&qid=1576122674&sr=8-5'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

def price_check():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:3]) #price[0:5]

    print(title.strip()) #to strip extra spaces...
    print(converted_price)

    if(converted_price<70):
        send_email()

#sending email function
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() #encrypt connections
    server.ehlo()

    server.login('sender_email', 'password') #password from google app password

    subject = 'Price fell down!'
    body = 'check the amazon link ' + URL
    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail('sender', 'receiver', msg)
    print("Email has been sent!")

    server.quit()

while(True):
    price_check()
    time.sleep()
