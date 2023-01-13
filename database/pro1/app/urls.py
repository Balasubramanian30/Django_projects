from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('homeUrl',views.home,name='home'),
    path('userDetailsSave',views.userDetailsAdd,name='userDetailsSave'),
    path('edituser/<int:id>', views.edituser, name='edituser'),
    path('userDetailsUpdate/<int:id>', views.userDetailsUpdate, name='userDetailsUpdate'),
    path('deleteuser/<int:id>', views.userDetailsDelete, name='deleteuser'),

]
