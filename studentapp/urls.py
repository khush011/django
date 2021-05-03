from django.urls import path, include
from .views import *
urlpatterns = [
    path('home/', home_view),
    path('about/', about_view),
    path('login/', login),
    path('', simple),
    path('info/',info),
    path('forms/',loginpy),
    path('studorm/',studorm),
    path('jobs/',jobs),
    path('studata/',add_Data),
    path('more/',more),
    path('delete/',delete)
]