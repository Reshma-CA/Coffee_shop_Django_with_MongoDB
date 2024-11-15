from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Welcome_page,name="welcome"),
    path('home/', views.home, name='home'),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path('logout/', views.logout, name='logout'),
    
]
