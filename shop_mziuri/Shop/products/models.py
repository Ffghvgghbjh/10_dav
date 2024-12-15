from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField() 
    create_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    stock_qty = models.IntegerField(default=0)
