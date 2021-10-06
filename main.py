# 2. Toate numerele sunt prime.
# 2. Funcția de calcul: get_longest_all_primes(lst: list[int]) -> list[int]
# 12. Toate numerele același număr de divizori.
# 12. Funcția de calcul: get_longest_same_div_count(lst: list[int]) -> list[int]

# O interfață cu utilizatorul care are un meniu de genul:
# Citire date.
# Determinare cea mai lungă subsecvență cu proprietatea 1.
# Determinare cea mai lungă subsecvență cu proprietatea 2.
# Ieșire.

def cititeLista():
    l = []
    n = int(input("Dati numar de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]")))
    return l

def isPrime(x):
    '''
    Determina daca un numar este prim
    :param x: un numar intreg
    :return: True, daca x este prim si False, in caz contrar
    '''
    if x < 2:
        return False
    for i in range( 2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def get_longest_all_primes(l):
    '''
    Determina numerele prime din lista
    :param l: lista de numere intregi
    :return: o subsecventa continand elementele din l
    '''
    rezultat = []
    for x in l:
        if isPrime(x):
            rezultat.append(x)
    return rezultat

def isDivisor(x):
   '''
   Determina numarul de divizori ai unui numar
   :param x: un numar intreg
   :return: numarul divizorilor numarului
   '''
   nrdivizori = 0
   d = 1
   while d <= x:
       if n % d == 0:
           nrdivizori = d + 1
       d = d + 1
   return nrdivizori

def get_longest_same_div_count(l):
    rezultat_div = []
    for x in l:
        if isDivisor(x):
            rezultat_div.append(x)
    return rezultat_div

def testIsPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True

def testGet_longest_all_primes():
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([3,4,5,6]) == [3,5]
    assert get_longest_all_primes([1,3,5,7,9]) == [3,5,7]
    assert get_longest_all_primes([4,6,9,10]) == []

def testGet_longest_same_div_count():
    assert get_longest_same_div_count()
    assert get_longest_same_div_count()
    assert get_longest_same_div_count()
    assert get_longest_same_div_count()
    assert get_longest_same_div_count()

def printMenu():
    print("1. Citire date: ")
    print("2. Determinarea celei mai lungi subsecvențe cu proprietatea ca toate numerele sunt prime: ")
    print("3. Determinarea celei mai lungi subsecvențe cu proprietatea ca toate numerele au acelasi numar de divizori: ")
    print("4. Iesire: ")

def main():
    testIsPrime()
    testGet_longest_all_primes()
    testGet_longest_same_div_count()
    list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = cititeLista()
        elif optiune == "2":
            print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Reincercati! ")

    main()