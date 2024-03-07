from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    """Модель пользователя платформы"""
    is_customer=models.BooleanField(default=False, verbose_name='Клиент')
    is_cleaner=models.BooleanField(default=False, verbose_name='Клинер')
    
    username=models.CharField(max_length=50, verbose_name='Имя')
    last_name=models.CharField(max_length=100, verbose_name='Фамилия', blank=True, null=True)
    
    phone=models.CharField(max_length=12, verbose_name='Номер телефона', unique=True)
    email=models.CharField(max_length=120, unique=True, verbose_name='Почта', blank=True, null=True)
    
    is_verified=models.BooleanField(default=False, verbose_name='Верифицирован')
    
    avatar=models.ImageField(
        upload_to='media/avatars/%Y/%m/%D/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['png','jpg','webp'])],
        verbose_name='Аватар'
    )
    
    password=models.CharField(verbose_name='Пароль')
    
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=['username', 'password']
    
    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
        unique_together=('phone', 'username')
    
    @property
    def is_authenticated(self):
        return True
    
    def __str__(self):
        return self.username