# python-rest-api-swagger
Projeto REST usando a entidade contatos

Aplicativo com as funcionalidades CRUD implementadas com Python 3.7, usando Flask e Swagger.

## Pré-requisitos

* Python >= 3.x
* Virtualenv >= 16.1.0
* Virtualenvwrapper >= 4.8.3.dev4

## Preparando o projeto

Tendo o Virtualenvwrapper instalado executar o seguinte comando para armazenar as dependências:
```
mkvirtualenv -p python3 python_rest_api_swagger
```

Então dentro do diretório da aplicação executar:
```
pip install -r requirements.txt
```

Para rodar os testes unitários e cobertura:
```
py.test tests --junitxml=./test_report.xml --cov=./tests --cov-report=html
```

Para iniciar a API usar comando abaixo:
```
python index.py
```