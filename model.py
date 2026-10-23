class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Conta:
    _proximo_numero = 1001  # gerador simples de números de conta

    def __init__(self, cliente: Cliente, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.numero = Conta._proximo_numero
        Conta._proximo_numero += 1
        self.cliente = cliente
        self.saldo = saldo_inicial

    def __str__(self):
        return f"Conta {self.numero} - {self.cliente.nome}"


class BancoDados:
    """Simula um banco de dados usando uma lista em memória."""

    def __init__(self):
        self._contas = []

    def salvar(self, conta: Conta):
        self._contas.append(conta)

    def listar(self):
        return list(self._contas)

    def buscar_por_numero(self, numero: int):
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        return None

    def buscar_por_cpf(self, cpf: str):
        for conta in self._contas:
            if conta.cliente.cpf == cpf:
                return conta
        return None
