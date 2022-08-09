from django.urls import path, re_path
from apps.accreditation.views import accreditationCreate, accreditationIndex, accreditationView, accreditationUpdate, TypeCreate, accreditationSearch, accreditationForm, AcreditationAPIList

urlpatterns = [
    path('', accreditationIndex.as_view(), name='accreditation.index'),
    path('search/', accreditationSearch.as_view(), name='accreditation.search'),
    path('form/<int:pk>', accreditationForm.as_view(), name='accreditation.form'),
    path('api/search/', AcreditationAPIList.as_view(), name='accreditation.api.view'),
    path('create/', accreditationCreate.as_view(), name='accreditation.create'),
    path('view/<str:pk>', accreditationView.index, name='accreditation.view'),
    path('update/<str:pk>', accreditationUpdate.as_view(), name='accreditation.update'),
    path('type/create/', TypeCreate.as_view(), name="accreditation.type_create")
]