from django.urls import path
from .view import home,signup,login,logout,cart,checkout,orders
from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('',home.index.as_view(),name="homepage"),
    path('signup',signup.signup.as_view(),name="signup"),
    path('login',login.login.as_view(),name="login"),
    path('logout',logout.logout,name="logout"),
    path('cart',cart.cart.as_view(),name="cart"),
    path('check-out',checkout.CheckOut.as_view(),name='checkout'),
    path('order',auth_middleware(orders.Order.as_view()),name='order')
]
