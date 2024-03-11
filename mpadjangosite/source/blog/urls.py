from django.urls import path
from .views import (
    MainView,
    DetailView,
    ContactsView,
    sendSuccess,
    TagView,
    SearchView,
)

app_name =  'blog'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('search/', SearchView.as_view(), name='search'),
    path('tag/<slug:tag_slug>/search/', SearchView.as_view(), name='search_with_tag'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/success/', sendSuccess),
    path('tag/<slug:tag_slug>/', TagView.as_view(), name='tag'),
    path('<slug:slug>/', DetailView.as_view(), name='detail'),
]
