from django.shortcuts import render
from django.views import View
from store.models import Product,Customer

class cart(View):

    def get(self,request):
        
        if request.session.get('cart'):
            list_ids=list(request.session.get('cart').keys())
            products=Product.get_all_products_by_listid(list_ids)
            return render(request,"cart.html",{'products':products})
        else:
            customer_id=request.session.get('customer')
            error_message=None
            customer_name=None
            if customer_id != None:
                customer=Customer.objects.get(id=customer_id)
                customer_name=customer.first_name

            print(error_message)
            error_message="Your cart is empty , please add iteams in your cart"
            context={
                'error_message':error_message,
                'customer_name':customer_name,
            }
            return render(request,"cart.html",context=context)