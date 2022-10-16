import numpy as np
from copy import deepcopy
#-------------------------------------------------------------
#effectifs
#-------------------------------------------------------------

L = [1, 28, 18, -2, 7, 50, 12, 17, 1, 1, 28, 5, 9]


def effectifs(L):
    D = {}
    max = L[0]
    min = L[0]

    for elt in L:

        if elt > max:
            max = elt

        if elt < min:
            min = elt

        if elt in D:
            D[elt] = D[elt]+1
        else:
            D[elt] = 1

    return D,min,max


#-------------------------------------------------------------
#tri dénombrement
#-------------------------------------------------------------

def tri_denombrement(A):
    B = []
    d, min, max = effectifs(A)

    for i in range(min, max+1):
        if i in d:
            for k in range(d[i]):
                B.append(i)

    return B



#-------------------------------------------------------------
#somme_pyramide
#-------------------------------------------------------------


P = [[2], [8,4], [1,3,5], [7,0,8,6], [6, 3, 10, 5, 1]]

def somme_pyramide(P, i, j):
    n = len(P)
    if i == n-1:
        return P[i][j]
    else:
       return P[i][j] + max(somme_pyramide(P, i+1,j), somme_pyramide(P, i+1, j+1))

print(somme_pyramide(P, 0, 0))

#-------------------------------------------------------------
#somme_pyramide_memo
#-------------------------------------------------------------

def somme_pyramide_memo(P):
    dico = {}
    def somme_pyramide_memo_aux(P, i, j):
        n = len(P)
        if i == n-1:
            dico[(i,j)] = P[i][j]
            return P[i][j]
        if (i,j) in dico:
            return dico[(i,j)]
        else:
            a = P[i][j] + max(somme_pyramide_memo_aux(P, i+1, j), somme_pyramide_memo_aux(P, i+1, j+1))
        return a
    a = somme_pyramide_memo_aux(P, 0, 0)
    return a

print(somme_pyramide_memo(P))

#-------------------------------------------------------------
#somme_pyramide_asc
#-------------------------------------------------------------

def somme_pyramide_asc(P):
    Pprime = deepcopy(P) 
    n = len(P)
    for i in range(n-2, -1, -1):
        for j in range(len(Pprime[i])):
            Pprime[i][j] += max(Pprime[i+1][j], Pprime[i+1][j+1])
    return Pprime[0][0]

print(somme_pyramide_asc(P))

#-------------------------------------------------------------
#somme_pyramide_asc_chemin
#-------------------------------------------------------------

def somme_pyramide_asc_chemin(P):
    Pprime = deepcopy(P)
    n = len(P)
    chemin = []
    for i in range(n-2, -1, -1):
        for j in range(len(Pprime[i])):
            if Pprime[i+1][j] > Pprime[i+1][j+1]:
                Pprime[i][j] += Pprime[i+1][j]
            else:
                Pprime[i][j] += Pprime[i+1][j+1]
    somme = Pprime[0][0]
    i = 0
    j = 0
    chemin.append(P[0][0])
    while i < n-1:
        if Pprime[i+1][j] > Pprime[i+1][j+1]:
            chemin.append(P[i+1][j])
            i += 1
        else:
            chemin.append(P[i+1][j+1])
            i += 1
            j += 1
    return somme, chemin
print(somme_pyramide_asc_chemin(P))