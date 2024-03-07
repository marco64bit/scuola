x = None
y = "marco"
i = ""
list = []
z = 1
k = 0

# if entra se il tipo di variabile passata esiste o è non è vuota
# booleani True
# non None
# stringhe entra non vuota, idem liste, idem dizionari
# numeri entra se non zero
if x:
    print("non entro")

if y:
    print("la stringa esiste")

if i:
    print("non entra")

if list:
    print("non entra")

if k:
    print("non entra")

if z:
    print("entra")


# if condizione:
# elif condizione 2:
# else:

nome = "marco"
if len(nome) > 10:
    print("> 10")
elif len(nome) > 5:
    print("> 5")
elif len(nome) > 4:
    print("> 4")
else:
    print("< 5")

if "...":
    pass

if "...":
    pass

# operatori and, or, not, is, in
# confronti ==, >, >=, <, <=, !=
num = 10
if (num > 10 and num < 20) or num == 0:
    print("ok")

# i : sono usati per creare un blocco


class Utente():
    pass


def foo():
    pass


if "ciao":
    pass

for x in [1, 2, 3]:
    pass

# with open("", "w") as f:
#    pass #blocco


# per condizioni lunghe a capo
num = 10
if num == 0 \
        or (num > 1 and num < 10) \
        or (num < -1) \
        or (num / 3 == 4):
    print("entra")


# cicli
# for, while

num = 20
while num > 10:
    num = num - 1

for carattere in "marco":
    print(carattere)

for num in [1, 2, 3]:
    print(num)

num1, num2 = [1, 2]
print(num1, num2)

list = [1, 2, 3]
# asterisco scoppia gli elementi nella lista, ma è meno efficiente di fare 
# .copy, se si volesse solo fare una copia
list_2 = [10, 11, *list]
print(list_2)

for index, value in enumerate(["a", "b", "c"]):
    print(value, index)
    
for x in range(100):
    print(".")

# il for cicla sempre su iterabili
