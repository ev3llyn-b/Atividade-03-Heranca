class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def exibir_info(self):
        super().exibir_info()
        print(f"Número de portas: {self.numero_portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_info(self):
        super().exibir_info()
        print(f"Cilindradas: {self.cilindradas}cc")

c = Carro("Toyota", "Corolla", 4)
m = Moto("Honda", "CG 160", 160)

c.exibir_info()
m.exibir_info()