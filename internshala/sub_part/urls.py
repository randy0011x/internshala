from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing),
    path('index/', views.index),
    path('menu/', views.menu),
    path('adminpage/', views.admin),
    path('delete_order/<int:id>', views.deleteorder),


]
