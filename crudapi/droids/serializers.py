from rest_framework import serializers
from .models import Droid
from django.contrib.auth.models import User


class DroidSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Droid
        fields = ('id', 'descricao', 'endereco', 'contato', 'anunciante', 'status')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    Droids = serializers.PrimaryKeyRelatedField(many=True, queryset=Droid.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'Droids')
