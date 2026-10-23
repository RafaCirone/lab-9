from model import Cliente, Conta, BancoDados


class BancoController:
    def __init__(self, view, banco: BancoDados):
        self.view = view
        self.banco = banco
        self.view.set_controller(self)

    def criar_conta(self):
        # 1. Recebe os dados da View
        nome = self.view.ler_nome()
        cpf = self.view.ler_cpf()
        saldo_texto = self.view.ler_saldo()

        # Validações
        if not nome or not cpf or not saldo_texto:
            self.view.exibir_erro("Preencha Nome, CPF e Saldo Inicial.")
            return

        cpf_numeros = cpf.replace(".", "").replace("-", "")
        if not cpf_numeros.isdigit() or len(cpf_numeros) != 11:
            self.view.exibir_erro("CPF inválido. Informe 11 dígitos.")
            return

        if self.banco.buscar_por_cpf(cpf_numeros):
            self.view.exibir_erro("Já existe uma conta cadastrada para este CPF.")
            return

        try:
            saldo = float(saldo_texto.replace(",", "."))
        except ValueError:
            self.view.exibir_erro("Saldo inicial deve ser um número.")
            return

        try:
            # 2. Instancia o Cliente
            cliente = Cliente(nome, cpf_numeros)
            # 3. Instancia a Conta
            conta = Conta(cliente, saldo)
        except ValueError as erro:
            self.view.exibir_erro(str(erro))
            return

        # 4. Salva no "banco de dados" (Model)
        self.banco.salvar(conta)

        # 5. Comanda a View para exibir a conta criada
        self.view.exibir_conta(conta)
        self.view.limpar_campos()
        self.view.exibir_mensagem(f"Conta {conta.numero} criada com sucesso!")

    def consultar_conta(self):
        termo = self.view.ler_busca().replace(".", "").replace("-", "")
        if not termo:
            self.view.exibir_erro("Informe o número da conta ou o CPF.")
            return

        conta = None
        if termo.isdigit() and len(termo) == 11:
            conta = self.banco.buscar_por_cpf(termo)
        elif termo.isdigit():
            conta = self.banco.buscar_por_numero(int(termo))

        if conta:
            self.view.exibir_conta(conta)
        else:
            self.view.exibir_erro("Conta não encontrada.")
