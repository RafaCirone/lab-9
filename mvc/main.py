import tkinter as tk

from model import BancoDados
from view import BancoView
from controller import BancoController


def main():
    root = tk.Tk()
    banco = BancoDados()
    view = BancoView(root)
    BancoController(view, banco)
    root.mainloop()


if __name__ == "__main__":
    main()
