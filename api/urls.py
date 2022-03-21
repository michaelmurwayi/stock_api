from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.routers import DefaultRouter

# create router and register viewsets
router = DefaultRouter()
router.register(r'stocks', views.StockViewSet)

# Automatically determined API urls

urlpatterns = [
    path('', include(router.urls)),
]