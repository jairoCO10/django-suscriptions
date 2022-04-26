from rest_framework import serializers

from  .models import laboratory

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = laboratory
        fields = '__all__'