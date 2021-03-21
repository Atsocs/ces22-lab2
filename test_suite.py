from questao1 import zip_
from questao2 import unzip
from questao3 import Agenda


def test_questao1():
    assert zip_([1, 2, 3], [4, 5, 6]) == [(1, 4), (2, 5), (3, 6)]


def test_questao2():
    assert unzip([(1, 4), (2, 5), (3, 6)]) == ([1, 2, 3], [4, 5, 6])


def test_questao3():
    agenda = Agenda({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7]})
    agenda.incluir_novo_nome("d", [8, 9])
    assert agenda.consultar_telefones('a') == [1, 2, 3]
    assert agenda.consultar_telefones('b') == [4, 5, 6]
    assert agenda.consultar_telefones('c') == [7]
    assert agenda.consultar_telefones('d') == [8, 9]


test_questao3()
