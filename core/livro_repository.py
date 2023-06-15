from abc import ABC, abstractmethod

from core.livro import Livro


class LivroRepository(ABC):
    @abstractmethod
    def adicionar_livro(self, livro):
        pass

    @abstractmethod
    def listar_livros(self):
        pass

    @abstractmethod
    def obter_livro(self, isbn):
        pass

    @abstractmethod
    def remover_livro(self, isbn):
        pass
