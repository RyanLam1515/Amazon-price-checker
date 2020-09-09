import tkinter as tk
import requests
from bs4 import BeautifulSoup
import smtplib 
import time
import html5lib

HEIGHT = 1000
WIDTH = 800

def check_price(URL,UserAgent,watch_price, To_Gmail, From_Gmail, password):

    headers = {"User-Agent": UserAgent}

    page = requests.get(URL,headers = headers)

    while(True):
        soup = BeautifulSoup(page.content, 'html5lib')
        try:
            title = soup.find(id="productTitle").get_text(strip=True)

            price = soup.find(id = "priceblock_ourprice").get_text()
        except: 
            print("Sorry this product cannot be found")

        print(price)
        watch_price = float(watch_price)

        converted_price = float(price[4:])


        if(converted_price < watch_price):
            send_mail(To_Gmail, From_Gmail, password, URL)
            break

    print(converted_price)
    print(title.strip())

def send_mail(To, From, password, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login(From,password)
    except: 
        print("Sorry this is an invalid email")

    subject = 'Price fell down!'
    body = 'Check the amazon link ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        From,
        To,
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#232F3E')
canvas.pack()

upper_frame = tk.Frame(root, bg='#FF9900', bd=5)
upper_frame.place(relx=0.5, rely=0.05, relwidth=0.80,
                  relheight=0.20, anchor='n')

URL_entry = tk.Entry(upper_frame, font = 40)
URL_entry.place(relx = 0.1, rely = 0.3,relwidth = 0.8, relheight = 0.15)
URL_entry.insert(-1,'Enter an amazon.ca link to a product')

UserAgent_entry = tk.Entry(upper_frame, font = 40)
UserAgent_entry.place(relx = 0.1, rely = 0.6,relwidth = 0.8, relheight = 0.15)
UserAgent_entry.insert(-1,'Enter your User agent. This can be found by googling "my user agent"')

middle_frame = tk.Frame(root, bg='#FF9900', bd=5)
middle_frame.place(relx=0.5, rely=0.35, relwidth=0.80,
                   relheight=0.20, anchor='n')

To_Gmail_entry = tk.Entry(middle_frame, font = 40)
To_Gmail_entry.place(relx = 0.1, rely = 0.25, relwidth = 0.8, relheight = 0.15)
To_Gmail_entry.insert(-1, "Enter the email you want notifications to be sent to")

From_Gmail_entry = tk.Entry(middle_frame, font = 40)
From_Gmail_entry.place(relx = 0.1, rely = 0.50, relwidth = 0.8, relheight = 0.15)
From_Gmail_entry.insert(-1, "Enter the email you will be sending notifications from and its password below")

Password_entry = tk.Entry(middle_frame, font = 40, show='*', textvariable = "enter your password")
Password_entry.place(relx = 0.1, rely = 0.75, relwidth = 0.8, relheight = 0.15)

lower_frame = tk.Frame(root, bg='#FF9900', bd=5)
lower_frame.place(relx=0.5, rely=0.65, relwidth=0.80,
                  relheight=0.20, anchor='n')

WatchPrice_entry = tk.Entry(lower_frame, font = 40)
WatchPrice_entry.place(relx = 0.1, rely = 0.3,relwidth = 0.8, relheight = 0.15)
WatchPrice_entry.insert(-1, "Enter price limit. ")

WatchTime_entry = tk.Entry(lower_frame, font = 40)
WatchTime_entry.place(relx = 0.1, rely = 0.6, relwidth = 0.8, relheight = 0.15)
WatchTime_entry.insert(-1, "Enter how long you want to watch the product")

button = tk.Button(root, text="Watch Product",fg= 'white',
                   font=('Franklin Gothic Demi Cond', 28), bg='#131A22', 
                   command =lambda: check_price(URL_entry.get(),UserAgent_entry.get(), WatchPrice_entry.get(),To_Gmail_entry.get(), From_Gmail_entry.get(), Password_entry.get()))
button. place(relx=0.5, rely=0.87, relheight=0.1, relwidth=0.3, anchor='n')


root.mainloop()
