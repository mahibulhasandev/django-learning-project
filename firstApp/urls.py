from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item', views.item, name='about'),
    path('<int:item_id>/', views.item_details, name='item_details'),
    path('item_stores', views.item_stores, name='item_stores'),
    


]