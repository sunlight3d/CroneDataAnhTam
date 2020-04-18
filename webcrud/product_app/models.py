from django.db import models


class TblProduct(models.Model):
    product_id = models.CharField(primary_key=True, blank=True, null=False, max_length=2000)
    product_name = models.CharField(max_length=2000)
    available = models.IntegerField(blank=True, null=True)
    image_name = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=2000)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblProducts'
