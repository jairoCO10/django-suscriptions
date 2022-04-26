from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import dimensionesViewSet,datosinicialesViewSet,serviciosViewSet


router = DefaultRouter()
router.register("dimensiones", dimensionesViewSet, basename="dimensiones")
router.register('datos-iniciales', datosinicialesViewSet, basename='datos-iniciales')
router.register('servicios', serviciosViewSet, basename='servicios')
portant_capacity_urlpatterns = [path("api/dimensiones/", include(router.urls)),
                            path('api/datos-iniciales/',include(router.urls)),
                           path('api/servicios/', include(router.urls)),
                           ]

