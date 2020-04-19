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
        category_id = request.GET['category_id']
        products = TblProduct.objects.filter(product_name__contains='')\
                    .filter(category_id=category_id)\
                    .order_by('product_name')        
        return render(request, self.template_name, {'products': products})

    def post(self, request, *args, **kwargs):        
        image_name = ''
        import pdb
        pdb.set_trace()        
        if request.method == 'POST' and 'product_image_file' in request.FILES:
            image_file = request.FILES['product_image_file']
            fs = FileSystemStorage()
            image_name = fs.save('static/images/', image_file)
            uploaded_file_url = fs.url(image_name)            
        new_product = TblProduct(product_id = int(request.POST['product_id']), \
                                 product_name = request.POST['product_name'],
                                 available = request.POST['product_available'],
                                 image_name = image_name,
                                 )
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
        products = TblProduct.objects.filter(product_name__contains='').order_by('product_name')
        return render(request, self.template_name, {'products': products})

    def put(self, request, *args, **kwargs):
        params = QueryDict(request.body)
        product_id = params.get('product_id')
        product_name = params.get('product_name')
        selected_product = TblProduct.objects.get(product_id=product_id)
        selected_product.product_name = product_name
        # import pdb
        # pdb.set_trace()
        return self.get(request, self.template_name)
