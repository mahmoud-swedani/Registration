from django.urls import path
from .views import *
from django.contrib.auth import views
urlpatterns = [
    path('', home,name='home-page'),
    #path(r'login/', views.login,name='login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    
]