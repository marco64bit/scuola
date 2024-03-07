from utils import util
import json

# variabili

print(util.sum(1, 2))

# string
text = "asd oasdij oiasdj oiasdj ioasd"
text * 5
text + "asd"  # non efficente
f"{text} asd"  # efficente
# tutte le funione della stringa divertiti
start = 0
end = 5
text[start: end]  # possono essere negativi
text.split(" ")  # ottengo le parole
email = "lordscapoladestra@gmail.com"
provider = email.split("@")[1].split(".")[0]
nome_email = email.split("@")[0]
dominio = email.split("@")[1].split(".")[1]

# numeri
print(type(text))
num = 1
num_float = 1.5
num * num_float
num ** num_float
num / num_float
round(num_float * 100) / 100
(((1 * 10)**2)/5) + 5

dizionario = {
    "username": "marco",
    "age": 15
}
lista = [1, 2, "ads", [1, 2], dizionario]


def move():
    return "move me"


lista_utenti = [
    {
        "username": "marco",
        "age": 30
    },
    {
        "username": "Alessio",
        "age": 39,
        "attributes": {
            "developer": 7
        },
        "move": move
    }
]

print(
    f"il livello di {lista_utenti[1]['username']} è {lista_utenti[1]['attributes']['developer']}")
print(
    f"le skill di {lista_utenti[1]['username']} sono {list(lista_utenti[1]['attributes'].keys())}")
print(lista_utenti[1]["move"]())

lista1 = [1, 2, 3]
lista2 = lista1.copy()
lista2[0] = 10

print(lista2)
print(lista1)

json_di_prova = [
    {
        "username": "marco",
        "age": 30
    },
    {
        "username": "Alessio",
        "age": 39,
        "attributes": {
            "developer": 8
        }
    }
]

search = "mar"
result = None
for utente in json_di_prova:
    if search in utente["username"]:
        result = utente
print("il risultato è ", result)


def ordine_utente(utente):
    return utente["username"]

json_di_prova.sort(key=ordine_utente, reverse=True)
print(json_di_prova)

print(["marco", "alessio"].index("marco"))
utente = {
    "name": "marco",
    "surname": "pret"
}
utente["name"]
utente.keys()
utente.values()

print(f"La data di nascita è {utente.get('data_di_nascita', '?')}")
print(f"il nome è {utente.get('name', '?')}")

# focus ottimizzzione
lista = ["marco", "pret"]
lista[0]



with open("./alessio/utenti.json", 'w', encoding='utf-8') as file: # è possibile salvare il json su un file (questo codice no nsta funzionando)
    json.dump(json_di_prova, file, ensure_ascii=False, indent=4)
    print("save")
print("file close")
