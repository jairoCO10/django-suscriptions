from rest_framework import serializers

from  .models import membresia

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = membresia
        fields = '__all__'
