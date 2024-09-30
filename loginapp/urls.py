from django.urls import path
from loginapp import views

urlpatterns = [
    path('',views.index),
    path('login',views.login, name='login'),
    path('profile',views.profile, name='profile'),
    path('logout',views.logout, name='logout'),
    path('edit',views.edit)
]
