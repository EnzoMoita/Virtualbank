    
    
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

def main():
    print("Bem-vindo ao Caixa do Enzin!")
    caixa = CaixaEletronico()
    while True:
        print("\n1. Verificar saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print(caixa.verificar_saldo())
        elif opcao == "2":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            print(caixa.depositar(valor_deposito))
        elif opcao == "3":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            print(caixa.sacar(valor_saque))
        elif opcao == "4":
            print("Obrigado por utilizar o caixa Enzin. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
