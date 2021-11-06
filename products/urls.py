from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('shopsingle/', views.shopsingle, name="shopsingle"),
    path('shop/', views.shop, name="shop"),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='LogOut'),
    path('signup/', views.signup, name='signup'),
    path('thankyou/', views.thankyou, name="thankyou"),
]
