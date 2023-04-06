from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer


class login(View):

    def get(self,request):
        return render(request,"login.html")
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        
        error_message=None

        if customer:
            if check_password(password,customer.password):
                request.session['customer']=customer.id
                request.session['email']=customer.email
                return redirect("homepage")
            else:
                error_message="Email or Password is invalid"
        else:
            error_message="Email or Password is invalid"

        return render(request,"login.html",{"error_message":error_message})
    


