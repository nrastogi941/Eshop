from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200,default=" ")
    image=models.ImageField(upload_to='Uploads/products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
        
    @staticmethod
    def get_all_products_by_listid(list_ids):
        return Product.objects.filter(id__in=list_ids)