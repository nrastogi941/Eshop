from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from store.models import Product,Orders,Customer


class CheckOut(View):
    
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer_id=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_all_products_by_listid(list(cart.keys()))
        
        print(address,phone,customer_id,cart,products)

        for product in products:
            order=Orders(Customer=Customer(id=customer_id), product=product,price=product.price,quantity=cart.get(str(product.id)),address=address,phone=phone)
            order.PlaceOrder()
        
        request.session['cart']={}

        return redirect('cart')
