from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutUser, name='logout'),

    path('user/', userPage, name="user-page"),

    path('account/', accountSettings, name='account'),
]