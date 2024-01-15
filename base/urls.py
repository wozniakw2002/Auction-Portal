from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auction/<str:id>/', views.auction, name='auction'),
    path('create-auction/', views.createAuction, name='create-auction'),
    path('update-auction/<str:pk>/', views.updateAuction, name='update-auction')
]
