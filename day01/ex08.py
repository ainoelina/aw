import requests
import smtplib

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
    if status != 200:
        send_mail()

get_request()