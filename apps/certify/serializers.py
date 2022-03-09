from rest_framework import serializers

from .models import citv, soat, src, svct

class SOATSerializer(serializers.ModelSerializer):
    class Meta:
        model = soat
        fields = ('__all__')

class CITVSerializer(serializers.ModelSerializer):
    class Meta:
        model = citv
        fields = ('__all__')

class SRCSerializer(serializers.ModelSerializer):
    class Meta:
        model = src
        fields = ('__all__')

class SVCTSerializer(serializers.ModelSerializer):
    class Meta:
        model = svct
        fields = ('__all__')