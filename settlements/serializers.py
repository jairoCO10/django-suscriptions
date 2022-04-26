from rest_framework import serializers
from .models import datosPrimary,diferenciales,preciosUnitarios,eficiencia,datosConsProfunda,geometriaCimentacionProfunda,precioMaterialCimentacionProfunda,rangoDimensiones,relacionCarga


class DatosPrimarySerializer(serializers.ModelSerializer):
    class Meta:
        model = datosPrimary
        fields = '__all__'

class diferencialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = diferenciales
        fields = '__all__'

class preciosUnitariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = preciosUnitarios
        fields = '__all__'



class eficienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = eficiencia
        fields = '__all__'


class datosConsProfundaSerializer(serializers.ModelSerializer):
    class Meta:
        model = datosConsProfunda
        fields = '__all__'

class geometriaCimentacionProfundaSerializer(serializers.ModelSerializer):
    class Meta:
        model = geometriaCimentacionProfunda
        fields = '__all__'

class precioMaterialCimentacionProfundaSerializer(serializers.ModelSerializer):
    class Meta:
        model = precioMaterialCimentacionProfunda
        fields = '__all__'


class rangoDimensionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = rangoDimensiones
        fields = '__all__'


class relacionCargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = relacionCarga
        fields = '__all__'
