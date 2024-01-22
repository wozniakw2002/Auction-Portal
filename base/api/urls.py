from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRouts),
    path('auctions/', views.getAuctions),
    path('auctions/<str:pk>/', views.getAuction)
]