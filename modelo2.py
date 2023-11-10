class Filme:
    def __init__(self, nome, ano, duraçao):
        self.__nome = nome.title()
        self.ano = ano
        self.duraçao = duraçao
        self.likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Série:
    def __init__(self, Nome, Ano, Temporadas):
        self.__nome = Nome.title()
        self.ano = Ano
        self.temporadas = Temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome (self, novo_nome):
        self.__nome = novo_nome.title()

vingadores = Filme( 'vingadores - guerra infinita', 2012,  180)
print(f'Nome: {vingadores.__nome} \n - Ano: {vingadores.ano} \n - Duração (em minutos): {vingadores.duraçao} \n - Likes: {vingadores.__likes}')

print('*' * 50)

the_boys = Série('The Boys', 2018, 4)
print(f'Nome: {the_boys.__nome} \n - Ano: {the_boys.ano} \n - Temporadas: {the_boys.temporadas} \n - Likes: {the_boys.__likes}')
