from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome: Nome do Cliente.
        cpf: CPF do Cliente.
        agencia: Agencia Responsável pela conta do Cliente.
        num_conta: Número da conta do Cliente.
        saldo: Saldo disponível na conta do Cliente
        limite: Limite de Cheque Especial do Cliente
        transacoes: Histórico de Transações

    """

    @staticmethod
    def _data_e_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self._cpf = cpf
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self.cartoes = []

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_e_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        if (self._saldo - valor) < self._limite_conta():
            print('você não tem saldo suficiente para sacar esse valor.')
            self.consultar()
            return False
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_e_hora()))
            return True

    def consultar(self):
        texto = f'Saldo Atual: R$ {self._saldo:_.2f}'
        print(texto.replace('.', ',').replace('_', '.'))

    def consultar_limite_cheque_especial(self):
        texto = f'Seu límite de Cheque Especial é de  R$ {self._limite_conta():_.2f}'
        print(texto.replace('.', ',').replace('_', '.'))

    def consultar_historico(self):
        print('Histórico de Transações')
        print('Valor | Saldo | Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)


class CartaoCredito:

    @staticmethod
    def _data():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data().month}/{CartaoCredito._data().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1000
        self._senha = '0000'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova senha inválida.')


if __name__ == '__main__':
    pass
