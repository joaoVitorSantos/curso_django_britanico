from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='account/logout.html')),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit', views.edit_profile, name="edit_profile"),
    path('change-password/', views.change_password, name="change_password"),
    path('reset-password/', PasswordResetView, name="reset_password"),
    path('reset-password/done/', PasswordResetDoneView, name="reset_password_done")
]