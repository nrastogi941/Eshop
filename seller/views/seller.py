from django.shortcuts import render
from django.views import View

class seller(View):

    def get(self,request):
        return render(request,"seller_home.html")


