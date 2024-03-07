# programma

### intro
- cos'è la programmazione
- i file sul computer, 
    ogni cosa su un computer viene salvata come un file e ogni file 
    contiene dati testuali in un codifica (ascii, utf8, latin, binario, etc...) ogni file ha un estensione
    .txt .jpg .mp4 .mov .py, a seconda di essa viene interpretato dal programma addetto a leggerlo/eseguirlo
    esistono i file che contengono come dato linee di codice, possono essere file eseguibili e quindi un programma
- la ram e l'hard disk
- le variabili in memoria

### python3

- la filosofia del linguaggio (ZEN Python e standar Pep8)
    - linee guida (vedi slides)
-   linguaggio interpretato e non compilato (errori solo in runtime)
- flessibile (scripting o strutturato)
- ad alto livello
- lista della spesa delle potenzilità
        - variabili
        - funzioni
        - oggetti
        - decoratori
        - iteratori
        - contesto
        etc..
- la sheel, l'autocomplete e il comando help
- i commenti e la documentazione delle funzioni


### le variabili

- tutti i tipi di variabili sono un oggetto in python3 e quindi hanno delle funzioni (metodi) interni
duck typing: la tipazione è desunta dal valore della variabile in quel momento
- tipazione condizionale (solo per aiutare la comprensione ma non genera errori in quanto python non è un linguaggio compilato)
    - interi
    - booleani
    - stringhe
    - liste
    - dizionari
    - set (liste senza ripetizione)
- focus su ogni tipo

- lo scope delle variabili (la loro visibilità e gestione della memoria ram)


## cicli e condizioni
    
- l'if, elif, else
- gli operatori logici and, or
- i controlli tra due valori:
    - not, not in, in, >, >=, <, <=, ==, !=
- il for e il while

## le funzioni
    
- def


## dubugging del codice

- tramite stack trace
- con python debugger `pdb`
    - i comandi del pdb
    - codice extra per usare il punto di debug solo quando necessario
- le buon vecchie print aiutano sempre

## test automatici
- Quando ha senso scrivere i test (librerie, microservizi, programmi medio grandi eduraturi nel tempo)
- aiutano alla scrittura di un codice ben   strutturato, modulare, scalabile. Un buon codice deve essere testabile in ogni sua funzionalità
- mantengono il programma funzionante in ogni sua parte dopo ogni sua modifica
- definiscono mentalmente cosa mi aspetto da ogni singolo pezzo di codice (casi limite e casi standard)
- TEST REGRESSION: quando scovo un bug scrivo un test nuovo perchè non stavo coprendo quella casistica, il test si deve rompere, poi fixo il bug, il test che avevo scritto prima deve funzionare *
- scrittura di un test insieme *

### refactor
- scrivere i test su un codice non testato implica spesso il refactor
- il refactor come fonte di pulizia del codice
- refactor su un codice insieme *

## infrastruttura

- il programmatore come un architetto
- lo scaffolding
- MVC (model view controller) design patterns
- view (la programmazione atomica Atom Design) *


## moduli e librerie

- l'import
- cos'è un modulo e come crearlo
- dipendenze circolari *


## gli oggetti *

- cos'è un oggetto
- quando ha senso averlo
- di cosa si occupa e cosa ci si mette dentro
- instanziare un oggetto
- ereditarietà tra oggetti
- metodi privati
- metodi statici e di classe
- metodi super privatu (python3 native)
- NO God object

# Django

- cos'è un il framework django e a cosa serve
- primo progetto django
- prima API di prova, introduzione api REST
- il primo modello (migrazione)

## esercizio la rubrica

- **programma rubrica** (La ribruca deve gestire i miei appuntamenti, inserirli in modo semplice e mostrarli in un calendario)
[CLIENT CONSOLE]
    - inserimento appuntamento
        - input di testo libero per salvare gli appuntamenti
        - dal testo libero deve capire e estrarre data, ora e titolo
        - chiesta la conferma di salvataggio
        - salvataggio aggiungendo un ID ( su file )
    - visualizzazione
        - (ALL_TIME) lista ordinata di eventi dal più vicino al più lontano paginati primi 5
        - (TODAY) appuntamenti di oggi in ordine temporale
        - (WEEK) appuntamenti in settimana divisi per giorno, in ordine temporale
    - ricerca
        - stringa di ricerca libera, cerca in tutti gli appuntamenti per dentro la data, ora, titolo, descrizione
    - Modifica 
        - selezionato l'ID (se non esiste L'ID errore opzionale) si può dire di modificarlo (inserimento descrizione, cambio titolo, data orario) (se )
    - Cancellazione
        - selezionato l'ID si può dire di cancellarlo (se non esiste L'ID errore opzionale)
- Rubrica v2
    - aggiungere registrazione/login iniziale
    - validare agganciando un server web
    - salvare i dati utente su server
    - si spostano i salvataggi da file a server API/Database
    - scrittura API e modelli DB
    - interazione con client
