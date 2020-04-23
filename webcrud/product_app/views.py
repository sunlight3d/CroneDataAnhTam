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
        if request.POST['type'] == 'insert':            
            new_product = TblProduct(product_id = request.POST['product_id'], \
                                     product_name = request.POST['product_name'],\
                                     description = request.POST['description'],\
                                     available = request.POST['product_available'],\
                                     image_name = image_name,\
                                     category_id = int(request.GET['category_id']))
            new_product.save()
        elif request.POST['type'] == 'update':            
            selected_product = TblProduct.objects.get(product_id=request.POST['product_id'])            
            if selected_product is not None:
                selected_product.product_name = request.POST['product_name']        
                selected_product.description = request.POST['description']        
                selected_product.available = request.POST['product_available']  
                if image_name.strip() != '' and selected_product.image_name.strip() != image_name.strip():                
                    image_path = os.path.join(os.path.abspath('.'), 'static/images/' + selected_product.image_name)                      
                    if os.path.exists(image_path):
                        os.remove(image_path)
                    selected_product.image_name = image_name       
                selected_product.save()
        return self.get(request, self.template_name)

    def delete(self, request, *args, **kwargs):
        params = QueryDict(request.body)        
        product_id = int(params.get('product_id'))
        product_name = params.get('product_name')
        selected_product = TblProduct.objects.get(product_id=product_id)                
        image_name = str(selected_product.product_id) + ".jpg"        
        if image_name != '':
            image_path = os.path.join(os.path.abspath('.'), 'static/images/' + image_name)  
            if os.path.exists(image_path):
                os.remove(image_path)
        selected_product.delete()
        return self.get(request, args, kwargs)    
