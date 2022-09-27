## Link Manager API
Api de gerenciamento de links

## Tecnologias
- Python
- Flask
- Sqlite3

## Como usar

### Local
1 - Crie um ambiente virtual. Exemplo: `virtualenv venv`

2 - Inicie o ambiente virtual. Exemplo: `source venv/bin/activate`

3 - Instale as dependências com o comando:
```
pip3 install -r requirements.txt
```
4 - A API estará exposta no host escolhido pelo flask, por padrão, é o host https://127.0.0.1:5000

### Preview Online

A API foi publicada no heroku e tem uma aplicação web simples de utilização da API de gerenciamento de links.
- Heroku host: https://api-link-manager.herokuapp.com/
- Webapp: https://carloseduardobertucio.github.io/link-manager-webapp/

## Documentação

### Rotas
#### `/link/readall`: 
- Método: GET

- Parametros: nenhum

- Retorno: JSON com lista de todos os links, 200

- Erro: Retorna 400 caso tenha um erro no processo get_all_links()

#### `/link/save`: 
- Método: POST

- Parametros: querystring com os parâmetros `label: str, url: str`

- Retorno: Mensagem de sucesso, 200

- Erro: Retorna 400 caso tenha um erro no processo create_link() ou os parâmetros `label` e `url` estejam vazios ou não existam na request

#### `/link/edit`: 
- Método: POST

- Parametros: querystring com os parâmetros `label: str, url: str, id: int`

- Retorno: Mensagem de sucesso, 200

- Erro: Retorna 400 caso tenha um erro no processo edit_link(), caso o parâmetro `id` seja vazio ou não exista na request e caso os parâmetros `url` e `label` estejam ambos vazios.

#### `/link/delete`: 
- Método: POST

- Parametros: querystring com o parâmetro `id: int`

- Retorno: Mensagem de sucesso, 200

- Erro: Retorna 400 caso tenha um erro no processo delete_link() ou caso o parâmetro `id` seja vazio ou não exista na request
