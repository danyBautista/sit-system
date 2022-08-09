from rest_framework import serializers

from .models import accreditation_type, accreditation

class serialiazerType(serializers.ModelSerializer):
    class Meta:
        model = accreditation_type

        fields = ('__all__')

class serializerAcreditation(serializers.ModelSerializer):
    class Meta:
        model = accreditation
        fields = ('__all__')