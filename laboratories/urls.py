from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import laboratoryViewSet


router = DefaultRouter()
router.register("laboratories", laboratoryViewSet, basename="laboratories")
laboratories_urlpatterns = [path("api/laboratories/", include(router.urls))]
