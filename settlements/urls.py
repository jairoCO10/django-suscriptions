from django.urls import URLPattern, path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import datosPrimaryViewSet,diferencialesViewSet,preciosUnitariosViewSet


router = DefaultRouter()
router.register("datos-primary", datosPrimaryViewSet, basename="dimensiones")
router.register('diferenciales', diferencialesViewSet, basename='datos-iniciales')
router.register('precios-unitarios', preciosUnitariosViewSet, basename='servicios')
settlements_urlpatterns = [path("api/datos-primary/", include(router.urls)),
                            path('api/diferenciales/',include(router.urls)),
                           path('api/precios-unitarios/', include(router.urls)),
                           ]

# urlpatterns =[

#     #path('BoxplotFuerza', views.BoxplotFuerza),
#     #path('BoxplotMomento', views.BoxplotMomento),
#     path('Asentamiento', views.Asentamiento2),
#     path('AsentRegister', views.AsentRegister),   
#     path('dimensionMayor', views.dimensionMayor), 
#     path('Excentricidades', views.Excentricidades), 
#     path('AsentamientoDiferencial', views.AsenD),
#     path('dimensionesConstruccion', views.dimensionesConstruccion),
#     path('CantidadObra', views.cant_ObraPres),
#     path('Verificar', views.verificar),    
#     path('secuencia', views.secuencia),
#     path('presupuesto',views.presupuesto),
#     path('AsentamiendoPersonalizado',views.AsentamiendoPersonalizado),
#     #path('profuVSCosto',views.prVScosto),
#     path('Capp',views.Capp),
#     path('AsentProf',views.AsentProf),
#     path('Eficiencia',views.Eficiencia),

# ]