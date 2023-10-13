from django.db import models

class user(models.Model):
    id_users = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()