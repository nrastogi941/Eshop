from django.shortcuts import render
from django.views import View
from store.models import Product

class cart(View):

    def get(self,request):
        list_ids=list(request.session.get('cart').keys())
        products=Product.get_all_products_by_listid(list_ids)
        return render(request,"cart.html",{'products':products})