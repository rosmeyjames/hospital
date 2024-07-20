
from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
path('doctorlist',views.doctorlist,name='doctrorlist'),
path('createbooking/<int:scheduleid>',views.createbooking,name='createbooking'),
path('userindex',views.userindex,name='userindex'),
path('approvedbookings',views.approvedbookings,name='approvedbookings'),
path('viewmedicine',views.viewmedicine,name='viewmedicine'),
path('cancelbooking/<int:bkid>',views.cancelbooking,name='cancelbooking'),
path('viewdiaganosis',views.viewmediaganosis,name='viewdiaganosis'),
path('billing',views.viewbilling,name='billing'),
path('checkout',views.create_checkout_session,name='checkout'),
path('success',views.success,name='success'),
path('cancel',views.cancel,name='cancel'),
 path('home',views.userhome,name='home')
    ]