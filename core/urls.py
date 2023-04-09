from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerUser,name='register'),
    path('login/', views.loginUser,name='login'),
    path('logout/', views.logoutUser,name='logout'),
    path('home/', views.home,name='home'),
    path('update-user/<str:pk>/', views.updateUser,name='update_user'),
    path('delete-user/<str:pk>/', views.deleteUser,name='delete_user'),
    path('search/', views.search_user,name='search'),
    path('staff-user/', views.staff_user,name='staff_user'),
    path('active-user/', views.active_user,name='active_user'),
    path('super-user/', views.super_user,name='super_user'),
]