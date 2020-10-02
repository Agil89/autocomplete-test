from django.db import models

class Objectt(models.Model):

    name = models.CharField('Name',max_length=40)

    class Meta:
        verbose_name = 'Object'
        verbose_name_plural = 'Objects'

    def __str__(self):
        return self.name



    
