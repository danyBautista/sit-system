from rest_framework import serializers

from apps.home.models import Consulting

class ConsultingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulting

        fields = ('__all__')