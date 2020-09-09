import requests
from bs4 import BeautifulSoup
import smtplib 
import time
import html5lib


URL = input('Enter a URL: ')

print(URL)

headers = {"User-Agent": input('Enter your User-Agent: ')}


def check_price():
    page = requests.get(URL,headers = headers)

    soup = BeautifulSoup(page.content, 'html5lib')

    title = soup.find(id="productTitle").get_text(strip=True)

    price = soup.find(id = "priceblock_ourprice").get_text()
    print(price)

    converted_price = float(price[4:])

    watch_price = float(input('Enter your watch price: '))

    if(converted_price < watch_price):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rayquaza1515@gmail.com','zvnfbiqaijatlmiw')

    subject = 'Price fell down!'
    body = 'Check the amazon link ' + URL

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