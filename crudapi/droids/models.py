from django.db import models


class Droid(models.Model):
    descricao = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    contato = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    anunciante = models.ForeignKey('auth.User', related_name='Droids', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']


