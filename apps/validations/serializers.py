from rest_framework import serializers

from .models import routes

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = routes
        fields = ('__all__')