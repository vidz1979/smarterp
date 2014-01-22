from django.db import models

class Pais(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'País'
        verbose_name_plural = u'Países'

    def estado_relation(self):
        return self.estado_set.filter(is_present=True)
