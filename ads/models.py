from django.db import models
from django.contrib.auth.models import User


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
    image_url = models.ImageField(upload_to='images/', blank=True, null=True)
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

