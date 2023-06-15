from core.livro import Livro
from core.livro_repository import LivroRepository


class LivroService:
    def __init__(self, livro_repository: LivroRepository):
        self.livro_repository = livro_repository

    def adicionar_livro(self, isbn, titulo, autor, ano):
        livro = Livro(isbn=isbn, titulo=titulo, autor=autor, ano=ano)
        return self.livro_repository.adicionar_livro(livro)

    def listar_livros(self):
        return self.livro_repository.listar_livros()

    def obter_livro(self, isbn):
        return self.livro_repository.obter_livro(isbn)

    def remover_livro(self, isbn):
        return self.livro_repository.remover_livro(isbn)
