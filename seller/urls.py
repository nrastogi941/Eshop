from django.urls import path
from .views import seller,login

urlpatterns = [
    path('seller',seller.seller.as_view()),
    path('seller-login',login.SellerLogin.as_view()),
]
