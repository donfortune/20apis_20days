
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('api/get_expenses/', views.get_Expenses, name='get_products'),
    path('api/get_expense/<int:id>/', views.get_Expense, name='get_product'),
    path('api/update_expense/<int:id>/', views.update_Expenses, name='update_product'),
    path('api/products/', views.get_Products, name='get_products'),

]