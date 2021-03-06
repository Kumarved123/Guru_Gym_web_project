from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from django.conf.urls import url

urlpatterns = [
    path('', views.register, name='index'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$',  views.logout_view, name='logout'),
    url(r'^accounts/profile/$', views.profile, name='logout'),
]