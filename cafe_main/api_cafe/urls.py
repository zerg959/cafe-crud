# api_cafe/urls.py
from django.urls import path, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r"orders", viewsets.OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
