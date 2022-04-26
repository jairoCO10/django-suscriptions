from django.urls import path
from .views import  current_user, UserList,get_user_information, login



# router = routers.DefaultRouter()
# router.register('groups', GroupViewSet)
# groups_urlpatterns = [path("api/groups/", include(router.urls))]


urlpatterns = [
    path('login', login),
    path('current_user/', current_user),
    path('info', get_user_information),
    path('register/', UserList.as_view())
]
