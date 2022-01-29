from unicodedata import category
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField( max_length=100)
    slug = models.SlugField(max_length=200, blank=True)

    #Overriding the save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class QuantityVarient(models.Model):
    variant_name = models.CharField(max_length=100)

    def __str__(self): 
        return self.variant_name

class ColorVarient(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField( max_length=100)
    
    def __str__(self): 
        return self.color_name

class SizeVarient(models.Model):
    size_name= models.CharField(max_length=100)    
    
    def __str__(self): 
        return self.size_name




class Product(models.Model):
    product_name = models.CharField( max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/products')
    price = models.CharField(max_length=20) 
    description = models.TextField()
    stock = models.IntegerField(default=100)

    quantity_type = models.ForeignKey(QuantityVarient, on_delete=models.PROTECT, null=True, blank=True)
    color_type = models.ForeignKey(ColorVarient, on_delete=models.PROTECT, null=True, blank=True)
    size_type = models.ForeignKey(SizeVarient, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.product_name  


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="static/products")      