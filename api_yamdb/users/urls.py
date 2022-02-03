from django.urls import include, path
from rest_framework import routers

from .views import UserAdminViewset

router = routers.DefaultRouter()
router.register('', UserAdminViewset, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
