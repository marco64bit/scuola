
VARIABILI

// tipi di variabili
let name = "patrice saoiasio saoi jsaio jass";
let age = 30.8
let male = true

// contenitori di variabili

// liste
let utenti = [
    "Patrice",
    "marco", 
    1, 
    true, 
    [
        1, 
        2, 
        3
    ]
]

// oggetto json
let profilo = {
    "name": "Patrice",
    "age": 30,
    "skills": [
        "html",
        "css"
    ],
    "lista_utenti": utenti
}

ISTRUZIONI

operazioni
let age = 30
let result = (age * 10 + 2 - 2 / 2) **2

controlli

if(result > 30) {
    console.log("ok")
} else if (result > 20 ){
    console.log("troppo giovane")
} else {
    console.log("troppo troppo giovane")
}

CICLI

for(let i = 0; i < 10; i += 1) {
    console.log("Ciao")
}

// -----------------------------------


function calcolaEta(anno) {
    /*
    questa funzione calcola l'età e ritorna il numero di anni
    */
    annoCorrente = new Date().getFullYear()
    return annoCorrente - anno
}

let eta = calcolaEta(1994)


document.






































let eta = calcolaEta(1994)

