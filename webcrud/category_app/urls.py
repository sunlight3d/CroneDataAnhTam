from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
app_name = "category_app"
urlpatterns = [
    url(r'', views.index, name='index')
]