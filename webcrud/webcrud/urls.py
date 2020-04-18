"""webcrud URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$/', include('category_app.urls')),
    url('^categories/', include('category_app.urls')),
    url('^products/', include('product_app.urls')),
]
