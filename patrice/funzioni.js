

// const calcolaSomma = (a, b) => {
//     return a + b
// }

// calcolaSomma(10, 5)

// const result = calcolaSomma(10, 5)
// console.log("il risultato è " + result)





















// const nome = "Marco"
// const age = 30
// let documento = `il mio nome è ${nome} e ho ${age}`;

// let number = 1.44
// let maggiorenne = true

// let listNomi = [
//     "nome1",
//     "nome2",
//     "pippo",
//     1,
//     true,
// ]

// let user = {
//     name: "marco",
//     age: 30,
//     skills: [
//         "javascript",
//         "css",
//         "html"
//     ]
// }

// let somma = () => {
//     console.log("hello")
// }

// let somma









const multiply = (number1, number2) => {
    return number1 * number2
}


const resultList = [];

for (let i = 1; i < 11; i++) { // quale tabellina sto facendo
    for (let j = 1; j < 11; j++) { // ciclo la singola tabellina
        const res = multiply(i, j);
        resultList.push(res)
    }
}
console.log(resultList)








