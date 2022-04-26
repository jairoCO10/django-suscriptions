"""soil_study_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from projects.urls import home_urlpatterns
from suscriptions.urls import suscriptions_urlpatterns
from geotechnical_profile.urls import geotechnical_urlpatterns
from laboratories.urls import  laboratories_urlpatterns
from perforation_register.urls import perforation_urlpatterns
from settlements.urls import settlements_urlpatterns
from portant_capacity.urls import portant_capacity_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('token-auth/', obtain_jwt_token),
    path('users/',include('users.urls')),
    #path('perfil/',include('geotechnical_profile.urls')),
    #path('settlements/',include('settlements.urls')),
    
    
   
]
urlpatterns += home_urlpatterns
urlpatterns += suscriptions_urlpatterns
urlpatterns += laboratories_urlpatterns
urlpatterns += geotechnical_urlpatterns
urlpatterns += perforation_urlpatterns
urlpatterns += settlements_urlpatterns
urlpatterns+= portant_capacity_urlpatterns

