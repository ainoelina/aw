import math
import statistics

def counter():
    lista = []
    ip = input("Syöte: ")
    for number in ip.split(", "):
        if number.isdigit():
            lista.append(int(number))
    minimi = min(lista)
    maximi = max(lista)
    mediaani = statistics.median(lista)
    ka = statistics.mean(lista)
    moodi = statistics.mode(lista)
    print(f"Pienin: {minimi}")
    print(f"Suurin: {maximi}")
    print(f"Keskiarvo: {ka:.2}")
    print(f"Mediaani: {mediaani}")
    print(f"Moodi: {moodi}")
    

def main():
    counter()

main()