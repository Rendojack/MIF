import numpy as np
from scipy.misc import derivative
from sympy import *

## 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
print('## 1.\n')

print(np.linspace(start = -1.3 , stop = 2.5, num = 64), '\n') # tiesiskai tolygiai pasiskirstes vektorius

## 2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].
print('## 2.\n')

print(np.tile(np.array([1, 2, 3]), reps = (3, 1)), '\n')

## 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
print('## 3.\n')

def is_odd(number):
    return number % 2 != 0

number = 0
counter = 0
array = []

while counter != 10:
    if is_odd(number) and isinstance(number, int):
        array.append(number)
        counter += 1

    number += 1

print(array, '\n')

## 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
print('## 4.\n')

matrix = np.full(shape = (10, 10), fill_value = 0)
print(np.pad(matrix, pad_width = 1, mode = 'constant', constant_values = 1), '\n')

## 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka 
print('## 5.\n')

## (panaudokite slicing+striding metodą).

matrix = np.zeros((8, 8), dtype = int)

# ::3  kas trecia pradedant nuo pradziu
# 1::3 kas trecia pradedant nuo 1
# i:j:k, starting, stopping, step

matrix[1::2 , ::2] = 1 # lyg eil
matrix[::2 , 1::2] = 1 # nelyg eil

print(matrix, '\n')

## 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j
print('## 6.\n')

matrix = np.zeros((8, 8), dtype = int)

for i in range (0, 9):
    for j in range (0, 9):
        if i == j:
            matrix[i-1,j-1] = i + j - 2

print(matrix, '\n')

## 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją 
## ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
print('## 7.\n')

matrix = np.random.rand(3, 5)

print(matrix, '\n')# random matrix
print(matrix.sum(), '\n')# bendra suma
print(matrix.sum(axis = 1), '\n')# eiluciu sumos
print(matrix.sum(axis = 0), '\n')# stulpeliu sumos

## 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). 
## Surūšiuokite eilutes pagal antrąjį stulpelį. 
## Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
print('## 8.\n')

matrix = np.random.rand(5, 5)

print(matrix, '\n')# random matrix
# i:j:k, starting, stopping, step
# : == :: - select all
# [:, 1] - antras stulpelis
print(matrix[matrix[:, 1].argsort()], '\n')# sorted matrix, by second column

## 9. Atvirkštinę matricą
print('## 9.\n')

matrix = np.random.rand(5, 5)

print(matrix, '\n')# random matrix
print(np.linalg.inv(matrix), '\n')# inverse of a matrix

## 10. Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
## Eigenvalue and Eigenvector
print('## 10.\n')

matrix = np.random.rand(3, 3)
eigenV, eigenVe = np.linalg.eig(matrix)

print(matrix, '\n')# random matrix
print(eigenV, '\n')# tikrines reiksmes
print(eigenVe, '\n')# tikrinis vektorius

## 11. Pasirinktos funkcijos išvestinę
print('## 11.\n')

def func(x):
    return x **3 + x **2

print(derivative(func, x0 = 1.0, dx = 1e-6), '\n')

## 12. Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
print('## 12.\n')

# sympy lib
x = Symbol('x')
print(integrate(x **3 + x **2, x), '\n')# indefinite integral
print(integrate(x **3 + x **2, (x, 1, 5)), '\n')# definite integral