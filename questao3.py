"""
3 – Escreva um programa para armazenar uma agenda de telefones em um dicionário.
Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da
pessoa. Seu programa deve ter as seguintes funções:
• incluirNovoNome – essa função acrescenta um novo nome na agenda, com um
ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
• incluirTelefone – essa função acrescenta um telefone em um nome existente
na agenda. Caso o nome não exista na agenda, você deve perguntar se a
pessoa deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior
para incluir o novo nome.
• excluirTelefone – essa função exclui um telefone de uma pessoa que já está na
agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
• excluirNome – essa função exclui uma pessoa da agenda.
• consultarTelefone – essa função retorna os telefones de uma pessoa na
agenda.
"""

from yn import yes_or_no


def _validar_telefone(tel):
    assert NotImplementedError


class Agenda:
    def __init__(self, telefones=None):
        assert telefones is None
        if telefones is None:
            telefones = {}
        self._telefones = telefones

    def incluir_novo_nome(self, nome, telefones):
        if nome in self._telefones:
            self._merge(nome, telefones)
        else:
            self._telefones[nome] = telefones

    def incluir_telefone(self, nome, telefone):
        if nome not in self._telefones:
            prompt = '"{nome}" não existe. Deseja incluí-lo na agenda?'.format(nome=nome)
            if yes_or_no(prompt):
                self.incluir_novo_nome(nome, [telefone])
        else:
            if telefone not in self._telefones[nome]:
                self._telefones[nome].append(telefone)

    def excluir_telefone(self, nome, telefone):
        if nome in self._telefones:
            if telefone in self._telefones[nome]:
                self._telefones[nome].remove(telefone)
                if not self._telefones[nome]:
                    self.excluir_nome(nome)

    def excluir_nome(self, nome):
        if nome in self._telefones:
            self._telefones.pop(nome)

    def consultar_telefones(self, nome):
        return self._telefones[nome] if nome in self._telefones else None

    def _merge(self, nome, new_telefones):
        old_telefones = self._telefones[nome]
        self._telefones[nome] = list(set(old_telefones) | set(new_telefones))
