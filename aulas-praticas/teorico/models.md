# MODELS

Um modelo se expressa através de classes que possuem uma coleção de dados e métodos.
O django trasnforma classes Python em tabelas SQL automaticamente.
Os modelos refletem o que está no Banco

## Aplicação

A classe de python herda de:

```
from django.db import models
```

E a utiliza como:

```
class Aluno(models.Model):
    nome =  models.CharField()

    def __str__(self):
        return self.nome
```

- Para criar as migrações (estabelecem uma ponte entre o models e o BD):

```
python manage.py makemigrations
```

- Para aplicar as modificações ao BD:

```
python manage.py migrate
```