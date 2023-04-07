from django.shortcuts import redirect

def logout(request):
    print(f"iteams in your cart before logout: {request.session.get('cart')}")
    if request.session.get('cart'):
        request.session['cart']=request.session.get('cart')
    else:
         request.session['cart']={}
    return redirect('login')