from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
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


class SearchForm(forms.Form):
    search = forms.CharField(label='Поисковый запрос', widget=forms.TextInput(attrs={
        'class': 'form-control me-2',
        'name': 'query',
        'aria-label': 'Search',
        'type': 'search',
        'placeholder': 'Поиск'
    }))
