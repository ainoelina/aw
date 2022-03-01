import requests
import smtplib
import datetime

#!/usr/bin/python


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("ainoaw85@gmail.com", "Tosisalainen1!")
    msg = "\nhei vain!\nweb server ei toimi :(\n"
    server.sendmail("you@gmail.com", "ainoaw85@gmail.com", msg)

def get_request():
    r = requests.get('http://51.124.168.159/health.html')
    status = r.status_code
    now = datetime.datetime.now()
    text = now.strftime("%H:%M:%S")
    if status != 200:
        send_mail()
    else:
        with open("log.txt", "a") as file:
            file.write(f"{text} status:\t")
            file.write(str(status))
            file.write('\n')

get_request()