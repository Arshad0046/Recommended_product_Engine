from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_image = models.URLField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
