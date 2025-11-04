from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False) #se no banco a tabela for criada, esse campo será VARCHAR(200) e não poderá ser nulo ou vazio.
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) #data e hora de criação do todo, será preenchido automaticamente quando o objeto for criado.
    deadline = models.DateTimeField(null=False, blank=False) #data e hora limite para completar o todo
    finished_at = models.DateTimeField(null=True, blank=True) #data e hora em que o todo foi finalizado, pode ser nulo ou vazio se o todo não foi finalizado ainda.