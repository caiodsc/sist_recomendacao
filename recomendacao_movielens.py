def carregaMovieLens():
    filmes = {}
    for linha in open('./u.item'):
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    #print(filmes)
    base = {}
    for linha in open('./u.data'):
        (usuario, idfilme, nota, tempo) = linha.split('\t')
        base.setdefault(usuario, {})
        base[usuario][filmes[idfilme]] = float(nota)
    print(base)

carregaMovieLens()