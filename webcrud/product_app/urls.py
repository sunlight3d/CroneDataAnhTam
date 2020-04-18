from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
app_name = "product_app"
urlpatterns = [
    # url(r'^$', views.index, name='index')
    url(r'^$', views.ProductsView.as_view())
]