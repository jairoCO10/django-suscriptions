from rest_framework import serializers
from .models import correlaciones, Observaciones, parametroSuelo, perfilGeotecnico


class correlaciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = correlaciones
        fields = '__all__'

class Observaciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Observaciones
        fields = '__all__'


class parametroSuelo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = parametroSuelo
        fields = '__all__'

class perfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = perfilGeotecnico
        fields = '__all__'
