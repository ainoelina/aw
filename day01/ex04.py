import argparse
import sys

def reader(f1, f2):
    lista = []
    try:
        with open(f1) as file:
            for line in file:
                line = line.replace('\n', '')
                lista.append(line)
    except:
        print("Virhe tiedoston kasittelyssa")
    lista3 = sorted(lista)
    lista2 = sorted(lista3, key=len)
    with open(f2, "w") as output:
        for i in lista2:
            output.write(i)
            output.write('\n')
    

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    reader(input_file, output_file)

main()
