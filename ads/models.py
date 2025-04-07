from datetime import timezone, datetime

from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    """
    Этот класс определяет модель для хранения информации об объявлениях в базе данных.
    """
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_name')
    title = models.TextField()
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.TextField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name = 'Объявление'
    #     verbose_name_plural = 'Объявления'
    #     ordering = ['-created_at']
    #
    # def __str__(self):
    #     return f'{self.title} (ID: {self.id})'


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

    # id = models.AutoField(primary_key=True)
    ad_sender = models.ForeignKey(
        Ad,
        related_name='sent_proposals',
        on_delete=models.CASCADE,
        verbose_name='Объявление отправителя'
    )
    ad_receiver = models.ForeignKey(
        Ad,
        related_name='received_proposals',
        on_delete=models.CASCADE,
        verbose_name='Объявление получателя'
    )
    comment = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(
        default=datetime.now(timezone.utc),
        verbose_name='Дата создания'
    )
    # class Meta:
    #     verbose_name = 'Предложение обмена'
    #     verbose_name_plural = 'Предложения обмена'
    #     ordering = ['-created_at']

    def __str__(self):
        return f'Предложение обмена: {self.ad_sender.title} <-> {self.ad_receiver.title}'

    # def clean(self):
    #     if self.ad_sender == self.ad_receiver:
    #         raise ValidationError('Объявления отправителя и получателя не могут быть одинаковыми')
    #     if ExchangeProposal.objects.filter(
    #         ad_sender=self.ad_sender,
    #         ad_receiver=self.ad_receiver,
    #         status='pending'
    #     ).exists():
    #         raise ValidationError('Предложение обмена уже существует')