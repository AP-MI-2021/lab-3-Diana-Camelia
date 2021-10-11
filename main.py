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
    for i in range(2, x // 2 + 1):
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
        if x % d == 0:
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
    assert get_longest_all_primes([3, 4, 5, 6]) == [3, 5]
    assert get_longest_all_primes([1, 3, 5, 7, 9]) == [3, 5, 7]
    assert get_longest_all_primes([4, 6, 9, 10]) == []

def testGet_longest_same_div_count():
    assert get_longest_same_div_count([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7]
    assert get_longest_same_div_count([]) == []
    assert get_longest_same_div_count([1, 2, 3]) == [2, 3]
    assert get_longest_same_div_count([1, 6, 9, ]) == [6, 9]
    assert get_longest_same_div_count([2, 2, 3, 9]) == [2, 2, 3]

def printMenu():
    print("1. Citire date: ")
    print("2. Determinarea celei mai lungi subsecvențe cu proprietatea ca toate numerele sunt prime: ")
    print("3. Determinarea celei mai lungi subsecvențe cu proprietatea ca toate numerele au acelasi numar de divizori: ")
    print("5. Determinare cea mai lungă subsecvență cu proprietatea 5.")
    print("4. Iesire: ")

def is_palindrome(n):
    '''
    Determina daca un numar este palindrom sau nu
    :param n numar intreg:
    :return True daca n este palindrom sau False daca nu:
    '''
    auxiliar = int(n)
    k = 0
    while auxiliar > 0:
        k = k * 10 + auxiliar % 10
        auxiliar = auxiliar // 10
    if n == k:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(189) is False
    assert is_palindrome(18981) is True
    assert is_palindrome(72) is False

def toateElementelePalindroame(lst):
    """
    Determina daca toate numerele dintr-o secventa a listei lst sunt palindrom
    :param lst - lista de numere:
    :return True sau False:
    """
    for x in lst:
        if is_palindrome(x) is False:
            return False
    return True

def test_is_palindrome():
    assert is_palindrome(189) is False
    assert is_palindrome(18981) is True
    assert is_palindrome(72) is False

def get_longest_all_palindromes(lst: list[int]):
    """
    Determina cea mai lunga subsecventa de numere de tip palindrom
    :param lst - lista de numere:
    :return cea mai lunga subsecventa de numere palindrom din lst:
    """
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toateElementelePalindroame(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([1, 2, 89, 3, 4, 5, 6]) == [3, 4, 5, 6]
    assert get_longest_all_palindromes([2, 3, 4, 1, 5]) == [2, 3, 4, 1, 5]

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
        elif optiune == "5":
            print(get_longest_all_palindromes(l))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Reincercati! ")

    main()