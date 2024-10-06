


// non si fa
/*
const autoMazda = {
    "modello": "mazda"
}
const cliente = {
    "name":  "marco",
    "money": 0,
    "sayHello": function () {
        return "hello i'm " + this.name;
    },
    "addMoney": function(moreMoney) {
        this.money = this.money + moreMoney;
    },
    "miaAuto": autoMazda
 }

 console.log(cliente.sayHello())
 console.log(cliente.money)
 utente.addMoney(20)
 console.log(cliente.money)*/

 
 class Auto {
    marca = ""
    modello = ""
    cilindrata = ""
    costo = 0
 }

 class Cliente {
    name = ""
    money = 0
    sesso = ""
    preventiviAuto = []
    miaAuto = new Auto()

    sayHello = () => {
        return "hello i'm " + this.name;
    }

    addMoney = (moreMoney) => {
        this.money = this.money + moreMoney;
    }

    aggiungiPreventivoAuto = (veicolo) => {
        this.preventiviAuto.push(veicolo)
    }

    compra = (auto) => {
        if(this.money >= auto.costo) {
            this.money = this.money - auto.costo
            console.log("acquisto completato")
            return true // solo per esempio
        } else {
            console.log("Soldi non sufficienti")
            return false
        }
    }
 }

 const mazda = new Auto()
 mazda.marca = "mazda"
 mazda.modello = "skyline"
 mazda.costo = 20000

 const fiatPunto = new Auto()
 fiatPunto.marca = "fiat"
 fiatPunto.modello = "punto"
 fiatPunto.costo = 8000

 const marco = new Cliente();
 marco.name = "marco"
 marco.addMoney(20)
 marco.compra(fiatPunto)

 const patri = new Cliente();
 patri.name = "patri"
 patri.addMoney(10000)
 patri.compra(fiatPunto)
 console.log(patri.money)