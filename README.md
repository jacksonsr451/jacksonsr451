# Biblioteca

Biblioteca é um sistema de gerenciamento de livros que oferece uma API para adicionar, listar, obter e remover livros da biblioteca. Ele foi desenvolvido em Python, seguindo os princípios da Clean Architecture.

## Visão geral do projeto

Este projeto tem como objetivo fornecer uma solução simples e flexível para o gerenciamento de uma biblioteca de livros. Ele segue a arquitetura Clean Architecture, o que permite uma separação clara entre as diferentes camadas do sistema.

## Funcionalidades principais

- Adicionar um livro à biblioteca, fornecendo as informações do livro, como ISBN, título, autor e ano de publicação.
- Listar todos os livros da biblioteca.
- Obter informações detalhadas de um livro específico com base no ISBN.
- Remover um livro da biblioteca com base no ISBN.

## Estrutura do projeto

O projeto está organizado da seguinte forma:

- `app.py`: Ponto de entrada da aplicação.
- `core/`: Contém as entidades de domínio, repositórios e casos de uso relacionados aos livros.
- `adapters/`: Contém implementações de adaptadores, como o repositório de livros.
- `interfaces/`: Contém a interface de controle da API.
- `tests/`: Contém os testes unitários para os casos de uso.
- `docs/`: Contém a documentação do projeto.

## Pré-requisitos

- Python 3.x
- Dependências listadas no arquivo `requirements.txt`

## Configuração do ambiente

1. Clone este repositório em sua máquina local.
2. Crie um ambiente virtual para o projeto:
    ```
    python -m venv venv
    ```
3. Ative o ambiente virtual:
    - Windows:
        ```
        venv\Scripts\activate
        ```
    - Unix/Linux:
        ```
        source venv/bin/activate
        ```
4. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```

## Executando o projeto

1. Certifique-se de estar no ambiente virtual (passo 3 da seção "Configuração do ambiente").
2. Execute o arquivo `app.py`:
    ```
    python app.py
    ```
3. O servidor será iniciado e estará pronto para receber as requisições para a API.

## Testando o projeto

1. Certifique-se de estar no ambiente virtual (passo 3 da seção "Configuração do ambiente").
2. Execute os testes unitários:
    ```
    python -m unittest discover -s tests
    ```
3. Os testes serão executados e você verá o resultado no console.

## Documentação

A documentação do projeto está disponível no diretório `docs/`. Consulte os arquivos Markdown para obter informações detalhadas sobre a estrutura, os endpoints da API, os parâmetros e as respostas esperadas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma "issue" relatando bugs, sugerindo melhorias ou enviando "pull requests" para adicionar novos recursos.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

