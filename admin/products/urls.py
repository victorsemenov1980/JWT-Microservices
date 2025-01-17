# -*- coding: utf-8 -*-

"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import ProductViewSet, UserAPIView
from . import views

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get':'list',
        'post':'create'})),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'})),
    path('user',UserAPIView.as_view()),
   
]