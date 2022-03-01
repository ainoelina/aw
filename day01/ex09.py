
def prime_numbers(nb):
    res = []
    for i in range(2, nb + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    return res

def SieveOfEratosthenes(nb):
    primes = prime_numbers(nb)
    for element in primes:
        print(f"{element} ", end="")
    print()

def main():
    nb = int(input("Anna luku: "))
    SieveOfEratosthenes(nb)

main()