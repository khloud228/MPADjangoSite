from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Post


# def main(request):
#     posts = Post.objects.all()
#     template_name = "blog/main.html"
#     print(posts[0].images.all().count())
#     context = {"posts": posts}
#     return render(request, template_name, context)


class MainView(View):
    def get(self, request, *args, **kwargs):
        template_name = "blog/main.html"
        posts = Post.objects.filter(published=True)
        context = {"posts": posts}
        return render(request, template_name, context)


class DetailView(View):
    def get(self, request, slug, *args, **kwargs):
        template_name = "blog/detail.html"
        post = get_object_or_404(Post, slug=slug)
        context = {"post": post}
        return render(request, template_name, context)
