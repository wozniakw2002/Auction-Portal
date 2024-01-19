from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('auction/<str:id>/', views.auction, name='auction'),
    
    path('create-auction/', views.createAuction, name='create-auction'),
    path('update-auction/<str:pk>/', views.updateAuction, name='update-auction'),
    path('delete-auction/<str:pk>/', views.deleteAuction, name='delete-auction')
]
