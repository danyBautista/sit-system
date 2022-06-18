from rest_framework import serializers

from .models import accreditation_type

class serialiazerType(serializers.ModelSerializer):
    class Meta:
        model = accreditation_type

        fields = ('__all__')