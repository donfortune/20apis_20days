from django.urls import path
from . import views

urlpatterns = [
    path('', views.generateShortUrl, name='generate'),
    #path('<str:short_url>', views.redirectShortUrl, name='redirect'),
    path('shortened/', views.generateShortUrl, name='shortened'),
    path('list/', views.listUrls, name='list'),
    path('add/', views.addUrl, name='add'),
    path('generate/<int:id>/', views.generateShortUrl, name='generate')
   
]