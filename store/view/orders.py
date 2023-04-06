from django.shortcuts import render
from django.views import View
from store.models import Orders
from django.utils.decorators import method_decorator

class Order(View):

    def get(self,request):

        customer_id=request.session.get('customer')
        order=Orders.get_orders_by_customerId(customer_id)
        print(f"Customer orders are :{order}")
        return render(request,"orders.html",{'orders':order})