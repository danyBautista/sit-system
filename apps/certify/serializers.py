from rest_framework import serializers

from .models import soat

class SOATSerializer(serializers.ModelSerializer):
    class Meta:
        model = soat
        fields = ('__all__')