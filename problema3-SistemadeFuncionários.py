class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus


class Programador(Funcionario):
    def __init__(self, nome, salario_base, horas_extras, valor_hora_extra):
        super().__init__(nome, salario_base)
        self.horas_extras = horas_extras
        self.valor_hora_extra = valor_hora_extra

    def calcular_salario(self):
        return self.salario_base + (self.horas_extras * self.valor_hora_extra)

funcionarios = [
    Gerente("Ana", 5000, 1500),
    Programador("Lucas", 3000, 10, 50),
    Programador("Mariana", 3200, 20, 40),
    Gerente("Carlos", 6000, 2000)
]

for f in funcionarios:
    print(f"{f.nome} - Salário: R${f.calcular_salario()}")