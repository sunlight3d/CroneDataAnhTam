from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import QueryDict
from django.http import HttpResponse
import datetime
import urllib.request
import os

from .models import TblProduct


class ProductsView(TemplateView):
    http_method_names = ['get', 'post', 'put', 'delete']
    template_name = 'product_app/index.html'    

    def get(self, request, *args, **kwargs):                    
        products = TblProduct.objects.filter(product_name__contains='')\
                    .filter(category_id=request.GET['category_id'])\
                    .order_by('product_name')        
        return render(request, self.template_name, {'products': products})

    def handle_uploaded_file(self, image_file, image_path):                
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
            destination.close()

    def post(self, request, *args, **kwargs):        
        image_name = ''        
        if request.method == 'POST' and 'product_image_file' in request.FILES:
            image_file = request.FILES['product_image_file']              
            # image_name = str(request.POST['product_id']) + "." + image_file.name.split('.')[-1]              
            image_name = str(request.POST['product_id']) + ".jpg"
            image_path = os.path.join(os.path.abspath('.'), 'static/images/' + image_name)                
            self.handle_uploaded_file(image_file, image_path)            
        new_product = TblProduct(product_id = request.POST['product_id'], \
                                 product_name = request.POST['product_name'],\
                                 available = request.POST['product_available'],\
                                 image_name = image_name,\
                                 category_id = int(request.GET['category_id']))
        new_product.save()
        return self.get(request, self.template_name)

    def delete(self, request, *args, **kwargs):
        params = QueryDict(request.body)        
        product_id = int(params.get('product_id'))
        product_name = params.get('product_name')
        selected_product = TblProduct.objects.get(product_id=product_id)                
        image_name = str(selected_product.product_id) + ".jpg"
        import pdb
        pdb.set_trace()
        if image_name != '':
            image_path = os.path.join(os.path.abspath('.'), 'static/images/' + image_name)  
            if os.path.exists(image_path):
                os.remove(image_path)
        selected_product.delete()
        return self.get(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        params = QueryDict(request.body)
        import pdb
        pdb.set_trace()
        product_id = params.get('product_id')
        product_name = params.get('product_name')
        selected_product = TblProduct.objects.get(product_id=product_id)
        selected_product.product_name = product_name        
        return self.get(request, self.template_name)
