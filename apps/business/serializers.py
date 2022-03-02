from rest_framework import serializers

from .models import business

class BusinessSerializers(serializers.ModelSerializer):
    class Meta:
        model = business

        fields = ('__all__')