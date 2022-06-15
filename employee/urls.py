# from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [

    # path('index', views.index),
    # path('login', views.login),
    # path('reg', views.registration)
    path('index', views.IndexView.as_view()),
    path('login', views.LoginView.as_view()),
    path("reg", views.RegView.as_view()),
]