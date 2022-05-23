from django.urls import path, re_path
from apps.accreditation.views import accreditationCreate, accreditationView

urlpatterns = [
    path('', accreditationView.as_view(), name='accreditation.index'),
    path('create/', accreditationCreate.as_view(), name='accreditation.create')
]