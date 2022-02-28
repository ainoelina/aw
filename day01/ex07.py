import smtplib

def maili():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("ainoaw85@gmail.com", "Tosisalainen1!")
    msg = "\nhei vain!\nemailia sinulle\n"
    server.sendmail("you@gmail.com", "ainoaw85@gmail.com", msg)

maili()