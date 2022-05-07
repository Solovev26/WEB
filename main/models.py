from django.db import models

# Create your models here.

class UserData(models.Model):
  f_name = models.CharField('Имя', max_length=100)
  l_name = models.CharField('Фамилия', max_length=100)
  e_mail = models.CharField('Email', max_length=100)
  password = models.CharField('Пароль', max_length=100)
  
  def __str__(self):
    return self.f_name

  class Meta:
    verbose_name = 'UserData'
    verbose_name_plural = 'UserDates'


class Message(models.Model):
  f_name = models.CharField('Имя', max_length=100)
  e_mail = models.CharField('Email', max_length=100)
  msg = models.TextField('Сообщение', max_length=100)
  
  def __str__(self):
    return self.msg

  class Meta:
    verbose_name = 'Message'
    verbose_name_plural = 'Messages'