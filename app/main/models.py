from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Модель договоров
class Contract(models.Model):
    name = models.CharField(
        verbose_name='Наименование договора',
        max_length=200,
        help_text='Обязательное поле. Максимальное количество символов - 200',
        unique=True,
        error_messages={
            'unique': 'Договор с таким названием уже существует',
        }
    )

    class Meta():
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        return self.name


#Модель должностей
class Position(models.Model):
    name = models.CharField(
        verbose_name='Название должности',
        max_length=150,
        help_text='Обязательное поле. Максимальное количество символов - 200'
    )
    contracts = models.ManyToManyField(
        Contract,
        through='PermissionContract',
        verbose_name='Доступные договоры',
        help_text='Выделите доступные договоры, которые будут доступны пользователю'
    )

    class Meta():
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name     


# Промежуточная таблица, связывающая Должности и Договоры
class PermissionContract(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        help_text='Обязательное поле. Выберете из списка существующего пользователя'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        help_text='Обязательное поле. Выберете из списка существующего пользователя'
    )

    class Meta():
        verbose_name = 'Разрешение на договоры'
        verbose_name_plural = 'Разрешения на договоры'
        unique_together = [['contract', 'position']]
    

# Модель для дочерних организаций
class Subsidiary(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='Обязательное поле. Выберете из списка существующего пользователя',
    )
    position =  models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name='Должность пользователя',
        help_text='Обязательное поле. Выберете из списка существующего списка'
    )

    class Meta():
        verbose_name = 'Работник дочерней организации'
        verbose_name_plural = 'Работники дочерней организации'


# Модель для субподрядчиков
class Subcontractor(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='Обязательное поле. Выберете из списка существующего пользователя',
    )
    position =  models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name='Должность пользователя',
        help_text='Обязательное поле. Выберете из списка существующего списка'
    )

    class Meta():
        verbose_name = 'Работник субподрядной организации'
        verbose_name_plural = 'Работники субподрядной организации'
