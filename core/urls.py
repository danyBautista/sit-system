# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('people/', include("apps.people.urls")),
    path('administration/', include("apps.administration.urls")),
    path('validations/', include("apps.validations.urls")),
    path('vehicles/', include("apps.vehicles.urls")),
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls"))            # UI Kits Html files
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)