
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('index', views.index),  
    path('info', views.info),
    path('works', views.works),
    path('links', views.links),
    path('registration', views.registration),
    path('user', views.user)
]