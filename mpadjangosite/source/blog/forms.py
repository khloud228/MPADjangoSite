from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваше имя'
    }))
    # email = forms.EmailField(max_length=100, label='Ваш адрес электронной почты', widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Ваш адрес электронной почты'
    # }))
    subject = forms.CharField(max_length=200, label='Тема', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Тема'
    }))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Сообщение',
        'rows': 2
    }))


class ContactForm2(forms.ModelForm):
    subject = forms.CharField(max_length=200, label='Тема', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Тема'
    }))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Сообщение',
        'rows': 2
    }))
    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            })
        }
