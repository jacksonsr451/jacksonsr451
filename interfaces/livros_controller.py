from flask import Blueprint, jsonify, request

from adapters.livro_repository_impl import LivroRepositoryImpl
from core.use_cases.livro_dto import LivroDTO
from core.use_cases.livro_use_cases import LivroUseCases

livros_bp = Blueprint('livros', __name__)

livro_use_cases = LivroUseCases(LivroRepositoryImpl())


@livros_bp.route('/livros', methods=['GET'])
def get_livros():
    livros = livro_use_cases.listar_livros()
    return jsonify({'livros': [livro.__dict__ for livro in livros]})


@livros_bp.route('/livros/<string:isbn>', methods=['GET'])
def get_livro(isbn):
    livro = livro_use_cases.obter_livro(isbn)
    if livro is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404
    return jsonify({'livro': livro.__dict__})


@livros_bp.route('/livros', methods=['POST'])
def add_livro():
    livro_data = request.json
    livro_dto = LivroDTO(
        isbn=livro_data['isbn'],
        titulo=livro_data['titulo'],
        autor=livro_data['autor'],
        ano=livro_data['ano'],
    )
    livro = livro_use_cases.adicionar_livro(livro_dto)
    return jsonify(
        {'mensagem': 'Livro adicionado com sucesso', 'livro': livro.__dict__}
    )


@livros_bp.route('/livros/<string:isbn>', methods=['DELETE'])
def delete_livro(isbn):
    livro = livro_use_cases.remover_livro(isbn)
    if livro is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404
    return jsonify(
        {'mensagem': 'Livro removido com sucesso', 'livro': livro.__dict__}
    )
