from rest_framework import serializers

from .models import vehicles

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicles
        fields = ('__all__')