from django.urls import path
from .views import current_user, UserList,get_user_information, login

urlpatterns = [
    path('login', login),
    path('current_user/', current_user),
    path('info', get_user_information),
    path('users/', UserList.as_view())
]
