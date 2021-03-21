# Escreva uma função chamada unzip que retorna uma tupla de duas listas que
# resultam da descompactação de uma lista compactada (consulte o exercício
# anterior). Portanto, unzip([(1, 4), (2, 5), (3, 6)]) retornaria ([1, 2, 3], [4, 5, 6]). Use a
# função em um programa e teste seu código com vários valores diferentes.

def unzip(lista_de_tuplas):
    xs, ys = [], []
    for (x, y) in lista_de_tuplas:
        xs.append(x)
        ys.append(y)
    return xs, ys
