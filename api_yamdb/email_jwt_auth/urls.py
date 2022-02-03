from django.urls import path

from .views import UserCreateOrSendMailCodeAPI, UserEmailCodeLoginAPI

urlpatterns = [
    path('signup/', UserCreateOrSendMailCodeAPI.as_view(), name='user'),
    path('token/', UserEmailCodeLoginAPI.as_view(), name='token'),
]
