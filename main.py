def citire_lista():
    lst = []
    n = int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst

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

while True:
    printMenu()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        l = citire_lista()
    elif optiune == "2":
        l1 = get_longest_all_palindromes(l)
        print(l1[:])
    elif optiune == "x":
        break