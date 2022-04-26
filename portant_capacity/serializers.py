from rest_framework import serializers
from .models import datosIniciales, dimensionesPersonalizadas,servicios



class DatosinicialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = datosIniciales
        fields = '__all__'


class dimesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = dimensionesPersonalizadas
        fields = '__all__'



class serviciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = servicios
        fields = '__all__'