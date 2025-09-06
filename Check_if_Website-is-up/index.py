import requests
import smtplib
from email.mime.text import MIMEText   # Used for sending plain text
from email.mime.multipart import MIMEMultipart   # Used for sending attachments
import os  # appart from os module we can als use dotenv
from dotenv import load_dotenv

load_dotenv()


def check_website(url):
    try:
        response =  requests.get(url)
        print(response)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def send_email(sender_email, password, receiver_email, subject, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['to'] = receiver_email
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Start TLS Encryption
        server.login(sender_email, password)  # FIXED
        server.sendmail(sender_email, receiver_email, message.as_string())  # FIXED
        server.quit() # Close the connection 
        print("Email Sent succesfuly")

    except:
        print("Failed to send the email")


url = "https://googliyaann.com"
# print(check_website("https://faxitudegyiuhdjnbis.com"))

if not check_website(url):
    sender_email = os.getenv("SENDER_EMAIL")
    subject = "Website is Down"
    body = "warning your website service PING is WARNING PING WARNING - Packet loss = 20%, RTA = 21.84 ms"
    receiver_email = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("APP_PASSWORD")  # USing App password Google
    send_email(sender_email, password, receiver_email, subject, body)
else:
    print("Website is Up")