from django.db import models
from django.contrib.auth.models import AbstractBaseUser


"""class UsuarioLogin(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombre = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellido = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200)
    usuario_activo = models.BooleanField(default=False)
    usuario_administrador = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre},{self.apellido}'

    def has_perm(self,perm,ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador"""
