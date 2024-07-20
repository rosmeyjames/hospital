from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('adminindex', views.adminindex, name='adminindex'),
    path('viewallbookings',views.view_all_bookings,name="viewallbookings"),
    path('bookingapproval',views.bookingapproval,name='bookingapproval')
    ]