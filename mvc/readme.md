Sistema Bancário - MVC (Python)

Sistema simples de gerenciamento bancário com interface gráfica (Tkinter), organizado na arquitetura MVC, que permite Criar Conta e Exibir/Consultar Dados da Conta.

Estrutura
├── model.py       # Cliente, Conta e BancoDados (lista em memória)
├── view.py        # Interface gráfica, métodos de entrada e exibição formatada
├── controller.py  # Recebe dados da View, cria Cliente/Conta, salva no Model e comanda a View
└── main.py        # Ponto de entrada
Como executar

Requer Python 3.8+ (o Tkinter já vem com a instalação padrão do Python).

bash
python main.py

No Linux, se o Tkinter não estiver instalado: sudo apt install python3-tk

Fluxo MVC
O usuário preenche Nome, CPF e Saldo Inicial na View e clica em "Criar Conta".
O Controller lê os dados da View, valida, instancia Cliente e Conta.
A conta é salva no BancoDados (Model).
O Controller comanda a View a exibir os dados da conta criada.
Também é possível consultar uma conta pelo número ou CPF.