from datetime import timezone, datetime

from django.db import models
from django.contrib.auth.models import User
from django.template.backends import django


class Ad(models.Model):
    """
    Этот класс определяет модель для хранения информации об объявлениях в базе данных.
    """
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
        ('cancelled', 'Отменено')
    ]
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')   # created_name
    title = models.TextField()
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус',
    )
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        """
        Метод используется для определения строкового представления объекта модели
        :return:
        """
        return str(self.user)

class ExchangeProposal(models.Model):
    """
    Модель предложения обмена
    """
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
        ('cancelled', 'Отменено')
    ]
    ad_sender = models.IntegerField()
    ad_receiver = models.IntegerField()
    comment = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # Используем auto_now_add вместо default
        verbose_name='Дата создания'
    )

    def __str__(self):
        return









# class ExchangeProposal(models.Model):
#     """
#     Модель предложения обмена
#     """
#     STATUS_CHOICES = [
#         ('pending', 'В ожидании'),
#         ('accepted', 'Принято'),
#         ('rejected', 'Отклонено'),
#         ('cancelled', 'Отменено')
#     ]
#
#     # id = models.AutoField(primary_key=True)
#     ad_sender = models.ForeignKey(
#         Ad,
#         related_name='sent_proposals',
#         on_delete=models.CASCADE,
#         verbose_name='Объявление отправителя'
#     )
#     ad_receiver = models.ForeignKey(
#         Ad,
#         related_name='received_proposals',
#         on_delete=models.CASCADE,
#         verbose_name='Объявление получателя'
#     )
#     comment = models.TextField()
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='pending',
#         verbose_name='Статус'
#     )
#
#     created_at = models.DateTimeField(
#         auto_now_add=True,  # Используем auto_now_add вместо default
#         verbose_name='Дата создания'
#     )
#
#     def __str__(self):
#         return f'Предложение обмена: {self.ad_sender.title} <-> {self.ad_receiver.title}'







    #
    # def get_status_display(self):
    #     """Получить отображаемое значение статуса"""
    #     return dict(self.STATUS_CHOICES)[self.status]
    #
    # def can_be_modified(self):
    #     """Проверить, можно ли изменить статус предложения"""
    #     return self.status == 'pending'
    #
    # def accept(self):
    #     """Принять предложение обмена"""
    #     if self.can_be_modified():
    #         self.status = 'accepted'
    #         self.save()
    #         return True
    #     return False
    #
    # def reject(self):
    #     """Отклонить предложение обмена"""
    #     if self.can_be_modified():
    #         self.status = 'rejected'
    #         self.save()
    #         return True
    #     return False
    #
    # def cancel(self):
    #     """Отменить предложение обмена"""
    #     if self.can_be_modified():
    #         self.status = 'cancelled'
    #         self.save()
    #         return True
    #     return False