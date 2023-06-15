# Documentação da Biblioteca

Esta é a documentação da biblioteca.

## Visão geral do projeto

O projeto da biblioteca é um sistema de gerenciamento de livros. Ele fornece uma API para adicionar, listar, obter e remover livros da biblioteca.

## Estrutura do projeto

O projeto segue a estrutura de Clean Architecture, com as seguintes camadas:

- `core`: Contém as entidades de domínio, repositórios e casos de uso relacionados aos livros.
- `adapters`: Contém implementações de adaptadores, como o repositório de livros.
- `interfaces`: Contém a interface de controle da API.
- `tests`: Contém os testes unitários para os casos de uso.

## Endpoints da API

O projeto expõe os seguintes endpoints:

### GET /livros

Retorna todos os livros da biblioteca.

#### Parâmetros de consulta

Nenhum.

#### Resposta

- 200 OK: Retorna uma lista de livros no formato JSON. Cada livro contém as seguintes propriedades:
    - `isbn` (string): O ISBN do livro.
    - `titulo` (string): O título do livro.
    - `autor` (string): O autor do livro.
    - `ano` (integer): O ano de publicação do livro.

Exemplo de resposta:

```json
{
  "livros": [
    {
      "isbn": "1234567890",
      "titulo": "Livro 1",
      "autor": "Autor 1",
      "ano": 2021
    },
    {
      "isbn": "0987654321",
      "titulo": "Livro 2",
      "autor": "Autor 2",
      "ano": 2022
    }
  ]
}
```

## GET /livros/{isbn}

Retorna um livro específico com base no ISBN.

### Parâmetros de rota

* isbn (string, obrigatório): O ISBN do livro.

### Resposta

* 200 OK: Retorna os detalhes do livro no formato JSON. Se o livro não for encontrado, retorna um objeto vazio.
    * isbn (string): O ISBN do livro.
    * titulo (string): O título do livro.
    * autor (string): O autor do livro.
    * ano (integer): O ano de publicação do livro.

### Exemplo de resposta:

```json
{
  "isbn": "1234567890",
  "titulo": "Livro 1",
  "autor": "Autor 1",
  "ano": 2021
}
```

## POST /livros

Adiciona um novo livro à biblioteca.

### Corpo da requisição

Enviar um objeto JSON contendo os seguintes campos:

* isbn (string, obrigatório): O ISBN do livro.
* titulo (string, obrigatório): O título do livro.
* autor (string, obrigatório): O autor do livro.
* ano (integer, obrigatório): O ano de publicação do livro.

Exemplo de corpo da requisição:

```json
{
  "isbn": "1234567890",
  "titulo": "Livro Teste",
  "autor": "Autor Teste",
  "ano": 2023
}
```

### Resposta

* 201 Created: Retorna os detalhes do livro adicionado no formato JSON.

Exemplo de resposta:

```json
{
  "isbn": "1234567890",
  "titulo": "Livro Teste",
  "autor": "Autor Teste",
  "ano": 2023
}
```

## DELETE /livros/{isbn}

Remove um livro da biblioteca com base no ISBN.

### Parâmetros de rota

* isbn (string, obrigatório): O ISBN do livro a ser removido.

### Resposta

* 204 No Content: Indica que o livro foi removido com sucesso.

## Executando o projeto

Para executar o projeto, você pode usar o comando python app.py. Certifique-se de ter as dependências instaladas corretamente.

## Testando o projeto

Para executar os testes unitários, você pode usar o comando `python -m unittest discover -s tests`.