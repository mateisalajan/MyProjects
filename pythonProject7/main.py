def uiLista_noua(l_versiuni, versiunea_curenta, lista_vanzari):
    return listaNoua(l_versiuni, versiunea_curenta, lista_vanzari)

elif optiune == '7':
lista = uiOrdonare(lista)
l_versiuni = uiLista_noua(l_versiuni, versiunea_curenta, lista)
versiunea_curenta = uiLista_noua(l_versiuni, versiunea_curenta, lista)

def listaNoua(l_versiuni, versiunea_curenta, lista_vanzari):
    '''
    adauga o lista cu vanzari la o lista de versiuni
    :param l_versiuni: lista de versiuni anterioare
    :param versiunea_curenta: versiunea curenta
    :param lista_vanzari: lista cu vanzari pe care o adaug la  lista de versiuni
    :return: lista de versiuni si versiunea curenta
    '''
    while versiunea_curenta < len(l_versiuni) - 1:
        l_versiuni.pop()

    l_versiuni.append(lista_vanzari)
    versiunea_curenta = versiunea_curenta + 1
    return l_versiuni, versiunea_curenta

pret_min = getPret(lista[0])
        for vanzare in lista:
            if getGen_carte(vanzare) == gen:
                if pret_min >= getPret(vanzare):
                    pret_min = getPret(vanzare)
        l_preturi_min.append(pret_min)

l_preturi_min = pretMinimGen(lista)
    assert len(l_preturi_min) == 3
    assert l_preturi_min[0] == 10.5
    assert l_preturi_min[1] == 27

def runMenu(lista):

    lista_versiuni = [lista]
    versiunea_curenta = 0

    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista_vanzari = uiAdaugaVanzare(lista)
            lista_versiuni, versiune_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == "2":
            lista_vanzari = uiStergeVanzare(lista)
            lista_versiuni, versiune_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == "3":
            lista_vanzari = uiModificaVanzare(lista)
            lista_versiuni, versiune_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == "4":
            lista_vanzari = uiDiscount(lista)
            lista_versiuni, versiune_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == "5":
            lista_vanzari = uiModificare_gen(lista)
            lista_versiuni, versiune_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == "6":
            lista = uiPretMinimGen(lista)
        elif optiune == '7':
            lista_vanzari = uiOrdonare(lista)
            lista_versiuni, versiune_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == '8':
            lista = uiTitluriDistincte(lista)
        elif optiune == 'u':
            if versiunea_curenta < 1:
                print('Nu se mai poate face undo')
            else:
                lista, versiune_curenta = uiUndo(lista_versiuni, versiunea_curenta)
                if lista == []:
                    print(f'Lista este goala {lista}')
        elif optiune == 'r':
            if versiunea_curenta == len(lista_versiuni) - 1:
                print('Nu se mai poate face redo')
            else:
                lista, versiunea_curenta = uiRedo(lista_versiuni, versiunea_curenta)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")