import requests
from bs4 import BeautifulSoup
import smtplib 
import time
import html5lib


URL = 'https://www.amazon.ca/TP-Link-Extender-Intelligent-Indicator-RE450/dp/B010S6SG3S/ref=sr_1_3?crid=10PUIFFU2CFHK&keywords=tp+link+wifi+range+extender&qid=1588454929&sprefix=tp+link%2Caps%2C199&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


def check_price():
    page = requests.get(URL,headers = headers)

    soup = BeautifulSoup(page.content, 'html5lib')

    title = soup.find(id="productTitle").get_text(strip=True)

    price = soup.find(id = "priceblock_ourprice").get_text()
    print(price)

    converted_price = float(price[4:])

    if(converted_price < 50.00):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 50.00): 
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rayquaza1515@gmail.com','zvnfbiqaijatlmiw')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.ca/TP-Link-Extender-Intelligent-Indicator-RE450/dp/B010S6SG3S/ref=sr_1_3?crid=10PUIFFU2CFHK&keywords=tp+link+wifi+range+extender&qid=1588454929&sprefix=tp+link%2Caps%2C199&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'rayquaza1515@gmail.com',
        'ryanlam1515@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 24)