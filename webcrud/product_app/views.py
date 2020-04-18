from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import QueryDict
from django.http import HttpResponse
import datetime

from .models import TblProduct


class ProductsView(TemplateView):
    http_method_names = ['get', 'post', 'put', 'delete']
    template_name = 'product_app/index.html'

    def get(self, request, *args, **kwargs):
        categories = TblProduct.objects.filter(product_name__contains='').order_by('product_name')
        import pdb
        pdb.set_trace()
        return render(request, self.template_name, {'categories': categories})

    def post(self, request, *args, **kwargs):
        new_product = TblProduct(int(request.POST['product_id']), request.POST['product_name'])
        new_product.save()
        return self.get(request, self.template_name)

    def delete(self, request, *args, **kwargs):
        params = QueryDict(request.body)
        # import pdb
        # pdb.set_trace()
        product_id = int(params.get('product_id'))
        product_name = params.get('product_name')
        selected_product = TblProduct.objects.get(product_id=product_id)
        selected_product.delete()
        categories = TblProduct.objects.filter(product_name__contains='').order_by('product_name')
        return render(request, self.template_name, {'categories': categories})

    def put(self, request, *args, **kwargs):
        params = QueryDict(request.body)
        product_id = params.get('product_id')
        product_name = params.get('product_name')
        selected_product = TblProduct.objects.get(product_id=product_id)
        selected_product.product_name = product_name
        # import pdb
        # pdb.set_trace()
        return self.get(request, self.template_name)
