from rest_framework import serializers

from  .models import home1

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = home1
        fields = '__all__'
