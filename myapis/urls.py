from django.urls import path

from .views import *

urlpatterns = [

        path('', MyAPIView.as_view(), name='africa')
    ]
