from rest_framework.generics import ListAPIView
from django.shortcuts import render

from .models import economic_activities
from .serializers import EconomicActivitiesSerializers
# Create your views here.

""" services start here """
class EconomicActivitieList(ListAPIView):
    serializer_class = EconomicActivitiesSerializers

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return economic_activities.objects.filter(
            heading__icontains=kword
        )