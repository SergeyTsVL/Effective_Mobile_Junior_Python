from django.test import TestCase
from django.contrib.auth.models import User
from ads.models import Ad


class AdTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаём суперпользователя для тестов
        cls.user = User.objects.create_superuser(
            username='TestUser',
            password='Test123456789User',
            email='test@example.com'
        )

        # Создаём тестовое объявление
        cls.ad = Ad.objects.create(
            user=cls.user,
            title="Конь",
            description="Старый но скачет"
        )

    def test_ad_can_speak(self):
        # Проверяем, что объявление создано корректно
        self.assertEqual(self.ad.user.username, 'TestUser')
        self.assertEqual(self.ad.title, "Конь")
        self.assertEqual(self.ad.description, "Старый но скачет")