def ncif(x):
    c = 0
    while x > 0:
        x //= 10
        c += 1
    return c
def citire_numere(nume_fisier):
    f = open(nume_fisier, "r")
    matr = []
    line = f.readline().split()
    line = [int(val) for val in line]
    while line != []:
        matr.append(line)
        line = f.readline().split()
        line = [int(val) for val in line]
    f.close()
    return matr
def prelucrare_lista(mat):
    for line in mat:
        minim = min(line)
        while minim in line:
            line.remove(minim)
    lenmin = min([len(line) for line in mat])
    for i in range(len(mat)):
        mat[i] = mat[i][:lenmin]

k = int(input("k = "))
L = citire_numere("numere.in")
cifre = []
for line in L:
    for val in line:
        if ncif(val) == k:
            cifre.append(val)
cifre.sort()
cifre.reverse()
l = len(cifre)
cifre1 = []
for val in cifre:
    if val not in cifre1:
        cifre1.append(val)
g = open("cifre.out", "w")
for val in cifre1:
    g.write(str(val) + " ")
g.close()

prelucrare_lista(L)
for line in L:
    print(*line, sep = " ")