from django.urls import path 
from rest_framework_simplejwt.views import TokenRefreshView
from .api_views import RegisterView,LoginView,LogoutView,UserProfileView

urlpatterns=[
    path('register/',RegisterView.as_view(),name='api_register'),
    path('login/',LoginView.as_view(),name='api_login'),
    path('logout/',LogoutView.as_view(),name='api_logout'),
    path('profile/',UserProfileView.as_view(),name='api_profile'),
    path('token/refresh',TokenRefreshView.as_view(),name='api_token_refresh'),

]