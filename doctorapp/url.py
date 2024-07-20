from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
path('index', views.index,name='index'),
path('createmedicine', views.createmedicine,name='createmedicine'),
path('createdepartment', views.createdepartment,name='createdepartment'),
path('medicinelist', views.medicinelist,name='medicinelist'),
path('medicineupdate/<int:medid>', views.updatemedicine,name='updatemedicine'),
path('medicinedelete/<int:medid>', views.deletemedicine,name='deletemedicine'),
path('createposition', views.createposition,name='createposition'),
path('listposition', views.positionlist,name='listposition'),
path('deleteposition/<int:posid>', views.deleteposition,name='deleteposition'),
path('updateposition/<int:posid>', views.updateposition,name='updateposition'),
path('addstaff', views.addstaff,name='addstaff'),
path('updatetaff/<int:sid>', views.updatestaff,name='updatestaff'),
path('deletetaff/<int:sid>', views.deletestaff,name='deletestaff'),
path('stafflist', views.stafflist,name='stafflist'),
path('',views.newlogin,name='login'),
path('register',views.registerdetails,name='register'),
path('createschedule', views.createschedule,name='createschedule'),
path('viewschedule', views.viewschedule,name='viewschedule'),
path('updateschedule/<int:schid>', views.updateschedule,name='updateschedule'),
path('deleteschedule/<int:schid>', views.deleteschedule,name='deleteschedule'),
path('prescription',views.doc_presc,name='prescription'),
path('labtest',views.createnewlabtest,name='labtest'),
path('diaganosis',views.usercreatediaganosis,name='diaganosis'),
]