from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import (LogoutView, LoginView, PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.urls import path
from . import views
from account import views as auth_views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', auth_views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('delete/<int:id>/', views.delete),
]