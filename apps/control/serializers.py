from rest_framework import serializers

from .models import economic_activities

class EconomicActivitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = economic_activities
        fields = ('__all__')