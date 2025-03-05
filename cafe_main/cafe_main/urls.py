"""
URL configuration for cafe_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

# from rest_framework import routers
# from api_cafe import viewsets
from rest_framework.routers import DefaultRouter

# from api_cafe.viewsets import OrderViewSet
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api_cafe.urls")),
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
    path("orders/create/", views.order_create, name="order_create"),
    path("orders/<int:pk>/update/", views.order_update, name="order_update"),
    path("orders/<int:pk>/delete/", views.order_delete, name="order_delete"),
    path("revenue/", views.revenue, name="revenue"),
    path("", views.index, name="index"),
]
