from django.shortcuts import render,HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.
def index(request):
    products=None
    category=Category.get_all_categories()

    category_id=request.GET.get('category')

    if category_id:
        products=Product.get_all_products_by_categoryid(category_id)
    else:
        products=Product.get_all_products()

    context={
        "products":products,
        "categories":category,
    }
    return render(request,"index.html",context=context)

def signup(request):

    if request.method == "GET":
        return render(request,"signup.html")
    
    if request.method == "POST":
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")

        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        customer.register()
        return HttpResponse("Registration successfull")
