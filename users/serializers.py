from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import User


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = groups
#         fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):

    #token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


    class Meta:
        model = User
        fields = ("__all__")


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token',  'email', 'password')
