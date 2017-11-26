from base_de_dados import avaliacoes
from math import sqrt
import numpy as np

def euclidiana (usuario1, usuario2):
    i = False
    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]:
            i = True
            break
    if not i:
        return 0
    c = sqrt(sum((avaliacoes[usuario1].get(d, 0) - avaliacoes[usuario2].get(d, 0)) ** 2 for d in set(avaliacoes[usuario1]) & set(avaliacoes[usuario2])))
    return 1/(1+c)

def getSimilares(usuario):
    similaridade = [(euclidiana(usuario, outro), outro) for outro in avaliacoes if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade
print(getSimilares('Marcos'))



