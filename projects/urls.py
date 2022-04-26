from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
from .views import homeViewSet



router = DefaultRouter()
router.register("projects", homeViewSet, basename="projects")
home_urlpatterns = [path("api/home/", include(router.urls))]




urlpatterns =[
    path('home_post/', views.homeViewSet),
    
    path('home_post_CRUD', views.home_post_CRUD),
    path('home_get_CRUD', views.home_get_CRUD),
    path('homeview/', views.home_list),
    path('homedetail/<int:pk>/', views.home_detail),
    ]
