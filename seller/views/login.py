from django.shortcuts import render
from django.views import View

class SellerLogin(View):

    def get(self,request):
        return render(request,"seller_login.html")


