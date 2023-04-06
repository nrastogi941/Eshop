import re
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer

class signup(View):

    def get(self,request):
        return render(request,"signup.html")
    
    def post(self,request):
        print(request.POST)
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")

        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)

        error_message=self.validate_form_details(customer)

        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect("homepage")
        else:
            value={
                "first_name":first_name,
                "last_name":last_name,
                "phone":phone,
                "email":email,
            }

            context={
                "error_message":error_message,
                "value":value,
            }
            return render(request,"signup.html",context=context)
        
    def validate_form_details(self,customer):
        error_message = None
        if len(customer.first_name) < 3:
            error_message="First Name must be 3 char long or more"
        elif len(customer.last_name) < 3:
            error_message="Last Name must be 3 char long or more"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", customer.email):
            error_message = "Invalid email format"
        elif not re.match(r"\d{10}", customer.phone):
            error_message = "Invalid phone number format"
        elif len(customer.password) < 6:
            error_message="Password must be 6 char long"
        elif customer.is_email_exists():
            error_message="Email Already Registered..."
        elif customer.is_phone_exists():
            error_message="Phone Number Already Registered..."

        return error_message