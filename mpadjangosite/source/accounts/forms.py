from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)


class SignUpForm(forms.ModelForm):
    retry_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес электронной почты'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }
    
    def clean_retry_password(self):
        password, retry_password = self.cleaned_data['password'], self.cleaned_data['retry_password']
        if password and retry_password and password != retry_password:
            raise forms.ValidationError('Пароли не совпадают!')

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Этот адрес электронной почты уже используется!')
        return str(self.cleaned_data['email'][0]).lower() + self.cleaned_data['email'][1:]


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }))


class PasswordChangeFormCustom(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Старый пароль'
            }))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Новый пароль'
            }))
    new_password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }))   


class PasswordResetFormCustom(PasswordResetForm):
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Адрес электронной почты'
    }))


class SetPasswordFormCustom(SetPasswordForm):
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Новый пароль'
    }))
    new_password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль'
    }))
