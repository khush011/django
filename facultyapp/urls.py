from django.urls import path, include

from .views import *

urlpatterns = [
    path('home/', f_home_view),
    path('about/', f_about_view),
    path('login/', login),
    path('', simple),
]