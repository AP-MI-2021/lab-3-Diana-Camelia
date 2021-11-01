"""
 O interfață cu utilizatorul care are un meniu de genul:
 Citire date.
 Determinare cea mai lungă subsecvență cu proprietatea 2.
 Determinare cea mai lungă subsecvență cu proprietatea 12.
 Ieșire.

2. Toate numerele sunt prime.
    Funcția de calcul: get_longest_all_primes(lst: list[int]) -> list[int]
12. Toate numerele același număr de divizori.
    Funcția de calcul: get_longest_same_div_count(lst: list[int]) -> list[int]
7. Toate numerele sunt neprime.
    Funcția de calcul: get_longest_all_not_prime(lst: list[int]) -> list[int]
"""

def printMenu():
    print("1. Citire lista. ")
    print("2. Determinarea celei mai lungi subsecvențe cu proprietatea ca toate numerele sunt prime. ")
    print("3. Determinarea celei mai lungi subsecvențe cu proprietatea ca toate numerele au acelasi numar de divizori. ")
    print("4. Determinarea celei mai lungi subsecvențe cu proprietatea ca toate numerele sunt neprime.")
    print("x. Iesire. ")

def citireLista():
    l = []
    n = int(input("Dati numar de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "] = ")))
    return l

"""
2. Toate numerele sunt prime.
    Funcția de calcul: get_longest_all_primes(lst: list[int]) -> list[int]
"""

def isPrime(x):
    '''
    Determina daca un numar este prim
    :param x: un numar intreg
    :return: True, daca x este prim si False, in caz contrar
    '''
    ok = True
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0 and ok == True:
            ok = False
    if ok:
        return True
    else:
        return False

def testIsPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True

def get_longest_all_primes(l):
    '''
    Determina cea mai lunga secventa de numere prime din lista
    :param l: lista de numere intregi
    :return: o subsecventa continand elementele din l
    '''
    n = len(l)
    i = 0
    k = 0
    nr_prime = 0
    poz_max = 0
    lung_max = 0
    rezultat = []
    while i <= n:
        k = i
        nr_prime = 0
        while isPrime(l[k]) is True and k <= n:
            nr_prime = nr_prime + 1
            k = k + 1
        if nr_prime > lung_max:
            lung_max = nr_prime
            poz_max = i
        i = i + 1
    for j in range(n):
        if j >= poz_max and j <= lung_max:
            rezultat.append(l[j])
    return rezultat

def testGet_longest_all_primes():
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([3, 4, 5, 7, 13, 6]) == [5, 7, 13]
    assert get_longest_all_primes([1, 3, 5, 7, 9]) == [3, 5, 7]
    assert get_longest_all_primes([4, 6, 9, 10]) == []

"""
12. Toate numerele același număr de divizori.
    Funcția de calcul: get_longest_same_div_count(lst: list[int]) -> list[int]
"""

def numar_de_divizori(x):
    '''
    Determina numarul de divizori ai unui numar
    :param x: un numar intreg
    :return: numarul divizorilor numarului
    '''
    nrdivizori = 0
    d = 1
    while d <= x:
        if x % d == 0:
            nrdivizori = nrdivizori + 1
        d = d + 1
    return nrdivizori

def get_longest_same_div_count(l):
    """
    Determina cea mai lunga secventa din lista cu proprietatea ca numerele au acelasi numar de divizori.
    :param l: Lista de numere intregi
    :return: Cea mai lunga secventa din lista cu proprietatea ca numerele au acelasi numar de divizori
    """
    l_divizori = []
    for i in range(len(l)):
        l_divizori.append(numar_de_divizori(l[i]))
    k = 2
    aparitie_divizor = 0
    maxim_divizor = 0
    while k < 10000:
        for j in range(len(l_divizori)):
            if l_divizori[j] == k:
                aparitie_divizor = aparitie_divizor + 1
        if aparitie_divizor > maxim_divizor:
            maxim_divizor = k
        aparitie_divizor = 0
        k = k + 1
    l_numere_cu_acelasi_numar_de_div = []
    for n in range(len(l)):
        if l_divizori[n] == maxim_divizor:
            l_numere_cu_acelasi_numar_de_div.append(l[n])
    return l_numere_cu_acelasi_numar_de_div

def testGet_longest_same_div_count():
    assert get_longest_same_div_count([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7]
    assert get_longest_same_div_count([]) == []
    assert get_longest_same_div_count([1, 2, 3]) == [2, 3]
    assert get_longest_same_div_count([2, 2, 3, 9]) == [2, 2, 3]

"""
7. Toate numerele sunt neprime.
    Funcția de calcul: get_longest_all_not_prime(lst: list[int]) -> list[int]
"""

def get_longest_all_not_prime(l):
    """
    Determina numerele prime din lista
    :param l: lista de numere intregi
    :return: o subsecventa continand elementele din l
    """
    rezultat1 = []
    for x in l:
        if isPrime(x) == False:
            rezultat1.append(x)
    return rezultat1

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([]) == []
    assert get_longest_all_not_prime([3, 4, 5, 6]) == [4, 6]
    assert get_longest_all_not_prime([1, 3, 5, 7, 9]) == [1, 9]
    assert get_longest_all_not_prime([4, 6, 9, 10]) == [4, 6, 9, 10]

def main():
    testIsPrime()
    testGet_longest_all_primes()
    testGet_longest_same_div_count()
    printMenu()
    l = []
    while True:
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            print(get_longest_all_not_prime(l))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati! ")

main()