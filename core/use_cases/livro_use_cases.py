from core.livro import Livro
from core.livro_repository import LivroRepository
from core.use_cases.livro_dto import LivroDTO


class LivroUseCases:
    def __init__(self, livro_repository: LivroRepository):
        self.livro_repository = livro_repository

    def adicionar_livro(self, livro_dto: LivroDTO):
        livro = Livro(
            isbn=livro_dto.isbn,
            titulo=livro_dto.titulo,
            autor=livro_dto.autor,
            ano=livro_dto.ano,
        )
        return self.livro_repository.adicionar_livro(livro)

    def listar_livros(self):
        return self.livro_repository.listar_livros()

    def obter_livro(self, isbn):
        return self.livro_repository.obter_livro(isbn)

    def remover_livro(self, isbn):
        return self.livro_repository.remover_livro(isbn)
