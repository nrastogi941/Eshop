from django.shortcuts import render,redirect
from store.models.category import Category
from store.models.product import Product
from django.views import View

class index(View):

    def get(self,request):
        roducts=None
        categories=Category.get_all_categories()
        category_id=request.GET.get('category')
        if category_id:
            products=Product.get_all_products_by_categoryid(category_id)
        else:
            products=Product.get_all_products()
        
        context={
            "products":products,
            "categories":categories
        }

        print(f"the login user is : {request.session.get('email')}")
        return render(request,"index.html",context=context)
    
    def post(self,request):
        print(f" request is : {request.POST } and the product_id is : {request.POST.get('product_id')}")
        
        product_id =request.POST.get('product_id')
        decrement_value=request.POST.get('decrement_product_value')
        
        cart=request.session.get('cart')

        if cart:
            quantity=cart.get(product_id)

            if quantity:
                if decrement_value:
                    cart[product_id]=quantity-1
                    if cart[product_id]==0:
                        cart.pop(product_id)
                else:
                    cart[product_id]=quantity+1
            else:
                cart[product_id]=1
        else:
            cart={}
            cart[product_id]=1

        request.session['cart']=cart

        print(f"cart : {cart}")
        return redirect("homepage")