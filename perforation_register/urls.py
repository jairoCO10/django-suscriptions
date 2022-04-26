from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import SondeosViewSet, registroViewSet


router = DefaultRouter()
router.register("sondeos", SondeosViewSet, basename="sondeos")
router.register("registro_perforacion", registroViewSet, basename="registro_perforacion")

perforation_urlpatterns = [path("api/sondeos/", include(router.urls)),
                        path('api/registro-perforacion/', include(router.urls))
                        ]
