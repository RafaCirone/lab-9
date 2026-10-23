import tkinter as tk
from tkinter import ttk, messagebox


class BancoView:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Sistema Bancário - MVC")
        self.root.geometry("520x520")
        self.root.resizable(False, False)
        self.controller = None

        self._criar_interface()

    def set_controller(self, controller):
        self.controller = controller

    # ------------------------------------------------------------------
    # Construção da interface
    # ------------------------------------------------------------------
    def _criar_interface(self):
        # --- Cadastro ---
        frame_cadastro = ttk.LabelFrame(self.root, text="Criar Conta", padding=10)
        frame_cadastro.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_cadastro, text="Nome:").grid(row=0, column=0, sticky="w", pady=3)
        self.entry_nome = ttk.Entry(frame_cadastro, width=40)
        self.entry_nome.grid(row=0, column=1, pady=3)

        ttk.Label(frame_cadastro, text="CPF:").grid(row=1, column=0, sticky="w", pady=3)
        self.entry_cpf = ttk.Entry(frame_cadastro, width=40)
        self.entry_cpf.grid(row=1, column=1, pady=3)

        ttk.Label(frame_cadastro, text="Saldo Inicial (R$):").grid(row=2, column=0, sticky="w", pady=3)
        self.entry_saldo = ttk.Entry(frame_cadastro, width=40)
        self.entry_saldo.grid(row=2, column=1, pady=3)

        ttk.Button(frame_cadastro, text="Criar Conta",
                   command=self._on_criar_conta).grid(row=3, column=0, columnspan=2, pady=8)

        # --- Consulta ---
        frame_consulta = ttk.LabelFrame(self.root, text="Consultar Conta", padding=10)
        frame_consulta.pack(fill="x", padx=10)

        ttk.Label(frame_consulta, text="Nº da conta ou CPF:").grid(row=0, column=0, sticky="w")
        self.entry_busca = ttk.Entry(frame_consulta, width=25)
        self.entry_busca.grid(row=0, column=1, padx=5)
        ttk.Button(frame_consulta, text="Consultar",
                   command=self._on_consultar).grid(row=0, column=2)

        # --- Exibição ---
        frame_saida = ttk.LabelFrame(self.root, text="Dados da Conta", padding=10)
        frame_saida.pack(fill="both", expand=True, padx=10, pady=10)

        self.texto_saida = tk.Text(frame_saida, height=12, state="disabled",
                                   font=("Courier New", 10))
        self.texto_saida.pack(fill="both", expand=True)

    # ------------------------------------------------------------------
    # Eventos -> repassados ao Controller
    # ------------------------------------------------------------------
    def _on_criar_conta(self):
        if self.controller:
            self.controller.criar_conta()

    def _on_consultar(self):
        if self.controller:
            self.controller.consultar_conta()

    # ------------------------------------------------------------------
    # Métodos de entrada
    # ------------------------------------------------------------------
    def ler_nome(self) -> str:
        return self.entry_nome.get().strip()

    def ler_cpf(self) -> str:
        return self.entry_cpf.get().strip()

    def ler_saldo(self) -> str:
        return self.entry_saldo.get().strip()

    def ler_busca(self) -> str:
        return self.entry_busca.get().strip()

    def limpar_campos(self):
        for entry in (self.entry_nome, self.entry_cpf, self.entry_saldo):
            entry.delete(0, tk.END)

    # ------------------------------------------------------------------
    # Métodos de saída
    # ------------------------------------------------------------------
    def exibir_conta(self, conta):
        saldo_fmt = f"{conta.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        texto = (
            "========================================\n"
            "            DADOS DA CONTA\n"
            "========================================\n"
            f" Número da Conta : {conta.numero}\n"
            f" Titular         : {conta.cliente.nome}\n"
            f" CPF             : {conta.cliente.cpf}\n"
            f" Saldo           : R$ {saldo_fmt}\n"
            "========================================\n"
        )
        self._escrever_saida(texto)

    def exibir_mensagem(self, mensagem: str):
        messagebox.showinfo("Informação", mensagem)

    def exibir_erro(self, mensagem: str):
        messagebox.showerror("Erro", mensagem)

    def _escrever_saida(self, texto: str):
        self.texto_saida.config(state="normal")
        self.texto_saida.delete("1.0", tk.END)
        self.texto_saida.insert(tk.END, texto)
        self.texto_saida.config(state="disabled")
