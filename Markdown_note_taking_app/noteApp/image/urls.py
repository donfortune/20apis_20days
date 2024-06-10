
from django.urls import path

from . import views

urlpatterns = [
    path('api/lists/', views.image_list, name='image_list'),
    path('api/delete/', views.delete_list, name='delete_list'),
    path('api/file/<int:id>/', views.file, name='file'),
    path('api/file/check/<int:id>/', views.check_grammar, name='check_grammar')
]