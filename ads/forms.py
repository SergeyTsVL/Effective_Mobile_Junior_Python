from django import forms
from .models import Ad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AdForm(forms.ModelForm):
    """
    Этот блок кода определяет метаданные (Meta) для модели Ad. model = Ad: Это указывает Django,
    что эти метаданные относятся к модели Advertisement. Это не обязательно нужно явно указывать, так как Django обычно
    может определить это автоматически.
    fields = ['id', 'user', 'title', ...] Это список полей модели, которые будут отображаться в форме модели. В
    данном случае это заголовок объявления (title), пользователь (user), ...
    """
    class Meta:
        model = Ad
        fields = ['id', 'user', 'title', 'description', 'image_url', 'category', 'status', 'created_at']

class ExchangeProposalForm(forms.ModelForm):
    """
    Этот блок кода определяет метаданные (Meta) для модели Ad. model = Ad: Это указывает Django,
    что эти метаданные относятся к модели Advertisement. Это не обязательно нужно явно указывать, так как Django обычно
    может определить это автоматически.
    fields = ['id', 'user', 'title', ...] Это список полей модели, которые будут отображаться в форме модели. В
    данном случае это заголовок объявления (title), пользователь (user), ...
    """
    class Meta:
        model = Ad
        fields = ['id', 'ad_sender', 'ad_receiver', 'comment', 'status', 'created_at']

class SignUpForm(UserCreationForm):
    """
    Этот класс SignUpForm представляет собой кастомную форму регистрации пользователя, которая расширяет стандартную
    форму UserCreationForm. UserCreationForm - Это стандартная форма Django для регистрации новых пользователей.
    SignUpForm расширяет UserCreationForm, что позволяет переопределить некоторые аспекты формы, если необходимо.
    Использование Meta позволяет задать метаданные формы без необходимости создавать отдельный экземпляр класса.
    Поле fields определяет, какие поля формы будут отображаться. В данном случае это базовые поля для регистрации
    пользователя.
    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)