## Ambiente virtual

Ambiente de trablaho isolado para instalações e melhor organização para desempenho do projeto --> usualmente denominado por venv onde ficará somente as bibliotecas para a excecução

Framework --> conjunto de ferramentas que utilizam bibliotecas

O pillow é uma biblioteca de gerenciamento de imagens

- Como instalar?
 
```python -m venv venv```

- Para ativar

```venv\scripts\activate``` 

- Para instalar dependências

```pip install django```

- Para criar um requirements.txt

```pip freeze > requirements.txt```

```pip install -r requirements.txt```

Lembrando que para vizualizar as dependências podemos pazer um ```pip list```

## Criando um projeto

```django-admin startproject loja .```  
(para criar dentro da pasta do meu repositório)

```python manage.py runserver```
(para rodar o projeto)

## comandos essenciais

Quando há uma conexção com o BD podemos fazer um makemigrations, scripts criados (códigos excecutados no próprio banco) com base nos modelos criados no projeto, e em seguida o migrations para atualizar o BD

```python manage.py makemigrations```

```python manage.py migrate```

## painel administrativo

```python manage.py createsuperuser``` 
(lembrando de fazer o makemigrations antes para que possa criar as tabelas padrão do django)