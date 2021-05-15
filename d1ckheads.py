import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen

url = 'ENTER THEH URL '
response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()

while True:

    try:

        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(240)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()

        if newHash == currentHash:
            continue

        else:

            msg = EmailMessage()
            msg.set_content(url)
            msg['From'] = 'emailaddress@gmail.com'
            msg['To'] = 'emailaddress@gmail.com'
            msg['Subject'] = 'Lets Stalk Daitona because Im a loser - New Daily Activity Report'
            fromaddr = 'emailaddress@gmail.com'
            toaddrs = ['emailaddress@gmail.com']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('emailaddress@gmail.com', 'insertpasswordhere')
            server.send_message(msg)
            server.quit()
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(240)
            continue

    except Exception as e:

        msg = EmailMessage()
        msg.set_content(url)
        msg['From'] = 'emailaddress@gmail.com'
        msg['To'] = 'emailaddress@gmail.com'
        msg['Subject'] = 'DAR NETWORK FAILURE'
        fromaddr = 'emailaddress@gmail.com'
        toaddrs = ['emailaddress@gmail.com']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('emailaddress@gmail.com', 'insertpasswordhere')
        server.send_message(msg)
        server.quit()
