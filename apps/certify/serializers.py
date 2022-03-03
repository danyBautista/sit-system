from rest_framework import serializers

from .models import citv, soat

class SOATSerializer(serializers.ModelSerializer):
    class Meta:
        model = soat
        fields = ('__all__')

class CITVSerializer(serializers.ModelSerializer):
    class Meta:
        model = citv
        fields = ('__all__')