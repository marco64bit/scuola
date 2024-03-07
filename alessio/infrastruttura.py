
def foo2(res):
    status = 'normal'
    
    if res > 100:
        return 'danger'
    elif res >  50:
        return 'alert'

    return status

def foo(var1, var2):
    res = var1 * var2
    return foo2(res)


import pdb;pdb.set_trace()
print(f"livello del fiume {foo(5, 15)}")


# si può aggiungere del codice temporaneo, come un if, per richiamare il 
# debugger solo per una condizione che mi interessa 

for x in range(100):
    if x % 2 != 0:
        import pdb;pdb.set_trace()
    foo(x , x + 1)
    
    
# il debugger è `import pdb;pdb.set_trace()`
# se lanci `
# import pdb
# help(pdb)` ne scopri le funzionalità
# le principali sono
# 'n' next: vai alla linea successiva
# 'l' line: stampa il codice intorno alla line dove sei
# 's' step: entra in una funzione
# 'c' continue: vai al prossimo pdb.set_trace()


# 1 linea guida di quel linguaggio (leggibilità)
#
# organizzazione
#  infrastruttura (cosa fa cosa e come si divide il codice)
#  scaffolding (organizzazione cartelle e file)
#
# test automatici (non sempre) Unit Test
# quando?
#  importante se si scrivono, scriverli da subito
#  è difficile scrivere test su codice già scritto e non prensato per essere testato, serve il refactor lungo e faticoso
#  se sto scrivendo una libreria (insieme di funzioni che utilizzerà il tuo codice)
#  se il prodotto ha una vita medio/lunaga e non è minuscolo (se cresce e si modifica)

# su progetti già avviati posso testare il nuovo. Scrivo i test solo sul codice che sviluppo da oggi in poi



# scaffolding (organizzare cartelle)
"""
    readme.md (spiega il progetto cosa fa, come si installa, come si avvia, come si lanciana i test, come si rilascia. utility e note)
    config.json (file di configuarazione dove stanno le variabili)
    app/
        view/
            components/ -> componenti eseguono a una funzione, possono contenere altri componenti chiamti view, il componente non si riutilizza
                sidebar/
                dashboard/
                post/
                    post.js
                    view_header
                    view_media
                    view_content
                    view_actions
                    view_comments
            widgets/
                slider/
                fader/
                tastierino/
                gallery/
        controller/
            utente/
        services/
            login/
        model/ -> si interfaccia con la base dati (database, file, store in memoria) applica logice esclusivamente ralative alla manipolazione dei dati
        -- inserimento, lettura (formattazione), cancellazione, modifica
            utente/
                utente.py 
            tracce/
            preferenze/
            strumenti/
"""


"""
effetti/
    pitch/
    ...
"""