from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
from .views import suscriptionViewSet



router = DefaultRouter()
router.register("suscription", suscriptionViewSet, basename="suscriptions")
suscriptions_urlpatterns = [path("api/suscriptions/", include(router.urls))]




# urlpatterns =[
#     path('home_post/', views.homeViewSet),
    
#     path('home_post_CRUD', views.home_post_CRUD),
#     path('home_get_CRUD', views.home_get_CRUD),
#     path('homeview/', views.home_list),
#     path('homedetail/<int:pk>/', views.home_detail),
#     ]
