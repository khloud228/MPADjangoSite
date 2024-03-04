from typing import Any
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required
def logoutview(request):    
    logout(request)
    return redirect('blog:main')

class SignUpView(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
