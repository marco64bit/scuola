# Corso di programmazione front-end

linguaggi trattati
- html 5
- css 3 / scss
- javascript es6 / Typescript (forse)

Frameworks
- React

### Programma

- [ ] Differenze tra html, css, js (struttura, stile, logiche)
- [ ] Linguaggi di markup e linguaggi di programmazione
- [ ] la storia del frontend web, dal modificare l'html col js allo scrivere l'html dal javascript (jsx/react)
- [ ] scrittura pagina html e legame con css e js
- [ ] React, cos'è, Atom design, componenti
- [ ] React, creazione prima app, piccole modifiche

- [ ] **Esercizio 1**: Il sito per vedere i gatti del giorno. Scrivere una login page in html, unire il css, unire il javascript
    - [ ] form e validazione (html, css, js)
    - [ ] salvare i risultati di un form in uno stato json (js)
    - [ ] inviarli a un server (scritto da marco) e gestire successo e errore, salvare la risposta di successo in localStorage
    - [ ] se l'utente è loggato mostrare una nuova pagina con 2 link (link al profilo, link ai "gatti di oggi")
    - [ ] il profilo mostra le info di registrazione
        - [ ] il pulsante logout
        - [ ] la modifica dei dati di profilo chiamando il server
    - [ ] i gatti di oggi mostra il risultato di una ajax all'api pubblica dei gatti, mostrando i primi 5 risultati e paginandoli

- Ajax, cos'è, come si effettuano le chiamate di rete, standard HTTP
- Accenno di standard REST API (creare dei servizi)

- [ ] **Esercizio 2** la prima react app, rifare l'esercizio 1


## esercizio la rubrica

- **programma rubrica** REACT (La rubrica deve gestire i miei appuntamenti, inserirli in modo semplice e mostrarli in un calendario)
[CLIENT WEB]
    - inserimento appuntamento
        - form inserimento appuntamento
        - data, ora e titolo e descrizione
        - pulsante salva, per ora su localStorage in json aggiungendo un ID
    - visualizzazione
        - mostra un calendario stile google calendar
        - (DAY) lista appuntamenti del giorno inseriti in una timeline
        - (MONTH) griglia del calendario mensile con solo lo snippet del titolo appuntamento nei giorni
    - ricerca
        - stringa di ricerca libera, cerca in tutti gli appuntamenti per dentro la data, ora, titolo, descrizione
    - Dettaglio 
        - selezionato l'evento si possono modificare i campi e aggiornare il localstorage
        - nel dettaglio c'è anche il pulsante elimina
- Rubrica v2
    - aggiungere registrazione/login iniziale
    - login form con validare agganciando un server web
    - salvare i dati utente su server
    - si spostano i salvataggi da localstorage a server API/Database
    - scrittura API e modelli DB
    - interazione con client web


#### Lista degli argomenti per linguaggi

- **javascript**
    - caratteristiche del linguaggio
        - flessibilità, non tipazione
        - gestione errori (stacktrace in console, come leggere un errore)
        - logging (console.log)
        - debug
    - Le variabili (let, const)
        - il tipo string
        - il tipo number
        - il tipo array
        - il tipo object
    - I controlli (if, else, else if, switch)
        - gli operatori (&& || !== == >= <= < >)
    - cicli (for, while)
    - Le funzioni 
        - parametri in ingresso
        - return
        - code documentation
        - visibilità delle variabili (concetto di scope / life cycle)
        - funzioni ricorsive
        - funzioni nested

    - FOCUS array (forEach, map, filter, search, reduce, sort)
    - FOCUS Object/Json object
        - concetto di chiave valore, il formato json
    - Le classi (opzionale)
    - AJAX/XHR e fetch come si chiama il server
- **HTML 5**
    - header e body
        - dove si carica il css
        - dove si carica il javascript
        - i meta tag
    - tipi di elementi
    - gli attributi
    - i form
    - come interagire con css
    - come interagire con js
    - contenuti multimediali img, video, file
    - strutturare un pagina html (contenitori dentro altri contenitori)
- **CSS 3**
    - le classi css
    - la nomenclatura
    - la varie regole del css
        - regole sul testo
        - regole sui contenitori
- **il framework React**
    - teoria (atom design)
    - creazione prima app di prova
    - i componenti
        - lo stato
        - reload
        - props
        - rendering
        - css
    - lo stato
    - installare lib esterne (node)
    

