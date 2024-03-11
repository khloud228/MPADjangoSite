from django.core.paginator import Paginator
from django.core.paginator import Page
from django.shortcuts import get_list_or_404
from django.db.models import Q

from .models import Post

def get_page_obj(posts:Post, count_page_items:int, page_number:int) -> Page:
    paginator = Paginator(posts, count_page_items)
    return paginator.get_page(page_number)


def get_posts(query=None, tag_slug=None) -> Post:
    posts = Post.objects.filter(published=True)
    if tag_slug:
        posts = posts.filter(tag__slug=tag_slug)
    if query:
        posts.filter(Q(title__icontains=query) | Q(text__icontains=query))
    return posts