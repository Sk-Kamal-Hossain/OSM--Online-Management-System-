from django.contrib import admin
from django.urls import path
from . import views


#Dajngo admin header customization

admin.site.site_header = "Developer OSM Team"
admin.site.site_title = "Welcome To OSM Dashboard"
admin.site.index_title = "Welcome To This Portal"



urlpatterns = [
    path('', views.Index, name='Index'),
    #path('index.html', views.Index, name='Index'),
    path('signup.html', views.signup, name='signup'),
    path('login.html', views.login, name='login'),
    path('Reg_Done.html', views.Reg_Done, name='Reg_Done'),
    path('login_done.html', views.login_done, name='login_done'),
    path('shoping_cart.html', views.shoping_cart, name='shoping_cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('profile.html', views.profile, name='profile'),
    path('contact.html', views.contact, name='contact'),
]