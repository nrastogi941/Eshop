from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from store.models import Product,Orders,Customer


class CheckOut(View):
    
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer_id=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_all_products_by_listid(list(cart.keys()))
        
        print(address,phone,customer_id,cart,products)

        if customer_id != None:
            for product in products:
                order=Orders(Customer=Customer(id=customer_id), product=product,price=product.price,quantity=cart.get(str(product.id)),address=address,phone=phone)
                order.save()
            request.session['cart']={}
        else:
            messages.warning(request, 'Please login !!')
            return redirect('login')

        return redirect('cart')
