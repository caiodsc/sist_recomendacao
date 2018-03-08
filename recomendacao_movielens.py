from math import sqrt
def euclidiana (base, usuario1, usuario2):
    i = False
    for item in base[usuario1]:
        if item in base[usuario2]:
            i = True
            break
    if not i:
        return 0
    r = sqrt(sum([pow(base[usuario1][item] - base[usuario2][item], 2) for item in base[usuario1] if item in base[usuario2]]))
    return (1/(1+r))


def getSimilares(base, usuario):
    similaridade = [(euclidiana(base, usuario, outro), outro) for outro in base if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]

def getRecomendacoes(base, usuario):
    totais = {}
    somaSimilaridade = {}
    for outro in base:
        if outro == usuario: continue
        similaridade = euclidiana(base, usuario, outro)
        if similaridade <= 0: continue
        for item in base[outro]:
            if item not in base[usuario]:
                totais.setdefault(item, 0)
                totais[item] += base[outro][item] * similaridade
                somaSimilaridade.setdefault(item, 0)
                somaSimilaridade[item] += similaridade
    rankings = [(total/somaSimilaridade[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]


def carregaMovieLens():
    filmes = {}
    for linha in open('./u.item'):
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    base = {}
    for linha in open('./u.data'):
        (usuario, idfilme, nota, tempo) = linha.split('\t')
        base.setdefault(usuario, {})
        base[usuario][filmes[idfilme]] = float(nota)
    return base


base = carregaMovieLens()
print(getRecomendacoes(base, '1'))




