from django.urls import path, re_path
from apps.accreditation.views import accreditationCreate, accreditationIndex, accreditationView, accreditationUpdate

urlpatterns = [
    path('', accreditationIndex.as_view(), name='accreditation.index'),
    path('create/', accreditationCreate.as_view(), name='accreditation.create'),
    path('view/<str:pk>', accreditationView.index, name='accreditation.view'),
    path('update/<str:pk>', accreditationUpdate.as_view(), name='accreditation.update')
]