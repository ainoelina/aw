
import datetime

#!/usr/bin/python

def main():
    now = datetime.datetime.now()
    text = now.strftime("%H:%M:%S")
    text += '\n'
    with open("times.txt", "a") as file:
        file.write(text)

main()