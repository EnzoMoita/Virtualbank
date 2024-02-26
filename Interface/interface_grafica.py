import tkinter as tk
from tkinter import messagebox
from caixa_eletronico import CaixaEletronico

class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def verificar_saldo(self):
        return f"Seu saldo atual é de R${self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "O valor do depósito deve ser maior que zero."

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                return f"Saque de R${valor:.2f} realizado com sucesso."
            else:
                return "Saldo insuficiente."
        else:
            return "O valor do saque deve ser maior que zero."

def verificar_saldo():
    messagebox.showinfo("Saldo", caixa.verificar_saldo())

def depositar():
    valor = float(entry_valor.get())
    messagebox.showinfo("Depósito", caixa.depositar(valor))

def sacar():
    valor = float(entry_valor.get())
    messagebox.showinfo("Saque", caixa.sacar(valor))

caixa = CaixaEletronico()

root = tk.Tk()
root.title("Caixa Eletrônico")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_valor = tk.Label(frame, text="Valor:")
label_valor.grid(row=0, column=0)

entry_valor = tk.Entry(frame)
entry_valor.grid(row=0, column=1)

btn_verificar_saldo = tk.Button(frame, text="Verificar Saldo", command=verificar_saldo)
btn_verificar_saldo.grid(row=1, column=0, columnspan=2, pady=5, sticky="we")

btn_depositar = tk.Button(frame, text="Depositar", command=depositar)
btn_depositar.grid(row=2, column=0, columnspan=2, pady=5, sticky="we")

btn_sacar = tk.Button(frame, text="Sacar", command=sacar)
btn_sacar.grid(row=3, column=0, columnspan=2, pady=5, sticky="we")

root.mainloop()
