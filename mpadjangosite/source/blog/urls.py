from django.urls import path
from .views import (
    MainView,
    DetailView,
    ContactsView,
    sendSuccess
)

app_name =  'blog'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/success/', sendSuccess),
    path('<slug:slug>/', DetailView.as_view(), name='detail'),
]
