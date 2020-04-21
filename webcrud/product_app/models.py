from django.db import models
import re
import os
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles import finders

class TblProduct(models.Model):
    product_id = models.CharField(primary_key=True, blank=True, null=False, max_length=2000)
    product_name = models.CharField(max_length=2000)
    available = models.IntegerField(blank=True, null=True)
    image_name = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=2000)
    category_id = models.IntegerField(blank=True, null=True)

    @property
    def get_image_name(self):                        
        my_image_name = self.product_id + ".jpg"
        my_image_name = re.sub(r'\s+', '', my_image_name)
        my_image_name = re.sub(r'/', '-', my_image_name)        
        if finders.find('images/'+my_image_name) is None:            
            return 'noimage.jpg'
        return my_image_name
    
    class Meta:
        managed = False
        db_table = 'tblProducts'
