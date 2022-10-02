from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, verbose_name='Id Usuario')
    username = models.CharField(max_length = 15, unique=True, verbose_name= 'Usuario')
    password = models.CharField(max_length = 256, verbose_name= 'Contraseña')
    name = models.CharField(max_length = 30, verbose_name= 'Nombre propietario')
    email = models.EmailField(max_length = 100, verbose_name= 'Correo')
    phone_number = models.CharField(max_length = 200, verbose_name='Teléfono')
    city_owner = models.CharField(max_length=200, verbose_name='Ciudad del inmueble')

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'