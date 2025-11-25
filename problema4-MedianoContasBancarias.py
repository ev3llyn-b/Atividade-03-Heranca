class Conta:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
            return True
        else:
            print("Saldo insuficiente para saque!")
            return False

    def extrato(self):
        print(f"Titular: {self.titular}, Conta: {self.numero_conta}, Saldo: R$ {self.saldo:.2f}")


class ContaPoupanca(Conta):
    def render_juros(self, taxa):
        if taxa > 0:
            juros = self.saldo * (taxa / 100)
            self.saldo += juros
            print(f"Juros de R$ {juros:.2f} aplicados. Novo saldo: R$ {self.saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, titular, numero_conta, saldo=0, limite_cheque_especial=0):
        super().__init__(titular, numero_conta, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if valor > 0 and valor <= (self.saldo + self.limite_cheque_especial):
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
            return True
        else:
            print("Limite de saque excedido! Operação cancelada.")
            return False


cp = ContaPoupanca("Ana", "001", 1000)
cc = ContaCorrente("Carlos", "002", 500, limite_cheque_especial=300)

cp.extrato()
cp.sacar(1200)
cp.render_juros(10)
cp.extrato()

print()

cc.extrato()
cc.sacar(700)
cc.sacar(200)
cc.extrato()
