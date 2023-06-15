from core.livro import Livro
from core.livro_repository import LivroRepository


class LivroRepositoryImpl(LivroRepository):
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        return livro

    def listar_livros(self):
        return self.livros

    def obter_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def remover_livro(self, isbn):
        livro = self.obter_livro(isbn)
        if livro:
            self.livros.remove(livro)
            return livro
        return None
