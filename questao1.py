# Uma tupla é uma sequência de valores separados por vírgulas dentro de
# parênteses, como por exemplo (5,6). Escreva uma função chamada zip que recebe
# duas listas do mesmo comprimento e cria uma nova lista de duas tuplas, onde cada
# duas tuplas é a tupla dos elementos correspondentes das duas listas. Por exemplo,
# zip ([1, 2, 3], [4, 5, 6]) retornaria [(1, 4), (2, 5), (3, 6)]. Use a função em um programa
# e teste seu código com vários valores diferentes.

def zip_(lista1, lista2):
    n = min(map(len, (lista1, lista2)))
    return [(lista1[i], lista2[i]) for i in range(n)]
