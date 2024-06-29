from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.apiOverview, name='index'),
    path('product-list/', views.productLists, name='product-list'),
    path('add-product/', views.addProduct, name='add-product'),
    path('getProduct/<int:id>', views.productList, name='getProduct'),
    path('update-product/<int:id>', views.updateProduct, name='update-product'),

    path('order-items/', views.orderItems, name='order-items'),
    path('order-item/<int:id>/', views.orderItem, name='order-item'),
    path('create-order/', views.createOrderItem, name='create-order'),

    path('payment/', PaymentView.as_view(), name='payment'),
]
