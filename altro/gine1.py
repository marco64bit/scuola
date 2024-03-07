

def conta_numero_lettere(nome):
    count = 0
    for x in nome:
        count += 1
    return count

def disegnatore_di_triangoli(dimensione, primo_simbolo, secondo_simbolo):
    for y in range(1, dimensione):
        if y == 1:
            print(primo_simbolo)
        elif y == dimensione - 1:
            print(primo_simbolo * dimensione)
        else:
            print(primo_simbolo + secondo_simbolo * (y-2) + primo_simbolo)

print(count)
disegnatore_di_triangoli(5, "+", "*")
disegnatore_di_triangoli(7, "=", "_")
disegnatore_di_triangoli(10, "^", "-")

nome = input("inserisci nome ")

print("il nome inserito ha " + str(len(nome)) + " lettere")
print("il nome inserito ha " + str(conta_numero_lettere(nome)) + " lettere")
