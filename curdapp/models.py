from django.db import models

# Create your models here.
class Product(models.Model):
    prd_name = models.CharField(max_length=25)
    prd_price = models.IntegerField()
    prd_qnty = models.IntegerField()
    prd_desc = models.CharField(max_length=25)
    prd_mfg_date = models.DateField()
