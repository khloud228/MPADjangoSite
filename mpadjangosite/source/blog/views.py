from django.conf import settings
from django.views import View
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, get_list_or_404,  HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError

from .models import Post
from .forms import ContactForm
from .services import get_page_obj, get_posts

from typing import Any
from taggit.models import Tag


def page_not_found_view(request, exception):
    return render(request, 'error/404.html', status=404)

class MainView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('search')
        posts = get_posts(query=query)
        page_number = request.GET.get('page')
        page_obj = get_page_obj(posts, 6, page_number)
        template_name = 'blog/main.html'
        context = {
            "page_obj": page_obj
        }
        return render(request, template_name, context)


class DetailView(View):
    def get(self, request, slug, *args, **kwargs):
        template_name = "blog/detail.html"
        post = get_object_or_404(Post, slug=slug)
        context = {"post": post}
        return render(request, template_name, context)


class ContactsView(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.template_name = 'blog/contacts.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(instance=request.user, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            # email = form.cleaned_data['email']    Сейчас имэйл откуда отправляют поставлен на дефолтный
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject=f'От {name} | {subject}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    message=message,
                    recipient_list=['khloud228@yandex.ru']
                )
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок!')
            return HttpResponseRedirect('success')
        return render(request, self.template_name)


def sendSuccess(request):
    template_name = 'blog/thanks.html'
    return render(request, template_name)


class TagView(View):
    def get(self, request, tag_slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = get_posts(tag_slug=tag_slug)
        page_number = request.GET.get('page')
        page_obj = get_page_obj(posts, 6, page_number)
        common_tags = Post.tag.most_common()
        template_name = 'blog/tag.html'
        context = {
            'page_obj': page_obj,
            'title': f'#Тэг {tag.name}',
            'common_tags': common_tags,
            'tag_slug': tag_slug
        }
        return render(request, template_name, context)


class SearchView(View):
    def get(self, request, tag_slug=None, *args, **kwargs):
        query = request.GET.get('search')
        posts = get_posts(query=query, tag_slug=tag_slug)
        page_number = request.GET.get('page')
        page_obj = get_page_obj(posts, 6, page_number)
        template_name = 'blog/search.html'
        context={
            'page_obj': page_obj,
            'tag_slug': tag_slug
        }
        return render(request, template_name, context)
