
from datetime import datetime

lista_studenti = ["sasha", "marco", "ismaele", "ginevra"]
lista_presenze = []
lista_assenze = []

for studente in lista_studenti:
    risposta = input(f"{studente} presente?")
    if risposta == "si":
        lista_presenze.append(studente)
    else:
        lista_assenze.append(studente)


now = datetime.now()
with open(f'./assenze_{now.day}_{now.month}_{now.year}.txt', 'a+') as fp:
    print("ASSENZE: ")
    for studente in lista_assenze:
        print(studente)
        fp.write(studente)
        fp.write('\n')