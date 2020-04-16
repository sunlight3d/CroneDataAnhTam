from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
import datetime

from .models import TblCategory

class CategoriesView(TemplateView):
    template_name = 'category_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = TblCategory.objects.filter(category_name__contains = '')
        return context
