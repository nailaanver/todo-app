from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name="add"), 
    path('addrecord/',views.addrecord,name = "addrecord"),
    path('delete/<int:id>/',views.delete,name = "delete"),
    # path('delete/deletemember/<int:id>/',views.deletemember,name = "deletemember"),
    path('update/<int:id>/',views.update,name='update')
]