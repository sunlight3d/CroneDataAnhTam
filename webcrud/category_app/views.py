from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import QueryDict
from django.http import HttpResponse
import datetime

from .models import TblCategory


class CategoriesView(TemplateView):
    http_method_names = ['get', 'post', 'put', 'delete']
    template_name = 'category_app/index.html'

    def get(self, request, *args, **kwargs):
        categories = TblCategory.objects.filter(category_name__contains='')
        return render(request, self.template_name, {'categories': categories})

    def post(self, request, *args, **kwargs):
        new_category = TblCategory(int(request.POST['category_id']), request.POST['category_name'])
        new_category.save()
        return self.get(request, self.template_name)

    def delete(self, request, *args, **kwargs):
        params = QueryDict(request.body)
        import pdb
        pdb.set_trace()
        return self.get(request, self.template_name)
