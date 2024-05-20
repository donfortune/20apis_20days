from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('api/routes/', views.getRoutes, name='routes'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', views.protected_view, name='protected'),
    path('api/posts/', views.getPosts, name='posts'),
    path('api/posts/<int:id>/', views.getPost, name='post'),
    path('api/posts/create/', views.createPost, name='create_post')
]