from django.urls import path
from .views import (
    MainView,
    DetailView
)

app_name =  'blog'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('detail/<slug:slug>/', DetailView.as_view(), name='detail')
]
