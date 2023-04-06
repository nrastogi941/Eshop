from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50,default='',blank=True)
    phone=models.CharField(max_length=50,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)


    def PlaceOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customerId(customer_id):
        return Orders.objects.filter(Customer=customer_id).order_by('-id')