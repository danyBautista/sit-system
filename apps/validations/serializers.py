from dataclasses import field
from rest_framework import serializers

from .models import routes, binding_contracts, authorization_documents, validation_tools, procedure

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = routes
        fields = ('__all__')

class BindingContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = binding_contracts
        fields = ('__all__')

class AuthorizationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = authorization_documents
        fields = ('__all__')

class ValidationToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = validation_tools
        fields = ('__all__')

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = procedure
        fields = ('__all__')