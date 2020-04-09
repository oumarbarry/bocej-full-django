from django.db import models

class Center(models.Model):
    c_title = models.CharField('Nom du centre', max_length=200, null=True)
    c_address = models.CharField('Addresse', max_length=200, null=True)
    c_email = models.EmailField('Email', max_length=200, null=True)
    c_phone = models.CharField('Telephone', max_length=15, null=True)
    c_state = models.CharField('Etat', max_length=200, null=True)

    def __str__(self):
        return self.c_name
    class Meta:
        verbose_name_plural = 'CENTERS'