from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text="Необязательное поле. Введите свой номер телефона.")
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username' ,'first_name','last_name', 'country' ,'phone_number', 'password1' , 'password2' ]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Телефон должен состоять только из цифр")
        return phone_number

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = (
            'Пароль должен содержать минимум 8 символов. '
            'Не используйте простые пароли.'
        )

        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].help_text = 'Введите пароль ещё раз для подтверждения.'

        # Можно также изменить другие поля
        self.fields['email'].label = 'Электронная почта'
        self.fields['username'].label = 'Имя пользователя'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['country'].label = 'Страна'
        self.fields['phone_number'].label = 'Номер телефона'

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите почту'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ваш логин'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ваше имя'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ваша фамилия'
        })
        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль'
        })

class CustomAuthenticationForm(AuthenticationForm):
    """Стилизованная форма авторизации"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Электронная почта'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email',
            'autofocus': True,
        })

        self.fields['password'].label = 'Пароль'
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль',
        })