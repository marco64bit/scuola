

lista1 = [1,2,6,4,7]
lista2 = [3,5,6,9,12,7]


def numericomuni(lista1, lista2):
    lista3 = []
    for x in lista1:
        if (x in lista2) and (x not in lista3):
            lista3.append(x)
    return lista3

print(numericomuni(lista1, lista2))


