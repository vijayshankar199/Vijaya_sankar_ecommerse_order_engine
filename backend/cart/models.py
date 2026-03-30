from django.db import models
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user_id=models.CharField(max_length=50)

class Cartitem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()