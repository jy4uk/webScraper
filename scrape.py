import requests
import re
from bs4 import BeautifulSoup
import time
import smtplib, ssl

sender = "pythonscriptmail21@gmail.com"
EMAIL_ADDRESS = "jjyang14@gmail.com"
HEADERS = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"}
URL = "https://www.bestbuy.com/site/apple-pencil-2nd-generation/6252354.p?skuId=6252354"
page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')
retail_price = int(129)

def get_product_name():
    title = soup.find('h1').get_text().strip()
    return title

def get_price():
    price = soup.find("div",{"class":"priceView-hero-price"}, {"class":"priceView-customer-price"})
    cont = price.contents[0].get_text().strip()[1:]
    return cont

def send_email():
    import smtplib, ssl

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "jjyang14@gmail.com"
    receiver_email = "jjyang14@gmail.com"
    password = input("Type y3our password and press enter:")
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def is_cheaper():
    price = int(float(get_price()))
    product = str(get_product_name())
    diff = retail_price - price
    if  price < retail_price:
        print(product + " is cheaper than its normal price. It currently costs " + price + "which is " + diff + "cheaper than normal.")
        #send_email()
    else:
        print(product + " is not cheaper than normal. It costs $" + str(price) )
        #send_email()

if __name__ == "__main__":
    is_cheaper()