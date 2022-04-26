from django.urls import URLPattern, path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import observacionesViewSet,parametrosViewSet,correlacionesViewSet,perfilViewSet

router = DefaultRouter()
router.register("observaciones", observacionesViewSet, basename="observaciones")
router.register('parametros-suelos',parametrosViewSet, basename='parametros-suelos')
router.register('correlaciones',correlacionesViewSet, basename='correlaciones')
router.register('perfil',perfilViewSet, basename='perfil')



geotechnical_urlpatterns = [path("api/observaciones/", include(router.urls)),
                            path('api/parametros-suelos/', include(router.urls)),
                            path('api/correlaciones/', include(router.urls)),
                            path('api/perfil/', include(router.urls)),
                           
                        ]


# urlpatterns = [ path('Perfil2', views.Perfil)]