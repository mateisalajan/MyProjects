def citireLista():
    l = []
    givenString = input("dati lista de nr. float, despartite prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l

def nrIntregiLista(l):
    '''
    detremina nr. intregi dintr-o lista de float-uri
    :param l: lista de float-uri
    :return: nr. intregi din l
    '''
    rezultat = []
    for x in l:
        if x == int(x):
            rezultat.append(x)
    return rezultat

def testNrIntregiLista():
    assert nrIntregiLista([4.1, 5.9]) == []
    assert nrIntregiLista([2.12, 3.0, 9.9, 11.6, 10.0]) == [3.0, 10.0]

def celMaiMareNrDiv(l, x):
    '''
    determina cel mai mare nr. dintr-o lista divzibil cu un nr. citit
    :param l: lista de float-uri
    :param x: nr. intreg
    :return: cel mai mare nr. din l care este divizibil cu x
    '''
    #max = None
    #for y in l:
        #if y % x == 0 and (max is None or y > max):
            #max = y
    #return max
    reversedList = l[:]
    reversedList.sort(reverse=True)
    for y in reversedList:
        if y % x == 0:
            return y

def testCelMaiMareNrDiv():
    assert celMaiMareNrDiv([2.2, 5.0, 3.4, 8.8], 2) is None
    assert celMaiMareNrDiv([6.0, 5.7, 4.0, 9.2], 3) == 6.0
    assert celMaiMareNrDiv([4.9, 7.0, 2.5, 14.0], 7) == 14.0

def pfPalindrom(l):
    '''
    determina nr. ale caror parte fractionara este un nr. palindrom
    :param l: lista de float-uri
    :return: nr. din l ale caror parte fractionara este un nr. palindrom
    '''
    rezultat = []
    for x in l:
        xStr = str(x)
        pf = xStr.split('.')[1]
        if pf == pf[::-1]:
            rezultat.append(x)
    return rezultat

def testpfPalindrom():
    assert pfPalindrom([1.34, 4.35, 9.19]) == []
    assert pfPalindrom([2.0, 5.66, 7.31, 9.818]) == [2.0, 5.66, 9.818]

def procesareLista(l):
    '''
    Afisare nr. din lista în care float-urile cu partea întreagă a radicalului număr prim sunt
    puse ca string-uri cu caracterele în ordine inversă
    :param l: lista de float-uri
    :return: nr. din lista în care float-urile cu partea întreagă a radicalului număr prim sunt
    puse ca string-uri cu caracterele în ordine inversă
    '''
    rezultat = []
    for x in l:
        radical = x**0.5
        pi = int(radical)
        ok = True
        if pi < 2:
            ok = False
        else:
            for i in range(2, pi//2 +1):
                if pi % i == 0:
                    ok = False
        if ok:
            rezultat.append(str(x)[::-1])
        else:
            rezultat.append(x)
    return rezultat

def testProcesareLista():
    assert procesareLista([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]

def main():
    testNrIntregiLista()
    testCelMaiMareNrDiv()
    testpfPalindrom()
    testProcesareLista()
    l = []
    while True:
        print("1. Citire lista float-uri")
        print("2. afisare nr. intregi lista")
        print("3. afisare cel mai mare numar divizibil cu un nr. citit")
        print("4. afisare nr ale caror p.f este palindrom")
        print("5. Afisare nr. din lista în care float-urile"
              " cu partea întreagă a radicalului număr prim "
              "sunt puse ca string-uri cu caracterele în ordine inversă")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(nrIntregiLista(l))
        elif optiune == "3":
            x = int(input("dati un nr:"))
            print(celMaiMareNrDiv(l, x))
        elif optiune == "4":
            print(pfPalindrom(l))
        elif optiune == "5":
            print(procesareLista(l))
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("optiune gresita! reincercati: ")

main()