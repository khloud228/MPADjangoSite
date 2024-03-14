from django import template
from django.http import HttpRequest
from django.db.models import Count
from django.urls import reverse
from django.shortcuts import redirect

from source.blog.forms import SearchForm, CommentForm
from source.blog.models import Post
from source.blog.services import get_posts


register = template.Library()


@register.inclusion_tag('block/navbar.html')
def show_navbar_with_search_form(request:HttpRequest, tag_slug=None) -> dict:
    if 'search' in request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()
        if 'tag' in request.get_full_path():
            form.fields['search'].widget.attrs['placeholder'] = 'Поиск по тэгам'
        else:
            form.fields['search'].widget.attrs['placeholder'] = 'Глобальный поиск'
    context = {
        'form': form,
        'request': request,
        'tag_slug': tag_slug
    }
    return context


@register.inclusion_tag('block/aside.html')
def show_aside(post:Post) -> dict:
    common_tags = post.tag.most_common()
    post_tags_ids = post.tag.values_list('id', flat=True)
    related_posts = Post.objects.filter(published=True, tag__in=post_tags_ids).exclude(id=post.id)
    related_posts = related_posts.annotate(same_tag=Count('tag')).order_by('-same_tag',)[:4]
    context = {
        'common_tags': common_tags,
        'related_posts': related_posts
    }
    return context

