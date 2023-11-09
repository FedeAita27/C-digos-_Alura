class Filme:
    def __init__(self, nome, ano, duraçao):
        self.nome = nome
        self.ano = ano
        self.duraçao = duraçao

class Série:
    def __init__(self, Nome, Ano, Temporadas):
        self.nome = Nome
        self.ano = Ano
        self.temporadas = Temporadas

vingadores = Filme('vingadores', 2012, 180)
print(vingadores.nome, vingadores.ano, vingadores.duraçao)

the_boys = Série('the_boys', 2018, 4)
print(the_boys.nome,  the_boys.ano, the_boys.temporadas)
