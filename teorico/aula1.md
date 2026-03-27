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

Quando há uma conexção com o BD podemos fazer um makemigrations, scripts criados (códigos excecutados no próprio banco para atualizar o banco) com base nos modelos criados no projeto, e em seguida o migrations para salvar, aplicar, as alterações

```python manage.py makemigrations```

```python manage.py migrate```

## painel administrativo

```python manage.py createsuperuser``` 
(lembrando de fazer o makemigrations antes para que possa criar as tabelas padrão do django)

# Estrutura

````
Requisição pelo usuário --> urls.py --> views.py --> models.py (BD) --> templates --> resposta
````

*para utilizar essas estruturas precisamos de um app*

``python manage.py startapp nome``

## urls.py

Para uma nova url:

Importamos views -> ``from . import views``

Adicionamos um caminho-

```path('/', views.index, name='index')```

- ``'/'`` -> indica o caminho, a url no navegador

- ``views.index`` -> indica a função na views.py

- ``name='index'`` -> indica o nome da url


**é importante definir em settings.py em DIRS= {BASE_DIR / 'templates'}**

## views.py

Para uma nova view:

Importamos -> ``from django.shortcuts import render``

````
def index(request):
    return render(request, 'caminho do arquivo index.html')
````