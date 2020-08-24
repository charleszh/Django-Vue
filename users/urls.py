
from django.urls import path, re_path, include
from . import views

app_name = 'users'
urlpatterns = [
    #path(r'register/', views.register, name='register'),
    path(r'login/', views.login, name='login'),
    #re_path(r'user/(?P<pk>\d+)/profile/', views.profile, name='profile'),
    #re_path(r'user/(?P<pk>\d+)/profile/update/', views.profile_update, name='profile_update'),
    #re_path(r'user/(?P<pk>\d+)/profile/pwdchange/', views.pwd_change, name='pwd_change'),
    path(r'logout/', views.logout, name='logout')
]
