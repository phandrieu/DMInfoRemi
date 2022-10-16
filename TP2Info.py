import numpy as np
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



#-------------------------------------------------------------
#somme_pyramide_memo
#-------------------------------------------------------------

def somme_pyramide_memo(P, i, j):
    dico = {}
    def somme_pyramide_memo_aux(P, i, j):
        if i == n-1:
            dico[(i,j)] = P[i][j]
            return p[i][j]
        if (i,j) in dico:
            return dico[(i,j)]
        else:
            a = P[i][j] + max(somme_pyramide_memo_aux(P, i+1, j), somme_pyramide_memo_aux(P, i+1, j+1))
    return a
