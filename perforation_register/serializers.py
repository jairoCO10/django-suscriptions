from rest_framework import serializers

from  .models import Sondeo, registroDePerforacion

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sondeo
        fields = '__all__'

class registroSerializers (serializers.ModelSerializer):
    class Meta:
        model = registroDePerforacion
        fields = '__all__'