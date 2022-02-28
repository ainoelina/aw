

def len_sort(lista):
    lst2 = sorted(lista, key=len)
    return(lst2)

def reader():
    lista = []
    try:
        with open("ex03.txt") as file:
            for line in file:
                line = line.replace('\n', '')
                lista.append(line)
    except:
        print("Virhe tiedoston kasittelyssa")
    lista3 = sorted(lista)
    list2 = len_sort(lista3)
    with open("output.txt", "w") as output:
        for i in list2:
            output.write(i)
            output.write('\n')
    

def main():
    reader()

main()