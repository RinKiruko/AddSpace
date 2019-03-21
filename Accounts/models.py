from django.db import models
from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
	email = models.EmailField(null=True, verbose_name='E-mail', max_length=255, unique=True)
	password = models.CharField(null=True, verbose_name='Пароль', max_length=128)
	FirstName = models.CharField(null=True,verbose_name='Имя', max_length=50)
	LastName = models.CharField(null=True,verbose_name='Фамилия', max_length=50)
	
	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
	
	def __str__(self):
		try:
			return self.FirstName + ' ' + self.LastName
		except TypeError:
			return self.email