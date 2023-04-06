from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Orders

class ProductAdmin(admin.ModelAdmin):
    list_display=['name' , 'price' , 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Orders)
