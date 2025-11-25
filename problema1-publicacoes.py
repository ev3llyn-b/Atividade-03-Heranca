class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descrever(self):
        print(f"Título: {self.titulo}, Ano: {self.ano_publicacao}")


class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor

    def descrever(self):
        super().descrever()
        print(f"Autor: {self.autor}")


class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao)
        self.edicao = edicao

    def descrever(self):
        super().descrever()
        print(f"Edição: {self.edicao}")
        

l = Livro("Dom Casmurro", 1899, "Machado de Assis")
r = Revista("Superinteressante", 2024, "Edição 320")

l.descrever()
r.descrever()