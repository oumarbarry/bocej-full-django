from django.db import models
from center.models import Center
from django.contrib.auth.models import User

class UserBA(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Utilisateur', ) #username, email, password, activate, 
    full_name = models.CharField('Nom complet', max_length=250, null=True)
    phone = models.CharField('Telephone', max_length=15, null=True)
    type = models.CharField('Type (bocej/aguipe)', max_length=250, null=True) #bocej, aguipe
    role = models.CharField('Role (admin/simple_user)', max_length=250, null=True) #admin or simple_user
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'USERS of BOCEJ-AGUIPE'

class UserCenter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Utilisateur', ) #username, email, password, activate, 
    full_name = models.CharField('Nom complet', max_length=250, null=True)
    phone = models.CharField('Telephone', max_length=15, null=True)
    type = models.CharField('Type (center)', max_length=250, default='center', null=True) #center
    role = models.CharField('Role (admin/simple_user)', max_length=250, null=True) #admin or simple_user
    center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, verbose_name='Son Centre')
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'USERS of CENTERS'