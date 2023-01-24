from django.urls import path
from .views import *
 
urlpatterns = [
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('forgot/', forgot, name='forgot'),
    path('profile/', profile, name='profile'),
    path('logout/',logout, name='logout')
]