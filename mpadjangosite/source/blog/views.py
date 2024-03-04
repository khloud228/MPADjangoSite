from typing import Any
from django.views import View
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import ContactForm, ContactForm2


class MainView(View):
    def get(self, request, *args, **kwargs):
        template_name = "blog/main.html"
        posts = Post.objects.filter(published=True)
        paginator = Paginator(posts, 6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"page_obj": page_obj}
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
        form = ContactForm2(instance=request.user)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm2(instance=request.user, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject=f'От {name} | {subject}',
                    from_email='khloud228@yandex.ru',
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
