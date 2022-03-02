from rest_framework import serializers

from .models import vehicles, types

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicles
        fields = ('__all__')

class TypesVehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = types
        fields = ('__all__')