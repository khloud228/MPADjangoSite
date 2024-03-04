from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .forms import (
    SignInForm,
    PasswordChangeFormCustom,
    PasswordResetFormCustom,
    SetPasswordFormCustom
)
from .views import (
    SignUpView,
    dashboard,
    logoutview
)




urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('sign-in/', LoginView.as_view(
            template_name = 'accounts/signin.html',
            form_class=SignInForm
        ),
        name='signin'
    ),
    path('dashboard/', dashboard, name='dashboard'),
    path('sign-out/', logoutview, name='signout'),
    path('password-change/', PasswordChangeView.as_view(
            template_name='accounts/password_change_form.html',
            form_class=PasswordChangeFormCustom
        ),
        name='password_change'
    ),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        form_class=PasswordResetFormCustom
    ), name='password_reset'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        form_class=SetPasswordFormCustom
    ), name='password_reset_confirm'),
    path('password-reset-done/', PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
